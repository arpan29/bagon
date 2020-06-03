import django_filters

from api.models import Ticket

class TicketFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket
        fields = {
            'reg_no': ['exact'],
        }
