from random import randint
from time import sleep
class atm:
   def __init__(self):
    while True:
     print("1.login")
     print("2.create")
     print("3.exit")
     x=input("enter :")
     if(x=="3"):
      print("exiting .....")
      sleep(3)
      print("exit secsesful")
      break
     elif(x=="1"):
      self.login()
     elif(x=="2"):
      self.create()
     else:
      print("wrong input")
   def create(self):
    global data
    r_id=randint(11111,99999)
    while True:
     if(r_id not in  data):
      break
    self.name=input("enter your name :")
    while True:
     try:
      self.age=int(input("enter your age :"))
      if(self.age<18 or self.age>80):
       print("your to old or young")
      else:
       break
     except:
      print("invlid input")
    self.pin=input("set your pin :")
    data={r_id:{"name":self.name,"age":self.age,"pin":self.pin,"bal":0}}
    print(r_id)
    while True:
     print("1.see balce ")
     print("2.widrow ")
     print("3.dipozit")
     print("4.see delteld")
     print("5.exit")
     x=input("enter :")
     if(x=="5"):
      break
     elif(x=="1"):
      print("balce:",data[r_id]["bal"])
     elif(x=="2"):
      pin_s=input("enter your pin :")
      if(pin_s==data[r_id]["pin"]):
       try:
        wid=int(input("enter how widrow :"))
        data[r_id]["bal"]-=wid
       except:
        print("invlid input")
      else:
       print("wrong pin")
     elif(x=="3"):
      pin_s=input("enter your pin :")
      if(pin_s==data[r_id]["pin"]):
       try:
        dipo=int(input("enter how you whant to dipozit :"))
        data[r_id]["bal"]+=dipo
       except:
        print("invlid input")
      else:
       print("wrong pin")
     elif(x=="4"):
      pin_s=input("enter your pin :")
      if(pin_s==data[r_id]["pin"]):
       print("name:",data[r_id]["name"])
       print("age:",data[r_id]["age"])
       print("pin:",data[r_id]["pin"])
       print("id:",r_id)
      else:
       print("wrong pin")
     else:
      print("wrong input")
   def login(self):
    global data
    r_id_l=input("enter your id :")
    if(r_id_l not in data):
     print("id not found")
    if(r_id_l in data):
     pin_l=input("enter pin :")
     if(pin_l==data[r_id_l]["pin"]):
      print("wellcome back ")
      while True:
       print("1.see balce")
       print("2.widrow")
       print("3.dipozit")
       print("4.see deldet")
       print("5.exit")
       x=input("enter :")
       if(x=="5"):
        break
       elif(x=="1"):
        print("balce:",data[r_id_l]["bal"])
       elif(x=="2"):
        pin_s=input("enter your pin :")
        if(pin_s==data[r_id_l]["pin"]):
         try:
          wid=int(input("enter your widrow money :"))
          data[r_id_l]["bal"]-=wid
         except:
          print("invlid input ")
        else:
         print("wrong pin")
       elif(x=="3"):
         pin_s=input("enter your pin :")
         if(pin_s==data[r_id_l]["pin"]):
          try:
           dipo=int(input("enter how money you whant dipozit :"))
           data[r_id_l]["bal"]+=dipo
          except:
           print("wrong input")
         else:
          print("wrong pin ")


at=atm()

