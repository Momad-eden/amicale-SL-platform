from django.db import models
from django.core.exceptions import ValidationError
from students.models import Student


class House(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nom"
    )

    address = models.CharField(
        max_length=255,
        verbose_name="Adresse"
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    manager_name = models.CharField(
        max_length=150,
        verbose_name="Responsable"
    )

    manager_phone = models.CharField(
        max_length=20,
        verbose_name="Téléphone du responsable"
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Maison"
        verbose_name_plural = "Maisons"

    def __str__(self):
        return self.name
    
class Room(models.Model):
    GENDER_CHOICES = [
        ("M", "Masculine"),
        ("F", "Féminine"),
        ("X", "Mixte"),
    ]

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name="rooms"
    )

    number = models.CharField(
        max_length=20,
        verbose_name="Numéro"
    )

    capacity = models.PositiveIntegerField(
        default=4,
        verbose_name="Capacité"
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="X"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = ("house", "number")
        ordering = ["house", "number"]
        verbose_name = "Chambre"
        verbose_name_plural = "Chambres"

    def __str__(self):
        return f"{self.house.name} - Chambre {self.number}"
    


class Assignment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="assignments"
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="assignments"
    )

    entry_date = models.DateField()

    exit_date = models.DateField(
        null=True,
        blank=True
    )

    is_current = models.BooleanField(
        default=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-entry_date"]
        verbose_name = "Affectation"
        verbose_name_plural = "Affectations"

    def clean(self):
        if self.is_current:
            current_count = Assignment.objects.filter(
                room=self.room,
                is_current=True
            ).exclude(pk=self.pk).count()

            if current_count >= self.room.capacity:
                raise ValidationError(
                    "Cette chambre est déjà complète."
                )

            if Assignment.objects.filter(
                student=self.student,
                is_current=True
            ).exclude(pk=self.pk).exists():
                raise ValidationError(
                    "Cet étudiant possède déjà une affectation active."
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

        self.student.is_resident = self.is_current
        self.student.save()

    def __str__(self):
        return f"{self.student} → {self.room}"