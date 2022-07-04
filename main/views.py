from django.shortcuts import render
from . import models
from .search import search
from .auth import forgetPass,authorize,publisherSignin,publisherForgetPass
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from .makeMonney import clickBtn,goToIDPAY,addAmountInCredit
from .community import addComment
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# INDEX
def index(request):

    search_text = request.POST.get('search')
    result = None
    if search_text:

        return HttpResponseRedirect("/explore/?search="+search_text)
        # result=search (search_text,models.CourseTAG,models.TAG)


    doc={
        "result":result,
    }

    return render(request,'index.html',doc)


# RESULT & EXPLORE PAGE
def result(request):

    search_text = request.GET.get('search')
    near = request.GET.get('near')
    isFree = request.GET.get('free')
    mostView = request.GET.get('most-view')
    mostScore = request.GET.get('mostscore')
    page_number = request.GET.get('page')
    res_obj = all_res_obj = None
    res = None
    all_result=None

    # print(search_text)
    if search_text:

        res = search (search_text,models.CourseTAG,models.TAG,isFree,mostScore,mostView,near)

        if len(list(res)) == 0:
            all_result=models.CourseTAG.objects.filter(publisher__is_visible=True)

    else:
        if isFree:
            all_result = models.CourseTAG.objects.filter( Q(course__price=0) & Q(publisher__is_visible=True) )
        elif mostScore :
            all_result = models.CourseTAG.objects.filter(publisher__is_visible=True).order_by("-course__score")
        else:
            all_result=models.CourseTAG.objects.filter(publisher__is_visible=True)

    if res:
        res = Paginator(res,25)
        res_obj = res.get_page(page_number)
    if all_result:
        all_result = Paginator(all_result,25)
        all_res_obj = all_result.get_page(page_number)


    ORDER_KEY_WORD = None
    if near=="true":
        ORDER_KEY_WORD=0
    elif isFree=="true":
        ORDER_KEY_WORD =1
    elif mostView=="true":
        ORDER_KEY_WORD =2
    elif mostScore=="true":
        ORDER_KEY_WORD =3

    doc={
        "result":res_obj, "all_result":all_res_obj,"search":search_text,
        "order":ORDER_KEY_WORD,
    }

    return render(request,'result.html',doc)




# TAG
def tag (request,tag=None):

    TAG = models.TAG.objects.filter(name=tag.replace("%20", " "))[0]
    all_result=models.CourseTAG.objects.filter(Q(tag=TAG) & Q(publisher__is_visible=True))

    d = {
        'all_result':all_result,
    }

    return render(request,'result.html',d)



# COURSE
def course (request,id=None,course=None):


    userName = request.POST.get('name')
    phone = request.POST.get('phone')
    verifyPhone = request.POST.get('verifyPhone')
    password = request.POST.get('pass')
    confirmPass = request.POST.get('confirmPass')
    forgetPhone = request.POST.get('forgetPhone')
    comment = request.POST.get('comment')
    userPhone = request.POST.get('userPhone')

    click = request.POST.get('click')
    ip = get_client_ip(request)



    if click:
        clickBtn(models,id,ip)

    if comment:
        addComment(models,comment,userPhone,str(id))

    if phone or verifyPhone:
        print(verifyPhone)
        return authorize(models,confirmPass,password,verifyPhone,userName,phone)

    elif forgetPhone:
        forgetPass(models.User,forgetPhone)


    COURSE = models.CourseTAG.objects.filter(Q(course=id) & Q(publisher__is_visible=True))[0]
    tag_list= COURSE.tag.order_by("-rank")

    comment = models.UserAddComment.objects.filter(comment__course__id=id)

    d= {
        'res':COURSE,'tag_list':tag_list,'comment':comment,
    }
    return render(request,'course_single.html',d)



# TEACHERS Course
def teachersCourse (request,teacher=None):

    page_number = request.GET.get('page')
    tea = models.CourseTAG.objects.filter(Q(master=teacher) & Q(publisher__is_visible=True))
    # print(teacher)

    res = Paginator(tea,25)
    obj_page = res.get_page(page_number)

    d= {
        'all_result':obj_page,
    }
    return render(request,'result.html',d)


# TEACHERS
def teacher (request):

    page_number = request.GET.get('page')
    isMostScore = request.GET.get('mostscore')
    teacher_search = request.GET.get('search')

    res = None

    if teacher_search:
        res=models.Teacher.objects.filter(name__icontains=teacher_search)
    else:
        res=models.Teacher.objects.all()

    if not isMostScore:
        teacher = res.all()
    else:
        teacher = res.order_by("-score")

    res = Paginator(teacher,25)
    obj_page = res.get_page(page_number)

    d= {
        'teacher':obj_page,
    }
    return render(request,'result.html',d)




# PUBLISHER Course
def coursePublisher (request,pub_id=None):

    page_number = request.GET.get('page')
    search_text = request.GET.get('search')
    all_result = models.CourseTAG.objects.filter(Q(publisher__publisher__id=pub_id) & Q(publisher__is_visible=True))

    res = Paginator(all_result,25)
    p = res.get_page(page_number)


    if search_text:
        return HttpResponseRedirect("/explore/?search="+search_text)

    d= {
        'all_result':p,
    }
    return render(request,'result.html',d)


# PUBLISHER
def publisher (request):

    page_number = request.GET.get('page')
    pub = models.Publisher.objects.all()

    res = Paginator(pub,25)
    p = res.get_page(page_number)



    d= {
        'pub':p,
    }
    return render(request,'result.html',d)


def requestPartnership(request):


    d={}
    return render(request,"requestPartnership.html",d)


#  WEBSITE PANNEL
@csrf_exempt
def websitePannel(request,id=None):

    page_number = request.GET.get('page')
    amount = request.POST.get('chargePrice')

    pub = models.Publisher.objects.filter(id=id)[0]
    credit = models.Credit.objects.filter(publisher=pub)[0]
    clickCourse = models.ClickCourse.objects.filter(publisher=pub).order_by("-date")
    res = Paginator(clickCourse,25)
    result = res.get_page(page_number)

    if amount:
        return HttpResponseRedirect( goToIDPAY(amount,pub,models.Payment))

    if request.POST:
        payment_publisher = models.Payment.objects.filter(idpay_id=request.POST.get("id"))

        if payment_publisher:
            payment_publisher.update(stp2DataReseveIDPAY=str(request.POST),amount=request.POST.get("amount"))

            if str(request.POST.get("status")) == "100" or str(request.POST.get("status")) == "101" or str(request.POST.get("status")) == "200":
                addAmountInCredit(request.POST.get("amount"),pub,models.Credit)
                return HttpResponseRedirect("#")



    d={
        "all_result":result,"credit":credit,"publisher":pub,
        "len_click":len(list(clickCourse))
     }
    return render(request,"website_pannel.html",d)


def publisher_signin(request):

    phone = request.POST.get('phone')
    password = request.POST.get('password')
    forgetPhone = request.POST.get('forgetPassword')

    if phone:
        return publisherSignin(models.Publisher,phone,password)

    if forgetPhone:
        publisherForgetPass(models.Publisher,forgetPhone)



    d={

    }
    return render(request,"publisher_signin.html",d)



def contact (request):

    name  = request.POST.get('name')
    email = request.POST.get('email')
    msg   = request.POST.get('msg')

    if email:
        models.contactUs.objects.create(name=name,email=email,text=msg)

    return render(request,"contact.html")


def about (request):


    return render(request,"about.html")


# Get Client IP
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

