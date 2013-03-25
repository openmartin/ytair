# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext as _

##valid
#VALID_STATUS = (
#    ('Y', _('valid')),
#    ('N', _('invalid')),
#)
#
##has family
#HAS_FAMILY = (
#    ('Y', _('have')),
#    ('N', _('nothave')),
#)
#
#FAMILY_MEMBER_LIMIT = (
#    (0,'0'),
#    (1,'1'),
#    (2,'2'),
#    (3,'3'),
#    (4,'4'),
#    (5,'5'),
#    (6,'6'),
#    (7,'7'),
#    (8,'8'),
#    (9,'9'),
#)
#
#class Person(models.Model):
#    pname = models.CharField(_('name'), max_length=80)
#    pdept = models.CharField(_('dept'), max_length=80)
#    isvalid = models.CharField(_('isvalid'), max_length=1, default='Y', choices=VALID_STATUS)
#    remark = models.CharField(_('remark'), max_length=100)
#    
#    class Meta:
#        ordering = ['pdept']
#        verbose_name = _('person')
#        verbose_name_plural = _('persons')
#    
#    def __unicode__(self):
#        return self.pname
#    
#
#class Check(models.Model):
#    play_date = models.DateField(_('play_date'), primary_key=False)
#    person = models.ForeignKey(Person, verbose_name=_('person'), primary_key=False)
#    has_family = models.CharField(_('has_family'), max_length=1, default='N', choices=HAS_FAMILY)
#    family_member_amount = models.IntegerField(_('family_member_amount'), default=0, choices=FAMILY_MEMBER_LIMIT)
#    check_time = models.DateTimeField(_('check_time'))
#    
#    def __unicode__(self):
#        return self.play_date.strftime('%Y-%m-%d') + " " + self.person.pname
#    
#    class Meta:
#        ordering = ['-play_date']
#        verbose_name = _('check')
#        verbose_name_plural = _('check')
#
#        
#class PlayCalender(models.Model):
#    play_date = models.DateField(_('play_date'), primary_key=True)
#    
#    def __unicode__(self):
#        return self.play_date.strftime('%Y-%m-%d')
#    
#    class Meta:
#        ordering = ['-play_date']
#        verbose_name = _('play_date')
#        verbose_name_plural = _('play_date')

#YES_OR_NO
YES_OR_NO = (
    ('Y', _('yes')),
    ('N', _('no')),
)


class AirPollutants(models.Model):
    report_id = models.AutoField('id', primary_key=True)
    report_date = models.DateField(_('report_date'))
    report_hour = models.DateTimeField(_('report_date'))
    poll_value = models.FloatField(_('poll_value'))
    poll_item_code = models.CharField(_('poll_item_code'), max_length=80)
    poll_item_name = models.CharField(_('poll_item_code'), max_length=80)
    hourly = models.CharField(_('hourly'), max_length=1, choices=YES_OR_NO)
    daily = models.CharField(_('daily'), max_length=1, choices=YES_OR_NO)
    sample_longitude = models.CharField(_('sample_longitude'), max_length=80)
    sample_latitude = models.CharField(_('sample_latitude'), max_length=80)
    area_code = models.CharField(_('area_code'), max_length=80)
    area_name = models.CharField(_('area_name'), max_length=80)
    city_code = models.CharField(_('city_code'), max_length=80)
    city_name = models.CharField(_('city_name'), max_length=80)
    daily_avg = models.FloatField(_('daily_avg'))
    
    def __unicode__(self):
        return self.report_hour.strftime('%Y-%m-%d %H:%M') + self.poll_item_name
    
    class Meta:
        ordering = ['-report_hour', '-poll_item_code']
        verbose_name = _('AirPollutants')
        verbose_name_plural = _('AirPollutants')



class AirQuality(models.Model):
    report_id = models.AutoField('id', primary_key=True)
    report_date = models.DateField(_('report_date'))
    report_hour = models.DateTimeField(_('report_date'))
    aqi = models.FloatField(_('AirQuailtyIndex'))
    level = models.CharField(_('level'), max_length=80)
    level_str = models.CharField(_('level_str'), max_length=80)
    main_pollutants = models.CharField(_('main_pollutants'), max_length=80)
    hourly = models.CharField(_('hourly'), max_length=1, choices=YES_OR_NO)
    daily = models.CharField(_('daily'), max_length=1, choices=YES_OR_NO)
    sample_longitude = models.CharField(_('longitude'), max_length=80)
    sample_latitude = models.CharField(_('latitude'), max_length=80)
    area_code = models.CharField(_('area_code'), max_length=80)
    area_name = models.CharField(_('area_name'), max_length=80)
    city_code = models.CharField(_('city_code'), max_length=80)
    city_name = models.CharField(_('city_name'), max_length=80)
    
    def __unicode__(self):
        return self.report_hour.strftime('%Y-%m-%d %H:%M') + _('AirQuailty')
    
    class Meta:
        ordering = ['-report_hour']
        verbose_name = _('AirQuality')
        verbose_name_plural = _('AirQuality')



class AirVisibily(models.Model):
    report_id = models.AutoField('id', primary_key=True)
    report_date = models.DateField(_('report_date'))
    report_hour = models.DateTimeField(_('report_date'))
    visibily = models.FloatField(_('visibily'))
    image_url = models.CharField(_('image_url'), max_length=200)
    hourly = models.CharField(_('hourly'), max_length=1, choices=YES_OR_NO)
    daily = models.CharField(_('daily'), max_length=1, choices=YES_OR_NO)
    sample_longitude = models.CharField(_('longitude'), max_length=80)
    sample_latitude = models.CharField(_('latitude'), max_length=80)
    area_code = models.CharField(_('area_code'), max_length=80)
    area_name = models.CharField(_('area_name'), max_length=80)
    city_code = models.CharField(_('city_code'), max_length=80)
    city_name = models.CharField(_('city_name'), max_length=80)
    
    def __unicode__(self):
        return self.report_hour.strftime('%Y-%m-%d %H:%M') + _('visibily')
    
    class Meta:
        ordering = ['-report_hour']
        verbose_name = _('visibily')
        verbose_name_plural = _('visibily')
        

class UserToken(models.Model):
    uid = models.CharField (max_length=80, primary_key=True)
    access_token = models.CharField (max_length=80)
    expires_in = models.CharField (max_length=80)
    remind_in = models.CharField (max_length=80)

    


