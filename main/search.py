from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
import re
import threading
from django.db.models import Q


def search(text_search,courseTag,tag,isFree,mostScore,mostView,Near):

    ORDER_KEY_WORD = None
    if Near=="true":
        ORDER_KEY_WORD=0
    elif isFree=="true":
        ORDER_KEY_WORD =1
    elif mostView=="true":
        ORDER_KEY_WORD =2
    elif mostScore=="true":
        ORDER_KEY_WORD =3



    split_search = str(text_search).split(" ")
    words = remove_useless_words(split_search,tag)
    # print(words)


    RESULT_LIST = []
    BEST_ANS =[]
    OTHER_ANS =[]

    for i in words:

        l = getResultWord(i,courseTag,ORDER_KEY_WORD)
        # print(l)
        if l:
            RESULT_LIST += l
            l.clear()



    if ORDER_KEY_WORD !=3:
        RESULT_LIST = sorted(RESULT_LIST, key = lambda x: x[1],reverse=True)


    if ((len(RESULT_LIST) > 1) and (ORDER_KEY_WORD !=3)) or ORDER_KEY_WORD==0 :

        for len_res in range(len(RESULT_LIST)-1):
            if RESULT_LIST[len_res] == RESULT_LIST[len_res+1]:
                if not (RESULT_LIST[len_res] in BEST_ANS):
                    BEST_ANS.append(RESULT_LIST[len_res])


            else:
                if not (RESULT_LIST[len_res] in OTHER_ANS):
                    OTHER_ANS.append(RESULT_LIST[len_res])

        RESULT_LIST.clear()

        return BEST_ANS + OTHER_ANS

    else :
        return RESULT_LIST






def remove_useless_words(list_words,tag):

    ans_list = []

    for i in list_words:
        if not ans_list in list_words :

            if not ( i == "" or i=="and" or i=="or" or i=="with" or i=="from" or i=="in"  or i=="the" or i=="و" or i=="در" or i=="با" or i=="از" or i=="course" or i=="دوره" or i=="اموزش" or i=="آموزش"):

                ans_list.append(stemmer.stem(str(i)).lower())

    return ans_list


def getResultWord(i,courseTag,ordering):

    l = []
    tagList=[]


    if not ordering:
        for j in courseTag.objects.filter( tag__name__icontains= stemmer.stem(str(i))  ):

                count=-1
                for r in j.tag.filter(name=str(i)):
                    count+=1
                    if r.name == str(i):
                        tagList=[]
                        tagList.append(j)
                        tagList.append(list(j.rank)[count])
                        break
                        # RESULT_LIST.append(l)

                if len(tagList) !=0:
                    l.append(tagList)

        return l


    elif ordering==1:
        # =============== FREE =============

        for j in courseTag.objects.filter(
                Q( tag__name__icontains= stemmer.stem(str(i))) &
                Q( course__price=0 )  ):

                count=-1
                for r in j.tag.filter(name=str(i)):
                    count+=1
                    if r.name == str(i):
                        tagList=[]
                        tagList.append(j)
                        tagList.append(list(j.rank)[count])
                        break
                        # RESULT_LIST.append(l)

                if len(tagList) !=0:
                    l.append(tagList)

        return l

    # ================== MOST VIEW ===========
    elif ordering==2:
        pass

    # ================= MOST SCORE ===========
    elif ordering==3:

        for j in courseTag.objects.filter(tag__name__icontains= stemmer.stem(str(i))).order_by("-course__score"):
                count=-1
                for r in j.tag.filter(name=str(i)):
                    count+=1
                    if r.name == str(i):
                        tagList=[]
                        tagList.append(j)
                        tagList.append(list(j.rank)[count])
                        break
                        # RESULT_LIST.append(l)

                if len(tagList) !=0:
                    l.append(tagList)

        return l

