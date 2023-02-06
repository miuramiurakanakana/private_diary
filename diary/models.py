from accounts.models import CustomUser
from django.db import models


class Diary(models.Model):
    """日記モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40, blank=True, null=True)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    都道府県 = models.CharField(verbose_name='都道府県', max_length=40, blank=True, null=True)
    区分 = models.CharField(label='都道府県の区分', required=False)
    区分 = (
          ("1", "都"),
          ("2", "道"),
          ("3", "府"),
          ("4", "県"),
    )
    市町村 = models.CharField(verbose_name='市町村', max_length=40, blank=True, null=True)
    #chose市町村の区分 = (
    #    ("1", "市"),
    #    ("2", "区"),
    #    ("3", "町"),
    #    ("4", "村"),
    #)
    #市町村の区分 = models.ChoiceField(verbose_name='市町村の区分', choices=chose市町村の区分, required=False)
    市町村以下の住所 = models.CharField(verbose_name='市町村以下の住所', max_length=40, blank=True, null=True)
    お名前 = models.CharField(verbose_name='お名前',  max_length=40, blank=True, null=True)
    カナ = models.CharField(verbose_name='フリガナ', max_length=40, blank=True, null=True)
    市外局番 = models.CharField(verbose_name='市外局番', max_length=40, blank=True, null=True)
    市内局番 = models.CharField(verbose_name='市内局番', max_length=40, blank=True, null=True)
    加入者番号 = models.CharField(verbose_name='加入者番号', max_length=40, blank=True, null=True)
    誕生日 = models.CharField(verbose_name='誕生日', max_length=40, blank=True, null=True)
    年齢 = models.CharField(verbose_name='年齢', max_length=40, blank=True, null=True)
    体温_度 = models.CharField(verbose_name='体温(度)', max_length=40, blank=True, null=True)
    体温_分 = models.CharField(verbose_name='体温(分)', max_length=40, blank=True, null=True)
    #chose性別 = (
    #    ("1", "男性"),
    #    ("2", "女性"),
    #)
    #性別 = models.ChoiceField(verbose_name='性別', choices=chose性別, required=False)

    接種回数 = models.CharField(verbose_name='接種回数', max_length=40, blank=True, null=True)
    前回の摂取年 = models.CharField(verbose_name='前回の摂取年', max_length=40, blank=True, null=True)
    前回の摂取月 = models.CharField(verbose_name='前回の摂取月', max_length=40, blank=True, null=True)
    前回の摂取日 = models.CharField(verbose_name='前回の摂取日', max_length=40, blank=True, null=True)
    前回のワクチンの種類 = models.CharField(verbose_name='前回のワクチンの種類', max_length=40, blank=True, null=True)

    病名 = models.CharField(verbose_name='病名', max_length=40, blank=True, null=True)
    具合悪い点 = models.CharField(verbose_name='具合悪い点', max_length=40, blank=True, null=True)
    アレルギー = models.CharField(verbose_name='アレルギー', max_length=40, blank=True, null=True)
    具合が悪くなった予防接種名 = models.CharField(verbose_name='具合が悪くなった予防接種名', max_length=40, blank=True, null=True)
    症状 = models.CharField(verbose_name='症状', max_length=40, blank=True, null=True)
    前回受けた予防接種名 = models.CharField(verbose_name='前回受けた予防接種名', max_length=40, blank=True, null=True)
    前回受けた予防接種日 = models.CharField(verbose_name='前回受けた予防接種日', max_length=40, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        if self.title is None:
            return "タイトルなし"
        else:
            return self.title
