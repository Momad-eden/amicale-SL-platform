from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from .models import House, Room, Assignment
from .serializers import (
    HouseSerializer,
    RoomSerializer,
    AssignmentSerializer,
)


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    @action(detail=True, methods=["patch"])
    def release(self, request, pk=None):
        assignment = self.get_object()

        assignment.is_current = False
        assignment.exit_date = timezone.now().date()

        assignment.save()

        return Response({
            "message": "Chambre libérée avec succès."
        })