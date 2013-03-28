# -*- coding: utf-8 -*-
#from check_in.models import Person,Check,PlayCalender
from airquality.models import AirPollutants, AirQuality, AirVisibily, UserToken
from django.contrib import admin

#class PersonAdmin(admin.ModelAdmin):
#    fields = ('pname', 'pdept' , 'isvalid', 'remark')
#    list_display = ('pname', 'pdept' , 'isvalid')
#    list_display_links = ('pname',)
#    list_filter = ('isvalid',)
#
#admin.site.register(Person, PersonAdmin)
#
#class CheckAdmin(admin.ModelAdmin):
#    fields = ('play_date', 'person', 'has_family', 'family_member_amount', 'check_time')
#    list_display = ('play_date', 'person', 'has_family', 'family_member_amount')
#    list_display_links = ('play_date', 'person')
#    list_filter = ('has_family',)
#    
#admin.site.register(Check, CheckAdmin)    
#
#class PlayCalenderAdmin(admin.ModelAdmin):
#    fields = ('play_date',)
#
#admin.site.register(PlayCalender, PlayCalenderAdmin)


class AirPollutantsAdmin(admin.ModelAdmin):
    fields = ('report_date', 'report_hour', 'poll_value', 'poll_item_code', \
              'poll_item_name','hourly','daily', 'sample_longitude', 'sample_latitude', 'area_code',\
              'area_name', 'city_code', 'city_name')
    list_display = ('report_date', 'report_hour', 'poll_item_name', 'poll_value','area_name')
    list_display_links = ('report_date',)
    list_filter = ('hourly','daily')

admin.site.register(AirPollutants, AirPollutantsAdmin)


class AirQualityAdmin(admin.ModelAdmin):
    fields = ('report_date', 'report_hour', 'aqi', 'level', 'level_str', 'main_pollutants',\
              'hourly','daily', 'sample_longitude', 'sample_latitude', 'area_code',\
              'area_name', 'city_code', 'city_name')
    list_display = ('report_date', 'report_hour', 'aqi', 'area_name')
    list_display_links = ('report_date',)
    list_filter = ('hourly','daily')

admin.site.register(AirQuality, AirQualityAdmin)


class AirVisibilyAdmin(admin.ModelAdmin):
    fields = ('report_date', 'report_hour', 'visibily', 'image_url',\
              'hourly','daily', 'sample_longitude', 'sample_latitude', 'area_code',\
              'area_name', 'city_code', 'city_name')
    list_display = ('report_date', 'report_hour', 'visibily', 'image_url','area_name')
    list_display_links = ('report_date',)
    list_filter = ('hourly','daily')

admin.site.register(AirVisibily, AirVisibilyAdmin)


class UserTokenAdmin(admin.ModelAdmin):
    fields = ('uid', 'access_token', 'expires_in', 'remind_in')
    list_display = ('uid', 'access_token', 'expires_in')
    list_display_links = ('uid',)    
    
admin.site.register(UserToken, UserTokenAdmin)

