from django.db import models

# Create your models here.

class Login_info(models.Model):
    Username = models.CharField(primary_key= True, max_length=20)
    Password = models.CharField(max_length=20)
    DateTime = models.DateField(auto_now= True)

    def __str__(self):
        return self.Username
    