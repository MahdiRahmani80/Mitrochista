from bs4 import BeautifulSoup
import requests
import re,os
from .func import *


mainURL = "https://toplearn.com/courses?filterby=all&orderby=createAndUpdatedate&pageId=" # end in 53


def getData(url,connection,csv_writer,pub_st,all_tag,PUBLISHER,DOMAIN,instaBot,course_list):
    MainSite = "https://toplearn.com/"

    for i in range(1,53): # end number 53
        p = []
        images = []
        titles = []
        linkes = []

        response = requests.get(url+str(i))

        if response.status_code == 404:
            continue

        soup = BeautifulSoup(response.text,"html.parser")

        prices = soup.find_all("span", attrs={"class": "price"})
        courseLinks = soup.find_all("div",attrs={"class": "img-layer"})
        headers = soup.find_all("h2")

        for t in headers:
            titles.append(str(t.text).strip())
            # print(str(t.text).strip())



        for price in prices:
            p.append(price.text.strip())
            # print (price.text)

        for cur in courseLinks:
            linkes.append( "https://toplearn.com" + re.split(r'"',str(cur))[3] )
            # print ( "https://toplearn.com" + re.split(r'"',str(cur))[3] )

        for link in range( 0, len(linkes)):
            courseINFO = requests.get(linkes[link] )
            courseSOUP = BeautifulSoup(courseINFO.text,"html.parser")
            courseTime = courseSOUP.find_all("li",attrs={"class": "notShowInRecording"})[1]
            MASTER = str(courseSOUP.find("a",attrs={"rel": "author"}).get("title"))
            discription = courseSOUP.find("article",attrs={"class": "course-content-layer box-shadow"})
            d  = str(discription.text).replace('نظرهای دوره',"").replace('پرسش و پاسخ  مطرح کنید به سوالات در قسمت نظرات پاسخ داده نخواهد شد و آن نظر حذف میشود.','').replace('لطفا سوالات خود را راجع به این آموزش در این بخش','')

            course_price = 0

            if not str(p[ link ])=='رایگانـ':
                course_price = int(p[ link ].replace(",","").replace("تومان","").strip())
            else:
                course_price = 0


            time_str = str(courseTime.text).replace("مدت زمان دوره :","").strip().split(":")
            time = int(time_str[0])*60 + int(time_str[1])
            time_str = str(time_str[0])+":"+str(time_str[1])+":"+str(time_str[2])

            save_course_in_db(connection,all_tag,course_list,d,MASTER,titles[link],course_price,time,-1,linkes[link],time_str,csv_writer,pub_st,PUBLISHER,DOMAIN,instaBot)



def init(PUBLISHER,DOMAIN,instaBot):

    connection = sqlite3.connect('db.sqlite3',check_same_thread=False)
    pub_st = getPublisherStatus(DOMAIN,PUBLISHER)
    all_tag = getAllTags()

    # MAKE CSV LOG FILE
    csv_name = str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day)


    with open( "log/Toplearn/" + csv_name + '.csv', 'w+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        getData(mainURL,connection,writer,pub_st,all_tag,PUBLISHER,DOMAIN,instaBot,getAllExistCourses(connection))
