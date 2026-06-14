from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    photo_url = serializers.SerializerMethodField()

    level_display = serializers.CharField(
        source="get_level_display",
        read_only=True,
    )

    academic_status_display = serializers.CharField(
        source="get_academic_status_display",
        read_only=True,
    )

    class Meta:
        model = Student
        fields = "__all__"

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_photo_url(self, obj):
        request = self.context.get("request")

        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)

        return None