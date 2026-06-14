from rest_framework import serializers
from .models import House, Room, Assignment


class HouseSerializer(serializers.ModelSerializer):
    rooms_count = serializers.SerializerMethodField()
    capacity = serializers.SerializerMethodField()
    occupied = serializers.SerializerMethodField()
    available = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = "__all__"

    def get_rooms_count(self, obj):
        return obj.rooms.count()

    def get_capacity(self, obj):
        return sum(room.capacity for room in obj.rooms.all())

    def get_occupied(self, obj):
        return sum(
            room.assignments.filter(is_current=True).count()
            for room in obj.rooms.all()
        )

    def get_available(self, obj):
        return self.get_capacity(obj) - self.get_occupied(obj)


class RoomSerializer(serializers.ModelSerializer):
    occupied = serializers.SerializerMethodField()
    available = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    def get_occupied(self, obj):
        return obj.assignments.filter(
            is_current=True
        ).count()

    def get_available(self, obj):
        return obj.capacity - self.get_occupied(obj)
    

class AssignmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(
        source="student.__str__",
        read_only=True
    )

    room_name = serializers.CharField(
        source="room.__str__",
        read_only=True
    )

    class Meta:
        model = Assignment
        fields = "__all__"