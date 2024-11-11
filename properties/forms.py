from properties.models import *
from django import forms
from django.forms import modelformset_factory

POPULATION_OPTIONS = [
    ("Students", "Students"),
    ("Office Movers", "Office Movers"),
    ("Entrepreneurs", "Entrepreneurs"),
    ("Elderly Friendly", "Elderly Friendly"),
    ("Kid-Friendly", "Kid-Friendly"),
]

LOCALITY_OPTIONS = [
    ("Downtown", "Downtown"),
    ("Mid Town", "Mid Town"),
    ("Suburb", "Suburb"),
    ("Hospitals", "Hospitals"),
    ("Schools", "Schools"),
]
ENGAGEMENT_CENTERS_OPTIONS = [
    ("Food Joints", "Food Joints"),
    ("Coffee Shops", "Coffee Shops"),
    ("Pubs", "Pubs"),
    ("Shopping Malls", "Shopping Malls"),
    ("Clubs", "Clubs"),
    ("Celebrity House Nearby", "Celebrity House Nearby"),
    ("Walkways", "Walkways"),
    ("Biking Paths", "Biking Paths"),
    ("Parks and Sit-Outs", "Parks and Sit-Outs"),
    ("Libraries", "Libraries"),
    ("Museums", "Museums"),
]

INDUSTRIES_NEARBY_OPTIONS = [
    ("Crowd", "Crowd"),
    ("Pollution", "Pollution"),
    ("Hazardous Waste Sites", "Hazardous Waste Sites"),
]

UTILITIES_OPTIONS = [
    ("Power", "Power"),
    ("Water", "Water"),
    ("Garbage", "Garbage"),
]
MAINTENANCE_OPTIONS = [
    ("Plumbing", "Plumbing"),
    ("Electricians", "Electricians"),
    ("Carpenters", "Carpenters"),
    ("Gardeners", "Gardeners"),
    ("Interior Decorators", "Interior Decorators"),
]

HISTORICAL_INFORMATION = [
    ("Environmental", "Environmental"),
    ("Air Quality", "Air Quality"),
    ("Flood History", "Flood History"),
    ("Hurricane Occurrence", "Hurricane Occurrence"),
]
Healthcare_INFORMATION = [
    ("Clinics and medical offices", "Clinics and medical offices"),
    ("Hospitals", "Hospitals"),
    ("Birth centers", "Birth centers"),
    ("Ambulatory care", "Ambulatory care"),
    ("Nursing homes", "Nursing homes"),
    ("Nursing homes", "Nursing homes"),
    ("Primary care", "Primary care"),
    ("Orthopedics", "Orthopedics"),

]

Local_Administration = [
    ("City Governments", "City Governments"),
    (" County Governments", " County Governments"),
    ("Special Districts", "Special Districts"),
    ("Enforcement Agencies", "Enforcement Agencies"),
    ("Fire and Emergency Medical Services", "Fire and Emergency Medical Services"),
    ("Local Courts", "Local Courts"),

]

Safety_Security_Choices = [
    ('Neighborhood Crime ', 'Neighborhood Crime '),
    ('Police Station ', 'Police Station '),
    ('Fire Station Proximity', 'Fire Station Proximity'),
    ('Security camera', 'Security Camera'),
]
Accessibility_Choices = [
    ('Proximity to Public Transit', 'Proximity to Public Transit'),
    ('Handicap Accessibility', 'Handicap Accessibility'),
    ('Proximity to Airport', 'Proximity to Airport'),
    ('Road Quality', 'Road Quality'),
]
Green_Spaces_Choices = [
    ('Proximity to Parks', 'Proximity to Parks'),
    ('Gardens/Greenery', 'Gardens/Greenery'),
    ('Pet-Friendly Areas', 'Pet-Friendly Areas'),
]

Education_Child_Care_Choices = [
    ('Schools Nearby', 'Schools Nearby'),
    ('Childcare Centers', 'Childcare Centers'),
    ('Playgrounds', 'Playgrounds'),
]

Weather_Factors_Choices = [
    ('Average Annual Rainfall', 'Average Annual Rainfall'),
    ('Snowfall', 'Snowfall'),
]
class PropertyForm(forms.ModelForm):
    # utilities = forms.ModelChoiceField(queryset=Utilities.objects.all(), required=True)

    population_mix = forms.MultipleChoiceField(
        choices=POPULATION_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    locality = forms.MultipleChoiceField(
        choices=LOCALITY_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    ENGAGEMENT_CENTERS = forms.MultipleChoiceField(
        choices=ENGAGEMENT_CENTERS_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    INDUSTRIES_NEARBY = forms.MultipleChoiceField(
        choices=INDUSTRIES_NEARBY_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    UTILITIES = forms.MultipleChoiceField(
        choices=UTILITIES_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    MAINTENANCE = forms.MultipleChoiceField(
        choices=MAINTENANCE_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    
    HISTORICAL = forms.MultipleChoiceField(
        choices=HISTORICAL_INFORMATION,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    Healthcare = forms.MultipleChoiceField(
        choices=Healthcare_INFORMATION,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    Administration = forms.MultipleChoiceField(
        choices=Local_Administration,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    Safety_Security = forms.MultipleChoiceField(
        choices=Safety_Security_Choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    Accessibility = forms.MultipleChoiceField(
        choices=Accessibility_Choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    
    Green_Spaces = forms.MultipleChoiceField(
        choices=Green_Spaces_Choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    Education_Child_Care = forms.MultipleChoiceField(
        choices=Education_Child_Care_Choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    Weather_Factors = forms.MultipleChoiceField(
        choices=Weather_Factors_Choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model=property
        fields='__all__'
        exclude = ['owners','visit_count']
    

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  # Set fields to non-required if needed
            field.widget.attrs['placeholder'] = '' 


class RatingForm(forms.Form):
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],  # 1 to 5 rating choices
        label="Rate this property",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']  # Only need to specify the image field