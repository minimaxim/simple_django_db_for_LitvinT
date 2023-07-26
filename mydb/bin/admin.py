from django.contrib import admin

from .models import User, Messanger
from .models import PhoneNumber
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from .models import PhoneNumber, Messanger, User
from .forms import CsvUserForm


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)


admin.site.register(PhoneNumber, PhoneNumberAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'email', 'phone', 'messanger')
    list_filter = ('messanger', )
    search_fields = ('id', )

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('csv_file'):
            csv_file = form.cleaned_data['csv_file']
            for line in csv_file:
                name, username, email, phone, messanger = line.decode('utf-8').strip().split(',')
                user = User(
                    name=name,
                    username=username,
                    email=email,
                    phone=phone,
                    messanger_id=messanger
                )
                user.save()

        super().save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload/', self.upload_csv),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == 'POST':
            form = CsvUserForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['csv_file']
                # Обработка CSV файла и сохранение данных в базу данных
                for line in csv_file:
                    name, username, email, phone, messanger = line.decode('utf-8').strip().split(',')
                    user = User(
                        name=name,
                        username=username,
                        email=email,
                        phone=phone,
                        messanger_id=messanger
                    )
                    user.save()

                self.message_user(request, "CSV файл успешно загружен и обработан.")
                return redirect("..")

        else:
            form = CsvUserForm()

        return render(
            request,
            "admin/upload_csv.html",
            context={"form": form},
        )


admin.site.register(User, UserAdmin)


@admin.register(Messanger)
class MessangerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
