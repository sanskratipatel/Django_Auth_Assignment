from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .decoraters import profile_complete_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.conf import settings
from django.http import HttpResponse
from .models import UserProfile
from .forms import CompleteProfileForm 
import random
import logging


logger = logging.getLogger(__name__)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        logger.info(f'Received email for OTP: {email}')  

        # Check if the email exists in the database
        if not User.objects.filter(email=email).exists():
            logger.warning(f'Attempt to send OTP to non-registered email: {email}')
            return render(request, 'users/forgot_password.html', {'error': 'Email not registered. Please sign up.'})

        otp = random.randint(100000, 999999)  

        try:
            # Send the OTP via email
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            logger.info(f'OTP sent to {email}')
        except Exception as e:
            logger.error(f'Error sending email: {e}')
            return render(request, 'users/forgot_password.html', {'error': 'Failed to send OTP. Please try again.'})

        # Store OTP and email in session for later verification
        request.session['otp'] = otp
        request.session['email'] = email
        return redirect('verify_otp')  # Redirect to OTP verification page

    return render(request, 'users/forgot_password.html')  # Render the forgot password page


# View to render OTP verification page
def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        
        # Check if the OTP matches
        if otp == str(request.session.get('otp')):
            # OTP verified, allow user to reset password
            return redirect('reset_password')
        else:
            # Invalid OTP
            return render(request, 'users/verify_otp.html', {'error': 'Invalid OTP'})
    
    return render(request, 'users/verify_otp.html')



def reset_password_view(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        email = request.session.get('email')  # Assuming you stored the email in the session after OTP verification

        try:
            user = User.objects.get(email=email)

            # Check if the new password matches the old password
            if user.check_password(new_password):
                messages.error(request, "New password cannot be the same as the old password.")
                return render(request, 'users/reset_password.html', {'error': 'New password cannot be the same as the old password.'})

            if new_password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return render(request, 'users/reset_password.html', {'error': 'Passwords do not match.'})

            # Set the new password
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password has been reset successfully.")
            return redirect('login')  # Redirect to the login page after successful password reset

        except User.DoesNotExist:
            messages.error(request, "User  not found.")
            return render(request, 'users/reset_password.html', {'error': 'User  not found.'})

    return render(request, 'users/reset_password.html') 


class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'users/change_password.html'  # Path to the template
    success_url = reverse_lazy('login') 


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves the User instance
            UserProfile.objects.create(user=user)  # Create the UserProfile instance
            login(request, user)  # Log the user in
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')



# @login_required
# def dashboard_view(request):
#     return render(request, 'users/dashboard.html', {'username': request.user.username})

# @login_required
# def dashboard_view(request):
#     profile = request.user.userprofile
#     context = {
#         'username': request.user.username,
#         'email': request.user.email,
#         'date_joined': profile.date_joined,
#         'last_updated': profile.last_updated,
#     }
#     return render(request, 'users/dashboard.html', context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserProfile

@login_required
def dashboard_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Create a new UserProfile if it doesn't exist
        profile = UserProfile.objects.create(user=request.user)
    
    context = {
        'username': request.user.username,
        'email': request.user.email,
        'date_joined': profile.date_joined,  # Use profile's date_joined
        'last_updated': profile.last_updated,  # Use profile's last_updated
    }
    return render(request, 'users/dashboard.html', context)


@login_required
def profile_view(request):
    # Fetch user profiles from the database
    user = UserProfile.objects.all()  # Adjust the query as needed
    return render(request, 'users/profile.html', {'user_profiles': user})



# def profile_complete_required(view_func):
#     def wrapper(request, *args, **kwargs):
#         try:
#             profile = request.user.userprofile
#         except UserProfile.DoesNotExist:
#             return redirect('complete_profile')  # Redirect to a page to complete profile
#         return view_func(request, *args, **kwargs)
#     return wrapper

from django.shortcuts import render, redirect
from .forms import CompleteProfileForm

@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = CompleteProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CompleteProfileForm(instance=request.user.userprofile)
    return render(request, 'users/complete_profile.html', {'form': form})


