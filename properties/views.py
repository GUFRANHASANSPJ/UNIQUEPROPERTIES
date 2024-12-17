from django.shortcuts import render, get_object_or_404,redirect
from properties.models import property
from accounts.models import *
from properties.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
import requests
from django.core.paginator import Paginator
from .utils import *
from django.utils.text import slugify
from django.core.mail import send_mail
from django.contrib import messages
import math
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from properties.utils import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    rental_properties=property.objects.all()
    # Check if the user has an active subscription
    has_subscription = (
        Subscription.objects.filter(user=request.user).exists()
        if request.user.is_authenticated
        else False
    )
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
    top_visited_properties = property.objects.order_by('-visit_count')[:3]
    recently_added_property= property.objects.order_by('-posted_date')[:5]
    top_rated_property= property.objects.order_by('-p_rating')[:5]
    top_agents = Agents.objects.order_by('-id')[:3]

    return render(request,"index.html", {"rental_properties":rental_properties,
                                         "has_subscription":has_subscription,
                                         'top_agents':top_agents,
                                         'top_visited_properties':top_visited_properties,
                                         'recently_added_property':recently_added_property,
                                         'top_rated_property':top_rated_property,
                                         'wishlist_items':wishlist_items,
                                         }) 

def Rental(request):
    # Initialize query parameters
    sort_by = request.GET.get('sort')  # Get the 'sort' parameter
    sort_order = request.GET.get('order')  # Get the 'order' parameter
    
    # Start with a base query for rental properties
    rental_properties = property.objects.filter(post_type='Rent')

    # Only apply sorting if both 'sort' and 'order' parameters are present
    if sort_by and sort_order:
        # Determine the sort field
        if sort_by == 'price':
            sort_field = 'property_price'
        elif sort_by == 'date':
            sort_field = 'posted_date'  # Ensure this matches your model field
        
        # Reverse the sort order if 'desc' is specified
        if sort_order == 'desc':
            sort_field = f"-{sort_field}"
        
        # Apply sorting
        rental_properties = rental_properties.order_by(sort_field)

    # Get the wishlist items if the user is authenticated
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []

    # Paginate the results
    paginator = Paginator(rental_properties, 6)  # Show 6 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass context to the template
    return render(
        request, 
        "rental.html", 
        {
            "page_obj": page_obj, 
            "wishlist_items": wishlist_items, 
            "sort_by": sort_by or "",  # Pass empty string if not sorted
            "sort_order": sort_order or ""  # Pass empty string if no order selected
        }
    )


def Buy(request):
    buying_properties=property.objects.filter(post_type= 'Sell')

    sort_by = request.GET.get('sort')  # Get the 'sort' parameter
    sort_order = request.GET.get('order')  # Get the 'order' parameter
    # Only apply sorting if both 'sort' and 'order' parameters are present
    if sort_by and sort_order:
        # Determine the sort field
        if sort_by == 'price':
            sort_field = 'property_price'
        elif sort_by == 'date':
            sort_field = 'posted_date'  # Ensure this matches your model field
        
        # Reverse the sort order if 'desc' is specified
        if sort_order == 'desc':
            sort_field = f"-{sort_field}"
        
        # Apply sorting
        buying_properties = buying_properties.order_by(sort_field)

    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
    paginator = Paginator(buying_properties, 6)  # Show 6 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the appropriate page of results
    context= {
        "page_obj": page_obj, 
        "wishlist_items": wishlist_items, 
        "sort_by": sort_by or "",  # Pass empty string if not sorted
        "sort_order": sort_order or ""  # Pass empty string if no order selected
    }
    return render(request,"buy.html", context) 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send an email (customize email settings in settings.py)
        send_mail(
            subject,
            f"Message from {name} ({email}):\n\n{message}",
            email,
            ['gufran.h@intrustglobal.co.in'],  # Replace with your email
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return render(request, 'contact.html')  # Reload page after submission

    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about_us.html')

def property_details(request, id):
    property_detail = get_object_or_404(property, id=id)
    similar_properties = get_similar_properties(property_detail, limit=4)
    # Increment visit count
    property_detail.visit_count += 1
    property_detail.save()
    # Record the property as viewed for authenticated users
    if request.user.is_authenticated:
        ViewedProperty.objects.get_or_create(user=request.user, property=property_detail)

    has_subscription = (
        Subscription.objects.filter(user=request.user).exists()
        if request.user.is_authenticated
        else False
    )
    owner_id= property_detail.owners.id
    agent_id= property_detail.owners.id
    property_images=property_detail.images
    owner_details= get_object_or_404(property_owner, owner_id=owner_id)
    owner_details_auth= get_object_or_404(User, id=owner_id)
    # agent_details= get_object_or_404(Agents, agent_id=agent_id)
    form = RatingForm()

    # Get wishlist items for the current user
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
    context={
        'property_detail': [property_detail],
        'owner_details': [owner_details],
        'owner_details_auth': [owner_details_auth],
        # 'agent_details': [agent_details],
        'wishlist_items': wishlist_items,
        'has_subscription': has_subscription,
        'form': form,
        'property_images': property_images,
        'similar_properties': similar_properties,
    }
    print(similar_properties)
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
    owner_details_auth= get_object_or_404(User, id=owner_id)
    # agent_details= get_object_or_404(Agents, agent_id=agent_id)
    property_images=property_detail.images
    # Get wishlist items for the current user
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
    context={
        'property_detail': [property_detail],
        'owner_details': [owner_details],
        'owner_details_auth': owner_details_auth,
        # 'agent_details': [agent_details],
        'wishlist_items': wishlist_items,
        'has_subscription': has_subscription,
        'property_images': property_images,
    }
    return render(request, 'property_details_subscription.html', context)

def all_images(request, id):
    property_detail = get_object_or_404(property, id=id)
    return render(request, 'all_images.html',{"property_detail":property_detail})


def property_search(request):
    query = request.GET.get('q')  # Get the search query
    filters = {}

    # Filtering by query (e.g., address)
    if query:
        filters['city__icontains'] = query

    # Filtering by property type
    property_type = request.GET.get('property_type')  # E.g., "Rent" or "Sell"
    if property_type:
        filters['post_type'] = property_type

    # Filtering by price range
    min_price = request.GET.get('min_price')  # Minimum price
    if min_price:
        filters['property_price__gte'] = min_price

    max_price = request.GET.get('max_price')  # Maximum price
    if max_price:
        filters['property_price__lte'] = max_price

    # Filtering by city
    city = request.GET.get('city')
    if city:
        filters['city__icontains'] = city

    # Filtering by property_info
    property_info = request.GET.get('property_info')
    if property_info:
        filters['proprty_info__icontains'] = property_info

    # Filtering by pet_friendly
    pet_friendly = request.GET.get('pet_friendly')
    if pet_friendly:
        # Assuming `pet_friendly` is stored as a boolean in the database
        filters['pet_friendly'] = True if pet_friendly.lower() in ['true', '1', 'yes'] else False



    # Perform the query
    properties = property.objects.filter(**filters)
    # Get the wishlist items if the user is authenticated
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
     # Paginate the results
    paginator = Paginator(properties, 6)  # Show 6 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Render the results
    context={
        'page_obj': page_obj,
        "wishlist_items":wishlist_items,
        'query': query

    }
    return render(request, 'property_search_results.html',context )



def Agent_Details_For_users(request,id):
    agent_details = get_object_or_404(Agents, id=id)
    return render(request,'accounts/agent_details_for_users.html',{"agent_details":agent_details})



def AddNewProperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.owners = request.user

            # Process images
            image_files = request.FILES.getlist('images')
            if image_files:
                property_instance.images = save_images_to_property_folder(property_instance.name, image_files)

            property_instance.save()

            # Calculate and assign overall rating
            property_instance.p_rating = calculate_overall_rating(property_instance)
            property_instance.save()

            return redirect('index')  # Redirect after saving

    else:
        form = PropertyForm()

    # return render(request, 'addnewproperty.html', {'form': form})
    return render(request, 'address.html', {'form': form})


def edit_property(request, property_id):
    # Retrieve the specific property by its ID
    property_instance = get_object_or_404(property, id=property_id)

    if request.method == 'POST':
        # Bind form with POST data and file data for updating
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
           # Save changes to the property, including images
            property_instance = form.save(commit=False)
            # Process images
            image_files = request.FILES.getlist('images')
            if image_files:
                property_instance.images = save_images_to_property_folder(property_instance.name, image_files)

            property_instance.save()

            # Extract latitude and longitude from the POST data
            property_instance.lat = request.POST.get('lat')
            property_instance.lng = request.POST.get('lng')

            # After saving, recalculate and update the rating
            property_instance.p_rating = calculate_overall_rating(property_instance)
            
            # Save the property instance with the updated rating
            property_instance.save()
            return redirect('index') 
             # Redirect to the owner details page
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

def Buying_Property(request,id):
    property_detail = get_object_or_404(property, id=id)

    # Record the property as viewed for authenticated users
    if request.user.is_authenticated:
        Contacted_Property.objects.get_or_create(user=request.user, property=property_detail)

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

# Chatbot view
def chatbot_view(request):
    if request.method == 'POST':
        # Get the message sent by the user from the request
        user_message = request.POST.get('message', '').strip().lower()

        # Process the message and generate a response using regex
        bot_response = get_bot_response(user_message)

        # Return the bot response as a JSON
        return JsonResponse({'response': bot_response})

    # If the request is GET, simply render the chatbot page
    return render(request, 'chatbot.html')



def viewed_properties(request):
    if request.user.is_authenticated:
        # Get properties viewed by the logged-in user
        viewed_properties = ViewedProperty.objects.filter(user=request.user).select_related('property')
    else:
        viewed_properties = []

    return render(request, 'viewed_properties.html', {'viewed_properties': viewed_properties})

@login_required
def remove_from_viewed_properties(request, property_id):
    ViewedProperty.objects.filter(user=request.user, property_id=property_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def Contacted_properties(request):
    if request.user.is_authenticated:
        # Get properties viewed by the logged-in user
        contacted_properties = Contacted_Property.objects.filter(user=request.user).select_related('property')
    else:
        contacted_properties = []

    return render(request, 'contacted_properties.html', {'contacted_properties': contacted_properties})

@login_required
def Remove_from_contacted_properties(request, property_id):
    Contacted_Property.objects.filter(user=request.user, property_id=property_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def properties_near_me(request):
    # Get latitude and longitude from the request
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')

    if not lat or not lng:
        return render(request, 'error.html', {'message': 'Location not provided'})

    # Radius in kilometers
    RADIUS_KM = 15000

    # Haversine formula
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # Earth radius in km
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        return R * c

    # Fetch all properties and filter based on distance
    properties = property.objects.all()
    nearby_properties = []

    for prop in properties:
        if prop.lat and prop.lng:
            distance = haversine(float(lat), float(lng), float(prop.lat), float(prop.lng))
            if distance <= RADIUS_KM:
                nearby_properties.append({
                    'property': prop,
                    'distance': round(distance, 2)  # Round the distance to 2 decimal places
                })
    # Render the template with properties and their distances
    return render(request, 'nearby_properties.html', {'properties': nearby_properties})


def get_countries(request):
    countries = Country.objects.values('id', 'name', 'country_code')
    return JsonResponse(list(countries), safe=False)

def get_states(request, country_id):
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(states), safe=False)

def get_cities(request, state_id):
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)

def get_pincodes(request, city_id):
    pincodes = Pincode.objects.filter(city_id=city_id).values('id', 'pincode')
    return JsonResponse(list(pincodes), safe=False)