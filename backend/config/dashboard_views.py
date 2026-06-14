from rest_framework.views import APIView
from rest_framework.response import Response

from students.models import Student
from houses.models import House, Assignment, Room


class DashboardStatsView(APIView):
    def get(self, request):
        occupied = Assignment.objects.filter(
            is_current=True
        ).count()

        total_capacity = sum(
            room.capacity
            for room in Room.objects.all()
        )

        return Response({
            "students": Student.objects.count(),
            "houses": House.objects.count(),
            "occupied": occupied,
            "available": total_capacity - occupied,
        })