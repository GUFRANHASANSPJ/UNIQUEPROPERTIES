from properties.models import property
from django import forms

class PropertyForm(forms.ModelForm):
    class Meta:
        model=property
        fields='__all__'
        exclude = ['owners']

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False  # Set fields to non-required if needed
            field.widget.attrs['placeholder'] = '' 