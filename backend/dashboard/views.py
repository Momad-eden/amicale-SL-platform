from rest_framework.views import APIView
from rest_framework.response import Response

from students.models import Student
from houses.models import House, Assignment


class DashboardStatsView(APIView):
    def get(self, request):
        active_assignments = Assignment.objects.filter(
            is_current=True
        )

        total_capacity = sum(
            room.capacity
            for house in House.objects.all()
            for room in house.rooms.all()
        )

        occupied = active_assignments.count()

        return Response({
            "students": Student.objects.count(),
            "houses": House.objects.count(),
            "occupied": occupied,
            "available": total_capacity - occupied,
        })