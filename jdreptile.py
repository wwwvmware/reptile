import time
import requests
import re



def GETfristhtml(n):
    url = 'https://search.jd.com/Search?keyword=%E9%9E%8B%E5%AD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9E%8B%E5%AD%90&page='+str(2*n-1)+'&s=1&click=0'
    header = {'authority':'search.jd.com',
               'method': 'GET',
               'scheme':'https',
               'referer':'https://search.jd.com/Search?keyword=%E9%9E%8B%E5%AD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9E%8B%E5%AD%90&page=1&s=1&click=0',
               'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
               'x-requested-with':'XMLHttpRequest'
               }
    r = requests.get(url,headers = header)
    r.encoding = r.apparent_encoding
    jdhtml = r.text
    JDA = re.findall('class="p-price">([\s\S]*?)</strong>[\s\S]*?p-name-type-2">([\s\S]*?)<i class="promo-words"',jdhtml)
    JDB = re.findall('<i>(.*?)</i>[\s\S]*?href="(.*?)"[\s\S]*?<em>(.*?)</em>',str(JDA))
    JDC = re.sub('<.*?>',' ',str(JDB))
    print (len(JDC))

def GETlasthtml(n):
    a=time.time()
    b='%.5f'%a
    url = 'https://search.jd.com/s_new.php?keyword=%E9%9E%8B%E5%AD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9E%8B%E5%AD%90&page='+str(2*n)+'&s='+str(1+(n-1)*30)+'&scrolling=y&log_id='+ str(b)
    header = {'authority':'search.jd.com',
               'method': 'GET',
               'scheme':'https',
              'path':'/s_new.php?keyword=%E9%9E%8B%E5%AD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9E%8B%E5%AD%90&page=2&s=31&scrolling=y&log_id=1580827141.10589&tpl=3_M&show_items=37632423151,4511485,29012880250,3808309,7318164,10099270050,62735086440,57930278720,12315966459,30890079136,44626273102,56935390336,61582595748,5832455,65176198573,55928445356,1566467220,10876716031,10691554914,54062677090,6477914,16710528379,20901817794,5162430,16337852227,56471649190,63161768904,100001583797,4973819,5791317',
               'referer':'https://search.jd.com/Search?keyword=%E9%9E%8B%E5%AD%90&enc=utf-8&wq=%E9%9E%8B%E5%AD%90&pvid=7099e2ea2e374d749daab6592acf6136',
               'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
               'x-requested-with':'XMLHttpRequest'
               }
    r = requests.get(url,headers = header)
    r.encoding = r.apparent_encoding
    jdhtml1 = r.text
    JDd = re.findall('class="p-price">([\s\S]*?)</strong>[\s\S]*?p-name-type-2">([\s\S]*?)<i class="promo-words"',jdhtml1)
    JDe = re.findall('<i>(.*?)</i>[\s\S]*?href="(.*?)"[\s\S]*?<em>(.*?)</em>',str(JDd))
    JDf = re.sub('<.*?>',' ',str(JDe))
    print (len(JDf))

def main():


    n = 1
    
    print(GETfristhtml(n))
    print(GETlasthtml(n))
    



main()
