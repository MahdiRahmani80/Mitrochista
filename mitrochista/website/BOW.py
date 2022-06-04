
import requests
import threading
from time import sleep

# SAVE IN DB
def saveData(doc,tag,BOW):

	auth = ('mahdi', 'M@hdi1380')
	d = {"course":str(doc),"publisher":"982c797f-e045-4ce0-ae5b-61d383f9eef4","tag":str(tag),"rank":BOW}
	# print(d)

	requests.post("http://127.0.0.1:8001/api/create/coursetag/",json=d,auth=auth)



# def getAllDisc(course_list):
#     cu_list = []
#     for i in course_list:
#         cu_list.append(i[2])

#     return cu_list


def getTagIdFromName(tag_list,tag):
    for i in tag_list:
        if i[1]==tag:
            return i[0]


def IR(id,dicsription,title,tags):

	# for d in range(0,len( getAllDisc(docs)) ):
		# TODO d.text
		# splited_d_list = getAllDisc(docs[d]).get_text().split(' ')

	for t in tags:
		BOW = 0

		for word in title.split(' '):
			if t[1] == word:
				BOW += 50


		for word in str(dicsription).split(' '):
			if t[1] == word:
				BOW += 1


		# SAVE DATA IN NEW THERED
		if BOW !=0:
			saveData(id,getTagIdFromName(tags,t[1]),BOW)
			# t1 = threading.Thread(target=saveData,args=(id,getTagIdFromName(tags,t[1]),BOW))
			# t1.start()
			# sleep(0.5)

		# print( str(t) + " -> " + str(BOW))



