# Generated by Django 3.2.7 on 2023-02-07 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_alter_diary_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='diary',
            options={'verbose_name_plural': 'Diary2'},
        ),
        migrations.AddField(
            model_name='diary',
            name='お薬',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='お薬'),
        ),
        migrations.AddField(
            model_name='diary',
            name='お薬名',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='お薬名'),
        ),
        migrations.AddField(
            model_name='diary',
            name='お酒',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='お酒'),
        ),
        migrations.AddField(
            model_name='diary',
            name='たばこ',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='たばこ'),
        ),
        migrations.AddField(
            model_name='diary',
            name='たばこ期間',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='たばこ期間'),
        ),
        migrations.AddField(
            model_name='diary',
            name='たばこ頻度',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='たばこ頻度'),
        ),
        migrations.AddField(
            model_name='diary',
            name='ふりがな',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='ふりがな'),
        ),
        migrations.AddField(
            model_name='diary',
            name='アレルギー名',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='アレルギー名'),
        ),
        migrations.AddField(
            model_name='diary',
            name='住所',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='住所'),
        ),
        migrations.AddField(
            model_name='diary',
            name='体温',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='体温'),
        ),
        migrations.AddField(
            model_name='diary',
            name='妊娠',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='妊娠'),
        ),
        migrations.AddField(
            model_name='diary',
            name='性別',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='diary',
            name='手術日',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='手術日'),
        ),
        migrations.AddField(
            model_name='diary',
            name='手術病名',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='手術病名'),
        ),
        migrations.AddField(
            model_name='diary',
            name='手術病院',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='手術病院'),
        ),
        migrations.AddField(
            model_name='diary',
            name='手術経験',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='手術経験'),
        ),
        migrations.AddField(
            model_name='diary',
            name='授乳中',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='授乳中'),
        ),
        migrations.AddField(
            model_name='diary',
            name='携帯電話番号',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='携帯電話番号'),
        ),
        migrations.AddField(
            model_name='diary',
            name='治療中の病気',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='治療中の病気'),
        ),
        migrations.AddField(
            model_name='diary',
            name='生年月日',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='生年月日'),
        ),
        migrations.AddField(
            model_name='diary',
            name='病気',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='病気'),
        ),
        migrations.AddField(
            model_name='diary',
            name='禁煙期間',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='禁煙期間'),
        ),
        migrations.AddField(
            model_name='diary',
            name='血圧',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='血圧を入力してください'),
        ),
        migrations.AddField(
            model_name='diary',
            name='記入日',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='記入日'),
        ),
        migrations.AddField(
            model_name='diary',
            name='郵便番号',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='郵便番号'),
        ),
        migrations.AddField(
            model_name='diary',
            name='電話番号',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='アレルギー',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='アレルギー'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='年齢',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='病名',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='病名'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='症状',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='症状を選択してください'),
        ),
    ]