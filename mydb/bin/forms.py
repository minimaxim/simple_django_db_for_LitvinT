from django import forms

class ExcelFileForm(forms.Form):
    file = forms.FileField(
        label='Выберите Excel-файл',
        help_text='Только файлы формата .xlsx',
        widget=forms.FileInput(attrs={'accept': '.xlsx'}),
    )
