from unittest import result
from bs4 import BeautifulSoup
import requests
import re
import sqlite3
import threading
from time import sleep
from datetime import datetime
import uuid
from .BOW import IR
import csv
import psycopg2

# Request 4.8 req pre sec
# TODO WRITE LOGFILE IN "log/faradars.org/"


# OUR DOMAIN
DOMAIN = "http://127.0.0.1:8001/"

lock = threading.Lock()
mainURL = "https://faradars.org/explore?webinar=all&page=" # end in 208

def getAllExistCourses():

    connection = psycopg2.connect(
        host="localhost",
        database="mitro_postgress_db",
        user="mahdi",
        password="M@hdi1380")
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM main_course ")

    return list(cursor.fetchall())

def getCourseFromID(id):
    for i in getAllExistCourses():
        if str(i[0]) == str(id):
            return i

def publishCourse(course_id):

    connection = psycopg2.connect(
        host="localhost",
        database="mitro_postgress_db",
        user="mahdi",
        password="M@hdi1380")
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM main_publisher WHERE id='982c797fe0454ce0ae5b61d383f9eef4' ;" )
    result = cursor.fetchall()

    print(str(result[0][7]))

    is_visible = False
    if result[0][7]:
        is_visible =True


    d={
        "is_visible": is_visible,
        "publisher": "982c797f-e045-4ce0-ae5b-61d383f9eef4",
        "course":str(course_id)
    }
    auth = ('mahdi', 'M@hdi1380')
    requests.post( DOMAIN + "api/create/course/publish/",json=d,auth=auth)




def allCourseURL():
    url_list = []
    for i in getAllExistCourses():
        url_list.append(i[4])

    return url_list


def getCourseIdFromURL(url):

    for i in getAllExistCourses():
        if url == i[4]:
            return i[0]

def getAllExistCourses():

    connection = psycopg2.connect(
        host="localhost",
        database="mitro_postgress_db",
        user="mahdi",
        password="M@hdi1380")
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM main_course ")

    return list(cursor.fetchall())


def getAllTags():
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    return list(cursor.execute(" SELECT * FROM main_tag "))


def getTeachers():
    names = []
    connection = psycopg2.connect(
        host="localhost",
        database="mitro_postgress_db",
        user="mahdi",
        password="M@hdi1380")
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM main_teacher ")

    for i in list(cursor.fetchall()):
        names.append(i[1])
    return names

def getTeachersList():
    connection = psycopg2.connect(
        host="localhost",
        database="mitro_postgress_db",
        user="mahdi",
        password="M@hdi1380")
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM main_teacher ")

    return list(cursor.fetchall())

def getIdFromTeacher(t_list,t):
    for i in range(0,len(t_list)):
        if str(t_list[i][1])==t:
            return t_list[i][0]

def getScore():
    return 0







def save_course_in_db(all_tag,course_list,d,master,title,cast,time,buy_count,link,time_str,csv_writer):

    title = str(title).replace('<span class="course-page-title">',"").replace("</span>","")

    # UPDATE DATA
    if link in allCourseURL():

        d ={
            'title':title,
            'discription':str(d).replace("\""," "),
            'price':cast,
            'url':link,
            'students':buy_count,
            'time':str(time),
            'lang':"FA",
            'score': int(getScore()),
            'time_str':time_str
        }


        course_id = str(getCourseIdFromURL(link))
        last_course_data = getCourseFromID(course_id)
        # UPDATE , course id, price , students ,discription,time,score, time
        csv_writer.writerow(list(["UPDATE",course_id,last_course_data[3],last_course_data[5],last_course_data[8],str(datetime.now())]))

        auth = ('mahdi', 'M@hdi1380')
        requests.put( DOMAIN +"api/update/course/"+course_id,json=d,auth=auth)

    # SAVE LOG in CSV
    else:


        # CREATE COURSE

        d ={
            'title':title,
            'discription':str(d).replace("\""," "),
            'price':cast,
            'url':link,
            'students':buy_count,
            'time':str(time),
            'lang':"FA",
            'score': int(getScore()),
            'time_str':time_str
        }
        auth = ('mahdi', 'M@hdi1380')

        res = requests.post( DOMAIN + 'api/create/course/',json=d,auth=auth)
        course_id = getCourseIdFromURL(link)
        # PUBLISH COURSE
        publishCourse(course_id)
        IR(course_id,d,title,all_tag)

        teachers = getTeachers()

        # LOG in CSV
        # UPDATE , course id, price , students ,discription,time,score, time
        csv_writer.writerow(list(["CREATE",course_id,cast,buy_count,str(d).replace("\""," "),str(time).replace('<div class="col-6 mt-2">','').replace('</div>',''),int(getScore()),str(datetime.now())]))


        if str(master) in teachers :
            # course add teacher
            cat = {"teacher": str(getIdFromTeacher(getTeachersList(),str(master))) ,"Course": str(dict(res.json())["id"]) }
            requests.post( DOMAIN+'api/create/course/teacher/',json=cat,auth=auth)

            # Update score
        else:

            # Create Teacher
            at = {"name": str(master) ,"score": int(dict(res.json())["score"]) }
            # print(str(at))
            res_teacher = requests.post( DOMAIN + 'api/create/teacher/',json=at,auth=auth)

            # course add teacher
            cat = {"teacher": str(dict(res_teacher.json())["id"]),"Course": str(dict(res.json())["id"]) }
            # print(str(cat))
            requests.post( DOMAIN + 'api/create/course/teacher/',json=cat,auth=auth)








def getData(all_tag,course_list,url,FIRST,LAST,csv_writer):


    for i in range(FIRST,LAST): # end number 208
        linkes = []

        response = requests.get(url+str(i))

        if response.status_code == 404:
            continue

        soup = BeautifulSoup(response.text,"html.parser")
        prices = soup.find_all("div", attrs={"class": "card-footer d-flex justify-content-between w-auto show-footer-card"})
        courseLinks = soup.find_all("a",attrs={"rel": "noopener noreferrer"})

        # GO ON EVERY COURSES
        for cur in range (0, len(courseLinks)-6):
            linkes.append( str(courseLinks[cur].get("href") ))
        #     print(str(courseLinks[cur].get("href")))

        # input()


        for link in range( 0, len(linkes)):
            courseINFO = requests.get(linkes[link] )
            courseSOUP = BeautifulSoup(courseINFO.text,"html.parser")


            discription = courseSOUP.find("div",attrs={"class": "my-3 about moreActive persianFont"})
            d  = str(discription.text)
            # print (d)

            master = str(courseSOUP.find("div",attrs={"class": "pr-3 mt-2 text-justify"})).split("h6>")
            master = master[1][:-2]

            title=""
            title = str(courseSOUP.find("span",attrs={"class": "course-page-title"})) # .text

            # tag = courseSOUP.find_all("span",attrs={"style": "font-size: 12px;"})
            # print (str(tag))


            cast = str(prices[link].text).replace("\n","").replace(" ","")
            if cast == "رایگان!":
                cast = 0
            else:
                cast = int(cast.replace("تومان","").replace(",",""))
            # print(cast)

            # count_comment = courseSOUP.find("div",attrs={"class": "my-3 about moreActive persianFont"})

            time = courseSOUP.find_all("div",attrs={"class": "col-6 mt-2"})
            if cast == "رایگان!":
                time = str(time[1])
                time_str = time.replace('<div class="col-6 mt-2">','').replace('</div>','')
                # print(time)
                time = re.findall(r"\d+",time)

                if len(time) == 4:
                    time =  int(time[2])*60 + int(time[3])

                elif len(time) ==2:
                    time = courseSOUP.find_all("span",attrs={"class": "text-nowrap"})
                    time_str = str(time)
                    time = re.findall(r"\d+",str(time))
                    # print(time)
                    if len(time) == 2:
                        time =  int(time[0])*60 + int(time[1])
                    else:
                        if "ساعت" in time_str:
                            time =  int(time[0])*60
                        else:
                            time =  int(time[0])
                else:
                    time =  int(time[2])*60


            else :
                time =str(time[2])
                time_str = time
                time = re.findall(r"\d+",time)
                # print(time)

                if len(time) == 4 :
                    time =  int(time[2])*60 + int(time[3])

                elif len(time) ==2:
                    time = courseSOUP.find_all("span",attrs={"class": "text-nowrap"})
                    time_str = str(time[0])

                    time = re.findall(r"\d+",str(time))
                    # print(time)
                    if len(time) == 2:
                        time =  int(time[0])*60 + int(time[1])
                    else:
                        if "ساعت" in time_str:
                            time =  int(time[0])*60
                        else:
                            time =  int(time[0])

                else:
                    time =  int(time[2])*60
            # print(time)

            buy_count = courseSOUP.find_all("div",attrs={"id": "soldCount"})
            buy_count = int(str(buy_count[0].text).replace(" ","").replace("\n","").replace(",", "").replace("نفر", ""))


            # SAVE COURSE IN DB ********
            save_course_in_db(all_tag,course_list,d,master,title,cast,time,buy_count,linkes[link],time_str,csv_writer)


            # print (str(i) +" ** " +str(link))
            # input()




def init():

    # For find last page index
    explore_page = requests.get("https://faradars.org/explore")
    soup = BeautifulSoup(explore_page.text,'html.parser')
    pages = soup.find_all("a",attrs={"class":"page-link"})

    # MAKE CSV LOG FILE
    csv_name = str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day)
    with open( "log/Faradars/" + csv_name + '.csv', 'w+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)



        for i in range(1,int(pages[1:-1][-1].text)):

            # getData(getAllTags(),getAllExistCourses(),mainURL,i,i+1)
            t1 = threading.Thread(target=getData,args=(getAllTags(),getAllExistCourses(),mainURL,i,i+1,writer))
            t1.start()
            t1.join()

        # input()





    #  TODO UPDATE ALL FARADARS SCORE COURSES
    #  TODO UPDATE ALL FARADARS SCORE TEACHER





# RUN PROGRAM
# init()
