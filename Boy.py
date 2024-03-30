#!/usr/bin/python3
#-*-coding:utf-8-*-
#Recoded by Younis john (YounisXyz)
#Designed by Younis john (YounisXyz





###-----------------[LOGIN URL]---------------------####

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')


###-----------------[INSTALLING MODULES]---------------------####
try:
	import os,requests,json,datetime,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	from rich import print as prints
	from rich.console import Console as sol
	from rich import print as cetak
	from datetime import datetime
	from rich.panel import Panel as nel
	from rich.panel import Panel
	from rich.console import Console
	from rich.columns import Columns
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
###-----------------[INSTALL MISSING PIP REQUESTS]---------------------####
except ModuleNotFoundError: 
	os.system("clear");print('\n\t\033[0;37m [ installation module requests ] \n\033[1;32m')
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
	os.system('pip install requests')
	

###-----------------[CONNECT TO SERVER-{ua,string,proxy}]---------------------####
try:
	prox= requests.get('https://raw.githubusercontent.com/YounisXyz/XyzServer/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
