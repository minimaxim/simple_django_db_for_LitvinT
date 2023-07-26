# mydb/bin/views.py
from django.shortcuts import render, redirect
from .forms import TxtFileForm
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
