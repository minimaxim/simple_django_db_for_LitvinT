# mydb/bin/views.py
import csv
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


def upload_csv_file(request):
    if request.method == 'POST':
        form = CsvUserForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            messanger = form.cleaned_data['messanger']

            # Обработка данных из CSV файла и сохранение в модель User
            decoded_file = csv_file.read().decode('utf-8')
            csv_reader = csv.reader(decoded_file.splitlines(), delimiter=',')
            next(csv_reader)  # Пропустить заголовок CSV файла

            for row in csv_reader:
                name, username, email, phone = row
                user = User.objects.create(name=name, username=username, email=email, phone=phone, messanger=messanger)

            return redirect('admin:index')  # Перенаправление на страницу админки
    else:
        form = CsvUserForm()

    messangers = Messanger.objects.all()  # Получение списка мессенджеров
    return render(request, 'upload.html', {'form': form, 'messangers': messangers})