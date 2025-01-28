from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('userreg/',views.User_Registration,name='userreg'),
    path("userlogin/", views.UserLogin, name="userlogin"),
    path("userdetails",views.UserDetails,name="userdetails"),
    path('edit_user_profile/', views.edit_user_profile, name='edit_user_details'),
    # path("adminlogin/", views.OwnerLogin, name="adminlogin"),
    
    
    path('ownerreg/',views.Owner_Registration,name='ownerreg'),
    path("ownerdetails",views.OwnerDetails,name="ownerdetails"),
    path('edit_owner_profile/', views.edit_owner_profile, name='edit_owner_details'),

    path('agentreg/',views.Agent_Registration,name='agentreg'),
    path("agentdetails",views.AgentDetails,name="agentdetails"),
    path('edit_agent_profile/', views.edit_agent_profile, name='edit_agent_details'),

    path('login/',views.UserLogin, name='login'),
    path("logout",views.UserLogout,name="logout"),
    
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('wishlist/add/<int:property_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:property_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('mark-as-sold/<int:property_id>/', views.mark_as_sold, name='mark_as_sold'),

    path('subscribe/', views.create_subscription, name='create_subscription'),
    path('recommended_property/', views.recommended_property, name='recommended_property'),

    # Password reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
