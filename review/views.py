from django.shortcuts import render, redirect
from .models import Hotel, Review, Rating

from .forms import ReviewForm

def hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(pk=hotel_id)
    reviews = hotel.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hotel = hotel
            review.user = request.user
            review.save()
            # Redirect or add success message as needed
    else:
        form = ReviewForm()
    context = {'hotel': hotel, 'reviews': reviews, 'form': form}
    return render(request, 'reviews/hotel_detail.html', context)


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReviewForm
from .models import Hotel


def submit_review(request, hotel_id):
    if request.method == 'POST':
        hotel = Hotel.objects.get(pk=hotel_id)
        user = request.user
        form = ReviewForm(request.POST)
        if form.is_valid():
            overall_rating = int(request.POST['overall_rating'])
            if overall_rating > 5:
                messages.error(request, 'Overall rating cannot exceed 5')
                return redirect('submit_review', hotel_id=hotel_id)

            # Save the form data to create a new Review object
            review = form.save(commit=False)
            review.hotel = hotel
            review.user = user
            review.save()
            return redirect('hotel_detail', hotel_id=hotel_id)
    else:
        # If the request method is not POST, render the form to submit review
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})

    # def staff_review(request, hotel_id):
    #     if request.method == 'POST' and request.user.is_authenticated and request.user.is_staff:
    #         hotel = Hotel.objects.get(pk=hotel_id)
    #         comment = request.POST['comment']
    #         rating_data = request.POST.dict()
    #         del rating_data['comment']
    #         del rating_data['csrfmiddlewaretoken']
    #         for aspect, stars in rating_data.items():
    #             Rating.objects.create(hotel=hotel, aspect=aspect, stars=stars)
    #         Review.objects.create(hotel=hotel, user=request.user, comment=comment)
    #         return redirect('reviews/hotel_detail', hotel_id=hotel_id)
    #     else:
    #         # Render form to input review for staff
    #         pass


from django.contrib.auth import login, authenticate
from .forms import SignUpForm

from django.contrib import messages

from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        # If the form is invalid, return the form with errors
    else:
        form = SignUpForm()

    # Add the form with errors to the template context
    return render(request, 'registration/signup.html', {'form': form})


def home_view(request):
    return render(request, 'reviews/home.html')


from django.shortcuts import render
from .models import Review

def user_review_results(request):
    # Get reviews submitted by the currently authenticated user
    user_reviews = Review.objects.filter(user=request.user)
    return render(request, 'reviews/review_results.html', {'user_reviews': user_reviews})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('hotel_detail', hotel_id=review.hotel_id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Review

def delete_review(request, review_id):
    # Retrieve the review object to be deleted
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        # Delete the review object
        review.delete()
        # Redirect to a suitable URL after successful deletion
        return redirect('review_results')  # Replace 'review_results' with the URL name of the page where you want to redirect

    # If request method is not POST, render a confirmation page or handle it as desired
    return render(request, 'reviews/delete_review_confirmation.html', {'review': review})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logoutView(request):
    logout(request)
    return redirect('login')
