from django.urls import path
from properties import views
urlpatterns = [
    path("",views.index, name="index"),
    path("rental/",views.Rental, name="rental"),
    path("buy/",views.Buy, name="buy"),
    path('property_details/<int:id>/', views.property_details, name='property_details'),
    path('search/', views.property_search, name='property_search'),
    path('addnewproperty/', views.AddNewProperty, name='addnewproperty'),
    path('edit_property/<int:property_id>/', views.edit_property, name='edit_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('buying_property/', views.Buying_Property, name='buying_property'),

]
