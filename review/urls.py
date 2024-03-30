# reviews/urls.py
from django.urls import path
from . import views
from .views import hotel_detail, signup, home_view, user_review_results, edit_review, delete_review
from django.contrib.auth import views as auth_views


urlpatterns = [

    # path('hote/', hotel_detail, name='hoteli'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logoutView, name='logout'),

    path('signup/', signup, name='signup'),
    path('', home_view, name='home'),

    # path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    # path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('hotel/<int:hotel_id>/submit_review/', views.submit_review, name='submit_review'),
    # path('hotel/<int:hotel_id>/edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    # Add other URLs as needed
    path('review_results/', user_review_results, name='review_results'),

    path('review/edit/<int:review_id>/', edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', delete_review, name='delete_review'),

    # Add other URLs as needed
]


    # path('hotel/<int:hotel_id>/', hotel_detail, name='hotel_detail'),
    # path('submit-rating/<int:hotel_id>/', views.submit_rating, name='submit_rating'),
    #
    # path('submit-review/<int:hotel_id>/', views.submit_review, name='submit_review'),
    # path('get-ratings/<int:hotel_id>/', views.get_ratings, name='get_ratings'),
#
# ]
