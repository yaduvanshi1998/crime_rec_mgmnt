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
    
class Court_info(models.Model):
    Court_id = models.CharField(primary_key=True, max_length=10)
    Court_name = models.CharField(max_length=25)
    Address = models.TextField(max_length=125)
    Level = models.CharField(max_length=25)
    Phone_no = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)

    def __str__(self):
        return self.Court_name
    
class Judge_info(models.Model):
    Judge_id = models.CharField(primary_key=True, max_length=25, editable=False)
    F_name = models.CharField(max_length=25)
    L_name = models.CharField(max_length=25)
    Designation = models.CharField(max_length=25)
    Court_id = models.ForeignKey(Court_info, verbose_name="Court Info", on_delete=models.CASCADE)
    Age = models.IntegerField()
    Address = models.CharField(max_length=250)
    Phone_no = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.Judge_id:  # Only generate ID if it doesn't already exist
            # Get the last Judge_id, if available
            last_judge = Judge_info.objects.order_by('Judge_id').last()
            
            # Determine the next ID
            next_id_num = int(last_judge.Judge_id[1:]) + 1 if last_judge else 101
            
            # Set the new Judge_id with prefix 'J'
            self.Judge_id = f'J{next_id_num}'
        
        # Call the parent save method
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.Email
     