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

from .forms2 import InquiryForm2

logger = logging.getLogger(__name__)

from django.views import generic
class IndexView(generic.TemplateView):
    template_name = "index.html"

class Inquiry2View(generic.FormView):
    template_name = "inquiry2.html"
    form_class = InquiryForm2
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


        cc.setFont(fontname, 10)  # フォントのサイズを指定
        cc.drawString(328, 692, form.cleaned_data['都道府県'])  # x, y, 文字列を指定

        cc.showPage()
        cc.save()

        return HttpResponseRedirect("http://127.0.0.1:8000/static/assets/monshin2_output.pdf")


