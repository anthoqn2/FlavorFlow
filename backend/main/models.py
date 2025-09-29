from django.db import models

class Amount(models.Model):
    UNIT_CHOICES = (
    ('grams', 'grams'),
    ('cups', 'cups'),
    ('pounds', 'pounds'),
    ('ounces', 'ounces'),
    ('teaspoons', 'teaspoons'),
    ('tablespoons', 'tablespoons'),
    ('quarts', 'quarts'),
    ('pints', 'pints'),
    ('gallons', 'gallons'),
)

    value = models.FloatField()
    unit = models.CharField(max_length=50,  choices = UNIT_CHOICES)


    class Meta:
        abstract = True

class Ingredient(Amount):
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
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} {self.value} {self.unit}"
