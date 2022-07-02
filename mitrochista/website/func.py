
import requests
import threading
import requests
import re
import sqlite3
import threading
from datetime import datetime
import csv
from PIL import Image, ImageDraw, ImageFont




###  INSTA BOT
def postInInsagram(cap,bot):
    album_path = ["insta/we.jpg","insta/logo.jpg"]

    bot.album_upload(
        album_path,
        caption = cap
    )
    # bot.upload_photo([Image,"insta/we.jpg"],caption=caption)


def getInstaaption(title,d,master):

    ans =""
    ans += "نام دوره : "+title
    ans +="\nنام مدرس" +master
    ans += "\n\nبهترین دوره ها رو در میتروچیستا پیدا کنید \nمیتونید از صفحه پیجمون وارد سایتمون بشید "
    ans += "\n\n "+ str(d)[:1800]
    ans +="\n\n\nmitrochista.ir"

    return ans


def makeImage(course_id,img_title):
    img = Image.new('RGB', (1080, 1080), color = "#092C4C")

    fnt = ImageFont.truetype('insta/nunito_sans_black.ttf', 40)
    d = ImageDraw.Draw(img)

    d.multiline_text((900,900) , str(img_title), font=fnt, fill="#FFFF")

    img.save('insta/img/'+ course_id +'.jpeg')

    return 'insta/img/'+ course_id +'.jpeg'





# SAVE IN DB
def saveData(doc,tag_list,BOW_LIST,pub,domain,master):

	auth = ('mahdi', 'M@hdi1380')
	d = {"course":str(doc),"publisher":pub,"tag":tag_list,"rank":BOW_LIST,"master":master}
	# print(d)

	requests.post( domain +"api/create/coursetag/",json=d,auth=auth)



# def getAllDisc(course_list):
#     cu_list = []
#     for i in course_list:
#         cu_list.append(i[2])

#     return cu_list


def getTagIdFromName(tag_list,tag):
    for i in tag_list:
        if i[1]==tag:
            return i[0]


def IR(id,dicsription,title,tags,pub,domain,master):

	# for d in range(0,len( getAllDisc(docs)) ):
		# TODO d.text
		# splited_d_list = getAllDisc(docs[d]).get_text().split(' ')

    ANSWER_LIST = []
    BOW_LIST = []

    for t in list(tags):
        BOW = 0
		# print (t)

        for word in title.split(' '):
            if str(t[1]).lower() in str(word).lower() :
                BOW += 50


        for word in str(dicsription).split(' '):
            if str(t[1]).lower() in str(word).lower():
                BOW += 1

        if (BOW !=0) and not (t[0] in ANSWER_LIST):

            ANSWER_LIST.append(t[0])
            BOW_LIST.append(BOW)



    saveData(id,ANSWER_LIST,BOW_LIST,pub,domain,master)










#  DATA MANGEMENT



lock = threading.Lock()
mainURL = "https://faradars.org/explore?webinar=all&page="


def getAllExistCourses(connection):

    cursor = connection.cursor()
    l= cursor.execute(" SELECT * FROM main_course ")

    return list(l)

def getCourseFromID(connection,id):
    for i in getAllExistCourses(connection):
        if str(i[0]) == str(id):
            # print(i)
            return i

def publishCourse(DOMAIN,course_id,publisher_id,is_publish):

    d={
        "is_visible": is_publish,
        "publisher":  str(publisher_id),
        "course":str(course_id)
    }
    auth = ('mahdi', 'M@hdi1380')
    res = requests.post( DOMAIN + "api/create/course/publish/",json=d,auth=auth)
    return str(res.json()["id"])


def updatePublishCourse(DOMAIN,course_id,publisher_id,is_publish):

    d={
        "is_visible": is_publish,
        "publisher":  str(publisher_id),
        "course":str(course_id)
    }
    auth = ('mahdi', 'M@hdi1380')
    requests.put( DOMAIN + "api/update/course/publish/"+str(course_id),json=d,auth=auth)


def getPublisherStatus(DOMAIN,id):

    auth = ('mahdi', 'M@hdi1380')
    res = requests.get( DOMAIN + "api/publisher/"+id,auth=auth)

    return dict(res.json())["isScrapAlgorithmWrite"]




def allCourseURL(connection):
    url_list = []
    for i in getAllExistCourses(connection):
        url_list.append(i[4])

    return url_list


def getCourseIdFromURL(connection,url):

    for i in getAllExistCourses(connection):

        if url in i[4]:

            u_id = str(i[0])
            return u_id[:8]+"-"+u_id[8:12]+"-"+u_id[12:16]+"-"+u_id[16:20]+"-"+u_id[20:]

def getAllExistCourses(connection):

    cur = connection.cursor()


    return list(cur.execute(" SELECT * FROM main_course "))


def getAllTags():
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    return list(cursor.execute(" SELECT * FROM main_tag "))


def existTeachers(connection,t_name):

    cursor = connection.cursor()

    for i in list(cursor.execute(" SELECT * FROM main_teacher ")):
        if str(i[1]) == t_name:
            return True
        else:
            return False

def getTeachersList(connection):
    cursor = connection.cursor()


    return list(cursor.execute(" SELECT * FROM main_teacher "))

def getIdFromTeacher(t_list,t):
    for i in range(0,len(t_list)):
        if str(t_list[i][1])==t:

            u_id = str(t_list[i][0])
            return  u_id[:8]+"-"+u_id[8:12]+"-"+u_id[12:16]+"-"+u_id[16:20]+"-"+u_id[20:]


def getScore(cast,buy_count,time,rank,teacher_score):

    if not cast:
        cast =0
    if not (buy_count):
        buy_count=0
    if not(time):
        time=0
    if not rank:
        rank=0
    if not(teacher_score):
        teacher_score =0

    return (cast//100 + (2*buy_count) + time + (3*rank) + teacher_score//100) // 100


def getCourseRank(connection,id):
    cursor = connection.cursor()


    ans = 0
    for i in list(cursor.execute(" SELECT * FROM main_coursetag WHERE course_id='" + str(id).replace("-", "") +"';" )):
        # print(i[3])
        for j in str(i[3]).split():
            if j.isdigit():
                ans += int(j)

    # print(ans)
    return ans

def getTeacherRank(DOMAIN,master):

    auth = ('mahdi', 'M@hdi1380')
    r = requests.get( DOMAIN +"api/update/teacher/"+str(master),auth=auth)
    # print(r)
    if r.status_code != 404:
        return int(r.json()["score"])
    else:
        return










# SAVE IN DATABASE ->
def save_course_in_db(connection,all_tag,course_list,d,master,title,cast,time,buy_count,link,time_str,csv_writer,pub_st,PUBLISHER,DOMAIN,instaBot):

    disc_post_insta = str(d).strip()
    res = None

    # UPDATE DATA
    if str(link) in list(allCourseURL(connection)) :
        course_id = str(getCourseIdFromURL(connection,link))
        # print(str(course_id))

        # print("UPDATE MOOD")

        d ={
            'title':title,
            'discription':str(d).replace("\""," "),
            'price':cast,
            'url':link,
            'students':buy_count,
            'time':str(time),
            'lang':"FA",
            'score': int(getScore((cast),(buy_count),(time),(getCourseRank(connection,str(course_id))),(getTeacherRank(DOMAIN,str(master))))),
            'time_str':time_str
        }

        last_course_data = getCourseFromID(connection,str(course_id))

        # Publish course
        auth = ('mahdi', 'M@hdi1380')
        updatePublishCourse(DOMAIN,str(course_id),PUBLISHER,pub_st)

        requests.put( DOMAIN +"api/update/course/"+str(course_id),json=d,auth=auth)


        # UPDATE , course id, price , students ,discription,time,score, time
        if last_course_data:
            csv_writer.writerow(list(["UPDATE",str(course_id),last_course_data[3],last_course_data[5],last_course_data[8],str(datetime.now())]))


    # CREATE COURSE
    else:


        # print("CREATE MOOD")

        d ={
            'title':title,
            'discription':str(d).replace("\""," "),
            'price':cast,
            'url':link,
            'students':buy_count,
            'time':str(time),
            'lang':"FA",
            'score': int(getScore((cast),(buy_count),(time),0,0)),
            'time_str':time_str
        }
        auth = ('mahdi', 'M@hdi1380')


        res_cc = requests.post( DOMAIN + 'api/create/course/',json=d,auth=auth)
        if res_cc.status_code == 201:
            course_id = res_cc.json()['id']
            # print(str(course_id))
        else:
            course_id = str(getCourseIdFromURL(connection,link))


        # PUBLISH COURSE
        publish = publishCourse(DOMAIN,str(course_id),PUBLISHER,pub_st)



        # LOG in CSV
        # CREATE , course id, price , students ,discription,time,score, time
        csv_writer.writerow(list(["CREATE",str(course_id),cast,buy_count,str(d).replace("\""," "),str(time).replace('<div class="col-6 mt-2">','').replace('</div>',''),int(getScore(cast,buy_count,int(time),0,0)),str(datetime.now())]))


        if existTeachers(connection,str(master)) :
            # course add teacher

            try:
                at = {"name": str(master) ,"score": int(getScore(cast,buy_count,int(time),0,0)) }
                # print(at)
                res_teacher = requests.post( DOMAIN + 'api/create/teacher/',json=at,auth=auth)
            finally:

                # print("EXEIST TEACHER")

                try:
                    cat = {"teacher": str(getIdFromTeacher(getTeachersList(connection),str(master))) ,"Course": str(course_id) }
                    requests.post( DOMAIN+'api/create/course/teacher/',json=cat,auth=auth)
                finally:
                    # print("add course teacher")

                    # Update score
                    try:
                        res = requests.get( DOMAIN +"api/update/teacher/"+str(master),auth=auth)
                    finally:
                        # print("get teacher info")

                        dic = dict(res.json())
                        newScore = int(getScore(cast,buy_count,int(time),0,0)) + abs(dic["score"] - (int(getScore(cast,buy_count,int(time),0,0))))
                        dictionary = {"name":str(master),"score": newScore }

                        try:
                            requests.put( DOMAIN +"api/update/teacher/"+str(master),json=dictionary,auth=auth)
                        finally:
                            print("update score")

        else:

            res_teacher = None

            # print("CREATE TEACHER")

            # Create Teacher
            try:
                at = {"name": str(master) ,"score": int(getScore(cast,buy_count,int(time),0,0)) }
                # print(at)
                res_teacher = requests.post( DOMAIN + 'api/create/teacher/',json=at,auth=auth)
            finally:
                # print( "crate teacher status code -> " + str(res_teacher.status_code))

                # course add teacher
                if res_teacher.status_code == 201:
                    cat = {"teacher":getIdFromTeacher(getTeachersList(connection),str(master)) ,"Course": str(course_id) }
                    # print(str(cat))
                    requests.post( DOMAIN + 'api/create/course/teacher/',json=cat,auth=auth)

                else:

                    cat = {"teacher":getIdFromTeacher(getTeachersList(connection),str(master)) ,"Course": str(course_id) }
                    requests.post( DOMAIN+'api/create/course/teacher/',json=cat,auth=auth)

                    res_get_teacher_status = requests.get( DOMAIN +"api/update/teacher/"+str(master),auth=auth)
                    di = dict(res_get_teacher_status.json())
                    newScore =di["score"] + (int(getScore(cast,buy_count,int(time),0,0)))
                    dictionary = {"name":str(master),"score": newScore }
                    # print(d)
                    # print(newScore)
                    r= requests.put( DOMAIN +"api/update/teacher/"+str(master),json=dictionary,auth=auth)
                    # print(r.json())




            # Algorithem

            IR(str(course_id),d,title,all_tag,publish,DOMAIN,str(master))
            # POST in insta
            # postInInsagram(getInstaaption(title,disc_post_insta,master),instaBot)

            print(" -> DONE <- ")





