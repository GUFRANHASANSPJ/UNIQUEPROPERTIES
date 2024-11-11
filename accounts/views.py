from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile,property_owner,Wishlist
from properties.models import property
from accounts.forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages

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
            return HttpResponse("Check your credentials!")
    return render(request, "accounts/login.html")

def UserDetails(request):
    has_subscription = Subscription.objects.filter(user=request.user).exists()
    UserDetails=UserProfile.objects.get(user=request.user)
    return render(request,'accounts/userdetails.html',{'UserDetails':UserDetails,"has_subscription":has_subscription})

def edit_user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('userdetails')
    else:
        form = EditUserProfileForm(instance=user_profile)
    return render(request, 'accounts/edit_user_details.html', {'form': form})

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
    owner_profile = get_object_or_404(property_owner, owner=request.user)
    if request.method == 'POST':
        form = EditOwnerProfileForm(request.POST, request.FILES, instance=owner_profile)
        if form.is_valid():
            form.save()
            return redirect('ownerdetails')
    else:
        form = EditOwnerProfileForm(instance=owner_profile)
    return render(request, 'accounts/edit_owner_details.html', {'form': form})

def OwnerDetails(request):
    OwnerDetails=property_owner.objects.get(owner=request.user)
    OwnerProperties = property.objects.filter(owners=request.user).order_by('id')
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
    property_item = property.objects.get(id=property_id)
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