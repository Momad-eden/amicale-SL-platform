from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "Masculin"),
        ("F", "Féminin"),
    ]

    LEVEL_CHOICES = [
        ("L1", "Licence 1"),
        ("L2", "Licence 2"),
        ("L3", "Licence 3"),
        ("M1", "Master 1"),
        ("M2", "Master 2"),
        ("D", "Doctorat"),
    ]

    first_name = models.CharField(
        max_length=100,
        verbose_name="Prénom"
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="Nom"
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name="Sexe"
    )

    birth_date = models.DateField(
        verbose_name="Date de naissance"
    )

    birth_place = models.CharField(
        max_length=150,
        verbose_name="Lieu de naissance"
    )

    ufr = models.CharField(
        max_length=150,
        verbose_name="UFR"
    )

    department = models.CharField(
        max_length=150,
        verbose_name="Département"
    )

    program = models.CharField(
        max_length=150,
        verbose_name="Filière"
    )

    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        verbose_name="Niveau"
    )

    permanent_code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Code permanent"
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="Téléphone"
    )

    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Email"
    )

    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True,
        verbose_name="Photo"
    )

    is_resident = models.BooleanField(
        default=False,
        verbose_name="Étudiant résident"
    )

    joined_at = models.DateField(
        auto_now_add=True,
        verbose_name="Date d'adhésion"
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name="Membre actif"
    )

    ACADEMIC_STATUS_CHOICES = [
        ("ACTIVE", "Actif"),
        ("SUSPENDED", "Suspendu"),
        ("GRADUATED", "Diplômé"),
        ("DROPPED", "Abandon"),
    ]

    entry_year = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Année d'entrée à l'UADB"
    )

    home_department = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Département d'origine"
    )

    home_commune = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Commune d'origine"
    )

    guardian_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Nom du tuteur"
    )

    guardian_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Téléphone du tuteur"
    )

    academic_status = models.CharField(
        max_length=20,
        choices=ACADEMIC_STATUS_CHOICES,
        default="ACTIVE",
        verbose_name="Statut universitaire"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.permanent_code})"