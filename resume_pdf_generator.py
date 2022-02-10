#PDF
from turtle import left
from fpdf import FPDF 
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page ()

#JSON
import json
JSONInfosFile = open('resume_info.json', 'r')
JSONInfos = JSONInfosFile.read()
Infos = json.loads(JSONInfos)

#HEADER
pdf.image ('picture.png', 7, 8, 20 )
pdf.set_font ('arial', 'BU', 20)
pdf.cell(78,5,"AIRA X. DEE", ln=True, align= 'C')
pdf.set_font ('arial', '',  8)
pdf.cell(85,5,"airaxdee@gmail.com / 0935-654-7854", ln=True, align= 'C')
pdf.cell(123,5,"Objective: To be part of a company that furnishes professional growth", ln=True, align= 'C')

#PERSONAL INFORMATION
pdf.cell(100,8,"                ", ln= True,)
pdf.set_font ('arial', 'B',  10)
pdf.set_text_color (r= 70, g= 130, b= 180)
pdf.cell (120,10, 'PERSONAL INFORMATION', ln=True)
pdf.set_font ('arial', '',  8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10,3, Infos [0] ['Birthday'], ln=True,)
pdf.cell(10,3, Infos [0] ['Address'], ln=True,)
pdf.cell(10,3, Infos [0] ['Nationality'], ln=True,)
pdf.cell(10,3, Infos [0] ['Gender'], ln=True,)
pdf.cell(10,3, Infos [0] ['Status'], ln=True,)
pdf.cell(10,3, Infos [0] ['Height'], ln=True,)
pdf.cell(10,3, Infos [0] ['Weight'], ln=True,)

#EDUCATIONAL BACKGROUND
pdf.set_font ('arial', 'B',  10)
pdf.set_text_color (r= 70, g= 130, b= 180)
pdf.cell (120,10, 'EDUCATIONAL BACKGROUND', ln=True)
pdf.set_font ('arial', '',  8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10,3, Infos [0] ['Elementary'], ln=True,)
pdf.cell(10,3, Infos [0] ['Junior High School'], ln=True,)
pdf.cell(10,3, Infos [0] ['Senior High School'], ln=True,)
pdf.cell(10,3, Infos [0] ['College'], ln=True,)

#SKILLS
pdf.set_font ('arial', 'B',  10)
pdf.set_text_color (r= 70, g= 130, b= 180)
pdf.cell (120,10, 'SKILLS', ln=True)
pdf.set_font ('arial', '',  8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10,3, Infos [0] ['Creativity'], ln=True,)
pdf.cell(10,3, Infos [0] ['Leadership'], ln=True,)
pdf.cell(10,3, Infos [0] ['Computer'], ln=True,)
pdf.cell(10,3, Infos [0] ['Reading'], ln=True,)
pdf.cell(10,3, Infos [0] ['Writing'], ln=True,)

#ACHIEVEMENTS
pdf.set_font ('arial', 'B',  10)
pdf.set_text_color (r= 70, g= 130, b= 180)
pdf.cell (120,10, 'ACHIEVEMENTS', ln=True)
pdf.set_font ('arial', '',  8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10,3, Infos [0] ['Achievement1'], ln=True,)
pdf.cell(10,3, Infos [0] ['Achievement2'], ln=True,)
pdf.cell(10,3, Infos [0] ['Achievement3'], ln=True,)
pdf.cell(10,3, Infos [0] ['Achievement4'], ln=True,)

#CHARACTER REFERENCE
pdf.set_font ('arial', 'B',  10)
pdf.set_text_color (r= 70, g= 130, b= 180)
pdf.cell (120,10, 'CHARACTER REFERENCE', ln=True)
pdf.set_font ('arial', 'B',  8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10,4, Infos [0] ['Character Reference1'], ln=True,)
pdf.set_font ('arial', 'I',  8)
pdf.cell(10,4, Infos [0] ['Reference 1'], ln=True,)
pdf.set_font ('arial', 'B',  8)
pdf.cell(10,4, Infos [0] ['Character Reference2'], ln=True,)
pdf.set_font ('arial', 'I',  8)
pdf.cell(10,4, Infos [0] ['Reference 2'], ln=True,)

#FOOTER
pdf.cell(100,25,"I hereby certify that the above information are untrue and incorrect", ln=True,)
pdf.image ('signature.png', -7, 179, 50)
pdf.set_font ('arial', 'U', 10)
pdf.cell(100,5,"                ", ln= True,)
pdf.set_font ('arial', '', 10)
pdf.cell(100,5,"Aira X. Dee", ln=True,)

pdf.output ('AIRA_X_DEE.pdf')        