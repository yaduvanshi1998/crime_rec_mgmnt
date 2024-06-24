from django.db import models

# Create your models here.

class Login_info(models.Model):
    Username = models.CharField(primary_key= True, max_length=20)
    F_name = models.CharField(max_length=50)
    L_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=20, unique=True)
    Password = models.CharField(max_length=20)
    DateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Username
    
    #Login_info_obj = models.Manager()
    