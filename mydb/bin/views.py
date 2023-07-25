# views.py
from django.shortcuts import render
from .forms import UploadTxtFileForm
from .models import PhoneNumber

def upload_txt_file(request):
    if request.method == 'POST':
        form = UploadTxtFileForm(request.POST, request.FILES)
        if form.is_valid():
            txt_file = form.cleaned_data['txt_file']
            # Читаем данные из файла и записываем в таблицу PhoneNumber
            with txt_file.open() as file:
                for line in file:
                    number = line.strip()  # Убираем лишние символы, если нужно
                    PhoneNumber.objects.create(number=number)

    else:
        form = UploadTxtFileForm()

    return render(request, 'upload.html', {'form': form})
