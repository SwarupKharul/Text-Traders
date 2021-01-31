from django.db import models
import datetime
from location_field.models.plain import PlainLocationField
from django.db import models
from django.contrib.auth.models import User

book_choices=(
    ("academic","academic"),
    ("non-academic","non-academic")
)

class Books(models.Model):
    objects = None
    bookname = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, default='Anonymous')
    description = models.TextField(null=True)
    condition = models.CharField(max_length=100, default='Used')
    academic = models.CharField(choices=book_choices, max_length=13, default="academic")
    image1 = models.ImageField(upload_to='books/', default='Hello')
    image2 = models.ImageField(upload_to='books/', blank=True)
    image3 = models.ImageField(upload_to='books/', blank=True)
    image4 = models.ImageField(upload_to='books/', blank=True)
    #year = models.IntegerField(null=True)
    city = models.CharField(max_length=255, default='Pune')
    location = PlainLocationField(based_fields=['city'], zoom=7, default='Pune')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bookname
