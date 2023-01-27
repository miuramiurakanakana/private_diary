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
        output_path = './diary/static/assets/monshin_output.pdf'

        # 元のPDFを読み込み
        pages = PdfReader(monshin_template, decompress=False).pages

        # キャンバスのセット
        cc = canvas.Canvas(output_path, pagesize=portrait(A4))

        # ページ取得
        pp = pagexobj(pages[0])
        cc.doForm(makerl(cc, pp))

        # 文字サイズで書き出し
        cc.setFont(fontname, 20)  # フォントとサイズを指定
        bird前回受けた予防接種日 = form.cleaned_data['誕生日']
        bird前回受けた予防接種日 = "0000000000" # TODO 後で決しておく
        cc.drawString(64, 664, bird前回受けた予防接種日[0])  # x, y, 文字列を指定
        cc.drawString(81, 664, bird前回受けた予防接種日[1])  # x, y, 文字列を指定
        cc.drawString(98, 664, bird前回受けた予防接種日[2])  # x, y, 文字列を指定
        cc.drawString(115, 664, bird前回受けた予防接種日[3])  # x, y, 文字列を指定
        cc.drawString(143, 664, bird前回受けた予防接種日[4])  # x, y, 文字列を指定
        cc.drawString(160, 664, bird前回受けた予防接種日[5])  # x, y, 文字列を指定
        cc.drawString(188, 664, bird前回受けた予防接種日[6])  # x, y, 文字列を指定
        cc.drawString(205, 664, bird前回受けた予防接種日[7])  # x, y, 文字列を指定


        old = form.cleaned_data['年齢']
        old = "020"  # TODO 後で決しておく
        cc.drawString(261, 664, old[0])  # x, y, 文字列を指定
        cc.drawString(278, 664, old[1])  # x, y, 文字列を指定
        cc.drawString(295, 664, old[2])  # x, y, 文字列を指定

        tmp1 = form.cleaned_data['体温_度']
        tmp1 = "00"  # TODO 後で決しておく
        cc.drawString(483, 664, tmp1[0])  # x, y, 文字列を指定
        cc.drawString(500, 664, tmp1[1])  # x, y, 文字列を指定

        tmp2 = form.cleaned_data['体温_分']
        tmp2 = "0"  # TODO 後で決しておく
        cc.drawString(540, 664, tmp2[0])  # x, y, 文字列を指定


        # 文字サイズで書き出し
        cc.setFont(fontname, 15)  # フォントとサイズを指定

        #cc.drawString(60, 755, '京都')  # x, y, 文字列を指定
        cc.drawString(60, 755, form.cleaned_data['都道府県'])  # x, y, 文字列を指定
        cc.drawString(230, 755, form.cleaned_data['市町村'])  # x, y, 文字列を指定
        cc.drawString(60, 728, form.cleaned_data['市町村以下の住所'])  # x, y, 文字列を指定
        cc.drawString(60, 692, form.cleaned_data['お名前'])  # x, y, 文字列を指定
        cc.drawString(105, 615, form.cleaned_data['接種回数'])  # x, y, 文字列を指定
        cc.drawString(245, 615, form.cleaned_data['前回の摂取年'])  # x, y, 文字列を指定
        cc.drawString(316, 615, form.cleaned_data['前回の摂取月'])  # x, y, 文字列を指定
        cc.drawString(364, 615, form.cleaned_data['前回の摂取日'])  # x, y, 文字列を指定


        # 丸を描画する
        is都道府県の区分 = form.cleaned_data['都道府県の区分']
        if is都道府県の区分 == "1":
            cc.circle(195, 767, 7, 1, 0)  #都
        elif is都道府県の区分 == "2":
            cc.circle(212, 767, 7, 1, 0)  #道
        elif is都道府県の区分 == "3":
            cc.circle(194, 755, 7, 1, 0)  #府
        else:
            cc.circle(212, 756, 7, 1, 0)  #県

        is市町村の区分 = form.cleaned_data['市町村の区分']
        if is市町村の区分 == "1":
            cc.circle(347, 767, 7, 1, 0)  # 市
        elif is市町村の区分 == "2":
            cc.circle(365, 767, 7, 1, 0)  # 区
        elif is市町村の区分 == "3":
            cc.circle(347, 755, 7, 1, 0)  # 町
        else:
            cc.circle(365, 755, 7, 1, 0)  # 村


        isMale = form.cleaned_data['性別']
        if isMale=="1":
            cc.drawString(334, 666, '✓')
        else:
            cc.drawString(370, 664, '✓')

        isWakutin = form.cleaned_data['ワクチン接種を以前接種したことはありますか']
        if isWakutin=="1":
            cc.drawString(438, 615, '✓')
        else:
            cc.drawString(484, 615, '✓')

        isjumin = form.cleaned_data['現住所と住民票の住所は同じですか']
        if isjumin == "1":
            cc.drawString(438, 584, '✓')
        else:
            cc.drawString(484, 584, '✓')

        isワクチンの副反応について理解していますか = form.cleaned_data['ワクチンの副反応について理解していますか']
        if isワクチンの副反応について理解していますか == "1":
            cc.drawString(438, 564, '✓')
        else:
            cc.drawString(484, 564, '✓')

        is現在治療を受けていますか = form.cleaned_data['現在治療を受けていますか']
        if is現在治療を受けていますか == "1":
            cc.drawString(438, 521, '✓')
        else:
            cc.drawString(484, 521, '✓')

        is持病はありますか = form.cleaned_data['持病はありますか']
        if is持病はありますか == "1":
            cc.drawString(438, 458, '✓')
        else:
            cc.drawString(484, 458, '✓')

        is体に具合悪いところはありますか = form.cleaned_data['体に具合悪いところはありますか']
        if is体に具合悪いところはありますか == "1":
            cc.drawString(438, 438, '✓')
        else:
            cc.drawString(484, 438, '✓')
        is痙攣を起こしたことはありますか = form.cleaned_data['痙攣を起こしたことはありますか']
        if is痙攣を起こしたことはありますか == "1":
            cc.drawString(438, 418, '✓')
        else:
            cc.drawString(484, 418, '✓')
        is重度のアレルギーはありますか = form.cleaned_data['重度のアレルギーはありますか']
        if is重度のアレルギーはありますか == "1":
            cc.drawString(438, 394, '✓')
        else:
            cc.drawString(484, 394, '✓')
        is予防接種で具合が悪くなったことはありますか = form.cleaned_data['予防接種で具合が悪くなったことはありますか']
        if is予防接種で具合が悪くなったことはありますか == "1":
            cc.drawString(438, 365, '✓')
        else:
            cc.drawString(484, 365, '✓')
        is現在妊娠していますか = form.cleaned_data['現在妊娠していますか']
        if is現在妊娠していますか == "1":
            cc.drawString(438, 341, '✓')
        else:
            cc.drawString(484, 341, '✓')
        is_2週間以内に予防接種を打ちましたか = form.cleaned_data['_2週間以内に予防接種を打ちましたか']
        if is_2週間以内に予防接種を打ちましたか == "1":
            cc.drawString(438, 321, '✓')
        else:
            cc.drawString(484, 321, '✓')
        is_今日の予防接種について何か質問はありますか = form.cleaned_data['_今日の予防接種について何か質問はありますか']
        if is_今日の予防接種について何か質問はありますか == "1":
            cc.drawString(438, 301, '✓')
        else:
            cc.drawString(484, 301, '✓')

        is病名を選択してください = form.cleaned_data['病名を選択してください']
        if is病名を選択してください == "1":
            cc.drawString(81, 527, '✓')
        elif is病名を選択してください == "2":
            cc.drawString(129, 527, '✓')
        elif is病名を選択してください == "3":
            cc.drawString(173, 527, '✓')
        elif is病名を選択してください == "4":
            cc.drawString(219, 527, '✓')
        elif is病名を選択してください == "5":
            cc.drawString(279, 527, '✓')
        elif is病名を選択してください == "6":
            cc.drawString(380, 527, '✓')
        else:
            cc.drawString(81, 510, '✓')

        isサラサラにする薬 = form.cleaned_data['サラサラにする薬']
        if isサラサラにする薬 == "1":
            cc.drawString(81, 493, '✓')


        is何らかの投薬を受けていますか = form.cleaned_data['何らかの投薬を受けていますか']
        if is何らかの投薬を受けていますか == "1":
            cc.drawString(81, 493, '✓')
        else:
            cc.drawString(285, 493, '✓')

        is接種を希望しますか = form.cleaned_data['接種を希望しますか']
        if is接種を希望しますか == "1":
            cc.drawString(373, 183, '✓')
        else:
            cc.drawString(460, 493, '✓')

        #isSonota = form.cleaned_data['sonota']
        #cc.drawString(188, 510, '✓')



        cc.setFont(fontname, 10)  # フォントのサイズを指定
        cc.drawString(300, 460, form.cleaned_data['病名'])  # x, y, 文字列を指定
        cc.drawString(240, 440, form.cleaned_data['具合悪い点'])  # x, y, 文字列を指定
        cc.drawString(170, 390, form.cleaned_data['アレルギー'])  # x, y, 文字列を指定
        cc.drawString(235, 603, form.cleaned_data['前回のワクチンの種類'])  # x, y, 文字列を指定
        cc.drawString(70, 361, form.cleaned_data['具合が悪くなった予防接種名'])  # x, y, 文字列を指定
        cc.drawString(280, 361, form.cleaned_data['症状'])  # x, y, 文字列を指定
        cc.drawString(225, 324, form.cleaned_data['前回受けた予防接種名'])  # x, y, 文字列を指定
        # TODO なんかうごかない動cc.drawString(370, 324, form.cleaned_data['前回受けた予防接種日'])  # x, y, 文字列を指定
        cc.drawString(190, 495, form.cleaned_data['処方されている薬名を記入してください'])  # x, y, 文字列を指定
        cc.drawString(330, 495, form.cleaned_data['その他に処方されている薬名を記入してください'])  # x, y, 文字列を指定
        cc.drawString(223, 323, form.cleaned_data['_2週間以内に打った予防接種の種類'])  # x, y, 文字列を指定
        cc.drawString(370, 323, form.cleaned_data['_2週間以内に打った予防接種の日付'])  # x, y, 文字列を指定
        #cc.drawString(238, 512, form.cleaned_data['病名を選択してください4']) これはその他にしたやつ  # x, y, 文字列を指定

        cc.setFont(fontname, 7)  # フォントのサイズを指定
        # cc.drawString(60, 755, '京都')
        # x, y, 文字列を指定
        cc.drawString(60, 712, form.cleaned_data['伽奈'])  # x, y, 文字列を指定
        cc.drawString(280, 708, form.cleaned_data['市外局番'])   # x, y, 文字列を指定
        cc.drawString(280, 692, form.cleaned_data['市内局番'])   # x, y, 文字列を指定
        cc.drawString(328, 692, form.cleaned_data['加入者番号'])  # x, y, 文字列を指定





        cc.showPage()
        cc.save()

        #djangoの何らかの機能を使って、下のURLを新しいタブで開くこと
        # http://127.0.0.1:8000/static/assets/monshin_output.pdf

        return super().form_valid(form)