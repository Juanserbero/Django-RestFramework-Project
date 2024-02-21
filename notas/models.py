from django.db import models

class Notas (models.Model):
    id_nota = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=12,verbose_name='Título')
    contenido = models.CharField(max_length=10000,verbose_name='Contenido')
    
    
    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"

    def __str__(self):
        return self.titulo