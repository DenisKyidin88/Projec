from rest_framework import viewsets

from ..models import Car, Maintenance, Complaints, Guide
from .serilizers import CarSerializer, MaintenanceSerializer, ComplaintsSerializer, GuideSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing car.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MaintenanceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing maintenances.
    """
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ComplaintsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing complaints.
    """
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer


class GuideViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing guide.
    """
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    