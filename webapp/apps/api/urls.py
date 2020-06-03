from django.urls import path

from . import views

urlpatterns = [
    # URLs
    path('v1/parkings', views.Parkings.as_view(), name='tickets'),
    # path('v1/vehicles/<string: reg_no>/history', views.TicketHistory.as_view(), name='test'),
]
