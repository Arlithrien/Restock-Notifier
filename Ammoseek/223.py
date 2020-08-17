# Chris Fleming 
# Script that notifies you when cheap ammo is in stock
# currently set to find the cheapest 223 sold by BassPro/Cabela's, under 60 cents per round

import bs4
from bs4 import BeautifulSoup
import requests
import configparser
import re
from datetime import datetime
import time
from notify_run import Notify 
# notify = Notify()

config = configparser.ConfigParser()
config.read('config.ini')
headers = {'User-agent': 'Chrome/84.0.4147.125'}

# set notify  channel url below ie: notify = 'https://notify.run/XXXXXXXXXXX'
NOTIFY = ''

# desired cost per round
CPR = 0.60

# URL's of prefiltered ammoseek search queries. Example used is 223 filtered by keywords 'Cabela' and 'Bass Pro'
URLCB = 'https://ammoseek.com/ammo/223-Remington?co=new&pl=no&ikw=Cabela'
URLBP = 'https://ammoseek.com/ammo/223-Remington?co=new&ikw=Bass%20Pro&pl=no'

#sleep_mins = config['DEFAULT']['INTERVAL_MINS']

def scrape(NOTIFY, CPR, URLCB, URLBP):
  # scrape webpage of given URL(s)
  CB = requests.get(URLCB, headers=headers)
  BP = requests.get(URLBP, headers=headers)

  # scraping website(s), parsing lowest cpr
  soupC = BeautifulSoup(CB.text, 'html.parser')
  soupB = BeautifulSoup(BP.text, 'html.parser')
  mydivsC = soupC.findAll("div", {"class": "results-info-content"})
  mydivsB = soupB.findAll("div", {"class": "results-info-content"})
  lowpriceC = mydivsC[2]
  lowpriceB = mydivsB[2]
  cpr_cb = lowpriceC['data-lowprice']
  cpr_bp = lowpriceB['data-lowprice']

  # If not in stock, set cpr to infinity
  if cpr_cb == '':
    cpr_cb = float("inf")
  else:
    cpr_cb = float(cpr_cb)
  if cpr_bp == '':
    cpr_bp = float("inf")
  else:
    cpr_bp = float(cpr_bp)

  # If lowest cpr is lower than desired CPR, send push notification to device(s)
  if cpr_cb <= cpr_bp:
    if cpr_cb <= CPR:
      msg = "Cabela's: "+ str(cpr_cb)
      requests.post(NOTIFY, data=msg)
  elif cpr_bp <= CPR: 
    msg = "Bass Pro: "+ str(cpr_bp)
    requests.post(NOTIFY, data=msg)


scrape(NOTIFY, CPR, URLCB, URLBP)
