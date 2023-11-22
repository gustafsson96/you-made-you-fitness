from django.db import models

TYPE_OF_GUIDE = (
    ("Digital Copy", "Digital Copy"),
    ("Physical Copy", "Physical Copy"),
    ("Both Digital and Physical Copy", "Both Digital and Physical Copy"),
)


class Guide(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    type_of_guide = models.CharField(max_length=50, choices=TYPE_OF_GUIDE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
