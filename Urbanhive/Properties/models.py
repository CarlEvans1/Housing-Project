from django.db import models
from django.core.validators import RegexValidator, MinValueValidator


# Create your models here.
from Properties.validators import validate_available_houses
class Building(models.Model):
    """
    Represents a building with its attributes.

    Attributes:
        building_name (str): The name of the building.
        owner (str): The owner of the building.
        location (str): The location of the building.
        total_number_of_houses (int): The total number of houses in the building. Must be greater than or equal to 1.
        available_houses (int): The number of available houses in the building. Initially set to total_number_of_houses.
        amenities (ManyToManyField): The amenities available in the building.
    """
    building_name = models.CharField(max_length=255, null=False, blank=False, default='HomeHive')
    owner = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    total_number_of_houses = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    available_houses = models.PositiveIntegerField()
    #amenities = models.ManyToManyField('Amenity', blank=True)

    def __str__(self):
        """
        Returns a string representation of the Building object.

        Returns:
            str: A string representation of the Building object.
        """
        return f"Building at {self.location}, owner {self.owner} with {self.available_houses} houses available"

    def save(self, *args, **kwargs):
        """
        Custom save method to set available_houses initially equal to total_number_of_houses when creating a new building.
        """
        if not self.pk:
            self.available_houses = self.total_number_of_houses

        validate_available_houses(self.total_number_of_houses, self.available_houses)
        super(Building, self).save(*args, **kwargs)
