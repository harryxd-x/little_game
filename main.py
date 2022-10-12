# import
import os
import random
import json
with open('setting.json','r',encoding='utf8') as jfile:
  jdata = json.load(jfile)
try:
  from inputimeout import inputimeout, TimeoutOccurred
except:
  os.system('pip install inputimeout')
  from inputimeout import inputimeout, TimeoutOccurred

# setting
point = 0  # player point
times = 30  # countdown time
wrong = 10
bounes = 0  # 0 = false 1 = true
high = 10
ehigh = 5
elow = 0
low = 1

name = inputimeout(prompt=("what is your name (This will record if you are the highest marks)"), timeout= 30)
if not name:
  name = "guest"
print("hi ",name," welcome to ? game you can only have ", wrong," wrong ans and you only have ", times, "secound in 1 qustion pls do you best in every qustion\n")

while not wrong <= 0:
  things = random.randint(1, 6)  # random get +-x/
  txt = random.randint(1, 5) #random output text
  a = random.randint(low, high)  # first number
  b = random.randint(low, high)  # secound number
  # a + b
  aa = str(a)
  bb = str(b)
  #setting again
  if point <= 5:
    times = 30
    high = 10
    elow = 0
    ehigh = 2
    low = 1
  elif point <= 15:
    times = 25
    high = 50
    elow = 0
    ehigh = 10
    low = 0
    print("you only have ", times, "secound in 1 qustion now")
  elif point <= 30:
    times  = 20
    high = 100
    elow = 0
    ehigh = 15
    low = 0
    print("you only have ", times, "secound in 1 qustion now")
  elif point < 50:
    times  = 15
    high = 100
    elow = -15
    ehigh = 15
    low = -100
    print("you only have ", times, "secound in 1 qustion now")
  elif point >= 100:
    times = 10
    high = 1000
    elow = -20
    ehigh = 20
    low = -1000
    print("you only have ", times, "secound in 1 qustion now")
    

  if things == 1:

    ans = a + b
    try:
      inputans = inputimeout(prompt=(aa + " + " + bb + " = ?\n"), timeout= times)
      

    except TimeoutOccurred:
      inputans = 0.9487
      print(random.choice(jdata['timeout']))

  elif things == 2:

    ans = a - b
    try:
      inputans = inputimeout(prompt=(aa + " - " + bb + " = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(random.choice(jdata['timeout']))

  elif things == 3:
    ans = a * b
    try:
      inputans = inputimeout(prompt=(aa + " × " + bb + " = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(random.choice(jdata['timeout']))

  elif things == 4:

    if b > a:
      b = random.randint(low, a)
      bb = str(b)
    if b == 0 :
      b = random.randint(low, high)
      bb = str(b)

    ans = round(a / b)
    try:
      inputans = inputimeout(prompt=(aa + " ÷ " + bb + " = ? (rounding)\n"),timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(random.choice(jdata['timeout']))

  elif things == 5:

    if b > 10:
      b = random.randint(elow, ehigh)
      bb = str(b)
    if a > 10:
      a = random.randint(low, high)
      aa = str(a)

    ans = a**b
    try:
      inputans = inputimeout(prompt=(aa + " ^ " + bb + " = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(random.choice(jdata['timeout']))

  elif things == 6:
    if b < 0:
      b = random.randint(0, high)
      bb = str(b)
    ans = round(b**0.5)
    try:
      inputans = inputimeout(prompt=(" √￣(" + bb + ") = ? (rounding)\n"),timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(random.choice(jdata['timeout']))



  else:
    print("⛔️error") 

  if not inputans:
    print(random.choice(jdata['noinput']))

    print("The correct ans is ", ans)
    if point >= 50:
      print(random.choice(jdata['highwrong']))
    else:
      print(random.choice(jdata['wrong']))

    wrong = wrong - 1
    bounes = 0
    print("         ", wrong, " times left \n")

  else:
    try:
      if float(inputans) == float(ans):  #Player correct
        point = point + 1
        print(random.choice(jdata['nice']))
        

        if bounes == 0:  # if this time
          bounes = 1

        elif bounes == 1:
          wrong = wrong + 1
          print("         you get 1 more time ", wrong, " times left \n")

      else:  #Player wrong
        print("The correct ans is ", ans)
        print(random.choice(jdata['wrong']))

        wrong = wrong - 1
        bounes = 0

        print("         ", wrong, " times left \n")
    except:
      txt = random.randint(1, 5)
      if txt == 1:
          print(inputans," is not a number!")
      elif txt == 2:
          print("you think ",inputans,"is a number?")
      elif txt == 3:
          print("Don't spam ok this is a math you write ",inputans," ?")
      elif txt == 4:
          print("you spend 10 secound to spam",inputans," = you waste everyone 10 secound = you waste 300 secound = you waste everyone 5 min")
      elif txt == 5:
          print("Nice IQ ",inputans,"is a number \n you should go to see doctor")
      print("The correct ans is ", ans)
      print(random.choice(jdata['wrong']))

      wrong = wrong - 1
      bounes = 0
      print("         ", wrong, " times left \n")

  if wrong == 0:
    if int(point) > int(jdata['marks']):
      jdata['marks'] = point
      jdata['name'] = name
      print("you get a new record in this game")
    txt = random.randint(1, 5)
    print("         --Game Over--\nYou got ", point, "point!\nThe higher score record is ",jdata['marks'],"and He/She is ",jdata['name'])
    with open('setting.json','w',encoding='utf8') as jfile:
      json.dump(jdata,jfile,indent = 4)
  
    if point == 0:
        if txt == 1:
          print("Pls go back to your primary school")
        elif txt == 2:
          print("Oh You are so unluckly")
        elif txt == 3:
          print(
            "Like and subscribe in the next 3.2 seconds or your math exam mark will become 0")
        elif txt == 4:
          print("PlayerSoTrash = true")
        elif txt == 5:
          print("Do you want to play our baby mode?")
          print("Oh sorry we haven't baby mode")

    elif point <= 5:
        if txt == 1:
          print("Can you do it better?")
        elif txt == 2:
          print('"1"+"1"= 11')
        elif txt == 3:
          print("you should find your math teacher")
        elif txt == 4:
          print("Never gonna give you up Never gonna let you down")
        elif txt == 5:
          print("https://youtu.be/dQw4w9WgXcQ\n click this ☝")

    elif point <= 10:
        if txt == 1:
          print("You just pass?Nice")
        elif txt == 2:
          print(":)")
        elif txt == 3:
          print("Good")
        elif txt == 4:
          print(".w.")
        elif txt == 5:
          print("Add oil")

    elif point < 20:
        if txt == 1:
          print("OMG WOW!")
        elif txt == 2:
          print("403 error")
        elif txt == 3:
          print("Sorry this game haven't full mark:)")
        elif txt == 4:
          print(".W.")
        elif txt == 5:
          print("404 Not Find")

    elif point >= 20:
        if txt == 1:
          print("ඞSUSඞ")
        elif txt == 2:
          print("Do you know only 0.001% of people can see this message")
        elif txt == 3:
          print("Sorry this is not full mark:)")
        elif txt == 4:
          print(".O.")
        elif txt == 5:
          print("GG EZ")
