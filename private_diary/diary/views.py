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

from .forms import InquiryForm

logger = logging.getLogger(__name__)

from django.views import generic
class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')


    def form_valid(self, form):

        # フォントファイルを指定して、フォントを登録
        fontname = "IPA Gothic"
        pdfmetrics.registerFont(TTFont(fontname, './ipaexg.ttf'))

        monshin_template = './monshin_template.pdf'
        output_path = './monshin_output.pdf'

        # 元のPDFを読み込み
        pages = PdfReader(monshin_template, decompress=False).pages

        # キャンバスのセット
        cc = canvas.Canvas(output_path, pagesize=portrait(A4))

        # ページ取得
        pp = pagexobj(pages[0])
        cc.doForm(makerl(cc, pp))

        # 文字サイズで書き出し
        cc.setFont(fontname, 20)  # フォントとサイズを指定
        birdday = form.cleaned_data['birth']
        birdday = "0000000000" # TODO 後で決しておく
        cc.drawString(64, 664, birdday[0])  # x, y, 文字列を指定
        cc.drawString(81, 664, birdday[1])  # x, y, 文字列を指定
        cc.drawString(98, 664, birdday[2])  # x, y, 文字列を指定
        cc.drawString(115, 664, birdday[3])  # x, y, 文字列を指定
        cc.drawString(143, 664, birdday[4])  # x, y, 文字列を指定
        cc.drawString(160, 664, birdday[5])  # x, y, 文字列を指定
        cc.drawString(188, 664, birdday[6])  # x, y, 文字列を指定
        cc.drawString(205, 664, birdday[7])  # x, y, 文字列を指定


        old = form.cleaned_data['yearsOld']
        old = "020"  # TODO 後で決しておく
        cc.drawString(261, 664, old[0])  # x, y, 文字列を指定
        cc.drawString(278, 664, old[1])  # x, y, 文字列を指定
        cc.drawString(295, 664, old[2])  # x, y, 文字列を指定

        tmp1 = form.cleaned_data['bodyTemperature1']
        tmp1 = "00"  # TODO 後で決しておく
        cc.drawString(483, 664, tmp1[0])  # x, y, 文字列を指定
        cc.drawString(500, 664, tmp1[1])  # x, y, 文字列を指定

        tmp2 = form.cleaned_data['bodyTemperature2']
        tmp2 = "0"  # TODO 後で決しておく
        cc.drawString(540, 664, tmp2[0])  # x, y, 文字列を指定


        # 文字サイズで書き出し
        cc.setFont(fontname, 15)  # フォントとサイズを指定

        #cc.drawString(60, 755, '京都')  # x, y, 文字列を指定
        cc.drawString(60, 755, form.cleaned_data['address1'])  # x, y, 文字列を指定
        cc.drawString(230, 755, form.cleaned_data['address2'])  # x, y, 文字列を指定
        cc.drawString(60, 728, form.cleaned_data['address3'])  # x, y, 文字列を指定
        cc.drawString(60, 692, form.cleaned_data['name'])  # x, y, 文字列を指定
        cc.drawString(105, 615, form.cleaned_data['times'])  # x, y, 文字列を指定
        cc.drawString(245, 615, form.cleaned_data['lastTime1'])  # x, y, 文字列を指定
        cc.drawString(316, 615, form.cleaned_data['lastTime2'])  # x, y, 文字列を指定
        cc.drawString(364, 615, form.cleaned_data['lastTime3'])  # x, y, 文字列を指定

        # 丸を描画する
        isKubun1 = form.cleaned_data['kubun1']
        if isKubun1 == "1":
            cc.circle(195, 767, 7, 1, 0)  #都
        elif isKubun1 == "2":
            cc.circle(212, 767, 7, 1, 0)  #道
        elif isKubun1 == "3":
            cc.circle(194, 755, 7, 1, 0)  #府
        else:
            cc.circle(212, 756, 7, 1, 0)  #県

        isKubun2 = form.cleaned_data['kubun2']
        if isKubun2 == "1":
            cc.circle(347, 767, 7, 1, 0)  # 市
        elif isKubun2 == "2":
            cc.circle(365, 767, 7, 1, 0)  # 区
        elif isKubun2 == "3":
            cc.circle(347, 755, 7, 1, 0)  # 町
        else:
            cc.circle(365, 755, 7, 1, 0)  # 村


        isMale = form.cleaned_data['genders']
        if isMale=="1":
            cc.drawString(334, 666, '✓')
        else:
            cc.drawString(540, 664, '✓')

        isWakutin = form.cleaned_data['sessyu3']
        if isWakutin=="1":
            cc.drawString(438, 615, '✓')
        else:
            cc.drawString(484, 615, '✓')

        isjumin = form.cleaned_data['juumin']
        if isjumin == "1":
            cc.drawString(438, 584, '✓')
        else:
            cc.drawString(484, 584, '✓')

        isHannou = form.cleaned_data['hannou']
        if isHannou == "1":
            cc.drawString(438, 564, '✓')
        else:
            cc.drawString(484, 564, '✓')

        isTiryo = form.cleaned_data['tiryo']
        if isTiryo == "1":
            cc.drawString(438, 521, '✓')
        else:
            cc.drawString(484, 521, '✓')

        isByoki = form.cleaned_data['byoki']
        if isByoki == "1":
            cc.drawString(438, 458, '✓')
        else:
            cc.drawString(484, 458, '✓')

        isGuai = form.cleaned_data['guai']
        if isGuai == "1":
            cc.drawString(438, 438, '✓')
        else:
            cc.drawString(484, 438, '✓')
        isKeiren = form.cleaned_data['keiren']
        if isKeiren == "1":
            cc.drawString(438, 418, '✓')
        else:
            cc.drawString(484, 418, '✓')
        isAllegy2 = form.cleaned_data['allegy2']
        if isAllegy2 == "1":
            cc.drawString(438, 394, '✓')
        else:
            cc.drawString(484, 394, '✓')
        isNotGood = form.cleaned_data['notGood']
        if isNotGood == "1":
            cc.drawString(438, 365, '✓')
        else:
            cc.drawString(484, 365, '✓')
        isPregnancy = form.cleaned_data['pregnancy']
        if isPregnancy == "1":
            cc.drawString(438, 341, '✓')
        else:
            cc.drawString(484, 341, '✓')
        isTwoWeek = form.cleaned_data['twoWeek']
        if isTwoWeek == "1":
            cc.drawString(438, 321, '✓')
        else:
            cc.drawString(484, 321, '✓')
        isQuestion = form.cleaned_data['question']
        if isQuestion == "1":
            cc.drawString(438, 301, '✓')
        else:
            cc.drawString(484, 301, '✓')

        isByomei = form.cleaned_data['byomei']
        if isByomei == "1":
            cc.drawString(81, 527, '✓')
        elif isByomei == "2":
            cc.drawString(129, 527, '✓')
        elif isByomei == "3":
            cc.drawString(173, 527, '✓')
        elif isByomei == "4":
            cc.drawString(219, 527, '✓')
        elif isByomei == "5":
            cc.drawString(279, 527, '✓')
        elif isByomei == "6":
            cc.drawString(380, 527, '✓')
        elif isByomei == "7":
            cc.drawString(81, 510, '✓')
        else:
            cc.drawString(188, 510, '✓')



        cc.setFont(fontname, 10)  # フォントのサイズを指定
        cc.drawString(300, 460, form.cleaned_data['sick'])  # x, y, 文字列を指定
        cc.drawString(240, 440, form.cleaned_data['badCondition'])  # x, y, 文字列を指定
        cc.drawString(170, 390, form.cleaned_data['allegy1'])  # x, y, 文字列を指定
        cc.drawString(235, 603, form.cleaned_data['kind'])  # x, y, 文字列を指定
        cc.drawString(70, 361, form.cleaned_data['sessyu1'])  # x, y, 文字列を指定
        cc.drawString(280, 361, form.cleaned_data['symptoms'])  # x, y, 文字列を指定
        cc.drawString(225, 324, form.cleaned_data['sessyu2'])  # x, y, 文字列を指定
        cc.drawString(370, 324, form.cleaned_data['day'])  # x, y, 文字列を指定

        cc.setFont(fontname, 7)  # フォントのサイズを指定
        # cc.drawString(60, 755, '京都')
        # x, y, 文字列を指定
        cc.drawString(60, 712, form.cleaned_data['kana'])  # x, y, 文字列を指定
        cc.drawString(280, 708, form.cleaned_data['tell_shigaikyokuban'])   # x, y, 文字列を指定
        cc.drawString(280, 692, form.cleaned_data['tell_shinaikyokuban'])   # x, y, 文字列を指定
        cc.drawString(328, 692, form.cleaned_data['tell_kanyuusyaban'])  # x, y, 文字列を指定





        cc.showPage()
        cc.save()

        return super().form_valid(form)