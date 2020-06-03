from rest_framework.views import APIView
from mew.core.utils import APIResponse

from api.services import ParkingService


class Parkings(APIView):

    def post(self, request):
        """
        """

        data = {
            "facility_id": request.data.get("facility_id", None),
            "reg_no": request.data.get("reg_no", None),
            "vehicle_type": request.data.get("vehicle_type", None)
        }
        response = ParkingService().create_ticket(data)
        return APIResponse.send(response)

    def put(self, request):
        """
        """
        ticket_id = request.data.get("ticket_id", None)
        response = ParkingService().update_ticket(ticket_id)
        return APIResponse.send(response)

    def get(self, request):
        """
        """
        response = ParkingService().get_tickets(request)
        return APIResponse.send(response)
