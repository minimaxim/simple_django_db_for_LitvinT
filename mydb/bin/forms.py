# mydb/bin/forms.py
from django import forms

class TxtFileForm(forms.Form):
    txt_file = forms.FileField(label='Выберите файл .txt')
