import xlwt
book=xlwt.Workbook()
table=book.add_sheet('over')
sheet=book.add_sheet('test')
table.write(0,0,'姓名')
book.save('测试')
book.save('测试.xls')
