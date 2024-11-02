from django.contrib import admin

from .models  import property_type,property
from accounts.models import property_owner
admin.site.register(property_type)
admin.site.register(property)
admin.site.register(property_owner)