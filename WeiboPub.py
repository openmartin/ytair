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
URL_PRE = 'http://60.208.91.115:6600/Images/'


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
    
    print access_token
    
    userToken = UserToken()
    userToken.uid = r.uid
    userToken.access_token = r.access_token
    userToken.expires_in = r.expires_in
    userToken.save()
    

air_pollutants_dict = {'NO2':'141', 'PM2.5':'132', \
                       'O3':'108', 'PM10':'107', \
                       'CO':'106', 'SO2':'101'}

def get_detail_AirPollutants(air_pollutants_list_hourly, air_pollutants_no):
    #141 NO2, 132 PM2.5, 108 O3, 107 PM10, 106 CO, 101 SO2
    for a in air_pollutants_list_hourly:
        if a.poll_item_code == air_pollutants_no:
            break
        else:
            pass
        
    return a.poll_value

if __name__ == '__main__':
    #url = get_authorize_url()
    #print url
    
    #SOMECODE = 'aec9b9cd5b7093d2108636acc8bc5604'
    #get_access_token(SOMECODE)
    
    uid = '3225569841'  #烟台占星
    userToken = UserToken.objects.get(pk='3225569841')
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
        
        weibo_template = u'#烟台##空气质量#采样点：$sample_locate，采样时间：$sample_time，空气质量$sample_aqi_des(AQI:$sample_aqi)，主要污染物为$sample_main_pollutants。'
        td = dict()
        td['sample_locate'] = sample_locate
        td['sample_time'] = sample_time
        td['sample_aqi_des'] = sample_aqi_des
        td['sample_aqi'] = sample_aqi
        td['sample_main_pollutants'] = sample_main_pollutants
        
        weibo_txt = Template(weibo_template).substitute(td)
        #print weibo_txt
        
        air_pollutants = AirPollutants.objects.filter(report_hour=report_hour, area_name=u'轴承厂', hourly='Y')
        pollutants_concen_txt = ''
        if len(air_pollutants) == 6:
            so2_concen = get_detail_AirPollutants(air_pollutants, air_pollutants_dict['SO2'])*1000
            no2_concen = get_detail_AirPollutants(air_pollutants, air_pollutants_dict['NO2'])*1000
            pm10_concen = get_detail_AirPollutants(air_pollutants, air_pollutants_dict['PM10'])*1000
            co_concen = get_detail_AirPollutants(air_pollutants, air_pollutants_dict['CO'])*1000
            o3_concen = get_detail_AirPollutants(air_pollutants, air_pollutants_dict['O3'])*1000
            pm25_concen = get_detail_AirPollutants(air_pollutants, air_pollutants_dict['PM2.5'])*1000
            
            pollutants_concen_template = u'各污染物浓度：二氧化硫(SO2)$so2_concenμg/m3、二氧化氮(NO2)$no2_concenμg/m3、可吸入颗粒物(PM10)$pm10_concenμg/m3、一氧化碳(CO)$co_concenμg/m3、臭氧(O3)$o3_concenμg/m3、细颗粒物(PM2.5)$pm25_concenμg/m3。'
            
            ts = dict()
            ts['so2_concen'] = so2_concen
            ts['no2_concen'] = no2_concen
            ts['pm10_concen'] = pm10_concen
            ts['co_concen'] = co_concen
            ts['o3_concen'] = o3_concen
            ts['pm25_concen'] = pm25_concen
            
            pollutants_concen_txt = Template(pollutants_concen_template).substitute(ts)
            #print pollutants_concen_txt
            
        else:
            pass
        
        weibo_txt = weibo_txt + pollutants_concen_txt
        #print weibo_txt
        
#         result = client.statuses.upload.post(status=weibo_txt,
#                                           #lat = sample_lantitude,
#                                           #long = sample_longitude,
#                                   pic=open(zcc_visibily.image_url, 'rb'))



