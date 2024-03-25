from customtkinter import *
import os
from tkinter import messagebox as msg
import threading
from Like_comment import likecomment
from PIL import Image
import sys

stop_flag = threading.Event()
def Logout():
    stop_function()
    os.remove("x_eca_234")
    gui.destroy()
    login()
def start_function():
    # Retrieve inputs from GUI
    hashtag = hashtag_entry.get()
    number_of_post = int(number_of_post_entry.get())

    # Reset the stop flag
    stop_flag.clear()

    # Run the function in a separate thread
    threading.Thread(target=work, args=(hashtag, number_of_post)).start()

def stop_function():
    # Set the stop flag to stop the function
    quit(start_function)
    stop_flag.set()
    sys.exit()

def work(hashtag,numberofpost):
    usernamelis = (get_user_pass()[0])
    passwordlis = (get_user_pass()[1])
    for i in range(len(usernamelis)):
        if stop_flag.is_set():  # Check if the stop flag is set
            break
        likecomment(usernamelis[i],passwordlis[i],hashtag,numberofpost)

def get_user_pass():
    if not os.path.exists("x_eca_234"):
        username = usernameentry.get()
        password = passwordentry.get()
    else:
        with open("x_eca_234",'r') as f:
            info = f.read()
            username = info.splitlines()[0]
            password = info.splitlines()[1]
            f.close()
    return username.split() , password.split()

def on_closing():
    quit(start_function)
    stop_flag.set()  # Set the stop flag to stop the function
    gui.destroy()
    sys.exit()  # Exit the Python script

def GUI():
    global gui,hashtag_entry,number_of_post_entry
    username = (get_user_pass()[0])
    password = (get_user_pass()[1])
    if len(username) != len(password):
        msg.showerror("Login Error","Number of USERNAMES are not equal to Number of PASSWORDS !!!")
        os.remove("x_eca_234")

        return login()

    try:
        if login_save.get() == 1:
            with open("x_eca_234","w") as f:
                f.write(f"{usernameentry.get()}\n{passwordentry.get()}")
                f.close()
        root.destroy()
    except:
        pass
    gui = CTk()
    gui.geometry()
    gui.minsize(400, 600)
    gui.maxsize(400, 600)
    gui.title("InstaBot")
    image_path = "instaa.png"
    image = CTkImage(light_image=Image.open(image_path),size=(250,250))
    CTkLabel(gui,image=image,text="").grid(row=0,column=0,columnspan=2,padx=25,pady=10)

    hashtag_entry = CTkEntry(gui,placeholder_text="#Hashtag",width=350,height=50,font=("arial",20))
    hashtag_entry.grid(row=1,column=0,columnspan=2,padx=25,pady=10)
    number_of_post_entry = CTkEntry(gui, placeholder_text="Post Number", width=175, height=50,
                             font=("arial", 15))
    number_of_post_entry.grid(row=2, column=0, padx=12.5,pady=10)
    start = CTkButton(gui,text="START",hover_color="lime",height=50,command=start_function)
    start.grid(row=2, column=1, padx=12.5,pady=10)
    logout = CTkButton(gui, text="LogOut", hover_color="red", height=30,command=Logout)
    logout.grid(row=8, column=1,pady=140)
    stop = CTkButton(gui, text="STOP", hover_color="red", height=30, command=stop_function)
    stop.grid(row=8, column=0, pady=140)
    gui.protocol("WM_DELETE_WINDOW", on_closing)
    gui.mainloop()
def login():
    global login_save, root, usernameentry, passwordentry
    root =CTk()
    root.geometry()
    root.minsize(500,200)
    root.maxsize(500,200)
    root.title("InstaBot Login")
    usernameentry=CTkEntry(root,width=400,height=30,placeholder_text="Username1 Username2 Username3 ....")
    usernameentry.grid(row=0,column=0,padx=40,pady=10)
    passwordentry=CTkEntry(root,width=400,height=30,placeholder_text="Password1 Password2 Password3 ....")
    passwordentry.grid(row=1,column=0,padx=40)
    CTkButton(root,text="Login",command=GUI).grid(padx=30,pady=15)
    login_save = CTkCheckBox(root, text="Save Info")
    login_save.grid()
    root.mainloop()

if __name__ == '__main__':
    if not os.path.exists("x_eca_234"):
        login()
    else:
        GUI()