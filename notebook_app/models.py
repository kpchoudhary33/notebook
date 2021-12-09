from django.db import models

# Create your models here.

class JupyterNoteBookData(models.Model):

    label = models.CharField(max_length=200)
    code = models.TextField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.label
