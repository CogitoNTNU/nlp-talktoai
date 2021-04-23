import tkinter
from tkinter import *
#from chatbot2 import customConversation
from chatbot2 import *

n = True

def send():
    global n 
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        if n:
            n = False
            res = firstConversation(msg)
            print(res)
        else:
            res = nextConversation(msg)    

        ChatLog.insert(END, "Bot: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 

base = Tk()
base.title("Hello")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()


# window = Tk()

# window.title("Chat Bot")
# window.geometry("400x500")
# window.resizable(width=False, height=False)

# main_menu = Menu(window)

# # Create the submenu 
# file_menu = Menu(window)

# # Add commands to submenu
# file_menu.add_command(label="New..")
# file_menu.add_command(label="Save As..")
# file_menu.add_command(label="Exit")
# main_menu.add_cascade(label="File", menu=file_menu)
# #Add the rest of the menu options to the main menu
# main_menu.add_command(label="Edit")
# main_menu.add_command(label="Quit")
# window.config(menu=main_menu)

# chatWindow = Text(window, bd=1, bg="gray",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
# chatWindow.place(x=6,y=6, height=385, width=370)

# messageWindow = Text(window, bd=0, bg="gray",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
# messageWindow.place(x=128, y=400, height=88, width=260)

# scrollbar = Scrollbar(window, command=chatWindow.yview, cursor="star")
# scrollbar.place(x=375,y=5, height=385)

# Button= Button(window, text="Send",  width="12", height=5,
#                     bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
# Button.place(x=6, y=400, height=88)

# def send():
#     text = text_box.get("0.0", tk.END)
#     text = text[:-1]
#     prev_length = len(text)


#window.mainloop()
# first = True
# text = ""
# window = tk.Tk()
# text_box = tk.Text()
# text_box.pack()
# text_box.insert("1.0", text)

# def onclick():
#     text = text_box.get("0.0", tk.END)
#     text = text[:-1]
#     prev_length = len(text)
#     new_text = customConversation(text,first)
#     print(new_text[prev_length: ])
#     text_box.delete("0.0", tk.END)
#     text_box.insert("0.0", new_text)

# button = tk.Button(window, text="Send", command=onclick)
# first = False
# button.pack()
# window.mainloop()
