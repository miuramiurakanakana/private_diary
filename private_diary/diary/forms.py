import os

from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):

    '''
    email = forms.EmailField(label='メールアドレス')
    '''

    address1 = forms.CharField(label='都道府県', max_length=30,required=False)
    choseKubun1 = (
        ("1","都"),
        ("2","道"),
        ("3","府"),
        ("4","県"),
    )
    kubun1 = forms.ChoiceField(label='都道府県の区分', choices=choseKubun1, required=False)
    address2 = forms.CharField(label='市町村', max_length=30,required=False)
    choseKubun2 = (
        ("1", "市"),
        ("2", "区"),
        ("3", "町"),
        ("4", "村"),
    )
    kubun2 = forms.ChoiceField(label='市町村の区分', choices=choseKubun2, required=False)
    address3 = forms.CharField(label='市町村以下の住所', max_length=30,required=False)
    name = forms.CharField(label='お名前', max_length=30,required=False)
    kana = forms.CharField(label='フリガナ', max_length=30,required=False)
    tell_shigaikyokuban = forms.CharField(label='市外局番', max_length=5,required=False)
    tell_shinaikyokuban = forms.CharField(label='市内局番', max_length=4,required=False)
    tell_kanyuusyaban = forms.CharField(label='加入者番号', max_length=4,required=False)
    birth = forms.CharField(label='誕生日', max_length=8,required=False)
    yearsOld = forms.CharField(label='年齢', max_length=3,required=False)
    bodyTemperature1 = forms.CharField(label='体温(度)', max_length=2,required=False)
    bodyTemperature2 = forms.CharField(label='体温(分)', max_length=2,required=False)
    choseGenders = (
        ("1","男性"),
        ("2","女性"),
    )
    genders = forms.ChoiceField(label='性別', choices=choseGenders,required=False)



    times = forms.CharField(label='接種回数',max_length=2,required=False)
    lastTime1 = forms.CharField(label='前回の摂取年',max_length=4,required=False)
    lastTime2 = forms.CharField(label='前回の摂取月', max_length=2,required=False)
    lastTime3 = forms.CharField(label='前回の摂取日', max_length=2,required=False)
    kind = forms.CharField(label='前回のワクチンの種類', max_length=30,required=False)

    sick = forms.CharField(label='病名',max_length=30,required=False)
    badCondition = forms.CharField(label='具合悪い点',max_length=30,required=False)
    allegy1 = forms.CharField(label='アレルギー',max_length=30,required=False)
    sessyu1 = forms.CharField(label='具合が悪くなった予防接種名',max_length=30,required=False)
    symptoms = forms.CharField(label='症状',max_length=30,required=False)
    sessyu2 = forms.CharField(label='前回受けた予防接種名', max_length=30,required=False)
    day = forms.CharField(label='前回受けた予防接種日', max_length=6,required=False)


    choseSessyu3 = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    sessyu3 = forms.ChoiceField(label='ワクチン接種を以前接種したことはありますか？', choices=choseSessyu3, required=False)
    choseJuumin = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    juumin = forms.ChoiceField(label='現住所と住民票の住所は同じですか？', choices=choseJuumin, required=False)
    choseHannou = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    hannou = forms.ChoiceField(label='ワクチンの副反応について理解していますか？', choices=choseHannou, required=False)
    choseTiryo = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    tiryo = forms.ChoiceField(label='現在治療を受けていますか？', choices=choseTiryo, required=False)
    choseByoki = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    byoki = forms.ChoiceField(label='持病はありますか？', choices=choseByoki, required=False)
    choseGuai = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    guai = forms.ChoiceField(label='体に具合悪いところはありますか？', choices=choseGuai, required=False)
    choseKeiren = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    keiren = forms.ChoiceField(label='痙攣を起こしたことはありますか？', choices=choseKeiren, required=False)
    choseAllegy2 = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    allegy2 = forms.ChoiceField(label='重度のアレルギーはありますか？', choices=choseAllegy2, required=False)
    choseNotGood= (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    notGood = forms.ChoiceField(label='予防接種で具合が悪くなったことはありますか？', choices=choseNotGood, required=False)
    chosePregnancy = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    pregnancy = forms.ChoiceField(label='予防接種で具合が悪くなったことはありますか？', choices=chosePregnancy, required=False)
    choseTwoWeek = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    twoWeek = forms.ChoiceField(label='2週間以内に予防接種を打ちましたか？', choices=choseTwoWeek, required=False)
    choseQuestion = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    question = forms.ChoiceField(label='今日の予防接種について何か質問はありますか？', choices=choseQuestion,widget=forms.RadioSelect(), required=False)
    byomei1 = forms.BooleanField(label='何らかの持病をもっていますか？',)
    choseByomei = (
        ("1", "心臓病"),
        ("2", "腎臓病"),
        ("3", "肝臓病"),
        ("4", "血液疾患"),
        ("5", "血が止まりにくい病気"),
        ("6", "免疫不全"),
        ("7", "毛細血管漏出症候群"),
    )
    byomei = forms.MultipleChoiceField(label='病名を選択してください？', choices=choseByomei, required=False)
    byomei2 = forms.BooleanField(label='上記以外の持病をもっていますか？', )
    sonota1 = forms.CharField(label='その他の病気', max_length=30, required=False)

    kusuri = forms.BooleanField(label='何らかの投薬を受けていますか？')

    choseKusuri = (
        ("1", "血をサラサラにする薬"),
        ("2", "その他の薬"),
    )
    kusuri = forms.ChoiceField(label='何らかの投薬を受けていますか？', choices=choseKusuri, required=False)

    choseSarasara = (
        ("1", "はい"),
    )
    sarasara = forms.BooleanField(label='血液をサラサラにする薬を処方されていますか？')

    choseKibou = (
        ("1", "接種を希望します"),
        ("2", "接種を希望しません"),
    )
    kibou = forms.ChoiceField(label='医師の説明を受け、接種を希望しますか？', choices=choseKibou, required=False)

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
        self.fields['kubun1'].widget.attrs['class'] = 'form-control'
        self.fields['kubun1'].widget.attrs['placeholder'] = '都道府県の区分をここに入力してください。'
        self.fields['address2'].widget.attrs['class'] = 'form-control'
        self.fields['address2'].widget.attrs['placeholder'] = '市町村をここに入力してください。'
        self.fields['kubun2'].widget.attrs['class'] = 'form-control'
        self.fields['kubun2'].widget.attrs['placeholder'] = '市町村の区分をここに入力してください。'
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
        self.fields['yearsOld'].widget.attrs['class'] = 'form-control'
        self.fields['yearsOld'].widget.attrs['placeholder'] = '年齢をここに入力してください。'
        self.fields['bodyTemperature1'].widget.attrs['class'] = 'form-control'
        self.fields['bodyTemperature1'].widget.attrs['placeholder'] = '体温(度)をここに入力してください。'
        self.fields['bodyTemperature2'].widget.attrs['class'] = 'form-control'
        self.fields['bodyTemperature2'].widget.attrs['placeholder'] = '体温(分)をここに入力してください。'
        self.fields['genders'].widget.attrs['class'] = 'form-control'
        self.fields['genders'].widget.attrs['placeholder'] = '性別をここに入力してください。'

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
        self.fields['allegy1'].widget.attrs['class'] = 'form-control'
        self.fields['allegy1'].widget.attrs['placeholder'] = 'アレルギーをここに入力してください'
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

        self.fields['sessyu3'].widget.attrs['class'] = 'form-control'
        self.fields['sessyu3'].widget.attrs['placeholder'] = '以前予防接種を受けたことはありますか？　はいorいいえでお応えください'
        self.fields['juumin'].widget.attrs['class'] = 'form-control'
        self.fields['juumin'].widget.attrs['placeholder'] = '現住所と住民票の住所は同じですか？　はいorいいえでお応えください'
        self.fields['hannou'].widget.attrs['class'] = 'form-control'
        self.fields['hannou'].widget.attrs['placeholder'] = 'ワクチンの副反応について理解していますか？　はいorいいえでお応えください'
        self.fields['tiryo'].widget.attrs['class'] = 'form-control'
        self.fields['tiryo'].widget.attrs['placeholder'] = 'ワクチンの副反応について理解していますか？　はいorいいえでお応えください'
        self.fields['byoki'].widget.attrs['class'] = 'form-control'
        self.fields['byoki'].widget.attrs['placeholder'] = '持病はありますか？　はいorいいえでお応えください'
        self.fields['guai'].widget.attrs['class'] = 'form-control'
        self.fields['guai'].widget.attrs['placeholder'] = '具合が悪い点はありますか？　はいorいいえでお応えください'
        self.fields['keiren'].widget.attrs['class'] = 'form-control'
        self.fields['keiren'].widget.attrs['placeholder'] = '痙攣を起こしたことはありますか？　はいorいいえでお応えください'
        self.fields['allegy2'].widget.attrs['class'] = 'form-control'
        self.fields['allegy2'].widget.attrs['placeholder'] = '重度のアレルギーを起こしたことはありますか？　はいorいいえでお応えください'
        self.fields['notGood'].widget.attrs['class'] = 'form-control'
        self.fields['notGood'].widget.attrs['placeholder'] = '予防接種で具合が悪くなったことはありますか？　はいorいいえでお応えください'
        self.fields['pregnancy'].widget.attrs['class'] = 'form-control'
        self.fields['pregnancy'].widget.attrs['placeholder'] = '妊娠又は授乳中ですか？　はいorいいえでお応えください'
        self.fields['twoWeek'].widget.attrs['class'] = 'form-control'
        self.fields['twoWeek'].widget.attrs['placeholder'] = '妊娠又は授乳中ですか？　はいorいいえでお応えください'
        self.fields['question'].widget.attrs['class'] = 'form-control'
        self.fields['question'].widget.attrs['placeholder'] = '今回の予防接種について質問はありますか？　はいorいいえでお応えください'
        self.fields['byomei1'].widget.attrs['id'] = 'byomei1-id'
        self.fields['byomei'].widget.attrs['class'] = 'form-control'
        self.fields['byomei'].widget.attrs['placeholder'] = '何らかの持病をお持ちですか？　該当するものを選択してください'
        self.fields['byomei2'].widget.attrs['id'] = 'byomei2-id'
        self.fields['sonota1'].widget.attrs['class'] = 'form-control'
        self.fields['sonota1'].widget.attrs['placeholder'] = '上記以外の病気を入力してください'

        self.fields['kusuri'].widget.attrs['class'] = 'form-control'
        self.fields['kusuri'].widget.attrs['placeholder'] = '何らかの投薬を受けていますか？　はいorいいえでお応えください'

        self.fields['kibou'].widget.attrs['class'] = 'form-control'
        self.fields['kibou'].widget.attrs['placeholder'] = '医師の説明を受けて接種を希望しますか？　はいorいいえでお応えください'

        self.fields['sarasara'].widget.attrs['class'] = 'form-control'
        self.fields['sarasara'].widget.attrs['placeholder'] = '血液をサラサラにする薬を処方されていますか？　はいの場合は✓してください'



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
        self.fields['degree'].widget.attrs['class'] = 'form-control'
        self.fields['degree'].widget.attrs['placeholder'] = '体温をここに入力してください。'
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
            '''
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
           '''
            message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,cc=cc_list)
            message.send()



