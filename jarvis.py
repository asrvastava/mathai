
#======================================#
#-----------imports--------------------#
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wk
import smtplib as sb,ssl
import webbrowser as wb
import os
from selenium import webdriver
import pyautogui as pg
import psutil as pu
import pyjokes as pj
import pymysql
import adminstration
import sqlai

# initialization of pyttsx3 module 
abc = pyttsx3.init()
 
# function for sending email
def sendmail(to,content):

    with sb.SMTP_SSL('smtp.gmail.com',465,content) as server:
        server.login('asrvastava8295@gmail.com','asrmath1053')
        server.sendmail('asrvastava8295@gmail.com',to,content)
        server.close()

# function for jokes  
def jokes():
    speak(pj.get_jokes(language="hin",category="neutral"))

# function for speaking something
def speak(audio):
    abc.say(audio)
    abc.runAndWait()

# function for wishing
def wish():
    hour = datetime.datetime.now().hour

    if hour > 5 and hour < 12:
        speak("good morning sir")
    elif hour == 12:
        speak("good noon sir") 
    elif hour > 12 and hour < 18:
        speak("good afternoon sir")
    elif hour > 18 and hour < 20:
        speak("good evening  sir")
    else:
        speak("good night sir")

# function for time
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(time)

# function for date
def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(day)
    speak(month)
    speak(year)

# function for cpu status
def cpu():
    usage = str(pu.cpu_percent())
    speak("cpu is at" + usage)
    battery =pu.sensors_battery()
    speak("battery is at")
    speak(battery) 

def reset():
    
    # password reseting area 
    speak("your entered password is wrong")
    speak("do you want to change your password")
    sri=takecommand().lower()

    if "yes" in sri:
        speak("are you old user or new user")
        w2=takecommand().lower()

        if 'old user' in w2:
            speak("do you forget your password")
            w1=takecommand().lower()
            print(w1)

            if w1=='yes'or w1=="hmm" or w1=="hai":
                speak("enter your phone no.")
                phone_no=input("enter your phone no.")
                speak("enter your new password")
                npassword=input("enter your new password")
                j=adminstration.forget(npassword,phone_no)
                str(j)

                if j :
                    speak("your passworld change successfully please restart the program")
                    exit()


            else:
                speak("please try after some time")  

        else:
            speak("do you want to be registered")
            re=takecommand().lower()
            if "yes" in re:
                newregistration()

            else:
                speak("thank you for visiting!!")    
    else:
        speak("i can't recognize you")
        exit()
       

def newregistration():
    server = pymysql.connect( host="localhost", user="root",password="Asrmath1053#")
    a = server.cursor()

    sql="USE jarvis;"
    a.execute(sql)
    
    speak("enter your name")
    name=input("enter your name")

    speak("enter your password")
    password=input("enter your password")

    speak("enter your email")
    email=input("enter your email")

    speak("enter your phoneno")
    phoneno=input("enter your phone no")
    
    try:
        a.execute("Insert into password values(%s,%s,%s,%s)",(name,password,email,phoneno))
    except:
        print(Exception)    

# taking command function from user
try:    
    def takecommand():
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("listing")
            r.pause_threshold = 3
            audio = r.listen(source)

            try:
                print("recognizing")
                try:
                    query = r.recognize_google(audio)
                except Exception:
                        speak("could you say it again")

                print(query)
                return query

            except Exception as e:
                print(e)

        

except Exception as k:
    speak(k)


# login area ==============#
speak('please enter your email')
email = input("enter your email")
str(email)
speak('enter your password')
password= input("enter your password")
str(password)
z=adminstration.admin(email,password)  
str(z)
null=""

# main content of program started

if z:
    speak('welcome')
    speak(z)
   
    if __name__ == "__main__":
        wish()
        while 1==1:
            query = takecommand().lower()
            if 'time' in query:
                time()

            elif 'what is your name' in query:
                speak(" i am maith your ai assitant") 

            elif 'build you' in query:
                speak('ankit kr. srivastava')  

            elif 'hey maith'in query:  
                speak("yes")
                speak(z)

            elif 'in which language your coded' in query:
                speak('python version 3.6.2')

            elif 'important imports'in query:
                try:

                    f=open('about.txt','r')

                except Exception:
                    speak(Exception)    
                

            elif 'who am i ' in query:
                speak(z)  

            elif 'do you remember anything' in query:
                try:
                    f =open('data.txt','r')
                    speak("you said to remember that"+f.read())    

                except Exception :
                    speak('you did not say any thing')        
    

            elif 'date' in query:
                date()
    

            elif 'remember that' in query:
                speak("what should i remember")    
                data = takecommand()
                speak("you said that" + data)
                data = data + time() + date()
                speak("is it correct")
                k = takecommand()
                if k=='yes':
                    r = open('data.txt','w')
                    r.write(data)
                    r.close()
                
            elif 'wikipedia' in query:
                speak("searching")
                query = query.replace("WIKIPEDIA","")
                result = wk.summary(query, sentences=3)
                print(result)
                speak(result)   

            elif 'send email' in query:
                speak("what you want send??")
                content = takecommand()
                speak("whom you want to send it")
                to = input("enter email id")
                sendmail(to,content)
                speak("email has been send")
             

            elif 'search' in query:
                speak("what do you want to serach")
                search = takecommand().lower()
                driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
                driver.get(search + ".com")

            elif 'logout' in query:
                os.system("shutdown -1") 

            elif 'shutdown' in query:
                os.system("shutdown /s /t 1") 

            elif 'restart' in query:
                os.system("shutdown /r /t 1")  

            elif 'play ' in query:
                try:
                    songs_dir ='G:\\Music'
                    songs = os.listdir(songs_dir)
                    os.startfile(os.path.join(songs_dir,songs[0]))
                except Exception:
                    speak(Exception)
                    print(Exception)  

            elif 'open vscode' in query:
                dir='c:\\users\\hp\\documents\\VSCodeUserSetup-x64-1.45.1.exe'
                w= os.listdir(dir)
                os.startfile(os.path.join(dir,w[0]))                

            elif 'screenshot' in query:
                try:
                    image =pg.screenshot()
                    image.save("c:\\users\\hp\\maith ai project\\screenshot")   
                    speak("screenshot taken") 
                except Exception :
                    print(Exception)
                    speak(Exception)    
        
            elif 'system status' in query:
                cpu()

            elif 'joke' in query:
                jokes()


            elif "database" in query:
                speak("enter database host ")  
                host=input("enter database host")
                speak("enter database password")
                password=("enter database password")
                speak("enter database username")
                username=input("enter database username")
                speak("what do you want to in databse")
                z=takecommand().lower()


                if 'create ' and 'database ' in z:
                    sqlai.create(host,password,username)

                if 'query' and 'database' in z:
                    sqlai.query(host,password,username)    



            elif 'offline'in query:
                exit() 

else:
    reset()



