import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser 
from gtts import gTTS
from playsound import playsound
url = 'http://docs.python.org/' 
 # Windows 
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 



webbrowser.get(chrome_path).open(url)
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices' )
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    tts = gTTS(audio,lang='tr')
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")
    
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Günaydın")

    elif hour>=12 and hour<18:
        print("İyi Günler")   

    else:
        speak("İyi Akşamlar!")  

    print("ben senin sesli asistanınım. Sana nasıl yardımcı olabilirim")       

def takeCommand():
    #kullanıcıdan mikrofon girdisini alır ve dizi çıktısını döndürür

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinleniyor...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Tanınan ...")    
        query = r.recognize_google(audio, language='tr-TR')
        print(f"Kullanıcı dedi: {query}\n")

    except Exception as e:
        print(e)    
        print("Tekrarlar mısınız...")  
        return "Boş"
    return query

# def sendEmail(to, content):
   # server = smtplib.SMTP('smtp.gmail.com', 587)
  #  server.ehlo()
  #  server.starttls()
   # server.login('youremail@gmail.com', 'your-password')
  #  server.sendmail('youremail@gmail.com', to, content)
  #  server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Sorguya dayalı görevleri yürütmek için mantık
        if 'wikipedia' in query:
            speak('Wikipedia aranıyor ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Wikipedia'ya göre")
            print(results)
            speak(results)
        elif 'nasılsın' in query:
            speak("İyi sen nasılsın ?")
        elif 'araştır' in query:
            kelimeler = query.split()
            endeks= kelimeler.index("araştır")
            aras=""
            i=endeks + 1
            while i<len(kelimeler):
                aras+=" "+kelimeler[i]
                i +=1
                print("sorgu= ",aras)
                webbrowser.open(f"https://www.google.com/search?q='{aras}'")
        elif 'youtube aç' in query:
            speak("Youtube açılıyor")
        elif 'tekerleme söyle' in query:
            speak("Bir berber bir berbere bre berber beri gel diye bar bar bağırmış.")
           
        elif 'instagram aç' in query:
             webbrowser.open("https://www.instagram.com/?hl=tr")

        elif 'google aç' in query:
            webbrowser.open("https://www.google.com/") 
        
                
        elif 'kapat' in query:
            speak("Hoşcakalın...")
            quit() 


        elif 'müzik aç' in query:
            webbrowser.open("https://www.youtube.com/watch?v=qAX_O2e3hx4&list=PL4fGSI1pDJn4Jw_bpjwRlIvxkW80YYEBJ")

        elif 'saat kaç' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Zaman :{strTime}")

        