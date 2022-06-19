

def search(text_search,courseTag,tag):

    split_search = str(text_search).split(" ")
    words = remove_useless_words(split_search)

    RESULT_LIST = []


    for i in words:


        t = tag.objects.filter(name = i )
        # print(len(list(t)))
        if len(list(t)) !=0 :
            RESULT_LIST.append(list(courseTag.objects.filter(tag_id = tag.objects.get(name = i ) ) ))
            print(RESULT_LIST)

    RESULT_LIST = RESULT_LIST.sort(key=len)
    # print(RESULT_LIST)

    j=0
    AND_SEARCH_RESULTS = []
    OR_SEARCH_RESULTS = []

    # while j < len(RESULT_LIST):
    #     for k in RESULT_LIST[0]:
    #         is_and = 0
    #         for l in RESULT_LIST[1:]:
    #             if k in l:
    #                 is_and+=1

    #         if is_and == len(RESULT_LIST)-1:
    #             AND_SEARCH_RESULTS.append(k)
    #         else:
    #             OR_SEARCH_RESULTS.append(k)

    # print(AND_SEARCH_RESULTS)




def remove_useless_words(list_words):
    return list_words
