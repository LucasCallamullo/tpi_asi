from django.db import models

# Create your models here.
class Degree(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    name = models.CharField(max_length=100)
    degree_program = models.ForeignKey('Degree', on_delete=models.CASCADE, related_name='subjects', null=True)
    slug = models.SlugField(max_length=110, null=True, blank=True)

    def __str__(self):
        return self.name

    
# ====================================================================
#    ===== TUTORES ====
# ====================================================================
# ====================================================================
#    ===== TUTORES ====
# ====================================================================
class Tutor(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='tutores', null=True)
    
    def __str__(self):
        return f"Tutor: {self.user.username}"

class MateriaTutor(models.Model):
    MODALIDAD_CHOICES = [
        ('virtual', 'Virtual'),
        ('hibrido', 'Híbrido'),
        ('presencial', 'Presencial'),
    ]
    
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE, related_name='materias', null=True)
    materia = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='tutores', null=True)
    modalidad = models.CharField(max_length=20, choices=MODALIDAD_CHOICES, default='virtual')
    año_promocion = models.IntegerField(verbose_name="Año de promoción")
    verificado = models.BooleanField(default=False)
    precio = models.FloatField(default=0.0)
    
    class Meta:
        # Para evitar que un tutor tenga la misma materia múltiples veces
        unique_together = ['tutor', 'materia']
        verbose_name = "Materia de Tutor"
        verbose_name_plural = "Materias de Tutores"
    
    def __str__(self):
        return f"{self.tutor} - {self.materia} ({self.modalidad})"