from pyexpat import model
from django.db import models
# Import user model
from django.core.validators import MaxValueValidator, MinValueValidator

#run migration agter changed the database column
class Weight(models.Model):
    weight = models.PositiveIntegerField(validators=[MaxValueValidator(500), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}: {self.weight} lb"