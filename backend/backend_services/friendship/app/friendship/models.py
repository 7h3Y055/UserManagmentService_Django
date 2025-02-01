from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
# Create your models here.

FRIENDSHIP_STATUS = {
    ('PN','pending'),
    ('FR','friends'),
    ('BL','blocked'),
}

class Friendship(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    sender_id = models.IntegerField()
    received_id = models.IntegerField()
    status = models.CharField(max_length=2, choices=FRIENDSHIP_STATUS, default='PN')
    
    class Meta:
        db_table = 'pong_friendship'