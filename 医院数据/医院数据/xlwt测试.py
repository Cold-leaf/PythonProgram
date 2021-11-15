import requests,re,xlwt,datetime
from bs4 import BeautifulSoup

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My sheet')
# 合并第0行的第0列到第3列。

worksheet.write_merge(0, 1, 0, 3, 'First Merge')

font = xlwt.Font()
font.blod = True
c
 
pattern_top = xlwt.Pattern()
pattern_top.pattern = xlwt.Pattern.SOLID_PATTERN
#pattern_top.pattern_fore_colour = 5


alignment = xlwt.Alignment()
alignment.horz = 0x02  # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
alignment.vert = 0x01  # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)

 
 
style = xlwt.XFStyle()
style.font = font
style.alignment = alignment
#style.pattern = pattern_top
 
# 合并第1行到第2行的第0列到第3列。
worksheet.write_merge(2, 3, 0, 3, 'Second Merge', style)
 
worksheet.write_merge(4, 6, 3, 6, 'My merge', style)
 
workbook.save('xlwt测试.xls')
