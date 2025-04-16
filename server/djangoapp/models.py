from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, default='Unknown')  # New field

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more if needed
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
                               validators=[
                                   MaxValueValidator(2023),
                                   MinValueValidator(2015)
                               ])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # New field

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"
