import os
# import sys
import random
import time
import json
from timeit import default_timer as timer
from datetime import timedelta
mdata = {}

try:
  from termcolor import colored
except:
  os.system('pip install termcolor')
  from termcolor import colored
try:
  from inputimeout import inputimeout, TimeoutOccurred
except:
  os.system('pip install inputimeout')
  from inputimeout import inputimeout, TimeoutOccurred

  
with open('setting.json','r',encoding='utf8') as jfile:
  jdata = json.load(jfile)
try:
  with open('Marks.json','r',encoding='utf8') as mfile:
   mdata = json.load(mfile)
except FileNotFoundError:
    pass

# setting，
point = 0  # player point
times = 30  # countdown time
wrong = 5
bounes = 0  # 0 = false 1 = true
high = 10
ehigh = 5
elow = 0
low = 1
thinghigh = 2
wrongnum = 0
empty = 0
text = 0
timeout = 0
qustion = 0

name = input("what is your name : ")
# os.execv(sys.executable, ['python'] + sys.argv)
if not name:
  name = "guest"
print(colored(f"Hi {name}! Welcome to the Python Calculation Bee (version {jdata['version']}). You can only have {wrong} incorrect answers but you can get more attempts if you make the ans correct, and you only have {times} seconds per question. It will become harder as you accumulate more points, so do your best in every question!\n", 'blue', attrs=['bold']))
start = timer()

while not wrong <= 0:
  things = random.randint(1, thinghigh)  # random get +-x/
  txt = random.randint(1, 5) #random output text
  a = random.randint(low, high)  # first number
  b = random.randint(low, high)  # secound number
  aa = str(a)
  bb = str(b)
  
  #setting again
  # makme it harder while the game
  if point <= 5:
    times = 30
    high = 10
    elow = 0
    ehigh = 0
    low = 1
    thinghigh = 3
    level = 1
    
  elif point <= 10:
    times = 25
    high = 50
    elow = 0
    ehigh = 0
    low = 0
    thinghigh = 4
    level = 2
    
    if point == 6:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
      
  elif point <= 15:
    times  = 20
    high = 100
    elow = 0
    ehigh = 5
    low = 0
    thinghigh = 5
    level = 3
    
    if point == 11:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
      
  elif point <= 20:
    times  = 15
    high = 200
    elow = 0
    ehigh = 10
    low = 0
    thinghigh = 6
    level = 4
    
    if point == 16:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
      
  elif point < 35:
    times  = 15
    high = 200
    elow = -10
    ehigh = 10
    low = -200
    thinghigh = 7
    level = 5
    
    if point == 21:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
      
  elif point >= 35:                                                                                                                                                                               
    times = 10
    high = 1000
    elow = -15
    ehigh = 15
    low = -1000
    thinghigh = 8
    level = 6
    
    if point == 35:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
    



      

  # start giving qustion
  qustion = qustion + 1
  if things == 1:

    ans = a + b
    try:
      inputans = inputimeout(prompt=(str(qustion) + ".  " + aa + " + " + bb + " = ?\n"), timeout= times)
      
    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))
      timeout = timeout + 1
      wrongnum = wrongnum - 1

  elif things == 2:

    ans = a - b
    try:
      inputans = inputimeout(prompt=(str(qustion) + ".  " + aa + " - " + bb + " = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))
      timeout = timeout + 1
      wrongnum = wrongnum - 1

  elif things == 3:
    ans = a * b
    try:
      inputans = inputimeout(prompt=(str(qustion) + ".  " + aa + " × " + bb + " = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))
      timeout = timeout + 1
      wrongnum = wrongnum - 1

  elif things == 4:

    if b > a:
      b = random.randint(low, a)
      bb = str(b)
      
    if b == 0 :
      b = random.randint(low, high)
      bb = str(b)

    ans = round(a / b)
    try:
      inputans = inputimeout(prompt=(str(qustion) + ".  " + aa + " ÷ " + bb + " = ? (rounding)\n"),timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))
      timeout = timeout + 1
      wrongnum = wrongnum - 1

      
  elif things == 5:

    ans = round(a*(b/100))
    try:
      inputans = inputimeout(prompt=(str(qustion) + ".  " + aa + " × " + bb + "% = ? (rounding)\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))
      timeout = timeout + 1
      wrongnum = wrongnum - 1


  elif things == 6:
    if b > 10 or b < -10:
      b = random.randint(-10, 10)
      bb = str(b)
    ans = a*10**b
    try:
      inputans = inputimeout(prompt=(str(qustion) + ".  " + aa + " × 10 ^ " + bb + " = ?\n"),timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))
      timeout = timeout + 1
      wrongnum = wrongnum - 1

      

  elif things == 7:

    if b > ehigh or b < elow or b == 0:
      b = random.randint(elow, ehigh)
      if b == 0:
        b = random.randint(-10, 1)
      bb = str(b)
    if a > 10 or a < -10 or a == 0:
      a = random.randint(-10, 10)
      if a == 0:
        a = random.randint(-10, 1)
      aa = str(a)
    
    ans = round(a**b)
    if ans >= 100000:
      a = random.randint(-10, 10)
      b = random.randint(elow, ehigh)
      bb = str(b)
      aa = str(a)
      ans = a**b
    
    try:
      inputans = inputimeout(prompt=(str(qustion) + ".  " + aa + " ^ " + bb + " = ?(rounding)\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))
      timeout = timeout + 1
      wrongnum = wrongnum - 1


      

  elif things == 8:
    if b < 0:
      b = random.randint(0, high)
      bb = str(b)
    ans = round(b**0.5)
    try:
      inputans = inputimeout(prompt=(str(qustion) + ".  " + " √￣(" + bb + ") = ? (rounding)\n"),timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))
      timeout = timeout + 1
      wrongnum = wrongnum - 1


    

  if not inputans:
    print(colored(random.choice(jdata['noinput']),'red'))

    print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
    empty = empty + 1
    if point >= 50:
      print(colored(random.choice(jdata['highwrong']),'red',attrs=['bold']))
    else:
      print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))

    wrong = wrong - 1
    bounes = 0
    print(colored(f"         {wrong}  attempts left \n", 'magenta',attrs=['bold']))

  else:
    try:
      if float(inputans) == float(ans):  #Player correct
        point = point + 1
        print(colored(random.choice(jdata['nice']), 'green',attrs=['bold']))
        

        if bounes == 0:  # if this time
          bounes = 1

        elif bounes == 1:
          wrong = wrong + 1
          print(colored(f"         You get 1 more try. You have {wrong} attempts remaining \n", 'green'))

      else:  #Player wrong
        print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
        print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))

        wrong = wrong - 1
        wrongnum = wrongnum + 1
        bounes = 0

        print(colored(f"         {wrong}  attempts left \n", 'magenta',attrs=['bold']))
    except:
      if inputans == "help":
          print(colored("count it and type it",'yellow',attrs=['bold']))
          print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
          print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))
          wrongnum = wrongnum + 1

          wrong = wrong - 1
          bounes = 0

          print(colored(f"         {wrong}  attempts left \n", 'magenta',attrs=['bold']))
      elif inputans == "leave" or inputans == "end":
          print(colored("ok you leave you so trash",'red',attrs=['bold']))
          print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
          print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))
          empty = empty + 1

          wrong = 0
          bounes = 0
      elif inputans == "pass" or inputans == "skip"or inputans == "idk":
          print(colored("ok you so trash",'yellow',attrs=['bold']))
          print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
          print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))
          empty = empty + 1

          wrong = wrong - 1
          bounes = 0

          print(colored(f"         {wrong}  attempts left \n", 'magenta',attrs=['bold']))
      else:
        txt = random.randint(1, 5)
        print(colored(random.choice(jdata['notnum']), 'red'))
        print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
        print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))

        wrong = wrong - 1
        text = text + 1
        bounes = 0
        print(colored(f"         {wrong}  attempts left \n", 'magenta',attrs=['bold']))

  if wrong == 0:
    Mark = round(int(point)/int(qustion)*100)
    
    if int(point) > int(jdata['marks']):
      jdata['marks'] = point
      jdata['name'] = name
      print(colored(f"{name} you get a new record in this game",'green'))
    txt = random.randint(1, 5)
    end = timer()
    timer =timedelta(seconds=end-start)
    print(colored(f"         --Game Over--\nYou earned {point} points for answering {qustion} questions ({Mark}%). \nYou got {wrongnum} wrong and you typed text {text} time(s). You left {empty} question(s) empty and timed out on {timeout} question(s).  \nThe higher score record is {jdata['marks']} and He/She is {jdata['name']}",'blue',attrs=['bold']))
    print(colored(f"you spend {timer} to play this game lol",'green'))
    
    with open('setting.json','w',encoding='utf8') as jfile:
      json.dump(jdata,jfile,indent = 4)
  
    if Mark <= 20:
      print(colored(random.choice(jdata['trashpoint']),'red'))

    elif Mark <= 49:
      print(colored(random.choice(jdata['notpasspoint']),'red'))


    elif point <= 65:
      print(colored(random.choice(jdata['passpoint']),'red'))

    elif point < 90:
      print(colored(random.choice(jdata['highpoint']),'red'))

    elif point >= 90:
      print(colored(random.choice(jdata['veryhighpoint']),'red'))





    


      
    ctime = str(timer)
    info = [f"Name: {name}" , f"Marks: {point}"  ,f"Marks: {Mark}%" ,f"qustion: {qustion}",f"Wrong: {wrongnum}",f"Empty: {empty}",f"timeout times: {timeout}",f"Write text in ans: {text}", f"Time: {ctime}"]
    group = mdata['count']
    mdata['count'] = group + 1
    mdata[group] = info
    time.sleep(2)
    print("data saved")

    with open('Marks.json', 'w',encoding='utf8') as mfile:
      json.dump(mdata, mfile)