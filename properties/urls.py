from django.urls import path
from properties import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path("",views.index, name="index"),
    path("rental/",views.Rental, name="rental"),
    path("buy/",views.Buy, name="buy"),
    path("contact/",views.contact, name="contact"),
    path('about/', views.about_us, name='about_us'),
    path('property_details/<int:id>/', views.property_details, name='property_details'),
    path('property_details_subscription/<int:id>/', views.property_details_Subscription, name='property_details_subscription'),
    path('allimages/<int:id>/', views.all_images, name='all_images'),
    path('search/', views.property_search, name='property_search'),
    path('addnewproperty/', views.AddNewProperty, name='addnewproperty'),
    path('edit_property/<int:property_id>/', views.edit_property, name='edit_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('buying_property/<int:id>/', views.Buying_Property, name='buying_property'),
    path('agent_details_for_users/<int:id>/', views.Agent_Details_For_users, name='agent_details_for_users'),
    path('property/<int:property_id>/rate/', views.submit_rating, name='submit_rating'),
    path("chatbot/", views.chatbot_view, name="rule_based_chatbot"),
    path('viewed_property/', views.viewed_properties, name='viewed_property'),
    path('remove_viewed_properties/remove/<int:property_id>/', views.remove_from_viewed_properties, name='remove_from_viewed_properties'),

    path('contacted_property/', views.Contacted_properties, name='contacted_property'),
    path('remove_contacted_properties/remove/<int:property_id>/', views.Remove_from_contacted_properties, name='remove_from_contacted_properties'),
    path('properties-near-me/', properties_near_me, name='properties_near_me'),

    path('api/countries/', views.get_countries, name='get_countries'),
    path('api/states/<int:country_id>/', views.get_states, name='get_states'),
    path('api/cities/<int:state_id>/', views.get_cities, name='get_cities'),
    path('api/pincodes/<int:city_id>/', views.get_pincodes, name='get_pincodes'),
]   +static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
