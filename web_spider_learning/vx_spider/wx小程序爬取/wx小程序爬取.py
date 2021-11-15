import requests,re,xlwt
from bs4 import BeautifulSoup
import bs4

#学校排名原例
'''
def getHTMLText(url):
    try:
        r=requests.get(urf,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for fr in soup.find_all('tr'):
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].text,tds[1].text,tds[3].text])
def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
def main():
    uinfo=[]
    urf='https://www.shanghairanking.cn/rankings/bcur/2020'
    html=getHTMLText(urf)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()
'''

#学校排名试验
'''
r=requests.get("https://www.shanghairanking.cn/rankings/bcur/2020")
r.encoding=r.apparent_encoding
demo=r.text
ulist=[]
soup=BeautifulSoup(demo,"html.parser")
print("{:^4}\t{:^70}\t{:^10}\t{:^6}\n".format("排名","学校名称","地区","总分"))
for link in soup.find_all('tr'):
    clist=[]
    for clink in link.find_all('td'):
       clist.append(str(clink.text.replace('\n','').replace(',','').replace(" ","")))
         
    #print(clist[::1]) 
    #print("{:^4}\t{:^70}\t{:^10}\t{:^6}".format(clist[0],clist[1],clist[2],clist[4]))
    #print(len(clist))
    #print(clist[0])

    if len(clist)>0:
        print("{:^4}\t{:<70}\t{:^10}\t{:^6}".format(clist[0],clist[1],clist[2],clist[4]))

    del clist
'''

#淘宝商品比较原例  
'''
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
        
def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods+ '&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210314&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48'
    infoList = []
    for i in range(depth):
        
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            print("Error")
            continue
    printGoodsList(infoList) 
    
main()  '''

#伪装headers
'''
headers ={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/65.0.3325.181 Safari/537.36'
        }
'''
#豆瓣电影top250试验
'''
book=xlwt.Workbook()
table=book.add_sheet('top')
table.write_merge(0,1,0,6,'豆瓣电影top250试验')
table.write(2,0,'名称')
table.write(2,1,'英文名')
table.write(2,2,'别名')
table.write(2,3,'人员')
table.write(2,4,'评价')
table.write(2,5,'评分')
table.write(2,6,'参评人数')

urf="https://movie.douban.com/top250"
page=1
while page<=10:
    if page==1:
        r=requests.get(urf,headers=headers)
    else:
        r=requests.get(urf+'?start='+str(25*(page-1))+'&filter=',headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo=r.text
    #print(r.text)
    soup=BeautifulSoup(demo,"html.parser")
    ulist=[]

    for link in soup.find_all('ol'):
    
        #print(link.text)
        i=25*(page-1)+3
        for clink in link.find_all('div','info'):
            clist=[]
            for dlink in clink.find_all('span','title'):
                clist.append(dlink.text.replace("\n","").replace("\xa0/\xa0","").replace("\xa0\xa0\xa0","").replace(" ",""))
            for elink in clink.find_all('span','other'):
                clist.append(elink.text.replace("\n","").replace("\xa0/\xa0","").replace("\xa0\xa0\xa0","").replace(" ",""))
            for flink in clink.find_all('p',''):
                clist.append(flink.text.replace("\n","").replace("\xa0/\xa0","").replace("\xa0\xa0\xa0","").replace(" ",""))
            for glink in clink.find_all('span','rating_num'):
                clist.append(glink.text.replace("\n","").replace("\xa0/\xa0","").replace("\xa0\xa0\xa0","").replace(" ",""))    
            for hlink in clink.find_all(string=re.compile('评价')):
                clist.append(hlink.replace("\n","").replace("\xa0/\xa0","").replace("\xa0\xa0\xa0","").replace(" ",""))
            
        
            #print("名称：{:<10}/{:<10}/{:<20} 信息：{:<100} 评价：{:<5}分 {:<10}人参与".format(clist[0],clist[1],clist[2],clist[3],clist[5],clist[6]))
            if len(clist)==7:
                table.write(i,0,clist[0])
                table.write(i,1,clist[1])
                table.write(i,2,clist[2])
                table.write(i,3,clist[3])
                table.write(i,4,clist[4])
                table.write(i,5,clist[5])
                table.write(i,6,clist[6])
                #print("{:<3}.名称：{:<}/ {:<}/ {:<} \n\t信息：{:<} \n\t评价：{:<30} 评分：{:<5}分\t{:<10}人参与\n".format(i,clist[0],clist[1],clist[2],clist[3],clist[4],clist[5],clist[6]))
            elif len(clist)==6:
                table.write(i,0,clist[0])
                table.write(i,1,clist[1])
                table.write(i,2,clist[2])
                table.write(i,3,clist[3])
                table.write(i,4,clist[4])
                table.write(i,5,clist[5])
                #print("{:<3}.名称：{:<}/ {:<} \n\t信息：{:<} \n\t评价：{:<30} 评分：{:<5}分\t{:<10}人参与\n".format(i,clist[0],clist[1],clist[2],clist[3],clist[4],clist[5]))
            i+=1
            
            del clist
    page+=1

book.save('豆瓣top.xls')
'''

headers = {
'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN',
}
urf="http://mp.weixin.qq.com/mp/jsreport?1=1&key=106&content=,biz:MzUxMzE2NDkwOQ==,mid:2247497838,uin:MTM4MzA1NjkxMw==[key1]Error%3A%20openWeApp%3Aok&r=0.9016350076216746"
page=1

r=requests.get(urf,headers=headers)
   
r.raise_for_status()
r.encoding = r.apparent_encoding
demo=r.text
print(r.text)
soup=BeautifulSoup(demo,"html.parser")
ulist=[]