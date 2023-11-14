#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coolsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

'''
python manage.py makemigrations  создание миграции
python manage.py sqlmigrate women 0001 просмотр sql запроса миграции
python manage.py migrate выполнение миграции

python manage.py shell_plus --print-sql  запуск улучшенной консоли

 w3 = Students(fio='Капшукова Дарья Руслановна', interesting= 'Рисование, футбол', is_smoke= False)

выбор всех объектов
Students.objects.all()
 выбор объектов по фильтру
  https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
Students.objects.filter(is_profcom=1)

выбор одной записи
Students.objects.get(pk=1)

сортировка записей 
Students.objects.order_by('fio')
обратный порядок 
Students.objects.order_by('-fio')

изменить все записи
Students.objects.update(is_profcom=0)  
'''