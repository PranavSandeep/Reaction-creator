import tkinter as tk
from tkinter import ttk
from pptx import Presentation
from tkinter import *
from pptx.util import Inches
import wikipedia
import os

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.prs = Presentation()
        style = ttk.Style(self)
        self.tk.call('source', 'azure dark.tcl')
        style.theme_use('azure')
        self.VarList = StringVar(self)
        self.VarList.set("Normal")
        self.SlideType = ["Normal", "Wikipedia"]
        self.SlideBox = OptionMenu(self, self.VarList, *self.SlideType)
        self.Title = tk.Entry(self)
        self.Subtitle = tk.Entry(self)
        self.Topic = tk.Entry(self)
        self.Sentences = tk.Entry(self)
        self.button = tk.Button(self, text="Get", command=self.CreatePPT)
        self.SlideBox.pack()
        self.button.pack()
        self.Title.pack()
        self.Subtitle.pack()
        self.Topic.pack()
        self.Sentences.pack()
        self.button2 = tk.Button(self, text="Search the web for info", command=self.SearchTheWeb)
        self.button2.pack()

    def CreatePPT(self):

        if self.VarList.get() == "Normal":
            blank_slide_layout = self.prs.slide_layouts[0]
            slide = self.prs.slides.add_slide(blank_slide_layout)

            title = slide.shapes.title

            subtitle = slide.placeholders[1]

            title.text = self.Title.get()
            subtitle.text = self.Subtitle.get()

            self.prs.save('Englishact.ppt')
            os.startfile('Englishact.ppt')

        elif self.VarList.get() == "Wikipedia":
            Fourth_layout = self.prs.slide_layouts[1]
            slide4 = self.prs.slides.add_slide(Fourth_layout)

            title4 = slide4.shapes.title
            Content4 = slide4.placeholders[1]

            title4.text = self.Title.get()
            Topic = self.Topic.get()
            Sentences = int(self.Sentences.get())
            try:
                Content4.text = wikipedia.summary(Topic, sentences=Sentences)

            except wikipedia.exceptions.DisambiguationError as e:
                print(
                    "Hmm... There are more than one topics about this topic. Perhaps try being more specific? Or this topic may "
                    "not exist")

            self.prs.save('Englishact.ppt')
            os.startfile('Englishact.ppt')



    def SearchTheWeb(self):
        Fourth_layout = self.prs.slide_layouts[1]
        slide4 = self.prs.slides.add_slide(Fourth_layout)

        title4 = slide4.shapes.title
        Content4 = slide4.placeholders[1]

        title4.text = self.Title.get()
        Topic = self.Topic.get()
        Sentences = int(self.Sentences.get())
        try:
            Content4.text = wikipedia.summary(Topic, sentences=Sentences)

        except wikipedia.exceptions.DisambiguationError as e:
            print(
                "Hmm... There are more than one topics about this topic. Perhaps try being more specific? Or this topic may "
                "not exist")

        self.prs.save('Englishact.ppt')
        os.startfile('Englishact.ppt')


app = SampleApp()
app.mainloop()


