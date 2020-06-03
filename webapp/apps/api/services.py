import logging
from datetime import datetime

from mew.client.google_calendar import GoogleCalendarClient
from webapp.celery_app import my_queue_processor
from mew.core.exceptions import InvalidInputException

from api.models import Parking, Ticket, Facility
from api.serializers import TicketSerializer
from api.filters import TicketFilter
from api.constants import PRICING


class ParkingService():
    """
    """

    def create_ticket(self, data):

        # Locking will be needed to make sure multiple parallel requests are handled properly

        if not data.get("facility_id") or not data.get("reg_no") or not data.get("vehicle_type"):
            # Add additional check for evaluating vehicle type is one of constants
            raise InvalidInputException("Missing necessary parameters.")

        facility_id = data.get("facility_id")
        reg_no = data.get("reg_no")
        vehicle_type = data.get("vehicle_type")

        facility_slot = self.get_facility_slot(facility_id, vehicle_type)

        if self.__is_parking_available(facility_slot):
            ticket = Ticket.objects.create(facility_id=facility_id, vehicle_type=vehicle_type, reg_no=reg_no, start_time=datetime.now(), amount=0)
            self.__decrease_available_slot(facility_slot)
            serialized_data = TicketSerializer(instance=ticket)
            return serialized_data.data
        else:
            raise InvalidInputException("Parking is FULL.")

    def update_ticket(self, ticket_id):
        """
        """
        if not ticket_id:
            raise InvalidInputException("Ticket ID is missing")

        try:
            ticket = Ticket.objects.get(id=ticket_id)
            if ticket.amount or ticket.end_time:
                raise InvalidInputException("Ticket has already been closed.")

            end_time = datetime.now()
            amount = PricingService().calculate_ticket_amount(ticket.vehicle_type, ticket.start_time, end_time)

            # Update Ticket Amount
            ticket.end_time = end_time
            ticket.amount = amount
            ticket.save()

            facility_slot = self.get_facility_slot(ticket.facility_id, ticket.vehicle_type)
            self.__increase_available_slot(facility_slot)

            serialized_data = TicketSerializer(instance=ticket)
            return serialized_data.data

        except Ticket.DoesNotExist:
            raise InvalidInputException("Ticket does not exist")

    def __decrease_available_slot(self, facility_slot):
        facility_slot.available_slots = facility_slot.available_slots - 1
        facility_slot.save()

    def __increase_available_slot(self, facility_slot):
        facility_slot.available_slots = facility_slot.available_slots + 1
        facility_slot.save()

    def get_facility_slot(self, facility_id, vehicle_type):
        """
        """
        facility_slot = Parking.objects.filter(is_deleted=False, facility_id=facility_id, vehicle_type=vehicle_type)
        if not facility_slot:
            raise InvalidInputException("No slot for %s available in facility" % (vehicle_type))
        return facility_slot[0]

    def __is_parking_available(self, facility_slot):

        return True if facility_slot.available_slots else False

    def get_tickets(self, request):
        result = TicketFilter(request.GET, queryset=Ticket.objects.filter(is_deleted=False))
        serialized_data = TicketSerializer(instance=result.qs, many=True).data
        return serialized_data


class PricingService():

    def get_pricing_model(self):
        """
        """
        return PRICING

    def calculate_ticket_amount(self, vehicle_type, start_time, end_time):
        """
        """
        pricing_model = self.get_pricing_model()
        vehicle_pricing = pricing_model.get(vehicle_type, None)

        if not vehicle_pricing:
            raise InvalidInputException("Vehicle type not supported.")

        end_time = end_time.replace(tzinfo=None)
        start_time = start_time.replace(tzinfo=None)
        parking_time = (end_time - start_time).total_seconds()

        if parking_time < 0:
            raise InvalidInputException("Start Time cannot be greater than End time.")

        amount = 0
        for rate in vehicle_pricing:
            if parking_time > rate["start"]:
                amount = amount + rate["rate"]
            else:
                break

        return amount
