from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "permanent_code",
        "first_name",
        "last_name",
        "gender",
        "ufr",
        "department",
        "program",
        "level",
        "phone",
        "is_active",
    )

    search_fields = (
        "permanent_code",
        "first_name",
        "last_name",
        "phone",
        "email",
        "guardian_phone",
    )

    list_filter = (
        "gender",
        "ufr",
        "department",
        "program",
        "level",
        "is_active",
        "is_resident",
        "entry_year",
        "academic_status",
    )

    readonly_fields = (
        "joined_at",
        "created_at",
        "updated_at",
    )

    fieldsets = (
    (
        "Informations personnelles",
        {
            "fields": (
                ("first_name", "last_name"),
                "gender",
                ("birth_date", "birth_place"),
                "photo",
            )
        },
    ),

    (
        "Informations académiques",
        {
            "fields": (
                "ufr",
                "department",
                "program",
                "level",
                "permanent_code",
                "entry_year",
                "academic_status",
            )
        },
    ),

    (
        "Origine géographique",
        {
            "fields": (
                "home_department",
                "home_commune",
            )
        },
    ),

    (
        "Contact d'urgence",
        {
            "fields": (
                "guardian_name",
                "guardian_phone",
            )
        },
    ),

    (
        "Coordonnées",
        {
            "fields": (
                "phone",
                "email",
            )
        },
    ),

    (
        "Informations sur l'amicale",
        {
            "fields": (
                "is_resident",
                "joined_at",
                "is_active",
            )
        },
    ),

    (
        "Traçabilité",
        {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            ),
        },
    ),
)