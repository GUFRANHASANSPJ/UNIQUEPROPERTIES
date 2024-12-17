from django import forms
from django.contrib.auth.models import User
from accounts.models import *
# from django_recaptcha.fields import ReCaptchaField

# user forms section
class UserForm1(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
        
class UserForm2(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields= ['phone','address','images']
    # captcha = ReCaptchaField()


class EditUserProfileForm1(forms.ModelForm):
    class Meta:
        model = User
        fields=["username","first_name","last_name","email",]

class EditUserProfileForm2(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=['phone','address','images']

# owners forms section
class OwnerForm1(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
        
class OwnerForm2(forms.ModelForm):
    class Meta:
        model=property_owner
        fields=['phone','address','owner_image']
    # captcha = ReCaptchaField()

class EditOwnerProfileForm1(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email",]

class EditOwnerProfileForm2(forms.ModelForm):
    class Meta:
        model=property_owner
        fields=['phone','address','owner_image'] 

# Agents forms section

class AgentForm1(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
        
class AgentForm2(forms.ModelForm):
    class Meta:
        model=Agents
        fields=['user_type','phone','address','agent_image']
    # captcha = ReCaptchaField()

class EditAgentProfileForm(forms.ModelForm):
    class Meta:
        model = Agents
        fields = ['phone', 'address', 'agent_image'] 

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['user', 'username', 'price']  # Include only relevant fields

    def __init__(self, *args, **kwargs):
        # Retrieve the current user from the view
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # If the user is provided, set the initial values for the fields and make them non-editable
        if user:
            self.fields['user'].initial = user
            self.fields['user'].queryset = User.objects.filter(id=user.id)  # Limit queryset to the current user
            self.fields['user'].disabled = True
            
            self.fields['username'].initial = user.username
            self.fields['username'].disabled = True

# Example form in Django to collect property preferences

class PropertySearchForm(forms.Form):
    # Property Type
    property_type = forms.ChoiceField(choices=[('Houses', 'Houses'), ('Townhouses', 'Townhouses'), 
                                              ('Condos', 'Condos'), ('Apartments', 'Apartments'),
                                              ('None','None')], 
                                      required=False)
    # Location Preferences
    # location = forms.CharField(max_length=100, required=True)

    # Price Range
    min_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    max_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)

    # Property Size
    min_sqft = forms.IntegerField(required=False)
    max_sqft = forms.IntegerField(required=False)

    # Bedrooms and Bathrooms
    bed = forms.ChoiceField(choices=[('1', '1 Bedroom'), ('2', '2 Bedrooms'), ('3+', '3+ Bedrooms')], 
                                 required=False)
    bath = forms.ChoiceField(choices=[('1', '1 Bathroom'), ('2', '2 Bathrooms'), ('3+', '3+ Bathrooms')],
                                 required=False)

    # Features and Amenities
    balcony = forms.BooleanField(required=False)
    # swimming_pool = forms.BooleanField(required=False)
    # gym = forms.BooleanField(required=False)
    parking = forms.ChoiceField(choices=[('two wheeler', 'two wheeler'),
                                         ('car', 'car'),
                                        ('No parking',  'No parking')], 
                                        required=False)
    garden = forms.BooleanField(required=False)
    Smart_Home_Features = forms.CharField(max_length=100, required=False)

    # Lifestyle Preferences
    post_type= forms.ChoiceField(choices=[('Sell', 'Sell'),
                                            ('Rent', 'Rent'),], 
                                        required=False)

    Building_Age= forms.IntegerField(required=False)

    # Security Features
    Neighborhood_Crime_Rate= forms.ChoiceField(choices=[('Low', 'Low'),
                                                    ('Moderate', 'Moderate'),
                                                    ('High', 'High')], 
                                        required=False)