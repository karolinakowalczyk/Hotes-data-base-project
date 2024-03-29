from django.urls import path
from . import views

app_name = 'databaseapp'

urlpatterns = [
        path('', views.index, name='index'),
        path('signOut/', views.signOut, name='signOut'),
        path('login/', views.login, name='login'),
        path('signUp/', views.signUp, name='signUp'),
        path('browse/', views.browse, name='browse'),
        path('userPanel/', views.userPanel, name='userPanel'),
        path('<int:room_id>/addReservation/<str:date_start>_<str:date_end>/', views.addReservation, name='addReservation'),
        path('<int:room_id>/addReservation/<str:date_start>_<str:date_end>/confirm', views.confirmReservation, name='confirmReservation'),
        path('<int:reservation_id>/deleteReservation/', views.deleteReservation, name='deleteReservation'),
        path('showUserReservation/', views.showUserReservation, name='showUserReservation'),
        path('adminPanel/', views.adminPanel, name='adminPanel'),
        path('adminPanel/guests/', views.guests, name='guests'),
        path('browse/results', views.browseResult, name='browseresults'),
        path('<int:reservation_id>/deleteCurrentReservation/', views.deleteCurrentReservation, name='deleteCurrentReservation'),
        path('prices/', views.prices, name = 'prices'),
        path('loginfailed/', views.loginfailed, name = 'loginfailed'),
        path('userPanel/password/', views.password, name='password'),
        path('userPanel/passworderror/', views.passworderror, name='passworderror'),
    ]
