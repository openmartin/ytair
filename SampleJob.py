# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime, date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airquality.settings")
from airquality.models import AirPollutants, AirQuality, AirVisibily
from AirQualityIndex import AirQualityIndex


if __name__ == '__main__':
    TestAirQualityIndex = AirQualityIndex()
    
    #获得采样时间
    air_visibly_hourly_list = []
    air_visibly_dayly_list = []
    
    air_visibly_hourly_list = TestAirQualityIndex.GetAirVisiblyHours()
    date_str = air_visibly_hourly_list[0].DtTime
    report_hour = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    report_hour
    print report_hour
    report_date = report_hour.date()
    print report_date
    
    for air_visibly_hourly in air_visibly_hourly_list:
        av = AirVisibily()
        av.report_date = report_date
        av.report_hour = report_hour
        av.visibily = float(air_visibly_hourly.Visibly)
        av.image_url = air_visibly_hourly.ImageUrl
        av.hourly = 'Y'
        av.daily = 'N'
        av.sample_latitude = air_visibly_hourly.Latitude
        av.sample_longitude = air_visibly_hourly.Longitude
        av.area_code = ''
        av.area_name = air_visibly_hourly.PName
        av.city_code = air_visibly_hourly.StCode
        av.city_name = air_visibly_hourly.StName
        av.save()
    
    air_visibly_dayly_list = TestAirQualityIndex.GetAirVisiblyDay()    
    for air_visibly_dayly in air_visibly_dayly_list:
        av = AirVisibily()
        av.report_date = report_date
        av.report_hour = report_hour
        av.visibily = float(air_visibly_dayly.Visibly)
        av.image_url = ''
        av.hourly = 'N'
        av.daily = 'Y'
        av.sample_longitude = ''
        av.sample_latitude = ''
        av.area_code = ''
        av.area_name = ''
        av.city_code = air_visibly_dayly.StCode
        av.city_name = air_visibly_dayly.StName
        av.save()

#    TestAirQualityIndex.GetDateTime()

    air_deploy_hour_list = TestAirQualityIndex.GetAirDeployHours()
    for air_deploy_hour in air_deploy_hour_list:
        ap = AirPollutants()
        ap.report_date = report_date
        ap.report_hour = report_hour
        ap.poll_value = float(air_deploy_hour.HourAvg)
        ap.poll_item_code = air_deploy_hour.ItemCode
        ap.poll_item_name = air_deploy_hour.ItemName
        ap.hourly = 'Y'
        ap.daily = 'N'
        ap.sample_latitude = air_deploy_hour.Latitude
        ap.sample_longitude = air_deploy_hour.Longitude
        ap.area_code = air_deploy_hour.AreaCode
        ap.area_name = air_deploy_hour.PName
        ap.city_code = air_deploy_hour.AreaCode
        ap.city_name = air_deploy_hour.StName
        ap.daily_avg = float(air_deploy_hour.ValueAvg)
        ap.save()
    
#    TestAirQualityIndex.GetAirDeployAQI()

    air_aqi_hour_list = TestAirQualityIndex.GetAirDeployAQIReal()
    for air_aqi_hour in air_aqi_hour_list:
        aq = AirQuality()
        aq.report_date = report_date
        aq.report_hour = report_hour
        aq.aqi = float(air_aqi_hour.AQI)
        aq.level = air_aqi_hour.Level
        aq.level_str = air_aqi_hour.STA
        aq.main_pollutants = air_aqi_hour.Pollutants
        aq.hourly = 'Y'
        aq.daily = 'N'
        aq.sample_latitude = air_aqi_hour.Latitude
        aq.sample_longitude = air_aqi_hour.Longitude
        aq.area_code = air_aqi_hour.AreaCode
        aq.area_name = air_aqi_hour.PName
        aq.city_code = air_aqi_hour.AreaCode
        aq.city_name = air_aqi_hour.StName
        aq.save()
    