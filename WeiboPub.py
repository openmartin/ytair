# -*- coding: utf-8 -*-
#芝罘区
#芝罘中心商业区
#芝罘西郊工业区
#莱山区
#福山区
#牟平区
#开发区
#微博内容的组织
#图片

from weibo import APIClient
import os
import sys
from datetime import datetime, date
import urllib2
from string import Template
import pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airquality.settings")
from airquality.models import AirPollutants, AirQuality, AirVisibily, UserToken
from django.db.models import Max
from AirQualityIndex import AirQualityIndex

APP_KEY = '1426435104'            # app key
APP_SECRET = '2c30096c3ae5fc8d235bd1afab7af926'      # app secret
CALLBACK_URL = 'http://ytair.hotjoke.cc'  # callback url

#能见图图片的Server
URL_PRE = 'http://120.192.19.202:6600/Images/'


client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)

def get_authorize_url():
    url = client.get_authorize_url()    # redirect the user to 'url'
    print url

def get_access_token(code):
    SOME_CODE = code
    r = client.request_access_token(SOME_CODE)
    access_token = r.access_token  # access token，e.g., abc123xyz456
    expires_in = r.expires_in      # token expires in
    client.set_access_token(access_token, expires_in)
    
    userToken = UserToken()
    userToken.uid = r.uid
    userToken.access_token = r.access_token
    userToken.expires_in = r.expires_in
    userToken.save()


if __name__ == '__main__':
    get_authorize_url()

#    SOMECODE = '3c06e6671b0f3c32b4626e4377bc34ed'
#    get_access_token(SOMECODE)
    uid = '1196520075'  #openmartin
    userToken = UserToken.objects.get(pk='1196520075')
    client.set_access_token(userToken.access_token, userToken.expires_in)
    
    #轴承厂
    #首先获取数据库中最大的时间
    #然后获取能见度图像
    #然后获取空气质量
    report_hour_max = AirVisibily.objects.all().aggregate(Max('report_hour'))
    print report_hour_max
    report_hour = report_hour_max['report_hour__max']
    
    zcc_visibily_qs = AirVisibily.objects.filter(report_hour=report_hour, area_name=u'轴承厂')
    zcc_visibily = zcc_visibily_qs[0]
    
    image_url = URL_PRE + zcc_visibily.image_url
    print image_url
    image_f = urllib2.urlopen(image_url)
    f = open(zcc_visibily.image_url, 'wb')
    f.write(image_f.read())
    f.close()
    
    zcc_aqi_qs = AirQuality.objects.filter(report_hour=report_hour, area_name=u'轴承厂', hourly='Y')
    if len(zcc_aqi_qs) == 0:
        raise 
    else:
        zcc_aqi = zcc_aqi_qs[0]
        print zcc_aqi
        
        aisa_shanghai_tz = pytz.timezone('Asia/Shanghai')  #数据库里面存的是UTC，需要转换成本地时区
        sample_locate = u'轴承厂'
        sample_time = report_hour.astimezone(aisa_shanghai_tz).strftime('%m月%d日%H时').decode('utf-8')
        sample_aqi_des = zcc_aqi.level_str
        sample_aqi = zcc_aqi.aqi
        sample_main_pollutants = zcc_aqi.main_pollutants.strip()
        sample_lantitude = '+' + zcc_aqi.sample_latitude
        sample_longitude = '+' + zcc_aqi.sample_longitude
        
        #民用的地图和政府用的地图差好多，真的是没有办法
        print sample_lantitude
        print sample_longitude
        
        weibo_template = u'#烟台##空气质量#采样点：$sample_locate，采样时间：$sample_time，空气质量$sample_aqi_des(AQI:$sample_aqi)，主要污染物为$sample_main_pollutants'
        td = dict()
        td['sample_locate'] = sample_locate
        td['sample_time'] = sample_time
        td['sample_aqi_des'] = sample_aqi_des
        td['sample_aqi'] = sample_aqi
        td['sample_main_pollutants'] = sample_main_pollutants
        
        weibo_txt = Template(weibo_template).substitute(td)
        #print weibo_txt
        result = client.statuses.upload.post(status=weibo_txt,
                                          #lat = sample_lantitude,
                                          #long = sample_longitude,
                                  pic=open(zcc_visibily.image_url, 'rb'))
    

#print client.statuses.upload.post(status=u'test weibo with picture',
#                                  pic=open(''))



