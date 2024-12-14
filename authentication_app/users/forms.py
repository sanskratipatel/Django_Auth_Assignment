# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import UserProfile

# class CompleteProfileForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=30, required=True)
#     last_name = forms.CharField(max_length=30, required=True)

#     class Meta:
#         model = UserProfile
#         fields = ['date_of_birth', 'phone_number']  # Add other UserProfile fields here

#     def save(self, commit=True):
#         # Save changes to the User model (first_name and last_name)
#         user = self.instance.user
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         if commit:
#             user.save()  # Save user changes
#             super().save(commit=commit)  # Save UserProfile model changes
#         return self.instance

# class SignUpForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirmation = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirmation = cleaned_data.get('password_confirmation')

#         if password != password_confirmation:
#             raise forms.ValidationError("Passwords do not match.")
#         return cleaned_data

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CompleteProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'phone_number', 'address']  # Add other UserProfile fields here

    def save(self, commit=True):
        # Save changes to the User model (first_name and last_name)
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()  # Save user changes
            super().save(commit=commit)  # Save UserProfile model changes
        return self.instance

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


