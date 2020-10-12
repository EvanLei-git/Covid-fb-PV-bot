import os
import sys
import bs4 as bs
import sys
from urllib.request import Request, urlopen
from fbchat import Client
from fbchat.models import *
import credentials
import send_to

#---Read html code---#
deaths=[]
countries=[]
cases=[]
req = Request('https://www.worldometers.info/coronavirus', headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
html = urlopen(req).read()
soup=bs.BeautifulSoup(html,"lxml")
table=soup.find("table",id="main_table_countries_today")
body=table.find("tbody")
rows=body.find_all("tr")

#---Save in Lists---#
for row in rows:
    countries.append (str(row.find_all("td")[0].text.strip()))
    cases.append (str(row.find_all("td")[1].text.strip()))
    deaths.append (str(row.find_all("td")[3].text.strip()))
#-----------------------------------------------------------------------BULGARIA----------------------------------------------------------------------#
#---Find Bulgaria's position and save new cases number and deaths---#
for k in range(len(countries)):
   if countries[k] == 'Bulgaria':
      pos_bulg=k
new_bulg_cases=cases[pos_bulg]
new_bulg_deaths=deaths[pos_bulg]
new_bulg_cases=int(float(new_bulg_cases.replace(',','')))
new_bulg_deaths=int(float(new_bulg_deaths.replace(',','')))

#---------------------------------------------BULGARIA'S DEATHS-----------------------------------#
#---Save corona deaths at bulgaria_deaths.txt---#
if os.stat("bulgaria_deaths.txt").st_size == 0:
    f1=open("bulgaria_deaths.txt",'w+')
    f1.write(str(new_bulg_deaths))
    f1.close()
f1=open("bulgaria_deaths.txt",'r+')
f1.seek(0)
existed_bulg_deaths=str(f1.read())
f1.close()

#---Find the difference for Bulgaria's Deaths---#
difference_bulg_deaths=int(new_bulg_deaths)-int(existed_bulg_deaths)

#---Save new bulgaria's deaths---#
if existed_bulg_deaths!= str(new_bulg_deaths):
    f1=open("bulgaria_deaths.txt",'w+')
    f1.seek(0)
    f1.write(str(new_bulg_deaths))
    f1.close()

#---------------------------------------------BULGARIA'S CASES-----------------------------------#
#---Find if bulgaria.txt has cases(and save if not)---#
if os.stat("bulgaria.txt").st_size == 0:
    f1=open("bulgaria.txt",'w+')
    f1.write(str(new_bulg_cases))
    f1.close()
f1=open("bulgaria.txt",'r+')
f1.seek(0)
existed_bulg_cases=str(f1.read())
f1.close()

#---Find the difference for Bulgaria---#
difference_bulg_cases=int(new_bulg_cases)-int(existed_bulg_cases)

#---Save new bulgaria cases---#
if existed_bulg_cases != str(new_bulg_cases):
    f1=open("bulgaria.txt",'w+')
    f1.seek(0)
    f1.write(str(new_bulg_cases))
    f1.close()
#---------------------------------------------SEND BULGARIA-----------------------------------#
if existed_bulg_cases!= str(new_bulg_cases) or existed_bulg_deaths!= str(new_bulg_deaths):

    client = Client( credentials.username, credentials.password, user_agent=None)
    if difference_bulg_cases!=0 and difference_bulg_deaths!=0:
        text_to_send="Βουλγαρία("+ str(pos_bulg+2)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_bulg_cases)+"(+"+str(difference_bulg_cases)+")"+" και Θάνατοι κορωνοϊού "+str(new_bulg_deaths)+"(+"+str(difference_bulg_deaths)+")."
    elif difference_bulg_cases!=0:
        text_to_send="Βουλγαρία(" +str(pos_bulg+2)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_bulg_cases)+"(+"+str(difference_bulg_cases)+")"+" και Θάνατοι κορωνοϊού "+str(new_bulg_deaths)+"."
    elif difference_bulg_deaths!=0:
        text_to_send="Βουλγαρία(" +str(pos_bulg+2)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_bulg_cases)+" και Θάνατοι κορωνοϊού "+str(new_bulg_deaths)+"(+"+str(difference_bulg_deaths)+")."
        
 #--------------------------------------------FOR BROTHER--------------------------------------------------#
    if difference_bulg_cases!=0:
        text_to_brother="Βουλγαρία(" +str(pos_bulg+2)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_bulg_cases)+"(+"+str(difference_bulg_cases)+")."
        client.send(Message(text=text_to_brother), thread_id=send_to.loukas, thread_type=ThreadType.USER)
    #-------------------------------------thread_id=  --->  (friend's fb_id)---------------------------------#
    client.send(Message(text=text_to_send), thread_id=send_to.mom, thread_type=ThreadType.USER)
    #--------------------------------------------------------------------------------------------------------#
    client.logout()
    
#-------------------------------------------------------------------------GREECE------------------------------------------------------------------#
#---Find Greece's position and save new cases number and deaths---#
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
    if difference_gr_cases!=0 and difference_gr_deaths!=0:
        text_to_send="Ελλάδα(" +str(pos_gr+2)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_gr_cases)+"(+"+str(difference_gr_cases)+")"+" και Θάνατοι κορωνοϊού "+str(new_gr_deaths)+"(+"+str(difference_gr_deaths)+")."
    elif difference_gr_cases!=0:
        text_to_send="Ελλάδα(" +str(pos_gr+2)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_gr_cases)+"(+"+str(difference_gr_cases)+")"+" και Θάνατοι κορωνοϊού "+str(new_gr_deaths)+"."
    elif difference_gr_deaths!=0:
        text_to_send="Ελλάδα(" +str(pos_gr+2)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_gr_cases)+" και Θάνατοι κορωνοϊού "+str(new_gr_deaths)+"(+"+str(difference_gr_deaths)+")."
   
  #--------------------------------------------FOR BROTHER--------------------------------------------------#
    if difference_gr_cases!=0:
        text_to_brother="Ελλάδα(" +str(pos_gr+2)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_gr_cases)+"(+"+str(difference_gr_cases)+")."
        client.send(Message(text=text_to_brother), thread_id=send_to.loukas, thread_type=ThreadType.USER)
    #-------------------------------------thread_id=  --->  (friend's fb_id)---------------------------------#
    client.send(Message(text=text_to_send), thread_id= send_to.mom, thread_type=ThreadType.USER)
    client.send(Message(text=text_to_send), thread_id= send_to.karakasis, thread_type=ThreadType.USER)
    client.send(Message(text=text_to_send), thread_id= send_to.sofiap, thread_type=ThreadType.USER)  
    client.send(Message(text=text_to_send), thread_id= send_to.omadiki, thread_type=ThreadType.GROUP)
    #--------------------------------------------------------------------------------------------------------#
    client.logout()


#-----------------------------------------------------------------------SPAIN----------------------------------------------------------------------#
#---Find Spain's position and save new cases number and deaths---#
for k in range(len(countries)):
   if countries[k] == 'Spain':
      pos_sp=k
new_sp_cases=cases[pos_sp]
new_sp_deaths=deaths[pos_sp]
new_sp_cases=int(float(new_sp_cases.replace(',','')))
new_sp_deaths=int(float(new_sp_deaths.replace(',','')))
#---------------------------------------------SPAIN'S DEATHS-----------------------------------#
#---Save corona deaths at spain_deaths.txt---#
if os.stat("spain_deaths.txt").st_size == 0:
    f1=open("spain_deaths.txt",'w+')
    f1.write(str(new_sp_deaths))
    f1.close()
f1=open("spain_deaths.txt",'r+')
f1.seek(0)
existed_sp_deaths=str(f1.read())
f1.close()

#---Find the difference for Spain's Deaths---#
difference_sp_deaths=int(new_sp_deaths)-int(existed_sp_deaths)

#---Save new Spain's deaths---#
if existed_sp_deaths!= str(new_sp_deaths):
    f1=open("spain_deaths.txt",'w+')
    f1.seek(0)
    f1.write(str(new_sp_deaths))
    f1.close()

#---------------------------------------------SPAIN'S CASES-----------------------------------#
#---Find if spain.txt has cases(and save if not)---#
if os.stat("spain.txt").st_size == 0:
    f1=open("spain.txt",'w+')
    f1.write(str(new_sp_cases))
    f1.close()
f1=open("spain.txt",'r+')
f1.seek(0)
existed_sp_cases=str(f1.read())
f1.close()

#---Find the difference for Spain---#
difference_sp_cases=int(new_sp_cases)-int(existed_sp_cases)

#---Save new spain cases---#
if existed_sp_cases != str(new_sp_cases):
    f1=open("spain.txt",'w+')
    f1.seek(0)
    f1.write(str(new_sp_cases))
    f1.close()
#---------------------------------------------SEND SPAIN-----------------------------------#
if existed_sp_cases!= str(new_sp_cases) or existed_sp_deaths!= str(new_sp_deaths):

    client = Client( credentials.username, credentials.password, user_agent=None)
    if difference_sp_cases!=0 and difference_sp_deaths!=0:
        text_to_send="Ισπανία(" +str(pos_sp+1)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_sp_cases)+"(+"+str(difference_sp_cases)+")"+" και Θάνατοι "+str(new_sp_deaths)+"(+"+str(difference_sp_deaths)+")."
    elif difference_sp_cases!=0:
        text_to_send="Ισπανία(" +str(pos_sp+1)+"η θέση): Κρούσματα κορωνοϊού "+str(new_sp_cases)+"(+"+str(difference_sp_cases)+")"+" και Θάνατοι "+str(new_sp_deaths)+"."
    elif difference_sp_deaths!=0:
        text_to_send="Ισπανία(" +str(pos_sp+1)+ "η θέση): Κρούσματα κορωνοϊού "+str(new_sp_cases)+" και Θάνατοι "+str(new_sp_deaths)+"(+"+str(difference_sp_deaths)+")."

    #-------------------------------------thread_id=  --->  (friend's fb_id)---------------------------------#
    client.send(Message(text=text_to_send), thread_id=send_to.mom, thread_type=ThreadType.USER)
    #--------------------------------------------------------------------------------------------------------#
    client.logout()
sys.exit()




