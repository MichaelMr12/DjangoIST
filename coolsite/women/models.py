from django.db import models

# для хранения ORM- моделей для представления данных из базы данных
# Create your models here.


data_db = [
    {'id': 1, 'FIO': 'Капшукова Дарья Руслановна', 'interesting': 'Рисование, футбол', 'is_smoke': False},
    {'id': 2, 'FIO': 'Горабалев Кирилл Артемович', 'interesting': 'Бокс, вязание', 'is_smoke': False},
    {'id': 3, 'FIO': 'Миколадзе Антон Алексеевич', 'interesting': 'история, литрература', 'is_smoke': True},
]


class Students(models.Model):
    fio = models.CharField(max_length=30)
    interesting = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_smoke = models.BooleanField(default=False)
    is_profcom = models.BooleanField(default=True)
