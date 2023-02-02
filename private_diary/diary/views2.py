from django.http import HttpResponseRedirect
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait, landscape, A3, A4, A5, A6, B3, B4, B5, B6
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import logging
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from .forms2 import Inquiry2Form

logger = logging.getLogger(__name__)

from django.views import generic
class IndexView(generic.TemplateView):
    template_name = "index.html"

class Inquiry2View(generic.FormView):
    template_name = "inquiry2.html"
    form_class = Inquiry2Form
    success_url = reverse_lazy('diary:inquiry2')


    def form_valid(self, form):

        # フォントファイルを指定して、フォントを登録
        fontname = "IPA Gothic"
        pdfmetrics.registerFont(TTFont(fontname, './ipaexg.ttf'))

        monshin2_template = './monshin2_template.pdf'
        output_path = './diary/static/assets/monshin2_output.pdf'


        # 元のPDFを読み込み
        pages = PdfReader(monshin2_template, decompress=False).pages
        # キャンバスのセット
        cc = canvas.Canvas(output_path, pagesize=portrait(A4))

        # ページ取得
        pp = pagexobj(pages[0])
        cc.doForm(makerl(cc, pp))


        # 位置指定〔　配列　〕　
        cc.setFont(fontname, 10)  # フォントとサイズを指定
        生年月日 = form.cleaned_data['生年月日']
        '''生年月日 = "000000"  # TODO 後で決しておく'''
        cc.drawString(293, 746, 生年月日[0])  # x, y, 文字列を指定
        cc.drawString(300, 746, 生年月日[1])  # x, y, 文字列を指定
        cc.drawString(335, 746, 生年月日[2])  # x, y, 文字列を指定
        cc.drawString(342, 746, 生年月日[3])  # x, y, 文字列を指定
        cc.drawString(378, 746, 生年月日[4])  # x, y, 文字列を指定
        cc.drawString(385, 746, 生年月日[5])  # x, y, 文字列を指定

        郵便番号 = form.cleaned_data['郵便番号']
        '''郵便番号 = "0000000"  # TODO 後で決しておく'''
        cc.drawString(90, 713, 郵便番号[0])  # x, y, 文字列を指定
        cc.drawString(97, 713, 郵便番号[1])  # x, y, 文字列を指定
        cc.drawString(104, 713, 郵便番号[2])  # x, y, 文字列を指定
        cc.drawString(144, 713, 郵便番号[3])  # x, y, 文字列を指定
        cc.drawString(151, 713, 郵便番号[4])  # x, y, 文字列を指定
        cc.drawString(158, 713, 郵便番号[5])  # x, y, 文字列を指定
        cc.drawString(165, 713, 郵便番号[6])  # x, y, 文字列を指定

        cc.setFont(fontname, 15)  # フォントのサイズを指定
        記入日 = form.cleaned_data['記入日']
        cc.drawString(479, 805, 記入日[0])  # x, y, 文字列を指定
        cc.drawString(489, 805, 記入日[1])  # x, y, 文字列を指定
        cc.drawString(516, 805, 記入日[2])  # x, y, 文字列を指定
        cc.drawString(526, 805, 記入日[3])  # x, y, 文字列を指定


        # 位置指定〔　基本文字　〕　
        cc.setFont(fontname, 10)  # フォントとサイズを指定
        cc.drawString(83, 762, form.cleaned_data['ふりがな'])  # x, y, 文字列を指定
        cc.drawString(360, 730, form.cleaned_data['年齢'])  # x, y, 文字列を指定

        cc.setFont(fontname, 15)  # フォントとサイズを指定
        cc.drawString(35, 690, form.cleaned_data['住所'])  # x, y, 文字列を指定
        cc.drawString(80, 655, form.cleaned_data['電話番号'])  # x, y, 文字列を指定
        cc.drawString(330, 655, form.cleaned_data['携帯電話番号'])  # x, y, 文字列を指定
        cc.drawString(180, 510, form.cleaned_data['血圧'])  # x, y, 文字列を指定
        cc.drawString(135, 407, form.cleaned_data['病気'])  # x, y, 文字列を指定
        cc.drawString(55, 350, form.cleaned_data['お薬名'])  # x, y, 文字列を指定
        cc.drawString(55, 287, form.cleaned_data['アレルギー名'])  # x, y, 文字列を指定
        cc.drawString(130, 230, form.cleaned_data['手術日'])  # x, y, 文字列を指定
        cc.drawString(130, 198, form.cleaned_data['手術病名'])  # x, y, 文字列を指定
        cc.drawString(130, 168, form.cleaned_data['手術病院'])  # x, y, 文字列を指定
        cc.drawString(195, 102, form.cleaned_data['たばこ頻度'])  # x, y, 文字列を指定
        cc.drawString(232, 102, form.cleaned_data['たばこ期間'])  # x, y, 文字列を指定
        cc.drawString(478, 102, form.cleaned_data['禁煙期間'])  # x, y, 文字列を指定

        cc.setFont(fontname, 20)  # フォントのサイズを指定
        cc.drawString(475, 730, form.cleaned_data['体温'])  # x, y, 文字列を指定

        cc.setFont(fontname, 25)  # フォントのサイズを指定
        cc.drawString(83, 735, form.cleaned_data['お名前'])  # x, y, 文字列を指定


        # チェックボタン
        cc.setFont(fontname, 15)  # フォントのサイズを指定
        is症状 = form.cleaned_data['症状']
        if is症状 == "1":
            cc.drawString(55, 574, '✓')  #発熱
        elif is症状 == "2":
            cc.drawString(55, 557, '✓')  #頭痛
        elif is症状 == "3":
            cc.drawString(55, 542, '✓') #腹痛
        elif is症状 == "4":
            cc.drawString(55, 526, '✓') #腰痛
        elif is症状 == "5":
            cc.drawString(55, 510, '✓') #血圧が高い
        elif is症状 == "6":
            cc.drawString(121, 574, '✓') #のどの痛み
        elif is症状 == "7":
            cc.drawString(121, 542, '✓') #吐き気
        elif is症状 == "8":
            cc.drawString(121, 526, '✓') #息苦しい
        elif is症状 == "9":
            cc.drawString(229, 574, '✓') #せき
        elif is症状 == "10":
            cc.drawString(205, 542, '✓') #おうと
        elif is症状 == "11":
            cc.drawString(205, 526, '✓') #からだがだるい
        elif is症状 == "12":
            cc.drawString(301, 574, '✓') #たん
        elif is症状 == "13":
            cc.drawString(277, 542, '✓') #下痢
        elif is症状 == "14":
            cc.drawString(373, 574, '✓') #鼻水
        elif is症状 == "15":
            cc.drawString(349, 542, '✓') #便秘
        elif is症状 == "16":
            cc.drawString(337, 526, '✓') #めまい
        elif is症状 == "17":
            cc.drawString(445, 574, '✓') #関節の痛み
        elif is症状 == "18":
            cc.drawString(421, 542, '✓') #食欲がない
        elif is症状 == "19":
            cc.drawString(421, 526, '✓') #ふらつく
        else:
            cc.drawString(55, 494, '✓') #その他

        is治療中の病気 = form.cleaned_data['治療中の病気']
        if is治療中の病気 == "1":
            cc.drawString(172, 465, '✓')
        else:
            cc.drawString(244, 465, '✓')

        is病名 = form.cleaned_data['病名']
        if is病名 == "1":
            cc.drawString(55, 448, '✓')  # 高血圧
        elif is病名 == "2":
            cc.drawString(55, 432, '✓')  # 脳こうそく
        elif is病名 == "3":
            cc.drawString(133, 448, '✓')  # 高脂血症
        elif is病名 == "4":
            cc.drawString(156, 432, '✓')  # 不整脈
        elif is病名 == "5":
            cc.drawString(228, 448, '✓')  # 糖尿病
        elif is病名 == "6":
            cc.drawString(241, 432, '✓')  # ぜんそく
        elif is病名 == "7":
            cc.drawString(313, 448, '✓')  # 腎臓病
        elif is病名 == "8":
            cc.drawString(337, 432, '✓')  # 緑内障
        elif is病名 == "9":
            cc.drawString(397, 448, '✓')  # 痛風
        elif is病名 == "10":
            cc.drawString(421, 432, '✓')  # 関節リウマチ
        else:
            cc.drawString(55, 416, '✓')  # その他

        isお薬 = form.cleaned_data['お薬']
        if isお薬 == "1":
            cc.drawString(197, 385, '✓')
        else:
            cc.drawString(269, 385, '✓')

        isアレルギー = form.cleaned_data['アレルギー']
        if isアレルギー == "1":
            cc.drawString(293, 306, '✓')
        else:
            cc.drawString(365, 306, '✓')

        is手術経験 = form.cleaned_data['手術経験']
        if is手術経験 == "1":
            cc.drawString(378, 259, '✓')
        else:
            cc.drawString(450, 258, '✓')

        isお酒 = form.cleaned_data['お酒']
        if isお酒 == "1":
            cc.drawString(112, 118, '✓')
        else:
            cc.drawString(184, 118, '✓')

        isたばこ = form.cleaned_data['たばこ']
        if isたばこ == "1":
            cc.drawString(109, 102, '✓')
        elif isたばこ == "2":
            cc.drawString(296, 102, '✓')
        else:
            cc.drawString(392, 102, '✓')

        is妊娠 = form.cleaned_data['妊娠']
        if is妊娠 == "1":
            cc.drawString(149, 56, '✓')
        else:
            cc.drawString(221, 56, '✓')

        is授乳中 = form.cleaned_data['授乳中']
        if is授乳中 == "1":
            cc.drawString(413, 56, '✓')
        else:
            cc.drawString(497, 56, '✓')



        # 位置指定〔　円　〕
        is性別 = form.cleaned_data['性別']
        if is性別 == "1":
            cc.circle(424, 749, 7, 1, 0)  # 男
        else:
            cc.circle(445, 749, 7, 1, 0)  # 女



        cc.showPage()
        cc.save()

        return HttpResponseRedirect("http://127.0.0.1:8000/static/assets/monshin2_output.pdf")


