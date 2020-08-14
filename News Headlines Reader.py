import requests
import json

def speak(str):
    from win32com.client import Dispatch
    a=Dispatch("SAPI.spVoice")
    a.Speak(str)

if __name__== '__main__':
    
    speak("here are today's news headlines")
    
    url = ("http://newsapi.org/v2/top-headlines?country=in&apiKey=734baa9fe3874c84826eafc185a06be4")

    my_request = requests.get(url).text
    my_json = json.loads(my_request)
     
    
    for i in range(1, 11):
        print(f"news number {i} :: "+ my_json['articles'][i-1]['title'])
        speak(f"news number {i}")
        speak(my_json['articles'][i-1]['title'])
    
    speak("thank you for listening")
        
    