# forms.py
from django import forms

class UploadTxtFileForm(forms.Form):
    txt_file = forms.FileField()
