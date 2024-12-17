from django.db import models
from django.contrib.auth.models import User

from accounts.models import *

   
class property(models.Model):
    post_type_choices=[
        ('Sell', 'Sell'),
        ('Rent', 'Rent'),
    ]
    post_type = models.CharField(max_length=100, choices=post_type_choices, null=True, )
    owners = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    property_type_CHOICES = [
        ('Houses', 'Houses'),
        ('Townhouses', 'Townhouses'),
        ('Condos',  'Condos'),
        ('Apartments',  'Apartments'),
        ('None',  'None'),
    ]
    property_type =models.CharField(max_length=100, choices=property_type_CHOICES, default='None', null=True, blank=True)

    name= models.CharField(max_length=50)
    Building_Age =models.IntegerField()
    property_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    area= models.CharField(max_length=50)
    length= models.CharField(max_length=50)
    breadth= models.CharField(max_length=50)

    country= models.CharField(null=True,max_length=50,default='US')
    state= models.CharField(null=True,max_length=50)
    county= models.CharField(null=True,max_length=50)
    city= models.CharField(null=True,max_length=50)
    address= models.CharField(null=True,max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Latitude
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Longitude

    visit_count = models.IntegerField(default=0)
    p_rating = models.FloatField(default=0.0)  # Overall rating
    rating = models.FloatField(default=0.0)  # Average rating
    rating_count = models.IntegerField(default=0)  # Rating field
    property_info_CHOICES = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK',  '3BHK'),
        ('4BHK',  '4BHK'),
    ]
    proprty_info= models.CharField(max_length=100, choices=property_info_CHOICES, default='1BHK', null=True, blank=True)
    proprty_status= models.BooleanField(default=True,null=True, blank=True)

    No_of_floors= models.IntegerField(null=True, blank=True)
    description = models.TextField(default="No description provided", blank=True)
    for_family= models.BooleanField(default=True,null=True, blank=True)
    for_business= models.BooleanField(default=True,null=True, blank=True)
    pet_friendly=models.BooleanField(default=True,null=True, blank=True)

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
    
    garden =models.BooleanField(default=True,null=True, blank=True)
    sunlight_access =models.BooleanField(default=True,null=True, blank=True)
    road_side_parking =models.BooleanField(default=True,null=True, blank=True)
    water_drainage =models.BooleanField(default=True,null=True, blank=True)
    bed= models.IntegerField(null=True, blank=True)
    bath= models.IntegerField(null=True, blank=True)

    image=models.ImageField(upload_to='properties_img/',blank=True,null=True)
    images = models.JSONField(default=list, blank=True,null=True)  # Stores image paths as a list in JSON
    Adjacent_Roads= models.CharField(null=True,max_length=100)

# L2 Fields

    # property Property_Features
    balcony= models.BooleanField(default=True,null=True, blank=True)
    basement= models.BooleanField(default=True,null=True, blank=True)
    roof_condition = [
        ('New', 'New'),
        ('Old', 'Old'),
    ]
    roof_condition= models.CharField(max_length=100, choices=roof_condition, default='New', null=True, blank=True)
    window = models.JSONField(default=list, blank=True)
    Flooring_type = [
        ('Hardwood', 'Hardwood'),
        ('Tile', 'Tile'),
        ('Carpet', 'Carpet'),
    ]
    flooring = models.CharField(max_length=100, choices=Flooring_type, default='Standard', null=True, blank=True)

    ceiling_type = [
        ('Standard', 'Standard'),
        ('High', 'High'),
    ]
    
    ceiling_condition= models.CharField(max_length=100, choices=ceiling_type, default='Standard', null=True, blank=True)
    Property_Features_descriptions= models.CharField(null=True,max_length=200, blank=True)


    # Environmental Factors
    air_Pollution_type = [
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
    ]
    Noise_Pollution_type = [
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
    ]
    air_Pollution_Levels= models.CharField(null=True, choices=air_Pollution_type, max_length=100, blank=True)
    Noise_Pollution= models.CharField(null=True,max_length=100, choices=Noise_Pollution_type,blank=True)
    Flood_Zone=models.BooleanField(default=False,null=True, blank=True)
    Earthquake_zone=models.BooleanField(default=False,null=True, blank=True)
    Environmental_Factors_descriptions= models.CharField(null=True,max_length=200, blank=True)

    #Accessebility
    public_transportation= models.CharField(null=True, max_length=100,blank=True)
    handicap_accesibility_type = [
        ('Full', 'Low'),
        ('Partial', 'Moderate'),
        ('Not Available', 'Not Available'),
    ]
    handicap_accesibility= models.CharField(null=True,choices=handicap_accesibility_type, max_length=100,blank=True)
    proximity_to_airport= models.CharField(null=True,max_length=100, blank=True)
    road_quality_type = [
        ('Paved', 'Paved'),
        ('Unpaved', 'Unpaved'),
    ]
    road_quality= models.CharField(null=True,max_length=100, choices=road_quality_type,blank=True)
    Accessebility_descriptions= models.CharField(null=True,max_length=200, blank=True)

    #Safety and security
    Neighborhood_Crime_Rate_type = [
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
    ]
    Neighborhood_Crime_Rate= models.CharField(null=True,max_length=100,choices=Neighborhood_Crime_Rate_type, blank=True)
    Police_Station_Proximity= models.CharField(null=True,max_length=100, blank=True)
    Fire_Station_Proximity= models.CharField(null=True,max_length=100, blank=True)
    Security_Features= models.CharField(null=True,max_length=100, blank=True)
    Safety_security_descriptions= models.CharField(null=True,max_length=200, blank=True)

    #Technology and Connectivity
    Internet_Speed_type = [
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
    ]
    Internet_Speed= models.CharField(null=True,max_length=100, choices=Internet_Speed_type, blank=True)
    Cell_Network_Coverage_type = [
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ]
    Cell_Network_Coverage= models.CharField(null=True,max_length=100,choices=Cell_Network_Coverage_type, blank=True)
    Electric_Vehicle_Charging= models.BooleanField(default=True,null=True, blank=True)
    Smart_Home_Features= models.JSONField(default=list, blank=True)
    Technoly_connectivity_descriptions= models.CharField(null=True,max_length=200, blank=True)

    #Community and Social Life
    Community_Events_type = [
        ('Monthly', 'Monthly'),
        ('Quaterly', 'Quaterly'),
        ('Yearly', 'Yearly'),
        ('No Events', 'No Events'),
    ]
    Community_Events= models.CharField(null=True,max_length=100,choices=Community_Events_type, blank=True)
    Neighborhood_Vibe_type = [
        ('Family-Friendly', 'Family-Friendly'),
        ('Active', 'Active'),
    ]
    Neighborhood_Vibe= models.CharField(null=True, max_length=100,choices=Neighborhood_Vibe_type, blank=True)
    Social_Clubs_and_Groups= models.CharField(null=True,max_length=100, blank=True)
    community_descriptions= models.CharField(null=True,max_length=200, blank=True)

#    Green Spaces and Outdoors
    Proximity_to_Parks= models.CharField(null=True,max_length=100, blank=True)
    Gardens_Greenery_type = [
        ('Private', 'Private'),
        ('Community', 'Community'),
    ]
    Gardens_Greenery= models.CharField(null=True,max_length=100, choices=Gardens_Greenery_type,blank=True)
    Pet_Friendly_Areas= models.BooleanField(default=True,null=True, blank=True)
    greenspaces_and_outdoor_descriptions= models.CharField(null=True,max_length=200, blank=True)

#   Education and Child Care
    Schools_Nearby= models.CharField(null=True,max_length=100, blank=True)
    Childcare_Centers= models.BooleanField(default=True,null=True, blank=True)
    Playgrounds_type = [
        ('Nearby', 'Nearby'),
        ('Onsite', 'Onsite'),
    ]
    Playgrounds= models.CharField(null=True, max_length=100,choices=Playgrounds_type ,blank=True)
    Education_descriptions= models.CharField(null=True,max_length=200, blank=True)

#   Utility and Service Quality
    Electricity_Reliability_type = [
        ('High', 'High'),
        ('Moderate', 'Moderate'),
    ]
    Water_Supply_Quality_type = [
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ]
    Waste_Collection_type = [
        ('Weekly', 'Weekly'),
        ('Bi-Weekly', 'Bi-Weekly'),
    ]
    Electricity_Reliability= models.CharField(null=True,max_length=100,choices=Electricity_Reliability_type, blank=True)
    Water_Supply_Quality= models.CharField(null=True,max_length=100,choices=Water_Supply_Quality_type, blank=True)
    Waste_Collection= models.CharField(null=True,max_length=100,choices=Waste_Collection_type, blank=True)
    Utility_and_Service_Quality_descriptions= models.CharField(null=True,max_length=200, blank=True)

#   Nearby Employment Centers
    Business_District_Proximity= models.CharField(null=True, max_length=100,blank=True)
    Industrial_Areas= models.CharField(null=True,max_length=100, blank=True)    
    Nearby_Employment_Centers_descriptions= models.CharField(null=True,max_length=200, blank=True)


#  Transportation and Commute
    Major_Highways_Access= models.CharField(null=True,max_length=100, blank=True)
    Commute_Time_to_Downtown= models.CharField(null=True, max_length=100,blank=True)    
    Transportation_and_Commute_descriptions= models.CharField(null=True,max_length=200, blank=True)



#  Special Features
    Historical_Building_Status_type = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    Cultural_Heritage_Sites_type = [
        ('Nearby', 'Nearby'),
        ('Not Nearby', 'Not Nearby'),
    ]
    Historical_Building_Status= models.CharField(null=True,max_length=100,choices=Historical_Building_Status_type, blank=True)
    Cultural_Heritage_Sites= models.CharField(null=True,max_length=100,choices=Cultural_Heritage_Sites_type, blank=True)    
    Luxury_Amenities= models.JSONField(default=list, blank=True)   
    Special_Features_descriptions= models.CharField(null=True,max_length=200, blank=True)


#  Community Support Services
    Food_Banks= models.CharField(null=True,max_length=100, blank=True)
    Community_Centers_type = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    Community_Centers= models.CharField(null=True,max_length=100,choices=Community_Centers_type, blank=True)    
    Community_Support_Services_descriptions= models.CharField(null=True,max_length=200, blank=True)
    

#  Weather-Related Factors
    Average_Annual_Rainfall= models.CharField(null=True,max_length=100, blank=True)
    Snowfall= models.CharField(null=True,max_length=100, blank=True)    
    Weather_Related_Factors_descriptions= models.CharField(null=True,max_length=200, blank=True)

    
#  Parking and Transportation
    Assigned_Parking_type = [
            ('Yes', 'Yes'),
            ('No', 'No'),
        ]
    Bicycle_Parking_type = [
            ('Yes', 'Yes'),
            ('No', 'No'),
        ]
    Assigned_Parking= models.CharField(null=True,max_length=100, choices=Assigned_Parking_type,blank=True)
    Bicycle_Parking= models.CharField(null=True, max_length=100,choices=Bicycle_Parking_type,blank=True)    
    Parking_and_Transportation_descriptions= models.CharField(null=True,max_length=200, blank=True)
    

    def __str__(self):
        return self.name
    

class ViewedProperty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey('property', on_delete=models.CASCADE)  # Replace 'Property' with your actual model name
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.user.username} viewed {self.property.title}"
    
class Contacted_Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey('property', on_delete=models.CASCADE)  # Replace 'Property' with your actual model name
    contact_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.user.username} viewed {self.property.title}"




class Country(models.Model):
    name = models.CharField(max_length=100)  
    country_code = models.CharField(max_length=10, unique=True) 

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class Pincode(models.Model):
    pincode = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='pincodes')

    def __str__(self):
        return self.pincode
