from django.db import models

TYPE_OF_GUIDE = (
    (1, "Digital Copy"),
    (2, "Physical Copy"),
    (3, "Both Digital and Physical Copy"),
)


class Guides(models.Model):