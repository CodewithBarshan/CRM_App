from django.db import models

# Create your models here.

class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    contact_no=models.CharField(max_length=50)
    address=models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}") #while calling any one of the above data ,first name and last name will be displayed on web page or admin panel 
    