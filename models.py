from django.db import models

class GroceryList(models.Model):
    groceryItemName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.groceryItemName