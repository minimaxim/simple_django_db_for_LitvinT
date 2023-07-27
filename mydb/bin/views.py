from django.shortcuts import render, redirect, reverse
from .models import User
import pandas as pd

def upload_excel_file(request):
    if request.method == 'POST':
        if 'excel_file' not in request.FILES:
            return render(request, 'upload.html', {'error': 'Файл не выбран'})

        excel_file = request.FILES['excel_file']

        # Проверка на расширение файла
        if not excel_file.name.endswith('.xlsx'):
            return render(request, 'your_app/upload.html')  # Replace 'your_app' with the actual app name if needed


        # Загрузка файла Excel в DataFrame
        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            return render(request, 'upload.html', {'error': f'Ошибка при чтении файла: {e}'})

        # Отсеиваем повторы по колонке phone и оставляем только уникальные записи
        df.drop_duplicates(subset='phone', inplace=True)

        # Проходим по DataFrame и создаем записи в базе данных
        for _, row in df.iterrows():
            name = row['name']
            country = row['country']
            email = row['email']
            phone = row['phone']
            login_bitmain = row['login_bitmain']
            telegram_link = row['telegram_link']
            instagram_link = row['instagram_link']
            twitter_link = row['twitter_link']
            vk_link = row['vk_link']
            facebook_link = row['facebook_link']
            linkedin_link = row['linkedin_link']
            whatsapp_link = row['whatsapp_link']

            # Создаем пользователя, пропустив создание, если такой номер телефона уже существует
            User.objects.get_or_create(
                name=name, country=country, email=email, phone=phone, login_bitmain=login_bitmain,
                telegram_link=telegram_link, instagram_link=instagram_link, twitter_link=twitter_link,
                vk_link=vk_link, facebook_link=facebook_link, linkedin_link=linkedin_link, whatsapp_link=whatsapp_link
            )

        # Выполняем редирект на страницу admin
        return redirect(reverse('admin:index'))

    return render(request, 'upload.html')
