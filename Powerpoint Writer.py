from pptx import Presentation
from pptx.util import Inches
import wikipedia
import os
import urllib.request
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title('Azure')

window_height = 530
window_width = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

style = ttk.Style(root)
root.tk.call('source', 'azure dark.tcl')
style.theme_use('azure')

button = Button(root, text="DELET", command=root.destroy)

button.pack()

root.mainloop()

prs = Presentation()
blank_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(blank_slide_layout)

title = slide.shapes.title

subtitle = slide.placeholders[1]

title.text = input("What do you want the title to be?")
subtitle.text = input("The subtitle?")

Second_layout = prs.slide_layouts[1]
slide2 = prs.slides.add_slide(Second_layout)

title2 = slide2.shapes.title
Content = slide2.placeholders[1]

title2.text = input("Aight, what will be the title of the next slide?")
Topic = input("What should be the topic be?")
Sentences = int(input("How many sentences should the summary be?"))
try:
    Content.text = wikipedia.summary(Topic, sentences=Sentences)

except wikipedia.exceptions.DisambiguationError as e:
    print("Hmm... There are more than one topics about this topic. Perhaps try being more specific? Or this topic may "
          "not exist")

Third_layout = prs.slide_layouts[6]
slide3 = prs.slides.add_slide(Third_layout)

left = top = Inches(1)

wikipage = wikipedia.page(Topic)
Imgurl = wikipage.images[0]

try:
    print(Imgurl)
    Name = random.randint(100000, 1230299999)
    path = input(
        "Give me a path to download all your imgages. Remember use '/' as the separator and add a '/' at the end of "
        "the path.\n For Example, C:/Test/yourdir/ ")
    urllib.request.urlretrieve(Imgurl, path + str(Name) + ".jpg")
    pic = slide3.shapes.add_picture(path + str(Name) + ".jpg", left, top)

except Exception as e:
    print(
        "Sorry, mate. But there is no wikipedia image for the topic you're searching for. Try inserting one manually.")

Fourth_layout = prs.slide_layouts[1]
slide4 = prs.slides.add_slide(Fourth_layout)

title4 = slide4.shapes.title
Content4 = slide4.placeholders[1]

title4.text = input("Aight, what will be the title of the next slide?")
Topic = input("What should be the topic be?")
Sentences = int(input("How many sentences should the summary be?"))
try:
    Content4.text = wikipedia.summary(Topic, sentences=Sentences)

except wikipedia.exceptions.DisambiguationError as e:
    print("Hmm... There are more than one topics about this topic. Perhaps try being more specific? Or this topic may "
          "not exist")



root = tk.Tk()
root.title('Azure')

window_height = 530
window_width = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

style = ttk.Style(root)
root.tk.call('source', 'azure dark.tcl')
style.theme_use('azure')

button = Button(root, text="DELET", command=root.destroy)

button.pack()

root.mainloop()

prs.save('Englishact.ppt')
os.startfile('Englishact.ppt')
