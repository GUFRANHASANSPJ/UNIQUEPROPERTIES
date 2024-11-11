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
        fields= ['user_type','phone','address','images']
    # captcha = ReCaptchaField()

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 'phone', 'address', 'images']



# owners forms section
class OwnerForm1(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
        
class OwnerForm2(forms.ModelForm):
    class Meta:
        model=property_owner
        fields=['user_type','phone','address','owner_image']
    # captcha = ReCaptchaField()

class EditOwnerProfileForm(forms.ModelForm):
    class Meta:
        model = property_owner
        fields = ['phone', 'address', 'owner_image'] 

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