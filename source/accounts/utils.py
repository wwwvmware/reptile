import requests
import re
import time
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


from .models import DataInfo
from .forms import DataTable

def send_mail(to, template, context):
    html_content = render_to_string(f'accounts/emails/{template}.html', context)
    text_content = render_to_string(f'accounts/emails/{template}.txt', context)

    msg = EmailMultiAlternatives(context['subject'], text_content, settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

def getpages(pageNum,currentIndex):
    currentPage=int(currentIndex)
    pageNumber=int(pageNum)
    pages = []
    first_page = 1
    print(currentPage)
    last_page = currentPage + 3
    if pageNumber >4:
        if currentPage >=3:
            first_page = currentPage - 2
        if last_page > pageNumber:
            last_page = pageNumber
        for i in range(first_page,last_page):
            pages.append(i)
    else:
        for i in range(first_page,pageNumber+1):
            pages.append(i)
    return pages


def get_data_by_searchKey(userid,searchKey):
    for index in range(2):
        data=GetJDFristHtml(searchKey,index)
        save_data(userid,data)
        data=GetJDLastHtml(searchKey,index)
        save_data(userid,data)
        # data = DataInfo(userid=userid)
        # data.name = 'test'
        # data.price = 10.0
        # data.url = 'test.com'
        # data.source_website="taobao"
        # data.save()
    return DataTable(DataInfo.objects.all())

def save_data(userid,source):
    dataArray = eval(source)
    for goodInfo in dataArray:
        data = DataInfo(userid=userid)
        data.name = goodInfo[2]
        data.price = goodInfo[0]
        data.url = goodInfo[1]
        data.source_website="jd"
        data.save()
def GetJDFristHtml(searchKey,pageIndex):
    url = 'https://search.jd.com/Search?keyword='+searchKey+'&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9E%8B%E5%AD%90&page='+str(2*pageIndex-1)+'&s=1&click=0'
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
    JDA = re.findall('class="p-price">([\\s\\S]*?)</strong>[\\s\\S]*?p-name-type-2">([\\s\\S]*?)<i class="promo-words"',jdhtml)
    JDB = re.findall('<i>(.*?)</i>[\\s\\S]*?href="(.*?)"[\\s\\S]*?<em>(.*?)</em>',str(JDA))
    JDC = re.sub('<.*?>',' ',str(JDB))
    return JDC

def GetJDLastHtml(searchKey,pageIndex):
    a=time.time()
    b='%.5f'%a
    url = 'https://search.jd.com/s_new.php?keyword='+searchKey+'&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%9E%8B%E5%AD%90&page='+str(2*pageIndex)+'&s='+str(1+(pageIndex-1)*30)+'&scrolling=y&log_id='+ str(b)
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
    jdhtml = r.text
    JDA = re.findall('class="p-price">([\\s\\S]*?)</strong>[\\s\\S]*?p-name-type-2">([\\s\\S]*?)<i class="promo-words"',jdhtml)
    JDB = re.findall('<i>(.*?)</i>[\\s\\S]*?href="(.*?)"[\\s\\S]*?<em>(.*?)</em>',str(JDA))
    JDC = re.sub('<.*?>',' ',str(JDB))
    return JDC

def send_activation_change_email(request, email, code):
    context = {
        'subject': _('Change email'),
        'uri': request.build_absolute_uri(reverse('accounts:change_email_activation', kwargs={'code': code})),
    }

    send_mail(email, 'change_email', context)


