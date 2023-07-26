# mydb/bin/forms.py
from django import forms
from .models import Messanger

class TxtFileForm(forms.Form):
    txt_file = forms.FileField(label='Выберите файл .txt')


class CsvUserForm(forms.Form):
    csv_file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['messanger'] = forms.ModelChoiceField(
            queryset=Messanger.objects.all(),
            label='Мессенджер',
            required=True
        )