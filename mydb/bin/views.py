# mydb/bin/views.py
import csv

from django.urls import reverse_lazy

from .models import PhoneNumber, User, Messanger
from django.shortcuts import render, redirect
from .forms import TxtFileForm, CsvUserForm
from .models import PhoneNumber


def upload_txt_file(request):
    if request.method == 'POST':
        form = TxtFileForm(request.POST, request.FILES)
        if form.is_valid():
            txt_file = request.FILES['txt_file']
            for line in txt_file:
                number = line.decode('utf-8').strip()
                PhoneNumber.objects.create(number=number)
            return redirect('admin:index')  # Перенаправляем на страницу админки
    else:
        form = TxtFileForm()
    return render(request, 'upload.html', {'form': form})


import re


def get_unique_name(existing_names, existing_phones):
    max_number = 0
    for name in existing_names:
        if name.startswith('user') and name[4:].isdigit():
            number = int(name[4:])
            max_number = max(max_number, number)

    return f'user{max_number + 1}' if max_number > 0 else 'user1'


def upload_csv_file(request):
    if request.method == 'POST':
        form = CsvUserForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']

            existing_phones = set(User.objects.values_list('phone', flat=True))
            existing_names = set(User.objects.values_list('name', flat=True))

            first_line_skipped = False  # Флаг для определения, что первая строка была пропущена

            for line in csv_file:
                if not first_line_skipped:
                    first_line_skipped = True
                    continue

                values = line.decode().strip().split(',')
                name = values[0]
                username = values[1]
                email = values[2]
                phone = values[3]
                messenger_name = values[4] if len(values) >= 5 else None

                if phone in existing_phones:
                    # Пропускаем дубликаты номеров
                    continue

                existing_phones.add(phone)

                if not name:
                    name = get_unique_name(existing_names, existing_phones)
                    existing_names.add(name)

                # Находим мессенджер по его имени или используем первый мессенджер из базы данных
                try:
                    if messenger_name:
                        messenger = Messanger.objects.get(name=messenger_name)
                    else:
                        messenger = Messanger.objects.first()
                except Messanger.DoesNotExist:
                    # Если указанный мессенджер не найден, используем первый мессенджер из базы данных
                    messenger = Messanger.objects.first()

                # Создаем пользователя с выбранным мессенджером
                user = User.objects.create(name=name, username=username, email=email, phone=phone, messanger=messenger)

            return redirect(reverse_lazy('admin:index'))
        else:
            messengers = Messanger.objects.all()
            return render(request, 'upload.html', {'form': form, 'messengers': messengers})

    form = CsvUserForm()  # Пустая форма для первоначального отображения
    messengers = Messanger.objects.all()
    return render(request, 'upload.html', {'form': form, 'messengers': messengers})


def admin_redirect(request):
    return redirect('/admin/')