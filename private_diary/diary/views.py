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
        cc.drawString(64, 664, birdday[0])  # x, y, 文字列を指定
        cc.drawString(81, 664, birdday[1])  # x, y, 文字列を指定
        cc.drawString(98, 664, birdday[2])  # x, y, 文字列を指定
        cc.drawString(115, 664, birdday[3])  # x, y, 文字列を指定
        cc.drawString(143, 664, birdday[4])  # x, y, 文字列を指定
        cc.drawString(160, 664, birdday[5])  # x, y, 文字列を指定
        cc.drawString(188, 664, birdday[6])  # x, y, 文字列を指定
        cc.drawString(205, 664, birdday[7])  # x, y, 文字列を指定

        old = form.cleaned_data['yearsOld']
        cc.drawString(295, 664, birdday[0])  # x, y, 文字列を指定
        cc.drawString(278, 664, birdday[0])  # x, y, 文字列を指定
        cc.drawString(261, 664, birdday[0])  # x, y, 文字列を指定


        # 文字サイズで書き出し
        cc.setFont(fontname, 15)  # フォントとサイズを指定

        #cc.drawString(60, 755, '京都')  # x, y, 文字列を指定
        cc.drawString(60, 755, form.cleaned_data['address1'] + "✓")  # x, y, 文字列を指定
        cc.drawString(230, 755, form.cleaned_data['address2'])  # x, y, 文字列を指定
        cc.drawString(60, 728, form.cleaned_data['address3'])  # x, y, 文字列を指定
        cc.drawString(60, 692, form.cleaned_data['name'])  # x, y, 文字列を指定
        cc.drawString(105, 615, form.cleaned_data['times'])  # x, y, 文字列を指定
        cc.drawString(245, 615, form.cleaned_data['lastTime1'])  # x, y, 文字列を指定
        cc.drawString(316, 615, form.cleaned_data['lastTime2'])  # x, y, 文字列を指定
        cc.drawString(364, 615, form.cleaned_data['lastTime3'])  # x, y, 文字列を指定


        cc.setFont(fontname, 10)  # フォントのサイズを指定
        cc.drawString(300, 460, form.cleaned_data['sick'])  # x, y, 文字列を指定
        cc.drawString(240, 440, form.cleaned_data['badCondition'])  # x, y, 文字列を指定
        cc.drawString(170, 390, form.cleaned_data['allegy'])  # x, y, 文字列を指定
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


        # 丸を描画する
        cc.circle(195, 755, 7, 1, 0)

        cc.showPage()
        cc.save()

        return super().form_valid(form)