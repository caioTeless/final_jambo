from reportlab.lib.styles import (getSampleStyleSheet, ParagraphStyle)
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter


class JamboPDF:

    generator_story = list()

    def __init__(self, file='', save_name=''):
        self.file = file
        self.style = getSampleStyleSheet()
        self.doc = SimpleDocTemplate((save_name + '.pdf'), pagesize=letter)
        self.title_app = 'JAMBO'

    def get_content(self):
        with open(self.file, 'r', encoding='utf-8') as txt_file:
            text_content = txt_file.read()
        return text_content

    @staticmethod
    def return_style_content():
        my_style_content = ParagraphStyle(
            'File',
            alignment=TA_JUSTIFY,
            fontName='Helvetica',
            fontSize=12,
            spaceAfter=6,
            spaceBefore=6,
            leading=24,
            leftIdent=12,
            rightIdent=12,
            spaceShrinkage=0.5,
            wordWrap=True
        )
        return my_style_content

    @staticmethod
    def return_style_title():
        my_style_title = ParagraphStyle(
            'File',
            fontName='Helvetica',
            fontSize=16,
            spaceAfter=50,
            alignment=TA_CENTER
        )
        return my_style_title

    def return_par_content(self):
        p = Paragraph(self.get_content(), self.return_style_content())
        return p

    def return_par_title(self):
        p = Paragraph(self.title_app, self.return_style_title())
        return p

    def return_generator_story(self):
        self.generator_story.append(self.return_par_title())
        self.generator_story.append(self.return_par_content())
        return self.generator_story

    def build_pdf(self):
        self.doc.build(self.return_generator_story())







