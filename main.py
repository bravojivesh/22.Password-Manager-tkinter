#JH UI: The trick is to use small width and height to begin with, and then keep adding widgets using grid.
# the elements used to position the widgets are relative. Keep this in mind.
# the font size, the width etc. will all change the position and size.
#if the second last row is 3, making the row under 4 or 10 will have the same effect due to the relative nature of the
# grid system.
import random
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

#--------------For generating password------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pword():
    # genrates a list consisting of elements randomly selected from the list "letters".
    # and the no. of elements is a random digit between 8 to 10.
    pword_letters=[random.choice(letters) for _ in range(random.randint(8,10))]
    pword_numbers= [random.choice(letters) for _ in range(random.randint(2,4))]
    pword_symbols=[random.choice(symbols) for _ in range(random.randint(2,4))]

    pword_final_list=pword_numbers+pword_symbols+pword_letters
    #combines the 3 lists

    random.shuffle(pword_final_list)
    #shuffles the combined list

    pword_str="".join(pword_final_list)
    #creates a string for the list joined by "". Which is empty space.
    # print(type(pword_str))

    entry_password.delete(0,tk.END)
    entry_password.insert(0,pword_str)

    pyperclip.copy(pword_str) #copies the password to clipboard

def add_f():
    x=entry_web.get() #storing what is typed in the web entry.
    y=entry_email.get() # stores email entry
    z=entry_password.get() #stores password

    if x =="" or y =="" or z =="":
        messagebox.showinfo(title="ERROR",message="You NEED to fill all the fields!!")

    # elif  x !="" or y!="" or z!="":
    else:
        is_a= messagebox.askokcancel(title="Confirmation",\
                                 message=f"You entered the following:\n Website: {x}\n Email: {y}\n Password: {z}")
    #the variable used (is_a) will automatically store when OK is selected.

        if is_a: #means when OK is selected.
            with open("Results.txt", "a") as results:  # a here means append
                results.write(f" {x} | {y} | {z} \n")  # \n so that the next entry is added in a newline

                entry_web.delete(0, tk.END)  # clear the web entry widget
                entry_password.delete(0, tk.END)  # clear the password entry widget

        else: #when cancel is selected
            pass




#++++++++++++++++++UI PARt++++++++++++++++++++++++++++++++++++
window1=tk.Tk()
window1.title("Password Manager")
window1.config (padx=30, pady=30)

canvas1= tk.Canvas(width=200,height=200)
photo1=tk.PhotoImage(file="logo.png")
canvas1.create_image(125,100,image=photo1,state="normal") #the numbers are x and y
# canvas1.grid(column=2,row=0)
canvas1.grid(column=1,row=0)

website_label=tk.Label(text="Website",font=("Arial", 14))
website_label.grid(column=0,row=1)

email_label=tk.Label(text="Email",font=("Arial", 14))
email_label.grid(column=0,row=2)

password_label=tk.Label(text="Password",font=("Arial", 14))
password_label.grid(column=0,row=3)

entry_web = tk.Entry(width=40, font=("Helvetica", 22))
#width and font size BOTH will change the size and position of the
#the entry
entry_web.grid(column=1,row=1,columnspan=4)
entry_web.focus()

entry_email = tk.Entry(width=40, font=("Helvetica", 22))
entry_email.grid(column=1, row=2,columnspan=4)
entry_email.insert(0, "something@email.com") #this adds some text as a default value

entry_password = tk.Entry(width=30, font=("Helvetica", 22))
entry_password.grid(column=1, row=3)

button1 = tk.Button(text="Generate Password", width=17,font=("Helvetica", 12),fg="Blue",bg="white",command=generate_pword)
button1.grid(column=2, row=3)

button2 = tk.Button(text="Add", width=58,font=("Helvetica", 15),fg="Blue",bg="white",command=add_f)
button2.grid(column=1, row=4,columnspan=5)

window1.mainloop()