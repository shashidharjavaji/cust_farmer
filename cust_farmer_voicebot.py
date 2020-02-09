#-*- coding: utf-8 -*-
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# nltk.download('all')
import random
import numpy as np
from array import array
from playsound import playsound
from gtts import gTTS
import os
import speech_recognition as sr

def stt():
    x=sr.Recognizer()
    with sr.Microphone() as source:
        audio2=x.listen(source,timeout=4,phrase_time_limit=3)
    return x.recognize_google(audio2)
def smart_agriculture():
        try:
                choice="Are you a Customer or a farmer"
                farmm="welcome to farmers page"
                buy="Can i know your name"
                cust="Welcome to Customer page"
                ss1=gTTS(text=cust,lang='en', slow=False)
                ff=gTTS(text=farmm,lang='en',slow=False)
                k=gTTS(text=buy,lang='en',slow=False)
                ss1.save("ss1.mp3")
                ff.save("ss2.mp3")
                k.save("s.mp3")
                print(" Options \n1.Customer \n2.farmer")
                cc=gTTS(text=choice, lang='en', slow=False)
                cc.save("ccc.mp3")
                playsound("ccc.mp3")
                pq=sr.Recognizer()
                with sr.Microphone() as source:
                        audio1=pq.listen(source, timeout=4,phrase_time_limit=3)
                cccc=pq.recognize_google(audio1)
                print(cccc)
                if pq.recognize_google(audio1)=="customer":
                        playsound("ss1.mp3")
                        playsound("s.mp3")
                        l=sr.Recognizer()
                        with sr.Microphone() as source:
                            audio=l.listen(source, timeout=4,phrase_time_limit=3)
                        name="Hello "+l.recognize_google(audio)+" what would you like to buy"
                        nn=gTTS(text=name,lang='en',slow=False)
                        nn.save("cname.mp3")
                        playsound("cname.mp3")
                        chc=gTTS(text="you would like to buy"+stt()+"How many kg's would you like to buy",lang='en',slow=False)
                        chc.save("chc.mp3")
                        playsound("chc.mp3")
                        xyz="number of kg's="+str(stt())
                        sds=gTTS(text=xyz,lang='en',slow=False)
                        sds.save("kgs.mp3")
                        playsound("kgs.mp3")
                        dddd="your items are available would to like to go and get the orders or you want our employee to get them to you"
                        s1=gTTS(text=stt(),lang='en',slow=False)
                elif pq.recognize_google(audio1)=="farmer":
                        playsound("ss2.mp3")
                        playsound("s.mp3")
                        l=sr.Recognizer()
                        #with sr.Microphone() as source:
                        #    audio=l.listen(source, timeout=4,phrase_time_limit=3)
                        #name="Hello ,what is your name"
                        #nn.save("name.mp3")
                        #playsound("name.mp3")
                        fn=str(stt())
                        fnn=gTTS(text="hello"+fn+"where do you stay",lang='en',slow=False)
                        fnn.save("fnn.mp3")
                        playsound("fnn.mp3")
                        ad1=str(stt())
                        add1=gTTS(text="Your address is"+ad1+"so,what crops do you grow",lang='en',slow=False)
                        add1.save("add1.mp3")
                        playsound("add1.mp3")
                        cro=str(stt())
                        cr1=gTTS(text="you grow"+cro+"how much quantity?",lang='en',slow=False)
                        cr1.save("cr1.mp3")
                        playsound("cr1.mp3")
                        qu=str(stt())
                        qu1=gTTS(text="Okay, you have"+qu+"kgs of"+cro,lang='en',slow=False)
                        qu1.save("qu1.mp3")
                        playsound("qu1.mp3")
                        #fi=gTTS(text="please enter your phone number",lang='en',slow=False)
                        #fi.save("fi.mp3")
                        #playsound("fi.mp3")
                        #ph_no=" "
                        #raw_input(ph_no)
                        #print(ph_no)
                        #pn=stt()
                        pn1=gTTS(text="We have your details saved  will let you know if your crops are ordered, Thank You.",lang='en',slow=False)
                        pn1.save("pn1.mp3")
                        playsound("pn1.mp3")


                        


        except:
                print("error")
smart_agriculture()
