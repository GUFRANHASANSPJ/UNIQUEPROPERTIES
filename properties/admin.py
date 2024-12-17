from django.contrib import admin

from .models  import *
from accounts.models import *
admin.site.register(property)
admin.site.register(property_owner)
admin.site.register(Subscription)
admin.site.register(UserProfile)
admin.site.register(Agents)
