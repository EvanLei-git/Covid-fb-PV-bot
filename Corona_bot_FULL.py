import os
import sys
import bs4 as bs
import sys
from urllib.request import Request, urlopen
from fbchat import Client
from fbchat.models import *
import credentials
import send_to


deaths=[]
countries=[]
cases=[]
#---Read html code---#
req = Request('https://www.worldometers.info/coronavirus')
html = urlopen(req).read()
soup=bs.BeautifulSoup(html,"lxml")
table=soup.find("table",id="main_table_countries_today")
body=table.find("tbody")
rows=body.find_all("tr")
#---Create Lists---#
deaths=[]
countries=[]
cases=[]
#---Save ALL stats in Lists---#
for row in rows:
    countries.append (str(row.find_all("td")[0].text.strip()))
    cases.append (str(row.find_all("td")[1].text.strip()))
    deaths.append (str(row.find_all("td")[3].text.strip()))

    
#-------------------------------------------------------------------------GREECE------------------------------------------------------------------#
#---Find Greece's covid case's position and save new cases number and deaths---#
for k in range(len(countries)):
   if countries[k] == 'Greece':
      pos_gr=k
new_gr_cases=cases[pos_gr]
new_gr_deaths=deaths[pos_gr]
new_gr_cases=int(float(new_gr_cases.replace(',','')))
new_gr_deaths=int(float(new_gr_deaths.replace(',','')))
#---------------------------------------------GREECE'S DEATHS-----------------------------------#
#---Save corona deaths at greece_deaths.txt---#
if os.stat("greece_deaths.txt").st_size == 0:
    f2=open("greece_deaths.txt",'w+')
    f2.write(str(new_gr_deaths))
    f2.close()
f2=open("greece_deaths.txt",'r+')
f2.seek(0)
existed_gr_deaths=str(f2.read())
f2.close()

#---Find the difference for Greece's Deaths---#
difference_gr_deaths=int(new_gr_deaths)-int(existed_gr_deaths)

#---Save new greece's deaths---#
if existed_gr_deaths!= str(new_gr_deaths):
    f2=open("greece_deaths.txt",'w+')
    f2.seek(0)
    f2.write(str(new_gr_deaths))
    f2.close()
#---------------------------------------------GREECE'S CASES-----------------------------------#
#---Find if greece.txt has cases(and save if not)---#
if os.stat("greece.txt").st_size == 0:
    f2=open("greece.txt",'w+')
    f2.write(str(new_gr_cases))
    f2.close()
f2=open("greece.txt",'r+')
f2.seek(0)
existed_gr_cases=str(f2.read())
f2.close()

#---Find the difference for Greece's cases---#
difference_gr_cases=int(new_gr_cases)-int(existed_gr_cases)

#---Save new Greece's cases---#
if existed_gr_cases!= str(new_gr_cases):
    f2=open("greece.txt",'w+')
    f2.seek(0)
    f2.write(str(new_gr_cases))
    f2.close()
#---------------------------------------------SEND GREECE-----------------------------------#
if existed_gr_cases!= str(new_gr_cases) or existed_gr_deaths!= str(new_gr_deaths):
    client = Client( credentials.username, credentials.password, user_agent=None)

    
    #------if both cases and deaths have changed-----#
    if difference_gr_cases!=0 and difference_gr_deaths!=0:
        text_to_send="Greece(" +str(pos_gr+2)+ "position ):covid cases "+str(new_gr_cases)+"(+"+str(difference_gr_cases)+")"+" and deaths "+str(new_gr_deaths)+"(+"+str(difference_gr_deaths)+")."
    #------elif only cases have changed-----#
    elif difference_gr_cases!=0:
        text_to_send="Greece(" +str(pos_gr+2)+ "position ):covid cases "+str(new_gr_cases)+"(+"+str(difference_gr_cases)+")"+" and deaths "+str(new_gr_deaths)+"."
    #------elif only deaths have changed-----#
    elif difference_gr_deaths!=0:
        text_to_send="Greece(" +str(pos_gr+2)+ "position ):covid cases "+str(new_gr_cases)+" and deaths "+str(new_gr_deaths)+"(+"+str(difference_gr_deaths)+")."
   
    #-------------------------------------thread_id=  --->  (friend's fb_id saved inside "send_to" file)---------------------------------#
    client.send(Message(text=text_to_send), thread_id= send_to.mom, thread_type=ThreadType.USER)
    client.send(Message(text=text_to_send), thread_id= send_to.dad, thread_type=ThreadType.USER)
    #--------------------------------------------------------------------------------------------------------#
    client.logout()


sys.exit()










