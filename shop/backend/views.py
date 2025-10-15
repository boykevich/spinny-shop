from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from backend.models import Bicycle

menu = \
[
    {'title': "About", 'url_name': 'about'},
    {'title': 'Login', 'url_name': 'login'},
    {'title': 'Logout', 'url_name': 'logout'},
    {'title': 'Support', 'url_name': 'support'},
    {'title': 'Add', 'url_name': 'add_bike'}
]

data_db = [
    {
        'id': 1,
        'title': 'Trek Marlin 7',
        'content': 'Горный велосипед Trek Marlin 7 с лёгкой алюминиевой рамой и 29-дюймовыми колёсами.',
        'is_published': True,
        'price': 10000
    },
    {
        'id': 2,
        'title': 'Giant Talon 1',
        'content': 'Классический хардтейл Giant Talon 1, оснащённый гидравлическими тормозами и воздушной вилкой.',
        'is_published': True,
        'price': 15000
    },
    {
        'id': 3,
        'title': 'Specialized Rockhopper',
        'content': 'Универсальный велосипед Specialized Rockhopper для начинающих и опытных райдеров.',
        'is_published': True,
        'price': 8000
    },
    {
        'id': 4,
        'title': 'Cannondale Trail 5',
        'content': 'Надёжный горный велосипед Cannondale Trail 5 с современным дизайном и 10-скоростной трансмиссией.',
        'is_published': True,
        'price': 12000
    },
    {
        'id': 5,
        'title': 'Scott Aspect 950',
        'content': 'Scott Aspect 950 — лёгкий хардтейл с 29-дюймовыми колёсами, идеален для длительных поездок по пересечённой местности.',
        'is_published': False,
        'price': 13500
    },
    {
        'id': 6,
        'title': 'Merida Big Nine 300',
        'content': 'Merida Big Nine 300 с алюминиевой рамой и передней амортизацией, создан для комфорта и скорости.',
        'is_published': True,
        'price': 11000
    }
]

def show_post(request, post_slug):
    post = get_object_or_404(Bicycle, slug=post_slug)

    data = {
        'title': post.name,
        'description': post.description,
        'menu': menu,
        'post': post
    }
    return render(request, 'backend/post.html', context=data)

# def index(request):
#     # template = render_to_string('backend/index.html')
#     # return HttpResponse(template)
#
#     data = {
#         'def_title': '',
#         'title': 'main page',
#         'menu': menu,
#         'posts': data_db,
#         # 'float': 55.1,
#         # 'lst': [1, 2, True, 'afg'],
#         # 'set': {1, 2, 5, 2},
#         # 'dict': {'fst_v': 52, 'snd_val': 22},
#         # 'obj': MyClass(10, 20),
#     }
#     return render(request, 'backend/index.html', context=data)

def index(request):
    posts = Bicycle.objects.filter(is_published=True)
    return render(request, 'backend/index.html', {
        'menu': menu,
        'title': 'Bicycles',
        'posts': posts,
    })

def about(request):
    return render(request, 'backend/about.html', {'title': 'About page', 'menu': menu})

def get_bike(request, bike_id):
    return HttpResponse(f"<h1>Here you can see all of the bikes that we have<h1><p>id: {bike_id}</p>")

def get_bike_by_slag(request, bike_slag):
    parm_of_get = request.GET
    if parm_of_get:
        print(parm_of_get)
    return HttpResponse(f"<h1>Here you can see the bike by its slag</h1><p>slag: {bike_slag}</p>")

def archive(request, year):
    if year > 2025:
        # url = reverse('backend:get_by_slag', args=('fsag',))
        return redirect('get_by_slag')
    return HttpResponse(f"<h1>Archive by years<h1/><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")

def login(request):
    return HttpResponse("Login page")

def logout(request):
    return HttpResponse("Logout page")

def support(request):
    return HttpResponse("Support page")

def add_bicycle(request):
    return HttpResponse("Add Bicycle page")