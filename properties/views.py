from django.shortcuts import render, get_object_or_404,redirect
from properties.models import property
from accounts.models import *
from properties.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
import os

def index(request):
    rental_properties=property.objects.all()
    # Check if the user has an active subscription
    has_subscription = Subscription.objects.filter(user=request.user).exists()
    top_visited_properties = property.objects.order_by('-visit_count')[:3]
    top_agents = Agents.objects.order_by('-id')[:3]

    return render(request,"index.html", {"rental_properties":rental_properties,
                                         "top_visited_properties": top_visited_properties,
                                         'top_agents':top_agents,
                                         'has_subscription':has_subscription}) 

def Rental(request):
    rental_properties=property.objects.all()
    return render(request,"rental.html", {"rental_properties":rental_properties}) 

def Buy(request):
    buying_properties=property.objects.all()
    return render(request,"buy.html", {"buying_properties":buying_properties}) 

def property_details(request, id):
    property_detail = get_object_or_404(property, id=id)
    # Increment visit count
    property_detail.visit_count += 1
    property_detail.save()
    has_subscription = Subscription.objects.filter(user=request.user).exists()
    owner_id= property_detail.owners.id
    agent_id= property_detail.owners.id
    owner_details= get_object_or_404(property_owner, owner_id=owner_id)
    # agent_details= get_object_or_404(Agents, agent_id=agent_id)

    # Get wishlist items for the current user
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
    context={
        'property_detail': [property_detail],
        'owner_details': [owner_details],
        # 'agent_details': [agent_details],
        'wishlist_items': wishlist_items,
        'has_subscription': has_subscription,
    }
    return render(request, 'property_details.html', context)

def property_details_Subscription(request, id):
    property_detail = get_object_or_404(property, id=id)
    # Increment visit count
    property_detail.visit_count += 1
    property_detail.save()
    has_subscription = Subscription.objects.filter(user=request.user).exists()
    owner_id= property_detail.owners.id
    agent_id= property_detail.owners.id
    owner_details= get_object_or_404(property_owner, owner_id=owner_id)
    # agent_details= get_object_or_404(Agents, agent_id=agent_id)

    # Get wishlist items for the current user
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
    context={
        'property_detail': [property_detail],
        'owner_details': [owner_details],
        # 'agent_details': [agent_details],
        'wishlist_items': wishlist_items,
        'has_subscription': has_subscription,
    }
    return render(request, 'property_details_subscription.html', context)


def property_search(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        # Filter properties by address (case-insensitive search)
        properties = property.objects.filter(address__icontains=query)
    else:
        # If no search query is provided, return all properties
        properties = property.objects.all()

    return render(request, 'property_search_results.html', {'properties': properties, 'query': query})


def Agent_Details_For_users(request,id):
    agent_details = get_object_or_404(Agents, id=id)
    return render(request,'accounts/agent_details_for_users.html',{"agent_details":agent_details})



def AddNewProperty(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)  # Bind data to the form
        if form.is_valid():  # Check if the form data is valid
            new_property = form.save(commit=False)  # Create, but don’t save to the DB yet
            new_property.owners = request.user  # Optional: link with the current user’s owner profile
            new_property.save()  # Save the new property to the database
            messages.success(request, "Property added successfully!")
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            return redirect("index")

    else:
        form = PropertyForm()  # Create an empty form for GET requests

    return render(request, 'addnewproperty.html', {"form": form})

# def AddNewProperty(request):
#     if request.method == 'POST':
#         property_form = PropertyForm(request.POST)
#         PropertyImageFormSet = modelformset_factory(PropertyImage, form=PropertyImageForm, extra=3)  # Allows up to 3 images
#         formset = PropertyImageFormSet(request.POST, request.FILES)

#         if property_form.is_valid() and formset.is_valid():
#             property_instance = property_form.save()

#             for form in formset:
#                 image = form.cleaned_data.get('image')
#                 if image:
#                     PropertyImage.objects.create(property=property_instance, image=image)

#             return redirect('index')  # Redirect to the property listing page after saving

#     else:
#         property_form = PropertyForm()
#         PropertyImageFormSet = modelformset_factory(PropertyImage, form=PropertyImageForm, extra=3)
#         formset = PropertyImageFormSet(queryset=PropertyImage.objects.none())  # Start with an empty formset

#     return render(request, 'addnewproperty.html', {'property_form': property_form, 'formset': formset})

# def AddNewProperty(request):
#     if request.method == "POST":
#         form = PropertyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")  # replace with your success URL
#     else:
#         form = PropertyForm()
#     return render(request, "addnewproperty.html", {"form": form})



def edit_property(request, property_id):
    # Retrieve the specific property by its ID
    property_instance = get_object_or_404(property, id=property_id)

    if request.method == 'POST':
        # Bind form with POST data and file data for updating
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        print(request.FILES) 
        if form.is_valid():
            form.save()  # Save changes to the property, including image
            return redirect('index')  # Redirect to the owner details page
    else:
        # Display form with current property data
        form = PropertyForm(instance=property_instance)

    return render(request, 'edit_property.html', {'form': form})


def delete_property(request, property_id):
    # Retrieve the specific property by its ID
    property_instance = get_object_or_404(property, id=property_id)

    if request.method == 'POST':
        property_instance.delete()  # Delete the property from the database
        return redirect('index')  # 

    return render(request, 'confirm_delete.html', {'property': property_instance})

def Buying_Property(request):
    return render(request,'accounts/buying_property.html')


def submit_rating(request, property_id):
    property_instance = get_object_or_404(property, id=property_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            new_rating = int(form.cleaned_data['rating'])

            # Update the average rating
            total_rating = property_instance.rating * property_instance.rating_count
            property_instance.rating_count += 1
            property_instance.rating = round((total_rating + new_rating) / property_instance.rating_count, 1)
            property_instance.save()

            messages.success(request, "Thank you for rating!")
            return redirect('property_details', id=property_id)

    else:
        form = RatingForm()

    return render(request, 'submit_rating.html', {'form': form, 'property': property_instance})