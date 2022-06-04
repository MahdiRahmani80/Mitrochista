import requests
import sqlite3
import json
import time
import threading
import psycopg2

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

tags = cursor.execute('SELECT * FROM main_tag')
connection.commit()


co = psycopg2.connect(
    host="localhost",
    database="mitro_postgress_db",
    user="mahdi",
    password="M@hdi1380")
cu = co.cursor()


cu.execute('SELECT * FROM main_tag')
l = cu.fetchall()

l = list(l)
d_list = []

for i in l:
	d_list.append(str(i[0]).replace("-",""))




# print (list(tags))
tags = list(tags)
tags.reverse()

def p (tag,d_list):

	d={"id":str(tag[0]),"name":str(tag[1]),"rank":int(tag[3])}
	auth = ('mahdi', 'M@hdi1380')

	if not ( str(tag[0]) in d_list):
		requests.post('http://127.0.0.1:8001/api/create/tag/',json=d,auth=auth)
		print ("DONE")	


#i=0
for tag in tags:

	t1 = threading.Thread(target=p,args=(tag,d_list))
	t1.start()
	#i+=1
	#if i%200 == 0:
		
		#time.sleep(0.1)	
	#	t1.join()
	#d={"id":str(tag[0]),"name":str(tag[1]),"rank":int(tag[3])}
	
	#auth = ('mahdi', 'M@hdi1380')
	#if not ( str(tag[0]) in d_list):
	#	print(tag)
	#	print(d_list[0])
	#	print(str(tag[0]))
	#	requests.post('http://127.0.0.1:8001/api/create/tag/',json=d,auth=auth)

