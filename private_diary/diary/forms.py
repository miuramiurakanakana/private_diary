import os

from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):

    '''


    email = forms.EmailField(label='メールアドレス')

    '''
    address1 = forms.CharField(label='都道府県', max_length=30)
    address2 = forms.CharField(label='市町村', max_length=30)
    address3 = forms.CharField(label='市町村以下の住所', max_length=30)
    name = forms.CharField(label='お名前', max_length=30)
    kana = forms.CharField(label='フリガナ', max_length=30)
    tell_shigaikyokuban = forms.CharField(label='市外局番', max_length=5)
    tell_shinaikyokuban = forms.CharField(label='市内局番', max_length=4)
    tell_kanyuusyaban = forms.CharField(label='加入者番号', max_length=4)
    birth = forms.CharField(label='誕生日', max_length=8)
    yearsOld = forms.CharField(label='年齢', max_length=3)



    times = forms.CharField(label='接種回数',max_length=2)
    lastTime1 = forms.CharField(label='前回の摂取年',max_length=4)
    lastTime2 = forms.CharField(label='前回の摂取月', max_length=2)
    lastTime3 = forms.CharField(label='前回の摂取日', max_length=2)
    kind = forms.CharField(label='前回のワクチンの種類', max_length=30)

    sick = forms.CharField(label='病名',max_length=30)
    badCondition = forms.CharField(label='具合悪い点',max_length=30)
    allegy = forms.CharField(label='アレルギー',max_length=30)
    sessyu1 = forms.CharField(label='具合が悪くなった予防接種名',max_length=30)
    symptoms = forms.CharField(label='症状',max_length=30)
    sessyu2 = forms.CharField(label='前回受けた予防接種名', max_length=30)
    day = forms.CharField(label='前回受けた予防接種日', max_length=6)
    '''
    tell_shigaikyokuban =  forms.CharField(label='市外局番', max_length=5)
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
        '''
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        '''
        self.fields['address1'].widget.attrs['class'] = 'form-control'
        self.fields['address1'].widget.attrs['placeholder'] = '都道府県名をここに入力してください。'
        self.fields['address2'].widget.attrs['class'] = 'form-control'
        self.fields['address2'].widget.attrs['placeholder'] = '市町村をここに入力してください。'
        self.fields['address3'].widget.attrs['class'] = 'form-control'
        self.fields['address3'].widget.attrs['placeholder'] = '市町村以下の住所をここに入力してください。'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['kana'].widget.attrs['class'] = 'form-control'
        self.fields['kana'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['tell_shigaikyokuban'].widget.attrs['class'] = 'form-control'
        self.fields['tell_shigaikyokuban'].widget.attrs['placeholder'] = '市外局番をここに入力してください。'
        self.fields['tell_shinaikyokuban'].widget.attrs['class'] = 'form-control'
        self.fields['tell_shinaikyokuban'].widget.attrs['placeholder'] = '市内局番をここに入力してください。'
        self.fields['tell_kanyuusyaban'].widget.attrs['class'] = 'form-control'
        self.fields['tell_kanyuusyaban'].widget.attrs['placeholder'] = '加入者番号をここに入力してください。'
        self.fields['birth'].widget.attrs['class'] = 'form-control'
        self.fields['birth'].widget.attrs['placeholder'] = '誕生日をここに入力してください。'


        self.fields['times'].widget.attrs['class'] = 'form-control'
        self.fields['times'].widget.attrs['placeholder'] = 'ワクチンの接種回数をここに入力してください。'
        self.fields['lastTime1'].widget.attrs['class'] = 'form-control'
        self.fields['lastTime1'].widget.attrs['placeholder'] = '前回のワクチン接種年をここに入力してください。'
        self.fields['lastTime2'].widget.attrs['class'] = 'form-control'
        self.fields['lastTime2'].widget.attrs['placeholder'] = '前回のワクチンの接種月をここに入力してください。'
        self.fields['lastTime3'].widget.attrs['class'] = 'form-control'
        self.fields['lastTime3'].widget.attrs['placeholder'] = '前回ワクチンの接種日をここに入力してください。'

        self.fields['sick'].widget.attrs['class'] = 'form-control'
        self.fields['sick'].widget.attrs['placeholder'] = '病名をここに入力してください。'
        self.fields['badCondition'].widget.attrs['class'] = 'form-control'
        self.fields['badCondition'].widget.attrs['placeholder'] = '具合悪い点をここに入力してください。'
        self.fields['allegy'].widget.attrs['class'] = 'form-control'
        self.fields['allegy'].widget.attrs['placeholder'] = 'アレルギーをここに入力してください'
        self.fields['kind'].widget.attrs['class'] = 'form-control'
        self.fields['kind'].widget.attrs['placeholder'] = '接種したワクチンの種類をここに入力してください'
        self.fields['sessyu1'].widget.attrs['class'] = 'form-control'
        self.fields['sessyu1'].widget.attrs['placeholder'] = 'アレルギーのある予防接種名をここに入力してください'
        self.fields['symptoms'].widget.attrs['class'] = 'form-control'
        self.fields['symptoms'].widget.attrs['placeholder'] = '症状をここに入力してください'
        self.fields['sessyu2'].widget.attrs['class'] = 'form-control'
        self.fields['sessyu2'].widget.attrs['placeholder'] = '前回受けた予防接種名をここに入力してください'
        self.fields['day'].widget.attrs['class'] = 'form-control'
        self.fields['day'].widget.attrs['placeholder'] = '前回受けた予防接種日をここに入力してください'
        '''
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'
        self.fields['tell_shigaikyokuban'].widget.attrs['class'] = 'form-control'
        self.fields['tell_shigaikyokuban'].widget.attrs['placeholder'] = '電話番号をここに入力してください。'
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
            '''
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
            '''


