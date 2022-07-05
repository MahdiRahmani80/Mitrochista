from bs4 import BeautifulSoup
import requests
import re
import sqlite3
import threading
from datetime import datetime
from .func import *
import csv
# import psycopg2



def getData(connection,all_tag,course_list,url,FIRST,LAST,csv_writer,pub_st,PUBLISHER,DOMAIN,instaBot):


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


            title = str(title).replace('<span class="course-page-title">',"").replace("</span>","")
            master = str(master).strip()



        # SAVE COURSE IN DB ********
        save_course_in_db(connection,all_tag,course_list,d,master,title,cast,time,buy_count,linkes[link],time_str,csv_writer,pub_st,PUBLISHER,DOMAIN,instaBot)


            # print (str(i) +" ** " +str(link))
            # input()




def init(PUBLISHER,DOMAIN,instaBot):

    connection = sqlite3.connect('db.sqlite3',check_same_thread=False)

    # For find last page index
    explore_page = requests.get("https://faradars.org/explore")
    soup = BeautifulSoup(explore_page.text,'html.parser')
    pages = soup.find_all("a",attrs={"class":"page-link"})

    pub_st = getPublisherStatus(DOMAIN,PUBLISHER)

    all_tag = getAllTags()

    # MAKE CSV LOG FILE
    csv_name = str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day)
    with open( "log/Faradars/" + csv_name + '.csv', 'w+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)



        for i in range(1,int(pages[1:-1][-1].text)):

            # getData(getAllTags(),getAllExistCourses(),mainURL,i,i+1)
            t1 = threading.Thread(target=getData,args=(connection,all_tag,getAllExistCourses(connection),mainURL,i,i+1,writer,pub_st,PUBLISHER,DOMAIN,instaBot))
            t1.start()
            t1.join()






# RUN PROGRAM
# init()
