from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('booking/pay/<int:booking_id>/', views.payment_view, name='payment_view'),  # updated
    path('booking/success/', views.payment_success, name='payment_success'),
    path('Day 2/index-red.html', views.index_red, name='index_red'),    
    
    path('France.html', views.france_view, name='france'),
    path('france/details1/', views.france_details1, name='france_details1'),
    path('france/details2/', views.france_details2, name='france_details2'),
    path('france/details3/', views.france_details3, name='france_details3'),
    path('france/details4/', views.france_details4, name='france_details4'),


    path('Germany.html', views.germany_view, name='germany'),
    path('Images/Germany/Details1.html', views.germany_details1, name='germany_details1'),
    path('Images/Germany/Details2.html', views.germany_details2, name='germany_details2'),
    path('Images/Germany/Details3.html', views.germany_details3, name='germany_details3'),
    path('Images/Germany/Details4.html', views.germany_details4, name='germany_details4'),





    path('dubai.html', views.dubai_view, name='dubai'),
    path('US.html', views.US_view, name='US'),
    path('Italy.html', views.italy_view, name='italy'),
    path('Kashmir.html', views.Kashmir_view, name='Kashmir'),
    path('Seville.html', views.seville_view, name='seville'),
    path('Singapore.html', views.singapore_view, name='singapore'),
    path('Turkey.html', views.turkey_view, name='turkey'),
    path('China.html', views.china_view, name='china'),
    path('Monaco City.html', views.Monaco_City_view, name='Monaco City'),
    path('UK.html', views.UK_view, name='UK'),
    path('Images/UK/Details1.html', views.uk_details1, name='uk_details1'),
    path('Images/UK/Details2.html', views.uk_details2, name='uk_details2'),
    path('Images/UK/Details3.html', views.uk_details3, name='uk_details3'),
    path('Images/UK/Details4.html', views.uk_details4, name='uk_details4'),

    path('explore/', views.explore, name='explore'),
]


