from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile,property_owner,Agents
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