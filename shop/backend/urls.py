from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "yyyy")

app_name = 'backend' # для неймспейса в reverse() шаблонах

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('add/', views.add_bicycle, name='add_bike'),
    path('support/', views.support, name='support'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # path('get_bike/<int:bike_id>/', views.get_bike, name='get_by_id'),
    # path('get_bike/<slug:bike_slag>/', views.get_bike_by_slag, name='get_by_slag'),
    # path('archive/<yyyy:year>/', views.archive, name='archive'),
    # path('post/<int:post_id>/', views.show_post, name='post]'),
]


