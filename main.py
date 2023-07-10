import io
import requests
import webbrowser
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

class NewsApp:
    def __init__(self):
        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=4b837dbb556047349490079bda448aac').json()

        # initial GUI load
        self.load_gui()

        # load the 1st news
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.title('AP 24/7 News')
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        # clear the screen
        self.clear()


        # placing the image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url ='https://t3.ftcdn.net/jpg/04/62/93/66/360_F_462936689_BpEEcxfgMuYPfTaIAOC1tCDurmsno7Sp.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root, image=photo)
        label.pack()

        # placing the heading
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white',
                        wraplength=350, justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        # Button functions
        if index!=0:
            prev = Button(frame, text='Prev', width=16, height=3,command=lambda:self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3,command=lambda : self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index!=len(self.data['articles'])-1:
            nxt = Button(frame, text='Next', width=16, height=3,command=lambda : self.load_news_item(index+1))
            nxt.pack(side=LEFT)

            # Your name label
            your_name = Label(self.root, text='Created by Anand Prabhat', bg='black', fg='white',
                              font=('verdana', 8), pady=1)
            your_name.place(relx=1.0, rely=1.0, anchor=SE, x=-10, y=-10)



        self.root.mainloop()
    def open_link(self,url):
        webbrowser.open(url)

obj = NewsApp()
