from django.urls import path, register_converter

from women.classurl import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cat/', categories, name='category'),
    path("articles/<yyyy:year>/", year_archive, name='articles'),
    path('cat/<int:catid>/', categories_id, name='cat'),
    path('cat/<slug:catid>/', categories_sl, name='cat_slug'),

]
