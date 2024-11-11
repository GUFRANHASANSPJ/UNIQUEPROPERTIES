from django.urls import path
from properties import views

urlpatterns = [
    path("",views.index, name="index"),
    path("rental/",views.Rental, name="rental"),
    path("buy/",views.Buy, name="buy"),
    path('property_details/<int:id>/', views.property_details, name='property_details'),
    path('property_details_subscription/<int:id>/', views.property_details_Subscription, name='property_details_subscription'),
    path('search/', views.property_search, name='property_search'),
    path('addnewproperty/', views.AddNewProperty, name='addnewproperty'),
    path('edit_property/<int:property_id>/', views.edit_property, name='edit_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('buying_property/', views.Buying_Property, name='buying_property'),
    path('agent_details_for_users/<int:id>/', views.Agent_Details_For_users, name='agent_details_for_users'),
    path('property/<int:property_id>/rate/', views.submit_rating, name='submit_rating'),

]
