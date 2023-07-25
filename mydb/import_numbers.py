import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydb.settings")
django.setup()

from bin.models import PhoneNumber


def import_numbers_from_txt(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = line.strip()
            if number:
                PhoneNumber.objects.create(number=number)


if __name__ == '__main__':
    txt_file_path = 'path/to/your/txt_file.txt'  # Замените на путь к вашему txt файлу
    import_numbers_from_txt(txt_file_path)
