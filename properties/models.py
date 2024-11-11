from django.db import models
from django.contrib.auth.models import User

# from accounts.models import property_owner

class property_type(models.Model):
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type

# class Utilities(models.Model):

#     power_supply =models.BooleanField(default=True,null=True, blank=True)
#     water_supply =models.BooleanField(default=True,null=True, blank=True)
#     garbage =models.BooleanField(default=True,null=True, blank=True)

    
class property(models.Model):
    post_type = models.ForeignKey(property_type,on_delete=models.CASCADE)
    owners = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # utilities = models.ForeignKey(Utilities, on_delete=models.SET_NULL, null=True, blank=True)

    visit_count = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)  # Average rating
    rating_count = models.IntegerField(default=0)  # Rating field
    name= models.CharField(max_length=50)
    property_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    country= models.CharField(null=True,max_length=50,default='US')
    state= models.CharField(null=True,max_length=50)
    city= models.CharField(null=True,max_length=50)
    address= models.CharField(null=True,max_length=200)
    Landmark= models.CharField(null=True,max_length=50)
    Adjacent_Roads= models.CharField(null=True,max_length=100)


    nearby_hospitals= models.CharField(null=True,max_length=200)
    nearby_schools= models.CharField(null=True,max_length=200)
    
    

    age =models.IntegerField()
    area= models.CharField(max_length=50)
    length= models.CharField(max_length=50)
    breadth= models.CharField(max_length=50)
    property_info_CHOICES = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK',  '3BHK'),
        ('4BHK',  '4BHK'),
    ]
    proprty_info= models.CharField(max_length=100, choices=property_info_CHOICES, default='1BHK', null=True, blank=True)
    proprty_status= models.BooleanField(default=True,null=True, blank=True)
    Lifts= models.BooleanField(default=True,null=True, blank=True)

    No_of_floors= models.IntegerField(null=True, blank=True)
    description = models.TextField(default="No description provided", blank=True)
    # furnished= models.BooleanField(default=True)
    # semi_furnished= models.BooleanField(default=True ,null=True, blank=True)
    for_family= models.BooleanField(default=True,null=True, blank=True)
    for_business= models.BooleanField(default=True,null=True, blank=True)

    pet_friendly=models.BooleanField(default=True,null=True, blank=True)
    # pet_friendly = models.BooleanField(default=False)

    parking_TYPE_CHOICES = [
        ('two wheeler', 'two wheeler'),
        ('car', 'car'),
        ('No parking',  'No parking'),
    ]

    facing_TYPE_CHOICES = [
    ('North', 'North'),
    ('North-East', 'North-East'),
    ('East', 'East'),
    ('South-East', 'South-East'),
    ('South', 'South'),
    ('South-West', 'South-West'),
    ('West', 'West'),
    ('North-West', 'North-West'),
]
    Furnish_Choices = [
    ('Furnished', 'Furnished'),
    ('Semi-Furnished', 'Semi-Furnished'),
    ('Not-Furnished', 'Not-Furnished'),
    
]

    posted_date = models.DateTimeField(auto_now_add=True,null=True)
    parking = models.CharField(max_length=100, choices=parking_TYPE_CHOICES, default='no_parking', null=True, blank=True)
    facing = models.CharField(max_length=100, choices=facing_TYPE_CHOICES, default='East', null=True, blank=True)
    furnish_detail = models.CharField(max_length=100, choices=Furnish_Choices, default='Not-Furnished', null=True, blank=True)
    Property_Features= models.CharField(null=True,max_length=50)
    
    garden =models.BooleanField(default=True,null=True, blank=True)
    sunlight_access =models.BooleanField(default=True,null=True, blank=True)
    road_side_parking =models.BooleanField(default=True,null=True, blank=True)
    water_drainage =models.BooleanField(default=True,null=True, blank=True)
    Environmental_Factors= models.CharField(null=True,max_length=50)
    
    


    image=models.ImageField(upload_to='properties_img/',blank=True,null=True)
    image1=models.ImageField(upload_to='properties_img/',blank=True,null=True)
    image2=models.ImageField(upload_to='properties_img/',blank=True,null=True)
    # images = models.JSONField(default=list, blank=True,null=True)  # Stores image paths as a list in JSON

    population_mix = models.JSONField(default=list, blank=True)
    locality = models.JSONField(default=list, blank=True)
    ENGAGEMENT_CENTERS= models.JSONField(default=list, blank=True)
    INDUSTRIES_NEARBY= models.JSONField(default=list, blank=True)
    UTILITIES= models.JSONField(default=list, blank=True)
    MAINTENANCE= models.JSONField(default=list, blank=True)
    HISTORICAL= models.JSONField(default=list, blank=True)
    Healthcare= models.JSONField(default=list, blank=True)
    Administration= models.JSONField(default=list, blank=True)
    Safety_Security= models.JSONField(default=list, blank=True)
    Accessibility= models.JSONField(default=list, blank=True)
    Green_Spaces= models.JSONField(default=list, blank=True)
    Education_Child_Care= models.JSONField(default=list, blank=True)
    Weather_Factors= models.JSONField(default=list, blank=True)
    

    def __str__(self):
        return self.name
    
class PropertyImage(models.Model):
    property = models.ForeignKey(
        property, 
        related_name='property_images',  # Change this to avoid conflict
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='properties/images/')
    
    def __str__(self):
        return f"Image for {self.property.name}"