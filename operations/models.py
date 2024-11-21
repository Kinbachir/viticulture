from django.db import models

class Exploitation(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Salarie(models.Model):
    name = models.CharField(max_length=255)
    exploitation = models.ForeignKey(Exploitation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class OperationCulturale(models.Model):
    TYPE_CHOICES = [
        ('phytosanitaire', 'Phytosanitaire'),
        ('taille', 'Taille'),
        ('vendange', 'Vendange'),
    ]

    date = models.DateField()
    salarie = models.ForeignKey(Salarie, on_delete=models.CASCADE)
    type_operation = models.CharField(choices=TYPE_CHOICES, max_length=50)
    duree = models.DurationField()
    details = models.TextField(blank=True, null=True)  # Notes supplémentaires

    def __str__(self):
        return f"{self.type_operation} - {self.salarie.name}"

class OperationPhytosanitaire(models.Model):
    operation = models.OneToOneField(OperationCulturale, on_delete=models.CASCADE)
    maladie_visee = models.CharField(max_length=255)
    stade_maladie = models.CharField(max_length=255)
    methode_traitement = models.CharField(max_length=255)
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Phytosanitaire: {self.operation}"
