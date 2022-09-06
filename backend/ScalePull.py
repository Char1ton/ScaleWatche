from lxml import html
import time
import pandas as pd
from tkinter import *
from csv import writer

#Helper Functions
class WeightPull:
    def Main():

        #Weight Controllers
        WeightMonL3 = html.parse("http://10.0.19.49/chan_monitor.cgi").getroot()
        WeightMonL2=html.parse("http://10.0.18.49/chan_monitor.cgi").getroot()
        WeightMonL1=html.parse("http://10.0.17.49/chan_monitor.cgi").getroot()
        WeightMonL4=html.parse("http://10.0.23.49/chan_monitor.cgi").getroot()
        
        WeightL3 = WeightMonL3.get_element_by_id("X00006081")
        WeightL2=WeightMonL2.get_element_by_id("X00006081")
        WeightL1 = WeightMonL1.get_element_by_id("X00006081")
        WeightL4=WeightMonL4.get_element_by_id("X00006081")
        
        WL3,WL2,WL1,WL4=(WeightL3.get('value')),(WeightL2.get('value')),(WeightL1.get('value')),(WeightL4.get('value'))
        WL3,WL2,WL1,WL4=float(WL3[0:5]),float(WL2[0:5]),float(WL1[0:5]),float(WL4[0:5])

        return WL1,WL2,WL3,WL4

if __name__== '__main__':
    WeightPull.Main()
