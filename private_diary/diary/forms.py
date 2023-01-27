import os

from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):

    '''
    email = forms.EmailField(label='メールアドレス')
    '''

    都道府県 = forms.CharField(label='都道府県', max_length=30,required=False)
    chose都道府県の区分 = (
        ("1","都"),
        ("2","道"),
        ("3","府"),
        ("4","県"),
    )
    都道府県の区分 = forms.ChoiceField(label='都道府県の区分', choices=chose都道府県の区分, required=False)
    市町村 = forms.CharField(label='市町村', max_length=30,required=False)
    chose市町村の区分 = (
        ("1", "市"),
        ("2", "区"),
        ("3", "町"),
        ("4", "村"),
    )
    市町村の区分 = forms.ChoiceField(label='市町村の区分', choices=chose市町村の区分, required=False)
    市町村以下の住所 = forms.CharField(label='市町村以下の住所', max_length=30,required=False)
    お名前 = forms.CharField(label='お名前', max_length=30,required=False)
    伽奈 = forms.CharField(label='フリガナ', max_length=30,required=False)
    市外局番 = forms.CharField(label='市外局番', max_length=5,required=False)
    市内局番 = forms.CharField(label='市内局番', max_length=4,required=False)
    加入者番号 = forms.CharField(label='加入者番号', max_length=4,required=False)
    誕生日 = forms.CharField(label='誕生日', max_length=8,required=False)
    年齢 = forms.CharField(label='年齢', max_length=3,required=False)
    体温_度 = forms.CharField(label='体温(度)', max_length=2,required=False)
    体温_分 = forms.CharField(label='体温(分)', max_length=2,required=False)
    chose性別 = (
        ("1","男性"),
        ("2","女性"),
    )
    性別 = forms.ChoiceField(label='性別', choices=chose性別,required=False)


    接種回数 = forms.CharField(label='接種回数',max_length=2,required=False)
    前回の摂取年 = forms.CharField(label='前回の摂取年',max_length=4,required=False)
    前回の摂取月 = forms.CharField(label='前回の摂取月', max_length=2,required=False)
    前回の摂取日 = forms.CharField(label='前回の摂取日', max_length=2,required=False)
    前回のワクチンの種類 = forms.CharField(label='前回のワクチンの種類', max_length=30,required=False)

    病名 = forms.CharField(label='病名',max_length=30,required=False)
    具合悪い点 = forms.CharField(label='具合悪い点',max_length=30,required=False)
    アレルギー = forms.CharField(label='アレルギー',max_length=30,required=False)
    具合が悪くなった予防接種名 = forms.CharField(label='具合が悪くなった予防接種名',max_length=30,required=False)
    症状 = forms.CharField(label='症状',max_length=30,required=False)
    前回受けた予防接種名 = forms.CharField(label='前回受けた予防接種名', max_length=30,required=False)
    前回受けた予防接種日 = forms.CharField(label='前回受けた予防接種日', max_length=6,required=False)


    choseワクチン接種を以前接種したことはありますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    ワクチン接種を以前接種したことはありますか = forms.ChoiceField(label='ワクチン接種を以前接種したことはありますか？', choices=choseワクチン接種を以前接種したことはありますか, required=False)
    chose現住所と住民票の住所は同じですか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    現住所と住民票の住所は同じですか = forms.ChoiceField(label='現住所と住民票の住所は同じですか？', choices=chose現住所と住民票の住所は同じですか, required=False)
    choseワクチンの副反応について理解していますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    ワクチンの副反応について理解していますか = forms.ChoiceField(label='ワクチンの副反応について理解していますか？', choices=choseワクチンの副反応について理解していますか, required=False)
    chose現在治療を受けていますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    現在治療を受けていますか = forms.ChoiceField(label='現在治療を受けていますか？', choices=chose現在治療を受けていますか, required=False)
    chose持病はありますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    持病はありますか = forms.ChoiceField(label='持病はありますか？', choices=chose持病はありますか, required=False)
    chose体に具合悪いところはありますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    体に具合悪いところはありますか = forms.ChoiceField(label='体に具合悪いところはありますか？', choices=chose体に具合悪いところはありますか, required=False)
    chose痙攣を起こしたことはありますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    痙攣を起こしたことはありますか = forms.ChoiceField(label='痙攣を起こしたことはありますか？', choices=chose痙攣を起こしたことはありますか, required=False)
    chose重度のアレルギーはありますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    重度のアレルギーはありますか = forms.ChoiceField(label='重度のアレルギーはありますか？', choices=chose重度のアレルギーはありますか, required=False)
    chose予防接種で具合が悪くなったことはありますか= (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    予防接種で具合が悪くなったことはありますか = forms.ChoiceField(label='予防接種で具合が悪くなったことはありますか？', choices=chose予防接種で具合が悪くなったことはありますか, required=False)
    chose現在妊娠していますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    現在妊娠していますか = forms.ChoiceField(label='現在妊娠していますか？', choices=chose現在妊娠していますか, required=False)
    _2週間以内に予防接種を打ちましたか = forms.BooleanField(label='2週間以内に予防接種を打ちましたか？', required=False)
    _2週間以内に打った予防接種の種類 = forms.CharField(label='2週間以内に打った予防接種の種類を記入してください', max_length=4, required=False)

    chose_今日の予防接種について何か質問はありますか = (
        ("1", "はい"),
        ("2", "いいえ"),
    )
    _今日の予防接種について何か質問はありますか = forms.ChoiceField(label='今日の予防接種について何か質問はありますか？', choices=chose_今日の予防接種について何か質問はありますか,widget=forms.RadioSelect(), required=False)
    何らかの持病をもっていますか = forms.BooleanField(label='何らかの持病をもっていますか？', required=False)
    chose病名を選択してください = (
        ("1", "心臓病"),
        ("2", "腎臓病"),
        ("3", "肝臓病"),
        ("4", "血液疾患"),
        ("5", "血が止まりにくい病気"),
        ("6", "免疫不全"),
        ("7", "毛細血管漏出症候群"),
    )
    病名を選択してください = forms.MultipleChoiceField(label='病名を選択してください♡', choices=chose病名を選択してください, required=False)
    上記以外の持病をもっていますか = forms.BooleanField(label='上記以外の持病をもっていますか？',  required=False)
    その他の病気 = forms.CharField(label='その他の病気', max_length=30, required=False)

    何らかの投薬を受けていますか = forms.BooleanField(label='何らかの投薬を受けていますか？', required=False)
    '''
    chose何らかの投薬を受けていますか = (
        ("1", "血をサラサラにする薬"),
        ("2", "その他の薬"),
    )
    何らかの投薬を受けていますか = forms.ChoiceField(label='何らかの投薬を受けていますか？', choices=chose何らかの投薬を受けていますか, required=False)
    
    choseサラサラにする薬 = (
        ("1", "はい"),
    )
    '''
    サラサラにする薬 = forms.BooleanField(label='血液をサラサラにする薬を処方されていますか？', required=False)

    処方されている薬名を記入してください = forms.CharField(label='処方されている薬名を記入してください', max_length=30, required=False)

    その他に処方されている薬 = forms.BooleanField(label='その他に処方されているお薬はありますか？', required=False)

    その他に処方されている薬名を記入してください = forms.CharField(label='その他に処方されている薬名を記入してください', max_length=30,
                                                    required=False)

    chose接種を希望しますか = (
        ("1", "接種を希望します"),
        ("2", "接種を希望しません"),
    )
    接種を希望しますか = forms.ChoiceField(label='医師の説明を受け、接種を希望しますか？', choices=chose接種を希望しますか, required=False)



    #degree = forms.SmallIntegerField(label='体温')

    '''
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        self.fields['お名前'].widget.attrs['class'] = 'form-control'
        self.fields['お名前'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        '''
        self.fields['都道府県'].widget.attrs['class'] = 'form-control'
        self.fields['都道府県'].widget.attrs['placeholder'] = '都道府県名をここに入力してください。'
        self.fields['都道府県の区分'].widget.attrs['class'] = 'form-control'
        self.fields['都道府県の区分'].widget.attrs['placeholder'] = '都道府県の区分をここに入力してください。'
        self.fields['市町村'].widget.attrs['class'] = 'form-control'
        self.fields['市町村'].widget.attrs['placeholder'] = '市町村をここに入力してください。'
        self.fields['市町村の区分'].widget.attrs['class'] = 'form-control'
        self.fields['市町村の区分'].widget.attrs['placeholder'] = '市町村の区分をここに入力してください。'
        self.fields['市町村以下の住所'].widget.attrs['class'] = 'form-control'
        self.fields['市町村以下の住所'].widget.attrs['placeholder'] = '市町村以下の住所をここに入力してください。'
        self.fields['お名前'].widget.attrs['class'] = 'form-control'
        self.fields['お名前'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['伽奈'].widget.attrs['class'] = 'form-control'
        self.fields['伽奈'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['市外局番'].widget.attrs['class'] = 'form-control'
        self.fields['市外局番'].widget.attrs['placeholder'] = '市外局番をここに入力してください。'
        self.fields['市内局番'].widget.attrs['class'] = 'form-control'
        self.fields['市内局番'].widget.attrs['placeholder'] = '市内局番をここに入力してください。'
        self.fields['加入者番号'].widget.attrs['class'] = 'form-control'
        self.fields['加入者番号'].widget.attrs['placeholder'] = '加入者番号をここに入力してください。'
        self.fields['誕生日'].widget.attrs['class'] = 'form-control'
        self.fields['誕生日'].widget.attrs['placeholder'] = '誕生日をここに入力してください。'
        self.fields['年齢'].widget.attrs['class'] = 'form-control'
        self.fields['年齢'].widget.attrs['placeholder'] = '年齢をここに入力してください。'
        self.fields['体温_度'].widget.attrs['class'] = 'form-control'
        self.fields['体温_度'].widget.attrs['placeholder'] = '体温(度)をここに入力してください。'
        self.fields['体温_分'].widget.attrs['class'] = 'form-control'
        self.fields['体温_分'].widget.attrs['placeholder'] = '体温(分)をここに入力してください。'
        self.fields['性別'].widget.attrs['class'] = 'form-control'
        self.fields['性別'].widget.attrs['placeholder'] = '性別をここに入力してください。'

        self.fields['接種回数'].widget.attrs['class'] = 'form-control'
        self.fields['接種回数'].widget.attrs['placeholder'] = 'ワクチンの接種回数をここに入力してください。'
        self.fields['前回の摂取年'].widget.attrs['class'] = 'form-control'
        self.fields['前回の摂取年'].widget.attrs['placeholder'] = '前回のワクチン接種年をここに入力してください。'
        self.fields['前回の摂取月'].widget.attrs['class'] = 'form-control'
        self.fields['前回の摂取月'].widget.attrs['placeholder'] = '前回のワクチンの接種月をここに入力してください。'
        self.fields['前回の摂取日'].widget.attrs['class'] = 'form-control'
        self.fields['前回の摂取日'].widget.attrs['placeholder'] = '前回ワクチンの接種日をここに入力してください。'

        self.fields['病名'].widget.attrs['class'] = 'form-control'
        self.fields['病名'].widget.attrs['placeholder'] = '病名をここに入力してください。'
        self.fields['具合悪い点'].widget.attrs['class'] = 'form-control'
        self.fields['具合悪い点'].widget.attrs['placeholder'] = '具合悪い点をここに入力してください。'
        self.fields['アレルギー'].widget.attrs['class'] = 'form-control'
        self.fields['アレルギー'].widget.attrs['placeholder'] = 'アレルギーをここに入力してください'
        self.fields['前回のワクチンの種類'].widget.attrs['class'] = 'form-control'
        self.fields['前回のワクチンの種類'].widget.attrs['placeholder'] = '接種したワクチンの種類をここに入力してください'
        self.fields['具合が悪くなった予防接種名'].widget.attrs['class'] = 'form-control'
        self.fields['具合が悪くなった予防接種名'].widget.attrs['placeholder'] = 'アレルギーのある予防接種名をここに入力してください'
        self.fields['症状'].widget.attrs['class'] = 'form-control'
        self.fields['症状'].widget.attrs['placeholder'] = '症状をここに入力してください'
        self.fields['前回受けた予防接種名'].widget.attrs['class'] = 'form-control'
        self.fields['前回受けた予防接種名'].widget.attrs['placeholder'] = '前回受けた予防接種名をここに入力してください'
        self.fields['前回受けた予防接種日'].widget.attrs['class'] = 'form-control'
        self.fields['前回受けた予防接種日'].widget.attrs['placeholder'] = '前回受けた予防接種日をここに入力してください'

        self.fields['ワクチン接種を以前接種したことはありますか'].widget.attrs['class'] = 'form-control'
        self.fields['ワクチン接種を以前接種したことはありますか'].widget.attrs['placeholder'] = '以前予防接種を受けたことはありますか？　はいorいいえでお応えください'
        self.fields['現住所と住民票の住所は同じですか'].widget.attrs['class'] = 'form-control'
        self.fields['現住所と住民票の住所は同じですか'].widget.attrs['placeholder'] = '現住所と住民票の住所は同じですか？　はいorいいえでお応えください'
        self.fields['ワクチンの副反応について理解していますか'].widget.attrs['class'] = 'form-control'
        self.fields['ワクチンの副反応について理解していますか'].widget.attrs['placeholder'] = 'ワクチンの副反応について理解していますか？　はいorいいえでお応えください'
        self.fields['現在治療を受けていますか'].widget.attrs['class'] = 'form-control'
        self.fields['現在治療を受けていますか'].widget.attrs['placeholder'] = 'ワクチンの副反応について理解していますか？　はいorいいえでお応えください'
        self.fields['持病はありますか'].widget.attrs['class'] = 'form-control'
        self.fields['持病はありますか'].widget.attrs['placeholder'] = '持病はありますか？　はいorいいえでお応えください'
        self.fields['体に具合悪いところはありますか'].widget.attrs['class'] = 'form-control'
        self.fields['体に具合悪いところはありますか'].widget.attrs['placeholder'] = '具合が悪い点はありますか？　はいorいいえでお応えください'
        self.fields['痙攣を起こしたことはありますか'].widget.attrs['class'] = 'form-control'
        self.fields['痙攣を起こしたことはありますか'].widget.attrs['placeholder'] = '痙攣を起こしたことはありますか？　はいorいいえでお応えください'
        self.fields['重度のアレルギーはありますか'].widget.attrs['class'] = 'form-control'
        self.fields['重度のアレルギーはありますか'].widget.attrs['placeholder'] = '重度のアレルギーを起こしたことはありますか？　はいorいいえでお応えください'
        self.fields['予防接種で具合が悪くなったことはありますか'].widget.attrs['class'] = 'form-control'
        self.fields['予防接種で具合が悪くなったことはありますか'].widget.attrs['placeholder'] = '予防接種で具合が悪くなったことはありますか？　はいorいいえでお応えください'
        self.fields['現在妊娠していますか'].widget.attrs['class'] = 'form-control'
        self.fields['現在妊娠していますか'].widget.attrs['placeholder'] = '妊娠又は授乳中ですか？　はいorいいえでお応えください'
        self.fields['_2週間以内に予防接種を打ちましたか'].widget.attrs['class'] = 'form-control'
        self.fields['_2週間以内に予防接種を打ちましたか'].widget.attrs['placeholder'] = '妊娠又は授乳中ですか？　はいorいいえでお応えください'
        self.fields['_2週間以内に打った予防接種の種類'].widget.attrs['class'] = 'form-control'
        self.fields['_2週間以内に打った予防接種の種類'].widget.attrs['placeholder'] = '2週間以内に打った予防接種の種類を記入してください'
        self.fields['_今日の予防接種について何か質問はありますか'].widget.attrs['class'] = 'form-control'
        self.fields['_今日の予防接種について何か質問はありますか'].widget.attrs['placeholder'] = '今回の予防接種について質問はありますか？　はいorいいえでお応えください'
        self.fields['何らかの持病をもっていますか'].widget.attrs['id'] = '何らかの持病をもっていますか-id'
        self.fields['病名を選択してください'].widget.attrs['class'] = 'form-control'
        self.fields['病名を選択してください'].widget.attrs['placeholder'] = '何らかの持病をお持ちですか？　該当するものを選択してください'
        self.fields['上記以外の持病をもっていますか'].widget.attrs['id'] = '上記以外の持病をもっていますか-id'
        self.fields['その他の病気'].widget.attrs['class'] = 'form-control'
        self.fields['その他の病気'].widget.attrs['placeholder'] = '上記以外の病気を入力してください'

        self.fields['何らかの投薬を受けていますか'].widget.attrs['class'] = 'form-control'
        self.fields['何らかの投薬を受けていますか'].widget.attrs['placeholder'] = '何らかの投薬を受けていますか？　はいorいいえでお応えください'

        self.fields['接種を希望しますか'].widget.attrs['class'] = 'form-control'
        self.fields['接種を希望しますか'].widget.attrs['placeholder'] = '医師の説明を受けて接種を希望しますか？　はいorいいえでお応えください'

        self.fields['サラサラにする薬'].widget.attrs['class'] = 'form-control'
        self.fields['サラサラにする薬'].widget.attrs['id'] = 'サラサラにする薬-id'
        self.fields['サラサラにする薬'].widget.attrs['placeholder'] = '血液をサラサラにする薬を処方されていますか？　はいの場合は✓してください'

        self.fields['処方されている薬名を記入してください'].widget.attrs['class'] = 'form-control'
        self.fields['処方されている薬名を記入してください'].widget.attrs['placeholder'] = '薬の名前を記述してください'

        self.fields['その他に処方されている薬名を記入してください'].widget.attrs['class'] = 'form-control'
        self.fields['その他に処方されている薬名を記入してください'].widget.attrs['placeholder'] = 'その他に処方されている薬名を記入してください'

        self.fields['その他に処方されている薬'].widget.attrs['class'] = 'form-control'
        self.fields['その他に処方されている薬'].widget.attrs['id'] = 'その他に処方されている薬-id'
        self.fields['その他に処方されている薬'].widget.attrs['placeholder'] = 'その他に処方されているお薬はありますか？'
        '''
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'
        self.fields['市外局番'].widget.attrs['class'] = 'form-control'
        self.fields['市外局番'].widget.attrs['placeholder'] = '電話番号をここに入力してください。'
        self.fields['前回受けた予防接種月'].widget.attrs['class'] = 'form-control'
        self.fields['前回受けた予防接種月'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['前回受けた予防接種日'].widget.attrs['class'] = 'form-control'
        self.fields['前回受けた予防接種日'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['性別'].widget.attrs['class'] = 'form-control'
        self.fields['性別'].widget.attrs['placeholder'] = '性別をここに入力してください。'
        self.fields['degree'].widget.attrs['class'] = 'form-control'
        self.fields['degree'].widget.attrs['placeholder'] = '体温をここに入力してください。'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'
         '''




        def send_email(self):

            お名前 = self.cleaned_data['お名前']
            email = self.cleaned_data['email']
            都道府県 = self.cleaned_data['都道府県']
            市町村 = self.cleaned_data['市町村']
            市町村以下の住所 = self.cleaned_data['市町村以下の住所']
            tell = self.cleaned_data['tell']
            year = self.cleaned_data['year']
            前回受けた予防接種月 = self.cleaned_data['前回受けた予防接種月']
            前回受けた予防接種日 = self.cleaned_data['前回受けた予防接種日']
            性別 = self.cleaned_data['性別']
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



