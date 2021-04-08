from tkinter import *
from model_generate import *

def button_click():
    output.delete('1.0', END)
    user_theme_sentence = user_input.get()
    user_input.delete(0, 'end')
    blog_post = return_blog_post(user_theme_sentence)
    output.insert(INSERT, blog_post)


win = Tk(className = " GPT2 Blog Post Generator")
win.geometry("600x600")

prompt_label = Label(win, text="Write something about a specific theme, and GPT2 will do it's magic: ")
prompt_label.config(font = ("Courier", 10))
user_input = Entry(win, width=80)

button = Button(win,text = "Enter", command = button_click)

output_label = Label(win, text="Blog post")
output_label.config(font = ("Courier", 10))
output = Text(win, font = ("Courier", 10))

prompt_label.pack()
user_input.pack()
button.pack()
output_label.pack()
output.pack()

#runs until exit is pressed
mainloop()

