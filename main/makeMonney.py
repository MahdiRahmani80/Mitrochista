import requests
from mitrochista.init_scrap import DOMAIN

def clickBtn(models,course_id,ip):

    cou = models.Course.objects.get(id=course_id)
    pub = models.Publish.objects.get(course=cou).publisher
    models.ClickCourse.objects.create(course=cou,ip=ip,publisher=pub)


    models.Credit.objects.filter(publisher=pub).update(monney = howIsShowPrice(models,pub,cou.price) )



def howIsShowPrice(models,pub,price):

    last_monney = models.Credit.objects.filter(publisher=pub)[0].monney

    if price == 0:
        last_monney=last_monney-100

    elif price <= 100000:
        last_monney=last_monney-200

    elif price <= 200000:
        last_monney=last_monney-250

    elif price <= 500000:
        last_monney=last_monney-400

    elif price<= 1000000:
        last_monney=last_monney-600

    else:
        last_monney=last_monney-700


    if last_monney <= -1000:
        pub.isScrapAlgorithmWrite=False
        pub.save()

        models.Publish.objects.filter(publisher=pub).update(is_visible=False)

    return last_monney


def goToIDPAY(amount,publisher):

    url ="https://api.idpay.ir/v1.1/payment"
    header={
        'X-API-KEY': '4ec53ca3-75e4-4a63-a4b1-628c4383d050',
        'X-SANDBOX': '1',
        "Content-Type": "application/json; charset=utf-8",
        }
    data={
        'order_id' : str(publisher.id),
        "amount" : int(amount),
        "desc" : "شارژ حساب وبسایت "+ str(publisher) +" به مبلغ "+str(amount)+" ریال ",
        "callback": DOMAIN + "pannel/website/"+str(publisher.id)
    }
    res = requests.post(url,json=data,headers=header)
    return res.json()["link"]


