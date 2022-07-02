

def addComment(models,text,userPhone,course_id):

    print(userPhone)
    user_obj = models.User.objects.filter(phone=userPhone)[0]
    cou = models.Course.objects.get(id=course_id)

    CC = models.CourseComment.objects.create(course=cou,comment=text)
    CC.save()
    models.UserAddComment.objects.create(user=user_obj,comment=CC).save()

    addScoreUser(user_obj)



def addScoreUser(user):
    user.score = user.score + 10
    user.save()
