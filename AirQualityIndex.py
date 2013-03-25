# -*- coding: utf-8 -*-

from string import Template
import requests
from  xml.dom  import  minidom
import chardet
from AirQualityModel import AirDeploy, AirVisibly

#参考资料
#webservice 地址 http://58.56.98.78:8801/AirDeploy.Web/AirDeployService.svc
#请求XML
#<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
#<s:Body>
#<GetAirDeployHours><strStCode>370600</strStCode><strItem>0</strItem></GetAirDeployHours>
#</s:Body>
#</s:Envelope>
#AQI计算办法
#http://kjs.mep.gov.cn/hjbhbz/bzwb/dqhjbh/jcgfffbz/201203/W020120410332725219541.pdf

#webservice 有以下方法
#GetAirVisiblyDay    能见度
#GetAirVisiblyHours  实时能见度 小时 有图像
#GetDateTime   当前时间
#GetAirDeployHours 实时污染物
#GetAirDeployAQI   空气质量指数
#GetAirDeployAQIReal 实时空气质量指数

#烟台空气质量
#返回的是一个[dict()]
class AirQualityIndex():
    
    def __init__(self):
        self.WSAddr = 'http://58.56.98.78:8801/AirDeploy.Web/AirDeployService.svc'
        self.StCode = '370600'
    
    def GetAirVisiblyDay(self):
        rXML = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><GetAirVisiblyDay /></s:Body></s:Envelope>'
        #print rXML
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                   'Host':'58.56.98.78:8801',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0',
                   'Content-Length':len(rXML), 
                   'Content-Type':'text/xml; charset=utf-8',
                   'Origin':'http://58.56.98.78:8801',
                   'Referer':'http://58.56.98.78:8801/LEast/ClientBin/AirDeploy.xap',
                   'soapaction':'\"urn:AirDeployService/GetAirVisiblyDay\"'}

        r = requests.post(self.WSAddr, data=rXML, headers = headers)
        #print r.text
        air_visibly_list = self.GetAirVisiblyFromXML(r.text)
        return air_visibly_list
    
    def GetAirVisiblyHours(self):
        rXML = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><GetAirVisiblyHours><strStCode>'+self.StCode+'</strStCode></GetAirVisiblyHours></s:Body></s:Envelope>'
        #print rXML
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                   'Host':'58.56.98.78:8801',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0',
                   'Content-Length':len(rXML), 
                   'Content-Type':'text/xml; charset=utf-8',
                   'Origin':'http://58.56.98.78:8801',
                   'Referer':'http://58.56.98.78:8801/LEast/ClientBin/AirDeploy.xap',
                   'soapaction':'\"urn:AirDeployService/GetAirVisiblyHours\"'}

        r = requests.post(self.WSAddr, data=rXML, headers = headers)
        #print r.text
        air_visibly_list = self.GetAirVisiblyFromXML(r.text)
        return air_visibly_list
    
    def GetDateTime(self):
        rXML = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><GetDateTime /></s:Body></s:Envelope>'
        #print rXML
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                   'Host':'58.56.98.78:8801',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0',
                   'Content-Length':len(rXML), 
                   'Content-Type':'text/xml; charset=utf-8',
                   'Origin':'http://58.56.98.78:8801',
                   'Referer':'http://58.56.98.78:8801/LEast/ClientBin/AirDeploy.xap',
                   'soapaction':'\"urn:AirDeployService/GetDateTime\"'}

        r = requests.post(self.WSAddr, data=rXML, headers = headers)
        #print r.text
        
    
    def GetAirDeployHours(self):
        rXML = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><GetAirDeployHours><strStCode>'+self.StCode+'</strStCode><strItem>0</strItem></GetAirDeployHours></s:Body></s:Envelope>'
        #print rXML
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                   'Host':'58.56.98.78:8801',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0',
                   'Content-Length':len(rXML), 
                   'Content-Type':'text/xml; charset=utf-8',
                   'Origin':'http://58.56.98.78:8801',
                   'Referer':'http://58.56.98.78:8801/LEast/ClientBin/AirDeploy.xap',
                   'soapaction':'\"urn:AirDeployService/GetAirDeployHours\"'}

        r = requests.post(self.WSAddr, data=rXML, headers = headers)
        #print r.text
        air_deploy_list = self.GetAirDeployFromXML(r.text)
        return air_deploy_list
        
    def GetAirDeployAQI(self):
        rXML = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><GetAirDeployAQI><strStCode>'+self.StCode+'</strStCode></GetAirDeployAQI></s:Body></s:Envelope>'
        #print rXML
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                   'Host':'58.56.98.78:8801',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0',
                   'Content-Length':len(rXML), 
                   'Content-Type':'text/xml; charset=utf-8',
                   'Origin':'http://58.56.98.78:8801',
                   'Referer':'http://58.56.98.78:8801/LEast/ClientBin/AirDeploy.xap',
                   'soapaction':'\"urn:AirDeployService/GetAirDeployAQI\"'}

        r = requests.post(self.WSAddr, data=rXML, headers = headers)
        #print r.text
        air_deploy_list = self.GetAirDeployFromXML(r.text)
        return air_deploy_list
    
    def GetAirDeployAQIReal(self):
        rXML = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><GetAirDeployAQIReal><strStCode>'+self.StCode+'</strStCode></GetAirDeployAQIReal></s:Body></s:Envelope>'
        #print rXML
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                   'Host':'58.56.98.78:8801',
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0',
                   'Content-Length':len(rXML), 
                   'Content-Type':'text/xml; charset=utf-8',
                   'Origin':'http://58.56.98.78:8801',
                   'Referer':'http://58.56.98.78:8801/LEast/ClientBin/AirDeploy.xap',
                   'soapaction':'\"urn:AirDeployService/GetAirDeployAQIReal\"'}

        r = requests.post(self.WSAddr, data=rXML, headers = headers)
        #print r.text
        air_deploy_list = self.GetAirDeployFromXML(r.text)
        return air_deploy_list
    
    def GetNodeValueOrNone(self, dom, tagName):
        t = dom.getElementsByTagName(tagName)[0]
        if t.getAttributeNode('i:nil') == 'true':
            return None
        elif t.firstChild == None:
            return None
        else:
            return t.firstChild.nodeValue
    
    def GetAirDeployFromXML(self, xmlstr):
        doc = minidom.parseString(xmlstr.encode('utf-8'))
        air_deploy_list = list()
        aird_l = doc.documentElement.getElementsByTagName('a:CM_AirDeploy')
        for aird in aird_l:
            air_deploy = AirDeploy()
            
            air_deploy.AQI = self.GetNodeValueOrNone(aird, 'a:strAQI')
            air_deploy.AreaCode = self.GetNodeValueOrNone(aird, 'a:strAreaCode')
            air_deploy.AreaName = self.GetNodeValueOrNone(aird, 'a:strAreaName')
            air_deploy.HourAvg = self.GetNodeValueOrNone(aird, 'a:strHourAvg')
            air_deploy.ItemCode = self.GetNodeValueOrNone(aird, 'a:strItemCode')
            air_deploy.ItemName = self.GetNodeValueOrNone(aird, 'a:strItemName')
            air_deploy.Latitude = self.GetNodeValueOrNone(aird, 'a:strLatitude')
            air_deploy.Longitude = self.GetNodeValueOrNone(aird, 'a:strLongitued')
            air_deploy.Level = self.GetNodeValueOrNone(aird, 'a:strLevel')
            air_deploy.PCode = self.GetNodeValueOrNone(aird, 'a:strPCode')
            air_deploy.PName = self.GetNodeValueOrNone(aird, 'a:strPName')
            air_deploy.Pollutants = self.GetNodeValueOrNone(aird, 'a:strPollutants')
            air_deploy.STA = self.GetNodeValueOrNone(aird, 'a:strSTA')
            air_deploy.StCode = self.GetNodeValueOrNone(aird, 'a:strStCode')
            air_deploy.StName = self.GetNodeValueOrNone(aird, 'a:strStName')
            air_deploy.SubID = self.GetNodeValueOrNone(aird, 'a:strSubID')
            air_deploy.ValueAvg = self.GetNodeValueOrNone(aird, 'a:strValueAvg')
            
            air_deploy_list.append(air_deploy)
            
        return air_deploy_list
    
    def GetAirVisiblyFromXML(self, xmlstr):
        doc = minidom.parseString(xmlstr.encode('utf-8'))
        air_visibly_list = list()
        airv_l = doc.documentElement.getElementsByTagName('a:CM_AirVisibly')
        for airv in airv_l:
            air_visibly = AirVisibly()
            
            air_visibly.Visibly = self.GetNodeValueOrNone(airv, 'a:dVisibly')
            air_visibly.DtTime = self.GetNodeValueOrNone(airv, 'a:strDtTime')
            air_visibly.Humidity = self.GetNodeValueOrNone(airv, 'a:strHumidity')
            air_visibly.ImageUrl = self.GetNodeValueOrNone(airv, 'a:strImageUrl')
            air_visibly.ItemDesc = self.GetNodeValueOrNone(airv, 'a:strItemDesc')
            air_visibly.Latitude = self.GetNodeValueOrNone(airv, 'a:strLatitude')
            air_visibly.Longitude = self.GetNodeValueOrNone(airv, 'a:strLongitued')
            air_visibly.MaxTime = self.GetNodeValueOrNone(airv, 'a:strMaxTime')
            air_visibly.PName = self.GetNodeValueOrNone(airv, 'a:strPName')
            air_visibly.ST = self.GetNodeValueOrNone(airv, 'a:strST')
            air_visibly.StCode = self.GetNodeValueOrNone(airv, 'a:strStCode')
            air_visibly.StName = self.GetNodeValueOrNone(airv, 'a:strStName')
            air_visibly.SubID = self.GetNodeValueOrNone(airv, 'a:strSubID')

            air_visibly_list.append(air_visibly)
            
        return air_visibly_list
    


#Test    
if __name__ == '__main__':
    TestAirQualityIndex = AirQualityIndex()
    TestAirQualityIndex.GetAirVisiblyDay()
    TestAirQualityIndex.GetAirVisiblyHours()
    TestAirQualityIndex.GetDateTime()
    TestAirQualityIndex.GetAirDeployHours()
    TestAirQualityIndex.GetAirDeployAQI()
    TestAirQualityIndex.GetAirDeployAQIReal()
    
    