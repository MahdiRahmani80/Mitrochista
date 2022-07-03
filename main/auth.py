import random
import  requests
from django.http import JsonResponse
from hashlib import sha256




def authorize(models,confirmPass,password,verifyPhone,userName,phone):

    if (confirmPass == password) and (password !="") and (confirmPass != "")  and (confirmPass != None) and (password != None) :
        sign_up = signUp(models.User,userName,phone,password,confirmPass)
        if sign_up:
            data = { 'signUp': True, "code": sign_up }
            return JsonResponse(data)

    elif (not (confirmPass == password)) and (confirmPass !="") and (password != None) and (confirmPass != None) :
        # todo: show message shuld equals
        print("TODO msg")

    elif verifyPhone and (verifyPhone != None) and (verifyPhone!=""):
        isVerified = verifyAccount(models.User,verifyPhone)
        data = { 'isVerified': isVerified, }
        return JsonResponse(data)

    elif phone:
        isLogin = signIn(models.User,phone,password)
        data = { 'isLogin': isLogin, }
        return JsonResponse(data)



def signIn(User,phone,password):

    user = User.objects.filter(phone=phone)
    if user[0].isVerified == True:
        hashPass = sha256(bytes(password,"utf-8"))
        if user[0].password == hashPass.hexdigest() :

            return True
        else:
            return False
    else:
        return "notVerified"


def signUp(User,userName,phone,password,confirmPass):


    if password == confirmPass:

        hashPass = sha256(bytes(password,"utf-8"))

        if not User.objects.filter(phone=phone):
            User.objects.create(name=userName,phone=phone,password=hashPass.hexdigest()).save()
            rand_code = str( random.randint(10000,99999))
            print(rand_code)

            sendSMS_verifyCode(phone,rand_code,749122)
            return rand_code
        else:
            return False


    return False


def forgetPass(User,forgetPhone):

    passwd = generateSimplePass()
    txt =  str(passwd)
    new_pass = str(sha256(bytes(str(passwd),"utf-8")).hexdigest())
    User.objects.filter(phone=forgetPhone).update(password=new_pass)
    sendSMS_verifyCode(forgetPhone,txt,230731)


def verifyAccount(User,phone):

    # print(phone)
    User.objects.filter(phone=phone).update(isVerified=True)
    return str(User.objects.get(phone=phone).isVerified)




def publisherSignin(publisher,phone,password):

    data = {}

    try:
        pub = publisher.objects.filter(connectionWay=phone)
    finally :

        if pub:
            if (str(pub[0].password) == str(password)):
                return JsonResponse({ 'isLogin': "true", "pub_id": pub[0].id })
            else:
                return JsonResponse({ 'isLogin': "false", })
        else :
            return JsonResponse({ 'isLogin': "false", })


def publisherForgetPass(publisher,phone):

    newPass = generateSimplePass()
    publisher.objects.filter(connectionWay=phone).update(password=newPass)

    sendSMS_verifyCode(phone,newPass,230731)

    return True



def sendSMS_verifyCode(phone,txt,template):

    userName = "mahdi1380"
    passwd = "vOsyRPwKNfjzDqIb7TYJbJbZterHZEEdRjybf445HRXsg2ovyv3JzCXscW6wMELy"
    line="30007732002064"
    header={
        'X-API-KEY': 'vOsyRPwKNfjzDqIb7TYJbJbZterHZEEdRjybf445HRXsg2ovyv3JzCXscW6wMELy',
        "Content-Type": "application/json; charset=utf-8",
        }
    url ="https://api.sms.ir/v1/send/verify"

    body=  {
        "mobile": str(phone),
        "templateId": template,
        "parameters": [
        {
            "name": "Code",
            "value": str(txt)
        }
        ]
    }

    res = requests.post(url,headers=header,json=body)


    print( " SMS CODE:  " + str(res.json()["status"]))
    return (res.json()["status"])


def generateSimplePass():
    rand = random.randint(1,20000)
    password = str(sha256(bytes(str(rand),"utf-8")).hexdigest())[:8]
    print(password)
    return password
