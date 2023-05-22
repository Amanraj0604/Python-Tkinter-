import tkinter as tk
import requests
import math
from PIL import Image,ImageTk 
root=tk.Tk()
root.title("Weather App")
root.geometry("600x500")

def format_response(weather):
    
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        ce=(temp-32)*5/9
        final_str='city:%s\ncondition:%s\nTemprature:%s C'%(city,condition,math.ceil(ce))
    except:
        final_str='There Was a problem rieving that information'
    return final_str
def get_weather(city):
    weather_key='474353fb51318c27c69d17f42f2fb9de'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    # print(response.json())
    weather=response.json()

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp']) 

    result['text']=format_response(weather)

   

img=Image.open(r'F:\1st Sem\python obb\wether1\Wether-Prediction\bg3.jpg')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

#key:474353fb51318c27c69d17f42f2fb9de
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}


heading_tital=tk.Label(bg_lbl,text='Earth including over 200,000 cities!',fg='red',font=('time new roman',18,'bold'))
heading_tital.place(x=80,y=18)  

frame_one=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('times new Roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='w')

btn=tk.Button(frame_one,text='get weather',fg='green',font=('time new Roman',16,'bold'),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10 )

frame_two=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,bg='white',justify='left',anchor='nw',font=('time new Roman',16,'bold'))
result.place(relwidth=1,relheight=1)

root.mainloop()