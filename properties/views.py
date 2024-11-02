from django.shortcuts import render, get_object_or_404,redirect
from properties.models import property
from accounts.models import *
from properties.forms import PropertyForm
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    rental_properties=property.objects.all()
    top_visited_properties = property.objects.order_by('-visit_count')[:3]
    return render(request,"index.html", {"rental_properties":rental_properties,
                                         "top_visited_properties": top_visited_properties,}) 

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

    owner_id= property_detail.owners.id
    agent_id= property_detail.owners.id
    owner_details= get_object_or_404(User, id=owner_id)
    agent_details= get_object_or_404(User, id=agent_id)

    # Get wishlist items for the current user
    wishlist_items = Wishlist.objects.filter(user=request.user).values_list('property_id', flat=True) if request.user.is_authenticated else []
    context={
        'property_detail': [property_detail],
        'owner_details': [owner_details],
        'agent_details': [agent_details],
        'wishlist_items': wishlist_items,
    }
    return render(request, 'property_details.html', context)


def property_search(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        # Filter properties by address (case-insensitive search)
        properties = property.objects.filter(address__icontains=query)
    else:
        # If no search query is provided, return all properties
        properties = property.objects.all()

    return render(request, 'property_search_results.html', {'properties': properties, 'query': query})

# def AddNewProperty(request):
#     if request.method == "POST":
#         form = PropertyForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_property = form.save(commit=False)
            
#             # Check if the logged-in user is an owner or agent
#             try:
#                 if hasattr(request.user, 'property_owner'):
#                     new_property.owners = request.user.property_owner.owner  # Assign property_owner's user ID
#                 elif hasattr(request.user, 'Agents'):
#                     new_property.owners = request.user.Agents.agent  # Assign agent's user ID
#                 else:
#                     messages.error(request, "User must be a property owner or agent to add properties.")
#                     return redirect('addnewproperty')
                
#                 new_property.save()
#                 messages.success(request, "Property added successfully!")
#                 return redirect("ownerdetails")
                
#             except Exception as e:
#                 messages.error(request, f"An error occurred: {str(e)}")
#     else:
#         form = PropertyForm()

#     return render(request, 'addnewproperty.html', {"form": form})

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


