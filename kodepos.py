#!/usr/bin/env python
"""
Indonesian post codes scraper
Data source from www.nomor.net

Author: Agus Ibrahim - http://fb.me/mynameisagoes

Credits:
www.nomor.net
https://github.com/rufuspollock/csv2sqlite
http://www.crummy.com/software/BeautifulSoup
http://python-requests.org
"""

import requests
import os
import csv
import sys
import csv2sqlite
from bs4 import BeautifulSoup
from datetime import datetime
startTime = datetime.now()
arg = sys.argv
mydir = os.path.dirname(__file__)
ke, x = 1, 0
perpage = len(arg) > 1 and (arg[1].isdigit() and int(arg[1]) or 1000) or 1000
fname = len(arg) > 2 and arg[2] or "data.csv"

headers = {'User-Agent': 'Mozilla/5.0 AgusIbrahim/45265'}
f = open(os.path.join(mydir, fname),  "w")
tab = "no,kodepos,kel,kodewilayah,kec,dt2,kota,prov"
out = csv.writer(f)
out.writerow(tab.split(","))


def parse(ss):
    global x
    soup = BeautifulSoup(ss, 'html.parser')
    for data in soup.findAll("tr", bgcolor="#ccffff"):
        row = [s.text for s in data.findAll("td")]
        out.writerow(row)
        x += 1


while True:
    # if ke>1: w="https://www.nomor.net/_kodepos.php?_i=desa-kodepos&daerah=&jobs=&perhal=%s&urut=8&asc=0001000&sby=000000&no1=%s&no2=%s&kk=%s"%(perpage, (perpage*(ke-2))+1, ((perpage*(ke-1))+1)-1, ke)
    # else: w="https://www.nomor.net/_kodepos.php?_i=desa-kodepos&daerah=&jobs=&perhal=%s&sby=000000&asc=0001000&urut=8"%perpage
    w = "https://www.nomor.net/_kodepos.php?_i=desa-kodepos&sby=000000&daerah=Desa-Bakongan-Kab.-Aceh%20Selatan&jobs=Keude%20Bakongan"
    c = requests.get(w, headers=headers).content
    if c.find("#ccffff") < 1:
        break
    parse(c)
    ke += 1
f.close()

endTime = datetime.now() - startTime

print("Convert into sqlite...")
csv2sqlite.convert(os.path.join(mydir, fname), os.path.join(
    mydir, os.path.splitext(fname)[0]+".db"), "kodepos")
print("All Done, %s data downloaded. time %s" % (x, endTime))
