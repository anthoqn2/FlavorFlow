from django.db import models

# Create your models here.

class Amount(models.Model):
    id = models.ObjectIdField(primary_key=True)
    value = models.FloatField()
    unit = models.CharField(max_length=50) # grams, cups

    class Meta:
        abstract = True

class Ingredient(models.Model):
    CATEGORY_CHOICES = [
    ('vegetable', 'Vegetable'),
    ('fruit', 'Fruit'),
    ('meat', 'Meat'),
    ('dairy', 'Dairy'),
    ('grain', 'Grain'),
    ('spice', 'Spice'),
    ('herb', 'Herb'),
    ('seafood', 'Seafood'),
    ('nut', 'Nut'),
    ('legume', 'Legume'),
    ('oil', 'Oil'),
    ('sweetener', 'Sweetener'),
    ('beverage', 'Beverage'),
    ('other', 'Other'),
    ]
    
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,choices = CATEGORY_CHOICES)
    amount = models.EmbeddedField(model_container=Amount)

    def __str__(self):
        return f"{self.name} {self.amount.value} {self.amount.unit}"
