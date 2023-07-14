from faker import Faker
import numpy as np
from random_object_id import generate
import time
import json
import random
import string

fake = Faker()
 
 
def randStr(chars =  string.hexdigits , N=10):
    return ''.join(random.choice(chars) for _ in range(N))
 
def generate_data(records):
    
    dic = []
    
    company_name= [
        'گوگل','اسنپ','کوکاکولا','Ebay','نکیا','سیسکو','Walmart','Nike','پارت','ایران خودرو','اپل','سامسونگ','هوآوی','علی بابا','آمازون','دیوار','بازار','مایکروسافت',
        'IBM','استارباکس','مک دونالد','openai','زاپوس' , 'Sky','Disney','Ikea','پپسی','BBC','YouTube','آپارات'
    ]
    
    loc = [
        "ایران-اصفهان",
        "آمریکا-نیویورک",
        "آلمان-فرانکفورت",
        "آلمان-برلین",
        "استرالیا-سیدنی",
        "استرالیا-ملبورن",
        "هلند-آمستردام",
        "ایتالیا-میلان",
        "ایتالیا-تورین",
        "ایتالیا-اسپنیزا",
        "اسپانیا-مادرید",
        "اسپانیا-بارسلون",
        "کانادا-ونکوور",
        "عراق-بغداد",
        "سوریه-دمشق",
        "ترکیه-استامبول",
        "امارات-دبی",
        "عربستان-مدینا",
        "نروژ-اسلو",
        "فرانسه-پاریس",
        "چین-پکن",
        "تایلند-بانکوک",
        "ترکیه-آنکارا",
        "ایران-یزد",
        "آمریکا-کالیفرنیا",
        "آمریکا-منهتن",
        "آمریکا-نیوجرسی",
        "ایران-مشهد",
        "ایران-تهران",
    ]
    title = [
        "توسعه دهنده وبسایت",
        "توسعه دهنده فرانت",
        "توسعه دهنده بک اند",
        "توسعه دهنده بازی",
        "برنامه نویس پایتون",
        "برنامه نویس فلاتر",
        "برنامه نویس هوش مصنوعی",
        "متخصص یادگیری ماشین",
        "طراحی رابط کاربری",
        "طراح محصول",
        "اسکرام مستر",
        "مدیر منابع انسانی",
        "مدیرعامل",
        "برنامه نویس اندروید",
        "برنامه نویس اسمبلی",
        "برنامه نویس جاوا",
        "بازی ساز",
        "مشاور توسعه دهندگی",
        "مهندس نرم افزار",
        "مهندس شبکه",
        "متخصص امنیت",
        "متخصص هوش مصنوعی",
        "محقق هوش مصنوعی",
        "پردازش زبان طبیعی",
        "مدیر مالی",
        "حسابدار",
        "استاد",
    ]
    job_site = [
        "هیبرید",
        "دورکاری",
        "در محل"
    ]
    
    job_type = [
        "پاره وقت",
        "تمام وقت",
        "پروژه ایی",
        "شراکتی",
        "کارآموزی",
    ]
    
    req = [
        "مسلط به دیتابیس Postgres، Mongo db",
        "مسلط به Redis",
        "تسلط بر مفاهیم برنامه نویسی شیء گرا",
        "مسلط به API نویسی Django Rest Framework",
        "مسلط به Repository pattern",
        "مسلط به تست نویسی، CI/CD، Docker",
        "مسلط به ابزارهای version control",
        "مسلط به سوکت نویسی",
        "3 سال سابقه کار در گروه شغلی مشابه",
        "مسلط به زبان برنامه نویسی پایتون",
        "آشنایی با مفاهیم برنامه نویسی شی گرا و تجربه ی عملی",
        "آشنایی با مفاهیم شبکه، لینوکس و تجربه ی عملی",
        "آشنایی با  Django-reset framework",
        "آشنایی با  مفاهیم مدیریت کد، ansible، git، CI/CD و ...",
        " علاقه مند به یادگیری و توانمند در حل مسائل کاربردی ",
        " تسلط و مهارت کافی در برنامه نویسی و تولید نرم افزار (به ویژه( Python) ",
        "آشنایی با مفاهیم و ابزارهای تحلیل و کاوش کلان داده (مانند ُSpark، hadoop  و. ...)",
        "آشنایی کافی با مفاهیم آمار و احتمال کاربردی در تحلیل داده و یادگیری ماشین ",
        "آشنایی با رویه های پیاده سازی و تولید محصولات یادگیری ماشین (ML Pipelines) ",
        "تسلط بر ابزارها و کتابخانه های پیاده سازی الگوریتم های یادگیری ماشین (از جمله scikit-learn, Pytorch و (TensorFlow ",
        "تسلط بر الگوریتم های پردازش متن و زبان طبیعی (Text Process & NLP)",
        "توانایی و تسلط بر طراحی و پیاده سازی گزارش های تحلیلی (در قالب dashboaard های عملیاتی)",
        "آشنایی با مفاهیم و ابزارهای هوش تجاری (BI) و تحلیل داده ",
        "آشنایی با grpc",
 
    ]
    
    des = [
        "ما به نیرویی با انگیزه و باتجربه در زمینه پایتون و Django نیاز داریم. دانستن rest-framework، معماری های سه لایه و micro-service برای ما ارزشمند است. نیروهای ما در محیطی فعال با تکنولوژی های نوین مدیریت پروژه و انواع روش های جدید توسعه همانند CD/CI، unit test، git و .... کار می کنند. کار ما توسعه ابزارهای مدیریت شبکه به ویژه مسائل مربوط به امنیت شبکه است. لذا، افرادی که به این مباحث آشنا باشند و یا مشتاق به یادگیری باشند، در اولویت  انتخاب خواهند بود.",
        "کار در پروژه هایی برای بزرگترین مراکز دولتی و خصوصی، ارائه هفتگی لیستی از تغییرات مورد نیاز در برنامه، کاملا دورکار و مستقل بدون نیاز به هماهنگی با همکار برنامه نویس دیگری، حقوق با توجه به میزان تجربه شما حداکثر ساعتی 150 هزار تومان، اعلام مدت زمان کار شده توسط شما.",
        "به دنبال فردی هستیم که دانش کافی و عمیقی از جاوااسکریپت و React.js داشته باشه و همیشه به دنبال یادگیری و چالش های مختلف در پروژه ها باشه. وابسته به فریمورک ها و لایبرری های مختلف نباشه و همیشه تلاش برای توسعه به بهترین روش ممکن باشه.",
    ]
    
    #Iterate the loop based on the input value and generate fake data
    # faker.email()   
    # faker.phone_number()
    
    for n in range(1, records):
        customer = {}
        customer['id']= int(n)
        customer['company_name']= str(np.random.choice(company_name))
        customer['location']= str(np.random.choice(loc))
        customer['job_title']= str(np.random.choice(title))
        customer['last']= int(fake.random_int(1,365))
        customer['applicant']= int(fake.random_int(1,100))
        customer['job_site']= str(np.random.choice(job_site))
        customer['job_type']= str(np.random.choice(job_type))
        customer['req']= str(np.random.choice(req))
        customer['des']= str(np.random.choice(des))
        customer['phone']= str(fake.phone_number())
        customer['Email']= str(fake.email())
        dic.append(customer)
 
    #Write the data into the JSON file
    with open('jafari.json','w') as fp:
            json.dump(dic,fp)
 
#Take the number of records from the user
num = int(input("Enter the number of records:"))
#Call the function to generate fake records and store into a json file
start = time.time()
generate_data(num)
end = time.time()
total_time = end - start
print(total_time)


# from faker import Faker
# import numpy as np
# from random_object_id import generate
# import time
# import json
# import calendar
# from datetime import date, datetime
# import random
# import string

# fake = Faker()
 
 
# def randStr(chars =  string.hexdigits , N=10):
#     return ''.join(random.choice(chars) for _ in range(N))
 
# def generate_data(records):
    
#     mmm = []
#     with open('customerNumber.txt') as txt:
#         for i in txt:
#             mmm.append(i)
    
#     platform= ["ATM","Internet","Bank"]
#     operation = ["KartBeKart","CashReceipt","CurrencyReceipt","TransferCurrency","TransferCash","CashDeposit","InternetPayment","POS"]
#     branch = [1,2,3]
#     customer = {}
#     dic = []
#     #Iterate the loop based on the input value and generate fake data
    
#     for n in range(0, records):
#         customer = {}
#         customer['_id']={"$oid":generate()}
#         customer['rowid']= int(n+1000001)
#         customer['id']= int(n+1000001)
#         customer['city']= str(fake.city())
#         customer['amount']= int(fake.random_int(1000001,99999999))
#         customer['operation']= str(np.random.choice(operation))
#         customer['platform']= str(np.random.choice(platform))
#         customer['origin']= str(randStr(N=31))
#         customer['destination']= str(randStr(N=29))
#         customer['branch_id']= int(np.random.choice(branch))
#         x = np.random.choice(mmm)
#         customer['customernumber_id'] = str(x[:-1])
#         tdate = fake.date_between(datetime(2022,10,25),datetime(2022,11,25))
#         calen = calendar.timegm(tdate.timetuple())
#         customer['Created_Time']= int(calen)
    
#         dic.append(customer)
 
#     #Write the data into the JSON file
#     with open('Testtt.json','w') as fp:
#             json.dump(dic, fp)

 
# #Take the number of records from the user
# num = int(input("Enter the number of records:"))
# #Call the function to generate fake records and store into a json file
# start = time.time()
# generate_data(num)
# end = time.time()
# total_time = end - start
# print(total_time)

# #Import Faker
# from faker import Faker
# import numpy as np
# from random_object_id import generate
# import time
# #Import JSON
# import json
 
# #Declare faker onject
# fake = Faker()
 
# #Define function to generate fake data and store into a JSON file
# def generate_data(records):
#     #Declare an empty dictionary
#     educations = [ 'Sikl' , 'Diploma' ,'karshenasi', 'Arshad', 'Doctora']
#     citys = ['alborz','ardabil','Urmia','tabriz','bushehr','shahrekord','isfahan','shiraz','rasht','gorgan','hamedan','bandarabbas','ilam','kerman','kermanshah','birjand','mashhad','bojnurd','ahwaz','yasuj','sanandaj','khorramabad','arak','sari','qazvin','qom','semnan','zahedan','tehran','yazd','zanjan']
    
#     pre_phone = ['15','39','01','11','12','13','33','36','37','03','38','21','17','90','91','92']
    
#     pre_sabet_phone = ['041','044','045','031','051','021','084','077','038','056','058',
#                        '061','024','023','054','071','087','074','013','011','076','081','035']
    
#     firstname_M = ['Hosein','Alireza','AmirHosein','Ali','MohammadReza','MohammadHosein','Mohsen','kaveh','Adel',
#                  'Mahdi','Ramin','Arian','Armin','Amir','Foad','Sadegh','Hamid','Reza','Erfan', 'GholamReza','Shayan','Masoud']
    
#     firstname_F = ['Zahra','Fatemeh','Mohadese','Samira','Atefeh','Samaneh','Mitra','Akram','Nazanin','Leyla','Sara','Nika','Mahsa']
    
#     lastname = ['Hoseini','Jafari','Akbarzadeh','Firozi','Abbasi','Abbasspor','Kashani','Mohammadi','Sazgar',
#                  'Shakeri','Arhami','Azadfekr','Beheshti Nia','Jafar Abadi','Amiri','Lakzaee','Erfani','Zomorodi',
#                  'Kord Abadi','Kargar Zadeh','Mohammad Zadeh', 'Javidi','Zareh','Sohrabi','Edalati','Hajar','Bonyadi','Bayati',
#                  'Frohan','Bayat','Shakeremi','Amini','Jafarian','Shayanfar','Kavosi']
    
#     firstname = []
#     weights = [0.6, 0.2, 0.1, 0.07, 0.03]
#     Gender = ['M','F']
#     customer = {}
#     dic = []
#     #Iterate the loop based on the input value and generate fake data
#     for n in range(0, records):
#         x = np.random.choice(Gender)
#         if x == 'M':
#             firstname = firstname_M
#         else : firstname = firstname_F
#         customer = {}
#         customer['_id']={"$oid":generate()}        
#         customer['rowid']= n+3
#         customer['customernumber'] = fake.md5()
#         customer['firstname']= str(np.random.choice(firstname))
#         customer['lastname']= str(np.random.choice(lastname))
#         customer['phone']= str(str(np.random.choice(pre_sabet_phone)+str(fake.random_int(1,10))+str(fake.random_int(100,1000))+str(fake.random_int(1000,10000))))
#         customer['mobile']= str("+989"+str(np.random.choice(pre_phone))+""+str(fake.random_int(101,999))+""+str(fake.random_int(1000,9999)))
#         customer['age']= fake.random_int(1,86)
#         customer['gender']= str(x)
#         customer['citizenship']= str('IR')
#         customer['resident']= str(np.random.choice(citys))
#         customer['education']= str(np.random.choice(educations))
#         customer['zipcode']= fake.random_int(10001,99999)
#         customer['accountnumber']= n+3
#         customer['branch_id']= n+3
#         dic.append(customer)
 
#     #Write the data into the JSON file
#     with open('Test.json', 'w') as fp:
#             json.dump(dic, fp)

 
#     print("File has been created.")
 
# #Take the number of records from the user
# num = int(input("Enter the number of records:"))
# #Call the function to generate fake records and store into a json file
# start = time.time()
# generate_data(num)
# end = time.time()
# total_time = end - start
# print(total_time)

# Grab Currrent Time After Running the Code


#Subtract Start Time from The End Time


# f = open('customer.json')
  
# # returns JSON object as 
# # a dictionary
# data = json.load(f)
  
# # Iterating through the json
# # list
# lest = []
# for i in data:
#     customer = {}
#     customer['customernumber'] = i['customernumber']
#     lest.append(customer)
#     print(i['customernumber'])
    
# with open('customernumber.json', 'w') as fp:
#     json.dump(lest, fp)  