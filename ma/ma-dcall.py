from docxtpl import DocxTemplate

doc =DocxTemplate("dcall-ma-server.docx")
name = {'name': 'Trade4145', 'model': 'Dell PowerEdge', 'sn': 'ABCDEFG'}
doc.render(name)
doc.save('dcall-ma-server-complete.docx')