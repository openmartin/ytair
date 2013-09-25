# -*- coding: utf-8 -*-
import json
import urllib
import urllib2

class BaiduWeather():
    def __init__(self):
        self.api_addr = 'http://api.map.baidu.com/telematics/v3/weather'
        self.ak = '45a7f8824904cd76965c78be58436e2d'
        
    def get_results(self, city, isquote=False):
        
        if isquote == False:
            api_para_dict = {"output":"json", "ak":self.ak, "location":city}
            api_para = urllib.urlencode(api_para_dict)
            url = self.api_addr + '?' + api_para
        else:
            api_para_dict = {"output":"json", "ak":self.ak}
            api_para = urllib.urlencode(api_para_dict)
            url = self.api_addr + '?' + api_para + '&address=' + city
            

        api_request = urllib2.Request(url)
        rsp_json = urllib2.urlopen(api_request, timeout=10)
        print rsp_json.geturl()
        
        self.result = json.loads(rsp_json.read())
        #print self.result
        return self.result
    
    def get_weather(self):
        json_result = self.result
        city = json_result['results'][0]['currentCity']
        date = json_result['date']
        today = json_result['results'][0]['weather_data'][0]
        today_str = u'今天' + today['date'] + today['weather'] + u',气温' + today['temperature'] + \
            u',' + today['wind']
        tomorrow = json_result['results'][0]['weather_data'][1]
        tomorrow_str = u'明天' + tomorrow['date'] + tomorrow['weather'] + u',气温' + tomorrow['temperature'] + \
            u',' + tomorrow['wind']
            
        #print today_str
        #print tomorrow_str
        return (today_str, tomorrow_str)

if __name__ == '__main__':
    baiduwea = BaiduWeather()
    baiduwea.get_results(u'北京')
    weather =  baiduwea.get_weather()
    print weather
    