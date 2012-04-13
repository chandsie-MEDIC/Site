from django.contrib.auth.models import User
from django.contrib.localflavor.us import models as usmodels
from django.db import models

class UserProfile (models.Model):
    user = models.OneToOneField(User)
    
    specialty = models.CharField(max_length = 60)
    url = models.URLField()
    address = models.TextField()
    phone_number = usmodels.PhoneNumberField()