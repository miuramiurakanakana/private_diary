import os

from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    '''
    email = forms.EmailField(label='メールアドレス')
    address1 = forms.CharField(label='都道府県', max_length=30)
    address2 = forms.CharField(label='市町村', max_length=30)
    address3 = forms.CharField(label='市町村以下の住所', max_length=30)
    tell_shigaikyokuban =  forms.CharField(label='市外局番', max_length=5)
    year = forms.IntegerField(label='年',max_value=2023,min_value=1900)
    month = forms.IntegerField(label='月',max_value=12,min_value=1)
    day = forms.IntegerField(label='日',max_value=31,min_value=1)
    genders = (
        ("1", "男性"),
        ("2", "女性"),
    )
    genders = forms.ChoiceField(label='性別',choices=genders)
    #degree = forms.SmallIntegerField(label='体温')


    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
        '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        '''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['address1'].widget.attrs['class'] = 'form-control'
        self.fields['address1'].widget.attrs['placeholder'] = '都道府県名をここに入力してください。'
        self.fields['address2'].widget.attrs['class'] = 'form-control'
        self.fields['address2'].widget.attrs['placeholder'] = '市町村をここに入力してください。'
        self.fields['address3'].widget.attrs['class'] = 'form-control'
        self.fields['address3'].widget.attrs['placeholder'] = '市町村以下の住所をここに入力してください。'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'
        self.fields['tell_shigaikyokuban'].widget.attrs['class'] = 'form-control'
        self.fields['tell_shigaikyokuban'].widget.attrs['placeholder'] = '電話番号をここに入力してください。'
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['year'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['month'].widget.attrs['class'] = 'form-control'
        self.fields['month'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['day'].widget.attrs['class'] = 'form-control'
        self.fields['day'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['genders'].widget.attrs['class'] = 'form-control'
        self.fields['genders'].widget.attrs['placeholder'] = '性別をここに入力してください。'
        #self.fields['degree'].widget.attrs['class'] = 'form-control'
        #self.fields['degree'].widget.attrs['placeholder'] = '体温をここに入力してください。'


        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'
'''
        def send_email(self):
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            address1 = self.cleaned_data['address1']
            address2 = self.cleaned_data['address2']
            address3 = self.cleaned_data['address3']
            tell = self.cleaned_data['tell']
            year = self.cleaned_data['year']
            month = self.cleaned_data['month']
            day = self.cleaned_data['day']
            genders = self.cleaned_data['genders']
            degree = self.cleaned_data['degree']

            title = self.cleaned_data['title']
            message = self.cleaned_data['message']

            subject = 'お問い合わせ{}'.format(title)
            message = '送信者名：{0}\nメールアドレス：{1}\nメッセージ：\n{2}'.format(name, email, message)
            from_email = os.environ.get('FROM_EMAIL')
            to_list = [
                os.environ.get('FROM_EMAIL')
            ]
            cc_list = [
                email
            ]

            message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,cc=cc_list)
            message.send()


