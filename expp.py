from bs4 import BeautifulSoup as bs
import requests
import time
import hashlib
def expp():
    f=open('cs.txt','r')
    urls=f.readlines()
    for url in urls:
        try:
            r=requests.get(url,timeout=5)
            if r.status_code==200:
                soup=bs(r.text,"lxml")
                if hashlib.md5:
                    mb1=soup.find_all(name="div",attrs={"class":"line1"})[0].text
                    mb2=soup.find_all(name="div",attrs={"class":"line2"})[0].text
                    f2.open("cs2.txt","a+")
                    f2.write(url+"\n"+mb1+"\n")
                    f2.close()
                    print(mb1)
                    print(mb2)
        except:
            pass
    f.close()
expp()
print("文档中所有网址均处理完毕。")