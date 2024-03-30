# reviews/forms.py
from django import forms
from .models import Review, Rating, Hotel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Add this import
from django import forms
from .models import Review

from django import forms
from .models import Review

from django import forms
from .models import Review

from django import forms
from django.core.exceptions import ValidationError
from .models import Review

from django import forms
from django.core.exceptions import ValidationError
from .models import Review

class ReviewForm(forms.ModelForm):
    overall_rating = forms.ChoiceField(choices=[
        (1, 'Bad'),
        (2, 'Average'),
        (3, 'Fair'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ], widget=forms.Select(attrs={'class': 'form-control'}))

    # Ensure that ratings do not exceed 5
    def clean(self):
        cleaned_data = super().clean()
        ratings = ['cleanliness_rating', 'staff_rating', 'amenities_rating']
        for rating in ratings:
            if rating in cleaned_data and int(cleaned_data[rating]) > 5:
                self.add_error(rating, 'Rating cannot exceed 5')

    class Meta:
        model = Review
        fields = ['overall_rating', 'cleanliness_rating', 'staff_rating', 'amenities_rating', 'text']

# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ['stars']
#
# class HotelForm(forms.ModelForm):
#     class Meta:
#         model = Hotel
#         fields = ['name', 'description']
# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
#
# class CustomAuthenticationForm(AuthenticationForm):
#     # Add any customizations here
#     pass


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
