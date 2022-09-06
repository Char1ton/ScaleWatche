from lxml import html
import time
import pandas as pd
from tkinter import *
from csv import writer

#Helper Functions
class WeightPull:
    def Main():
        
        #2-bit Memory
        WL=[0,0]
        mL=[0,0]

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
        ML3,ML2,ML1,ML4=float(miliL3[7][1].text_content()),float(miliL2[7][1].text_content()),float(miliL1[7][1].text_content()),float(miliL4[7][1].text_content())


        with open('Scale Analysis.csv','a',newline='') as f:
            writerobj=writer(f)
            writerobj.writerow([WL1,WL2,WL3,WL4])
            f.close()
        
        time.sleep(1)

if __name__== '__main__':
    WeightPull.Main()
