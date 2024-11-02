from django.db import models
from django.contrib.auth.models import User

# from accounts.models import property_owner

class property_type(models.Model):
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type

    
class property(models.Model):
    post_type = models.ForeignKey(property_type,on_delete=models.CASCADE)
    owners = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # owners = models.ForeignKey("accounts.property_owner", on_delete=models.SET_NULL, null=True, blank=True, default=None)  # Link to PropertyOwner
    visit_count = models.IntegerField(default=0)
    name= models.CharField(max_length=50)
    property_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    address= models.CharField(max_length=50)
    age =models.IntegerField()
    area= models.CharField(max_length=50)
    length= models.CharField(max_length=50)
    breadth= models.CharField(max_length=50)
    No_of_floors= models.IntegerField()
    description = models.TextField(default="No description provided", blank=True)
    furnished= models.BooleanField(default=True)
    semi_furnished= models.BooleanField(default=True)
    for_family= models.BooleanField(default=True)
    for_business= models.BooleanField(default=True)
    image=models.ImageField(upload_to='properties_img/',blank=True,null=True)

    def __str__(self):
        return self.name
