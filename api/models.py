from django.db import models

# Create your models here.
STATE_CHOICES = ((
    ('Bihar','Bihar'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Gujrat','Gujrat'),
))

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    gender = models.CharField(max_length=50)
    location = models.CharField( max_length=50)
    pImage = models.ImageField(upload_to='pImages',blank=True)
    rdoc = models.FileField( upload_to='rdocs',blank=True)
    