import os

from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):


    都道府県 = forms.CharField(label='都道府県', max_length=30, required=False)
    chose都道府県の区分 = (
        ("1", "都"),
        ("2", "道"),
        ("3", "府"),
        ("4", "県"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['都道府県'].widget.attrs['class'] = 'form-control'
        self.fields['都道府県'].widget.attrs['placeholder'] = '都道府県名をここに入力してください。'