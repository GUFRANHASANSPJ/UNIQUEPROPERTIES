from properties.models import *
from django import forms
from django.forms import modelformset_factory

Windows_OPTIONS = [
    ("Double Glazing", "Double Glazing"),
    ("Standard", "Standard"),
    
]

Smart_Home_Features_OPTIONS = [
    ("Sports", "Sports"),
    ("Arts", "Arts"),
    ("Volunteer", "Volunteer"),
]

Luxury_Amenities_OPTIONS = [
    ("Gym", "Gym"),
    ("Pool", "Pool"),
]

class PropertyForm(forms.ModelForm):
    window = forms.MultipleChoiceField(
        choices=Windows_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    Smart_Home_Features= forms.MultipleChoiceField(
        choices=Smart_Home_Features_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    Luxury_Amenities = forms.MultipleChoiceField(
        choices=Luxury_Amenities_OPTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model=property
        fields='__all__'
        exclude = ['owners','visit_count','images','lat', 'lng',"rating_count","rating","p_rating"]

    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        if latitude == '':
            return None  # Return None to store NULL in the database
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        if longitude == '':
            return None  # Return None to store NULL in the database
        return longitude


    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  # Set fields to non-required if needed
            field.widget.attrs['placeholder'] = '' 
            # Example: Customize specific fields if needed
        self.fields['description'].widget.attrs.update({'class': 'form-control w-75'})


class RatingForm(forms.Form):
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],  # 1 to 5 rating choices
        label="Rate this property",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
