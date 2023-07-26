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


def get_unique_name(existing_names):
    numeric_names = [
        int(re.search(r'\d+', name).group())
        for name in existing_names if re.search(r'\d+', name)
    ]

    if numeric_names:
        max_number = max(numeric_names)
        return f'user{max_number + 1}'

    return 'user1'


def upload_csv_file(request):
    if request.method == 'POST':
        form = CsvUserForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']

            existing_names = set(User.objects.values_list('name', flat=True))
            default_messanger = Messanger.objects.first()

            csv_reader = csv.reader(csv_file.read().decode().splitlines())
            next(csv_reader)  # Пропустить первую строку (заголовок столбцов)

            for line in csv_reader:
                name, username, email, phone = line

                if not name:
                    name = get_unique_name(existing_names)
                    existing_names.add(name)

                user = User.objects.create(name=name, username=username, email=email, phone=phone, messanger=default_messanger)

            return redirect(reverse_lazy('admin:index'))
        else:
            messangers = Messanger.objects.all()
            return render(request, 'upload.html', {'form': form, 'messangers': messangers})

    form = CsvUserForm()  # Пустая форма для первоначального отображения
    messangers = Messanger.objects.all()
    return render(request, 'upload.html', {'form': form, 'messangers': messangers})




def admin_redirect(request):
    return redirect('/admin/')