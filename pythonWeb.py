import bs4
import urllib.request
from urllib.request import urlopen as uReq
from urllib.parse import urlencode as dataRes
from bs4 import BeautifulSoup as soup

# open file csv
fileName = 'student.csv'
f = open(fileName, 'w')
header = 'code, maths , literary, english, physical, chemistry, biological, NS mark, history , geography, morality,' \
         ' SS mark\n'
f.write(header)


# function write mark
def writeFile(SBD):
    # creat connect to url, grabbing the page
    my_ul = 'https://thptquocgia.edu.vn/diemthi/'
    pay = {'sbd': SBD}
    payload = dataRes(pay)
    # payload = payload.encode('ascii') --post
    url = my_ul + '?' + payload
    # url = urllib.request.Request(my_ul, data=payload, method="Post") --post
    client = uReq(url)
    page_html = client.read()
    client.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")
    # grabs each mark
    container = page_soup.table.tbody.tr.findAll("td")
    # print("SBD: " + pay['sbd'])
    # for x in container:
    #     if x.text == '':
    #         print("-1")
    #     else:
    #         print(x.text + "\t")

    stringing = pay['sbd'] + ','
    for x in container:
        if x.text == '':
            check = '-1'
        else:
            check = x.text

        if x is container[10]:
            stringing = stringing + check + '\n'
        else:
            stringing = stringing + check + ','
    f.write(stringing)


for x in range(79236):
    index = 1000001
    sbd = '0' + str(index + x)
    writeFile(sbd)

f.close()
