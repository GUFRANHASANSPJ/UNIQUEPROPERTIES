from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile,property_owner,Wishlist
from properties.models import property as propertymodel
from accounts.forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def User_Registration(request):
    registation=False
    if request.method=='POST':
        form1 = UserForm1(request.POST, request.FILES)
        form2 = UserForm2(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()

            profile=form2.save(commit=False)
            profile.user=user
            profile.save()
            messages.success(request, "Resistered successfully!")
            registation=True
            return redirect('login')
    else:
        form1 = UserForm1()
        form2=UserForm2()
    return render(request,"accounts/usereg.html",{"form1":form1,"form2":form2, "registation":registation})

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "Logged in  successfully!")
                return redirect("index")
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("Check your credentials!!")
    return render(request, "accounts/login.html")

def UserDetails(request):
    has_subscription = Subscription.objects.filter(user=request.user).exists()
    UserDetails=UserProfile.objects.get(user=request.user)
    return render(request,'accounts/userdetails.html',{'UserDetails':UserDetails,"has_subscription":has_subscription})

def edit_user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form1 = EditUserProfileForm1(request.POST, request.FILES, instance=request.user)
        form2 = EditUserProfileForm2(request.POST, request.FILES, instance=user_profile)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.save()

            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('userdetails')
    else:
        form1 = EditUserProfileForm1(instance=request.user)
        form2 = EditUserProfileForm2(instance=user_profile)
    return render(request, 'accounts/edit_user_details.html', {'form1': form1, 'form2': form2 })

def UserLogout(request):
    logout(request)
    messages.success(request, "Logout successfully!")
    return redirect("login")

def Owner_Registration(request):
    registation=False
    if request.method=='POST':
        form1 = OwnerForm1(request.POST, request.FILES)
        form2 = OwnerForm2(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()

            profile=form2.save(commit=False)
            profile.owner=user
            profile.save()
            registation=True
            return redirect('login')
    else:
        form1 = OwnerForm1()
        form2=OwnerForm2()
    return render(request,"accounts/ownerreg.html",{"form1":form1,"form2":form2, "registation":registation})


def OwnerLogin(request):
    if request.method == 'POST':
        username = request.POST.get("admin_username")
        password = request.POST.get("admin_password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect("index")
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("Check your credentials!")
    return render(request, "accounts/login.html")


def edit_owner_profile(request):
    # Get the profile of the currently logged-in user
    owner_profile = get_object_or_404(property_owner, owner=request.user)

    if request.method == 'POST':
        # Pass the logged-in user's instance to the form
        form1 = EditOwnerProfileForm1(request.POST, instance=request.user)
        form2 = EditOwnerProfileForm2(request.POST, request.FILES, instance=owner_profile)

        if form1.is_valid() and form2.is_valid():
            # Save form1 (User model changes)
            user = form1.save(commit=False)
            user.save()

            # Save form2 (property_owner model changes)
            profile = form2.save(commit=False)
            profile.owner = user
            profile.save()

            return redirect('ownerdetails')
    else:
        # Pass the logged-in user's instance to the form
        form1 = EditOwnerProfileForm1(instance=request.user)
        form2 = EditOwnerProfileForm2(instance=owner_profile)

    return render(request, 'accounts/edit_owner_details.html', {'form1': form1, 'form2': form2})

@login_required
def OwnerDetails(request):
    OwnerDetails=property_owner.objects.get(owner=request.user)
    OwnerProperties = propertymodel.objects.filter(owners=request.user).order_by('id')
    # OwnerProperties = property.objects.filter(owners =OwnerDetails).order_by('id')
    return render(request,'accounts/ownerdetails.html',{'OwnerDetails':OwnerDetails,'OwnerProperties':OwnerProperties})

def OwnerLogout(request):
    logout(request)
    messages.success(request, "Logout successfully!")
    return redirect("login")

# def UserDetails(request):
#     if request.user.UserProfile.user_type =='regular':
#         print(request.user.id)
#         UserDetails=UserProfile.objects.get(user=request.user)
#         return render(request,'accounts/userdetails.html',{'UserDetails':UserDetails})
#     else:
#         print("hi")
#         UserDetails=property_owner.objects.get(owner=request.user)
#         return render(request,'accounts/ownerdetails.html',{'UserDetails':UserDetails})


def Agent_Registration(request):
    registation=False
    if request.method=='POST':
        form1 = AgentForm1(request.POST, request.FILES)
        form2 = AgentForm2(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()

            profile=form2.save(commit=False)
            profile.agent=user
            profile.save()
            messages.success(request, "Resistered successfully!")
            registation=True
            return redirect('login')
    else:
        form1 = AgentForm1()
        form2=AgentForm2()
    return render(request,"accounts/usereg.html",{"form1":form1,"form2":form2, "registation":registation})

def edit_agent_profile(request):
    agent_profile = get_object_or_404(Agents, agent=request.user)
    if request.method == 'POST':
        form = EditAgentProfileForm(request.POST, request.FILES, instance=agent_profile)
        if form.is_valid():
            form.save()
            return redirect('agentdetails')
    else:
        form = EditAgentProfileForm(instance=agent_profile)
    return render(request, 'accounts/edit_agent_details.html', {'form': form})


def AgentDetails(request):
    AgentDetails=Agents.objects.get(agent =request.user)
    AgentProperties = property.objects.filter(owners = request.user).order_by('id')
    return render(request,'accounts/agentdetails.html',{'AgentDetails':AgentDetails,
                                                        'AgentProperties':AgentProperties,})


# Wishlist section

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'accounts/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, property_id):
    property_item = propertymodel.objects.get(id=property_id)
    Wishlist.objects.get_or_create(user=request.user, property=property_item)
    # return redirect('wishlist')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_from_wishlist(request, property_id):
    Wishlist.objects.filter(user=request.user, property_id=property_id).delete()
    # return redirect('wishlist')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def create_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page or another view
    else:
        form = SubscriptionForm(user=request.user)
    return render(request, 'accounts/subscription_form.html', {'form': form})

def recommended_property(request):
    form = PropertySearchForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        print(form.cleaned_data)  # Debugging: print the cleaned form data
        
        # Initialize an empty list to store the matching score for each property
        properties_scores = []
        
        # Fetch all properties
        all_properties = propertymodel.objects.all()

        # Loop through all properties and score each one
        for property in all_properties:
            score = 0  # Start with a score of 0 for each property
            
            # Property Type Matching
            if form.cleaned_data.get('property_type') and form.cleaned_data['property_type'] != 'None':
                if property.property_type == form.cleaned_data['property_type']:
                    score += 10  # Add 10 points for exact match

            # Price Range Matching
            if form.cleaned_data.get('min_price') and form.cleaned_data.get('max_price'):
                if property.property_price >= form.cleaned_data['min_price'] and property.property_price <= form.cleaned_data['max_price']:
                    score += 8  # Add 8 points for price match

            # Property Size Matching
            if form.cleaned_data.get('min_sqft') and form.cleaned_data.get('max_sqft'):
                if property.area >= form.cleaned_data['min_sqft'] and property.area <= form.cleaned_data['max_sqft']:
                    score += 7  # Add 7 points for size match

            # Bedrooms and Bathrooms Matching
            if form.cleaned_data.get('bed'):
                if form.cleaned_data['bed'] == '1' and property.bed == 1:
                    score += 5
                elif form.cleaned_data['bed'] == '2' and property.bed == 2:
                    score += 5
                elif form.cleaned_data['bed'] == '3+' and property.bed >= 3:
                    score += 5

            if form.cleaned_data.get('bath'):
                if form.cleaned_data['bath'] == '1' and property.bath == 1:
                    score += 5
                elif form.cleaned_data['bath'] == '2' and property.bath == 2:
                    score += 5
                elif form.cleaned_data['bath'] == '3+' and property.bath >= 3:
                    score += 5

            # Features and Amenities Matching
            if form.cleaned_data.get('balcony') and property.balcony:
                score += 4  # Add points if property has a balcony
            if form.cleaned_data.get('garden') and property.garden:
                score += 4  # Add points if property has a garden
            if form.cleaned_data.get('parking') and property.parking == form.cleaned_data['parking']:
                score += 3  # Add points for matching parking type
            if form.cleaned_data.get('Smart_Home_Features') and form.cleaned_data['Smart_Home_Features'].lower() in property.Smart_Home_Features.lower():
                score += 6  # Add points if Smart Home Features match

            # Lifestyle Preferences Matching
            if form.cleaned_data.get('post_type') and property.post_type == form.cleaned_data['post_type']:
                score += 5  # Add points if post type matches

            # Building Age Matching
            if form.cleaned_data.get('Building_Age'):
                if property.Building_Age <= form.cleaned_data['Building_Age']:
                    score += 6  # Add points if building age is within the user's preference

            # Security Features Matching
            if form.cleaned_data.get('Neighborhood_Crime_Rate') and property.Neighborhood_Crime_Rate == form.cleaned_data['Neighborhood_Crime_Rate']:
                score += 4  # Add points for crime rate match

            # Add the property and its score to the list
            properties_scores.append((property, score))
        
        # Sort properties based on their score in descending order (higher score = better match)
        properties_scores.sort(key=lambda x: x[1], reverse=True)

        # Now filter out the properties with the highest scores
        recommended_properties = [item[0] for item in properties_scores if item[1] > 0]  # Only properties with a positive score

        # Pagination
        paginator = Paginator(recommended_properties, 6)  # Show 6 properties per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Render the results
        return render(request, 'accounts/recommended_property_results.html', {'recommended_properties': recommended_properties, 'form': form})

    # If the form is not valid or it's a GET request, render the form
    return render(request, 'accounts/recommended_property.html', {'form': form})