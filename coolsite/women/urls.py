from django.urls import path, register_converter

from women.classurl import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cub/', cub, name='cub'),
    path('cat/', categories, name='category'),
    path('student/<slug:student_fio>/', student, name='student'),
    path("articles/<yyyy:year>/", year_archive, name='articles'),
    path('cat/<int:catid>/', categories_id, name='cat'),
    path('cat/<slug:catid>/', categories_sl, name='cat_slug'),

]
