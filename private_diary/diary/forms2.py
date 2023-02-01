import os

from django import forms
from django.core.mail import EmailMessage

class Inquiry2Form(forms.Form):

    記入日 = forms.CharField(label='記入日', max_length=4, required=False)
    お名前 = forms.CharField(label='お名前', max_length=30, required=False)
    ふりがな = forms.CharField(label='ふりがな', max_length=30, required=False)
    生年月日 = forms.CharField(label='生年月日', max_length=6, required=False)
    年齢 = forms.CharField(label='年齢', max_length=3, required=False)
    chose性別 = (
        ("1", "男性"),
        ("2", "女性"),
    )
    性別 = forms.ChoiceField(label='性別', choices=chose性別, required=False)
    体温 = forms.CharField(label='体温', max_length=5, required=False)
    郵便番号 = forms.CharField(label='郵便番号', max_length=7, required=False)
    住所 = forms.CharField(label='住所', max_length=7, required=False)
    電話番号 = forms.CharField(label='電話番号', max_length=13, required=False)
    携帯電話番号 = forms.CharField(label='携帯電話番号', max_length=13, required=False)
    chose症状 = (
        ("1", "発熱"),
        ("2", "頭痛"),
        ("3", "腹痛"),
        ("4", "腰痛"),
        ("5", "血圧が高い"),
        ("6", "のどの痛み"),
        ("7", "吐き気"),
        ("8", "息苦しい"),
        ("9", "せき"),
        ("10", "おうと"),
        ("11", "からだがだるい"),
        ("12", "たん"),
        ("13", "下痢"),
        ("14", "鼻水"),
        ("15", "便秘"),
        ("16", "めまい"),
        ("17", "関節の痛み"),
        ("18", "食欲がない"),
        ("19", "ふらつく"),
        ("20", "その他")
    )
    症状 = forms.ChoiceField(label='症状を選択してください', choices=chose症状, required=False)
    血圧 = forms.CharField(label='血圧を入力してください', max_length=13, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['記入日'].widget.attrs['class'] = 'form-control'
        self.fields['記入日'].widget.attrs['placeholder'] = '記入日をここに入力してください。'
        self.fields['お名前'].widget.attrs['class'] = 'form-control'
        self.fields['お名前'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['ふりがな'].widget.attrs['class'] = 'form-control'
        self.fields['ふりがな'].widget.attrs['placeholder'] = 'ふりがなをここに入力してください。'
        self.fields['生年月日'].widget.attrs['class'] = 'form-control'
        self.fields['生年月日'].widget.attrs['placeholder'] = '生年月日をここに入力してください。'
        self.fields['年齢'].widget.attrs['class'] = 'form-control'
        self.fields['年齢'].widget.attrs['placeholder'] = '年齢をここに入力してください。'
        self.fields['性別'].widget.attrs['class'] = 'form-control'
        self.fields['性別'].widget.attrs['placeholder'] = '性別をここに入力してください。'
        self.fields['郵便番号'].widget.attrs['class'] = 'form-control'
        self.fields['郵便番号'].widget.attrs['placeholder'] = '郵便番号をここに入力してください。'
        self.fields['住所'].widget.attrs['class'] = 'form-control'
        self.fields['住所'].widget.attrs['placeholder'] = '住所をここに入力してください。'
        self.fields['電話番号'].widget.attrs['class'] = 'form-control'
        self.fields['電話番号'].widget.attrs['placeholder'] = '電話番号をここに入力してください。'
        self.fields['携帯電話番号'].widget.attrs['class'] = 'form-control'
        self.fields['携帯電話番号'].widget.attrs['placeholder'] = '携帯電話番号をここに入力してください。'
        self.fields['症状'].widget.attrs['class'] = 'form-control'
        self.fields['症状'].widget.attrs['placeholder'] = '症状をここに入力してください。'
        self.fields['血圧'].widget.attrs['class'] = 'form-control'
        self.fields['血圧'].widget.attrs['placeholder'] = '血圧をここに入力してください。'


