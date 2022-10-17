import os
import random
import json
from timeit import default_timer as timer
from datetime import timedelta

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


# setting
point = 0  # player point
times = 30  # countdown time
wrong = 10
bounes = 0  # 0 = false 1 = true
high = 10
ehigh = 5
elow = 0
low = 1
thinghigh = 2

try:
  name = inputimeout(prompt=("what is your name (This will record if you are the highest marks)"), timeout= 30)
except TimeoutOccurred:
  name = "guest"
if not name:
  name = "guest"
print(colored(f"hi {name} welcome to little game. you can only have {wrong} wrong ans and you only have {times} secound in 1 qustion . it will become harder when you have enough marks pls do you best in every qustion\n",'blue',attrs=['bold']))
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
    
  elif point <= 15:
    times = 25
    high = 50
    elow = 0
    ehigh = 0
    low = 0
    thinghigh = 4
    if point == 6:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
      
  elif point <= 30:
    times  = 20
    high = 100
    elow = 0
    ehigh = 5
    low = 0
    thinghigh = 5
    if point == 16:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
      
  elif point <= 49:
    times  = 15
    high = 200
    elow = 0
    ehigh = 10
    low = 0
    thinghigh = 6
    if point == 31:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
      
  elif point < 100:
    times  = 15
    high = 200
    elow = -10
    ehigh = 10
    low = -200
    thinghigh = 7
    if point == 50:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
      
  elif point >= 100:
    times = 10
    high = 1000
    elow = -15
    ehigh = 15
    low = -1000
    thinghigh = 8
    if point == 100:
      print(colored(f"you only have {times} secound in 1 qustion now", 'yellow',attrs=['bold']))
    





      

  # start giving qustion
  if things == 1:

    ans = a + b
    try:
      inputans = inputimeout(prompt=(aa + " + " + bb + " = ?\n"), timeout= times)
      
    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))

  elif things == 2:

    ans = a - b
    try:
      inputans = inputimeout(prompt=(aa + " - " + bb + " = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))

  elif things == 3:
    ans = a * b
    try:
      inputans = inputimeout(prompt=(aa + " × " + bb + " = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))

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
      print(colored(random.choice(jdata['timeout']),'red'))

      
  elif things == 5:

    ans = round(a*(b/100))
    try:
      inputans = inputimeout(prompt=(aa + " × " + bb + "% = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))


  elif things == 6:
    if b > 10 or b < -10:
      b = random.randint(-10, 10)
      bb = str(b)
    ans = a*10**b
    try:
      inputans = inputimeout(prompt=(aa + " × 10 ^ " + bb + " = ?\n"),timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))

      

  elif things == 7:

    if b > ehigh or b < elow:
      b = random.randint(elow, ehigh)
      bb = str(b)
    if a > 10 or a < -10:
      a = random.randint(-10, 10)
      aa = str(a)
    ans = a**b
    if ans >= 100000:
      a = random.randint(-10, 10)
      b = random.randint(elow, ehigh)
      bb = str(b)
      aa = str(a)
      ans = a**b
    
    try:
      inputans = inputimeout(prompt=(aa + " ^ " + bb + " = ?\n"), timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))


      

  elif things == 8:
    if b < 0:
      b = random.randint(0, high)
      bb = str(b)
    ans = round(b**0.5)
    try:
      inputans = inputimeout(prompt=(" √￣(" + bb + ") = ? (rounding)\n"),timeout= times)

    except TimeoutOccurred:
      inputans = 0.9487
      print(colored(random.choice(jdata['timeout']),'red'))


    

  if not inputans:
    print(colored(random.choice(jdata['noinput']),'red'))

    print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
    if point >= 50:
      print(colored(random.choice(jdata['highwrong']),'red',attrs=['bold']))
    else:
      print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))

    wrong = wrong - 1
    bounes = 0
    print(colored(f"         {wrong}  times left \n", 'magenta',attrs=['bold']))

  else:
    try:
      if float(inputans) == float(ans):  #Player correct
        point = point + 1
        print(colored(random.choice(jdata['nice']), 'green',attrs=['bold']))
        

        if bounes == 0:  # if this time
          bounes = 1

        elif bounes == 1:
          wrong = wrong + 1
          print(colored(f"         you get 1 more time {wrong} times left \n", 'green'))

      else:  #Player wrong
        print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
        print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))

        wrong = wrong - 1
        bounes = 0

        print(colored(f"         {wrong}  times left \n", 'magenta',attrs=['bold']))
    except:
      txt = random.randint(1, 5)
      if txt == 1:
          print(colored(f"{inputans} is not a number!", 'red'))
      elif txt == 2:
          print(colored(f"you think {inputans} is a number?", 'red'))
      elif txt == 3:
          print(colored(f"Don't spam ok this is a math you write {inputans} ?", 'red'))
      elif txt == 4:
          print(colored(f"you spend 10 secound to spam {inputans} = you waste everyone 10 secound = you waste 300 secound = you waste everyone 5 min", 'red'))
      elif txt == 5:
          print(colored(f"Nice IQ {inputans}is a number \n you should go to see doctor", 'red'))
      print(colored(f"The correct ans is {ans}" ,'blue',attrs=['bold']))
      print(colored(random.choice(jdata['wrong']), 'red',attrs=['bold']))

      wrong = wrong - 1
      bounes = 0
      print(colored(f"         {wrong}  times left \n", 'magenta',attrs=['bold']))

  if wrong == 0:
    if int(point) > int(jdata['marks']):
      jdata['marks'] = point
      jdata['name'] = name
      print(colored(f"{name} you get a new record in this game",'green'))
    txt = random.randint(1, 5)
    print(colored(f"         --Game Over--\nYou got {point} point!\nThe higher score record is {jdata['marks']} and He/She is {jdata['name']}",'blue',attrs=['bold']))
    end = timer()
    timer =timedelta(seconds=end-start)
    print(colored(f"you spend {timer} to play this game lol",'green'))
    with open('setting.json','w',encoding='utf8') as jfile:
      json.dump(jdata,jfile,indent = 4)
  
    if point <= 25:
        if txt == 1:
          print(colored("Pls go back to your primary school",'red'))
        elif txt == 2:
          print(colored("Oh You are so unluckly",'red'))
        elif txt == 3:
          print(colored("Like and subscribe in the next 3.2 seconds or your math exam mark will become 0",'red'))
        elif txt == 4:
          print(colored("PlayerSoTrash = true",'red'))
        elif txt == 5:
          print(colored("Do you want to play our baby mode?",'red'))
          print(colored("Oh sorry we haven't baby mode",'red'))

    elif point <= 49:
        if txt == 1:
          print(colored("Can you do it better?",'red'))
        elif txt == 2:
          print(colored('you should change your CPU','red'))
        elif txt == 3:
          print(colored("you should find your math teacher",'red'))
        elif txt == 4:
          print(colored("Never gonna give you up Never gonna let you down",'red'))
        elif txt == 5:
          print(colored("https://youtu.be/dQw4w9WgXcQ\n click this ☝",'red'))

    elif point <= 100:
        if txt == 1:
          print(colored("You just pass?Nice",'red'))
        elif txt == 2:
          print(colored(":)",'red'))
        elif txt == 3:
          print(colored("Good",'red'))
        elif txt == 4:
          print(colored(".w.",'red'))
        elif txt == 5:
          print(colored("Add oil",'red'))

    elif point < 200:
        if txt == 1:
          print(colored("Nice try",'red'))
        elif txt == 2:
          print(colored("403 error",'red'))
        elif txt == 3:
          print(colored("Do you know this game is so hard when you get this marks",'red'))
        elif txt == 4:
          print(colored(".W.",'red'))
        elif txt == 5:
          print(colored("404 Not Find",'red'))

    elif point >= 200:
        if txt == 1:
          print(colored("ඞSUSඞ",'red'))
        elif txt == 2:
          print(colored("Do you know only 0.001% of people can see this message",'red'))
        elif txt == 3:
          print(colored("When you hear this , you spent so many times",'red'))
        elif txt == 4:
          print(colored(".O.",'red'))
        elif txt == 5:
          print(colored("GG EZ",'red'))
