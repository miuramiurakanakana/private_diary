import os

from django import forms
from django.core.mail import EmailMessage

class Inquiry2Form(forms.Form):

    import datetime
    today = datetime.date.today()

    year = today.year
    month = today.month
    day = today.day

    print('year')  # 2018
    print('month')  # 3
    print('day')  # 12


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
    治療中の病気 = forms.BooleanField(label='治療中の病気', required=False)

    chose病名 = (
        ("1", "高血圧"),
        ("2", "脳こうそく"),
        ("3", "高脂血症"),
        ("4", "不整脈"),
        ("5", "糖尿病"),
        ("6", "ぜんそく"),
        ("7", "腎臓病"),
        ("8", "緑内障"),
        ("9", "痛風(尿酸値が高い)"),
        ("10", "関節リウマチ"),
        ("11", "その他"),
    )
    病名 = forms.MultipleChoiceField(label='病名', choices=chose病名, required=False,widget=forms.CheckboxSelectMultiple())

    病気 = forms.CharField(label='病気', max_length=13, required=False)

    choseお薬 = (
        ("1", "なし"),
        ("2", "あり"),
    )
    お薬 = forms.ChoiceField(label='お薬', choices=choseお薬, required=False)
    お薬名 = forms.CharField(label='お薬名', max_length=13, required=False)

    choseアレルギー = (
        ("1", "なし"),
        ("2", "あり"),
    )
    アレルギー = forms.ChoiceField(label='アレルギー', choices=choseアレルギー, required=False)
    アレルギー名 = forms.CharField(label='アレルギー名', max_length=30, required=False)

    chose手術経験 = (
        ("1", "なし"),
        ("2", "あり"),
    )
    手術経験 = forms.ChoiceField(label='手術経験', choices=chose手術経験, required=False)
    手術日 = forms.CharField(label='手術日', max_length=10, required=False)
    手術病名 = forms.CharField(label='手術病名', max_length=30, required=False)
    手術病院 = forms.CharField(label='手術病院', max_length=30, required=False)

    choseお酒 = (
        ("1", "飲む"),
        ("2", "飲まない"),
    )
    お酒 = forms.ChoiceField(label='お酒', choices=choseお酒, required=False)

    choseたばこ = (
        ("1", "吸う"),
        ("2", "吸わない"),
        ("3", "禁煙した"),
    )
    たばこ = forms.ChoiceField(label='たばこ', choices=choseたばこ, required=False)
    たばこ頻度 = forms.CharField(label='たばこ頻度', max_length=4, required=False)
    たばこ期間 = forms.CharField(label='たばこ期間', max_length=3, required=False)
    禁煙期間 = forms.CharField(label='禁煙期間', max_length=3, required=False)
    chose妊娠 = (
        ("1", "なし"),
        ("2", "あり"),
    )
    妊娠 = forms.ChoiceField(label='妊娠', choices=chose妊娠, required=False)
    chose授乳中 = (
        ("1", "いいえ"),
        ("2", "はい"),
    )
    授乳中 = forms.ChoiceField(label='授乳中', choices=chose授乳中, required=False)


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
        self.fields['治療中の病気'].widget.attrs['placeholder'] = 'form-control'
        self.fields['治療中の病気'].widget.attrs['id'] = '治療中の病気-id'
        self.fields['治療中の病気'].widget.attrs['placeholder'] = '治療中の病気はありますか？'
        self.fields['病名'].widget.attrs['placeholder'] = 'form-control'
        self.fields['病名'].widget.attrs['id'] = '病名-id'
        self.fields['病名'].widget.attrs['placeholder'] = '治療中の病気名を選択してください'
        self.fields['病気'].widget.attrs['class'] = 'form-control'
        self.fields['病気'].widget.attrs['placeholder'] = 'その他の病気をここに入力してください。'
        self.fields['お薬'].widget.attrs['class'] = 'form-control'
        self.fields['お薬'].widget.attrs['placeholder'] = '今飲んでいるお薬はありますか。'
        self.fields['お薬名'].widget.attrs['class'] = 'form-control'
        self.fields['お薬名'].widget.attrs['placeholder'] = '今飲んでいるお薬名をここに入力してください。'
        self.fields['アレルギー'].widget.attrs['class'] = 'form-control'
        self.fields['アレルギー'].widget.attrs['placeholder'] = 'アレルギーはありますか。'
        self.fields['アレルギー名'].widget.attrs['class'] = 'form-control'
        self.fields['アレルギー名'].widget.attrs['placeholder'] = 'アレルギー名を入力してください。'
        self.fields['手術日'].widget.attrs['class'] = 'form-control'
        self.fields['手術日'].widget.attrs['placeholder'] = '手術日を入力してください。'
        self.fields['手術病名'].widget.attrs['class'] = 'form-control'
        self.fields['手術病名'].widget.attrs['placeholder'] = '手術病名を入力してください。'
        self.fields['手術病院'].widget.attrs['class'] = 'form-control'
        self.fields['手術病院'].widget.attrs['placeholder'] = '手術病院を入力してください。'
        self.fields['お酒'].widget.attrs['class'] = 'form-control'
        self.fields['お酒'].widget.attrs['placeholder'] = '飲酒はしますか？'
        self.fields['たばこ'].widget.attrs['class'] = 'form-control'
        self.fields['たばこ'].widget.attrs['placeholder'] = '喫煙はしますか？'
        self.fields['たばこ頻度'].widget.attrs['class'] = 'form-control'
        self.fields['たばこ頻度'].widget.attrs['placeholder'] = 'たばこは1日何本吸いますか？'
        self.fields['たばこ期間'].widget.attrs['class'] = 'form-control'
        self.fields['たばこ期間'].widget.attrs['placeholder'] = 'たばこは何年間吸っていますか？'
        self.fields['禁煙期間'].widget.attrs['class'] = 'form-control'
        self.fields['禁煙期間'].widget.attrs['placeholder'] = '何年前から禁煙していますか？'
        self.fields['妊娠'].widget.attrs['class'] = 'form-control'
        self.fields['妊娠'].widget.attrs['placeholder'] = '妊娠の有無を選択してください。'
        self.fields['授乳中'].widget.attrs['class'] = 'form-control'
        self.fields['授乳中'].widget.attrs['placeholder'] = '授乳中ですか？。'
