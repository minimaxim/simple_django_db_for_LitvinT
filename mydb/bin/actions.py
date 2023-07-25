import pandas as pd
import io
from django.http import HttpResponse

def download_users_xlsx(modeladmin, request, queryset):
    # Получите выбранных пользователей
    users = queryset.all()

    # Создайте DataFrame из данных пользователей
    data = {
        'Имя': [user.first_name for user in users],
        'Фамилия': [user.last_name for user in users],
        'Email': [user.email for user in users],
        # Добавьте другие поля пользователя, если необходимо
    }
    df = pd.DataFrame(data)

    # Создайте Excel writer и запишите DataFrame в файл XLSX
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    output.seek(0)

    # Отправьте файл XLSX в ответе HTTP
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=users.xlsx'
    return response

download_users_xlsx.short_description = "Загрузить пользователей в XLSX"
