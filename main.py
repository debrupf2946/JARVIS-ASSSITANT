import speech_recognition as sr
import os
import webbrowser
import datetime
import openai
from config import apikey
import random
chatstr=""

def chat(query):
    global chatstr
    openai.api_key = apikey
    chatstr+=f"debrup:{query}\nJarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response['choices'][0]['text'])
    chatstr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']



def ai(prompt):


    openai.api_key = apikey
    text = f"open ai response for prompt {prompt} \n********************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this under try catch
    print(response['choices'][0]['text'])
    text+=response['choices'][0]['text']
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"prompt-{random.randint(1,2334354545455)}","w")  as f:
        f.write(text)

def say(text):
    os.system(f"say {text}")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            query=query.lower()
            print(f"User said {query}")
            return query
        except Exception as e:
            return " sorry can you say again"




if __name__ == '__main__':
    print('PyCharm')
    say(" Hello i am jarvis A.I")

    while True:
        print("Listening.....")
        query = takeCommand()
        chat(query)

        sites=[["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f" Opening {site[0]} sir....")
                webbrowser.open(site[1])
        #if "open music" in query.lower:
           # musicPath="type the path"
           # os.system(f"open {musicPath}")

        if "facetime".lower() in query.lower():

            os.system(f"open /System/Application/FaceTime.app")

        if "time" in query :
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir the time is {strfTime}")

        if "Hello".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)





        #query=" "+query
       # say(query)

