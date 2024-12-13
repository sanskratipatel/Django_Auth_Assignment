# users/decorators.py
from django.shortcuts import redirect
from .models import UserProfile

def profile_complete_required(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            return redirect('complete_profile')  # Redirect to a page to complete profile
        return view_func(request, *args, **kwargs)
    return wrapper
