from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

# для хранения представлений(контролеров) текущего приложения
# Create your views here.
from women.models import Students

data_db = [
    {'id': 1, 'FIO': 'Капшукова Дарья Руслановна', 'interesting': 'Рисование, футбол', 'is_smoke': False},
    {'id': 2, 'FIO': 'Горабалев Кирилл Артемович', 'interesting': 'Бокс, вязание', 'is_smoke': False},
    {'id': 3, 'FIO': 'Миколадзе Антон Алексеевич', 'interesting': 'история, литрература', 'is_smoke': True},
]

menu = [{'title': 'Главная', 'url_n': 'home'}, {'title': 'О программе', 'url_n': 'about'}, {'title': 'Крутая страница', 'url_n': 'cub'}]


def index(request):
    if (request.GET):
        print(request.GET)
    data = {'title': 'Главная страница',
            'students': data_db,
            'menu': menu,
            }
    return render(request, 'women/index.html', context=data)

def student(request, student_fio):
    data_db = get_object_or_404(Students, slug= student_fio)
    data = {'title': 'Главная страница',
            'students': data_db,
            'menu': menu,
            }
    return render(request, 'women/student.html', context=data)

def cub(request):
    return render(request, 'women/3D_kub.html', {'menu': menu, 'title': 'Крутая страница',})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О приложении',})


def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')


def categories_id(request, catid):
    if 30 < catid < 60:
        return redirect('home')
    elif 60 < catid < 90:
        return redirect('home', permanent=True)
    elif 90 < catid < 110:
        return redirect('cat_slug', 'dfdfdf')

        # raise Http404()

    return HttpResponse(f'<h1>Статьи по номерам  {catid}</h1>')


def categories_sl(request, catid):
    return HttpResponse(f'<h1>Статьи по названиям и категориям {catid}</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Статьи не найдена</h1>')


def year_archive(request, year):
    if int(year) > 2023 or int(year) < 2000:
        raise Http404()

    return HttpResponse(f'<h1>В этот год случилось  {year}</h1>')
