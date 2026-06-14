from django.contrib import admin
from .models import House, Room, Assignment


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "manager_name",
        "manager_phone",
        "is_active",
    )

    search_fields = (
        "name",
        "manager_name",
        "manager_phone",
    )

    list_filter = (
        "is_active",
    )

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "house",
        "number",
        "capacity",
        "gender",
        "current_occupancy",
        "available_places",
        "is_active",
    )

    search_fields = (
        "number",
        "house__name",
    )

    list_filter = (
        "house",
        "gender",
        "is_active",
    )

    def current_occupancy(self, obj):
        return obj.assignments.filter(
            is_current=True
        ).count()

    current_occupancy.short_description = "Occupants"

    def available_places(self, obj):
        return (
            obj.capacity
            - obj.assignments.filter(
                is_current=True
            ).count()
        )

    available_places.short_description = "Places restantes"

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "room",
        "entry_date",
        "exit_date",
        "is_current",
    )

    search_fields = (
        "student__first_name",
        "student__last_name",
        "student__permanent_code",
    )

    list_filter = (
        "is_current",
        "room__house",
    )

    autocomplete_fields = (
        "student",
        "room",
    )

    actions = ["release_rooms"]

    def release_rooms(self, request, queryset):
        updated = 0

        for assignment in queryset.filter(
            is_current=True
        ):
            assignment.is_current = False

            from django.utils import timezone

            assignment.exit_date = timezone.now().date()

            assignment.save()

            updated += 1

        self.message_user(
            request,
            f"{updated} chambre(s) libérée(s)."
        )

    release_rooms.short_description = (
        "Libérer les chambres sélectionnées"
    )