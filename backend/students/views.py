from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("last_name")

    serializer_class = StudentSerializer

    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        "first_name",
        "last_name",
        "permanent_code",
        "phone",
    ]

    filterset_fields = [
        "gender",
        "level",
        "ufr",
        "department",
        "is_active",
    ]