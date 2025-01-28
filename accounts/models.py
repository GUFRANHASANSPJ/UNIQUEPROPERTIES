from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from properties.models import property

class property_owner(models.Model):
    user_type = models.CharField(max_length=10, default='owner')
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=100)  
    address = models.CharField(max_length=255, blank=True, null=True)
    owner_image=models.ImageField(upload_to='owner_img/',blank=True,null=True)

    def __str__(self):
        return self.owner.username
    
class Agents(models.Model):
    user_type = models.CharField(max_length=10,  default='agent')
    agent = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)  
    address = models.CharField(max_length=255, blank=True, null=True)
    agent_image=models.ImageField(upload_to='agent_img/',blank=True,null=True)

    def __str__(self):
        return self.agent.username
    
class UserProfile(models.Model):  
    USER_TYPE_CHOICES = [
        ('regular', 'Regular User'),
        ('owner', 'Property Owner')
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='regular')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100) 
    address = models.CharField(max_length=255 ,blank=True,null=True)  
    images=models.ImageField(upload_to="user_imag",blank=True,null=True)

    def __str__(self):
        return self.user.username

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    property = models.ForeignKey("properties.property", on_delete=models.CASCADE, related_name='wishlisted_by')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.property.name}"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    username = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - ${self.price}"


