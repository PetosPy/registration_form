from tkinter import *
import json

FOREGROUND = "#151515"
BACKGROUND = "#e4efe7"
FONT=("helvetica", 15, "bold")

window = Tk()
window.title("Data Form")
window.geometry("800x800")



my_frame = Frame(bg=BACKGROUND)
my_frame.place(relwidth=1, relheight=1)

heading_label = Label(my_frame, text="REGISTRATION FORM", fg=FOREGROUND, bg=BACKGROUND, font=("times roman", 20, "underline"))
heading_label.place(x=220, y=20)


name_label = Label(my_frame,text="Name:", fg=FOREGROUND, bg=BACKGROUND, font=FONT)
name_label.place(x=50, y=100)
name_entry = Entry(width=25)
name_entry.place(x=200, y=105)

surname_label = Label(my_frame,text="Surname:", fg=FOREGROUND, bg=BACKGROUND, font=FONT)
surname_label.place(x=50, y=180)
surname_entry = Entry(width=25)
surname_entry.place(x=200, y=185)

DOB_label = Label(my_frame,text="D.O.B:", fg=FOREGROUND, bg=BACKGROUND, font=FONT)
DOB_label.place(x=50, y=260)
DOB_entry = Entry(width=25)
DOB_entry.place(x=200, y=265)

email_label = Label(my_frame,text="Email:", fg=FOREGROUND, bg=BACKGROUND, font=FONT)
email_label.place(x=50, y=340)
email_entry = Entry(width=25)
email_entry.place(x=200, y=345)

gender_label = Label(my_frame,text="Gender:", fg=FOREGROUND, bg=BACKGROUND, font=FONT)
gender_label.place(x=50, y=420)
male = Radiobutton(text="Male", value=1, bg=BACKGROUND, font=('Ariel', 12, 'bold'))
male.place(x=200, y=425)
female = Radiobutton(text="Female", value=2,bg=BACKGROUND, font=('Ariel', 12, 'bold'))
female.place(x=350, y=425)


country_label = Label(my_frame,text="Country:", fg=FOREGROUND, bg=BACKGROUND, font=FONT)
country_label.place(x=50, y=500)
#country_entry = Entry()

submit_button = Button(text="Submit", width=50,height=2, font=("helvetica", 10, "bold"), bg="#ffcc29", fg=FOREGROUND)
submit_button.place(x=200, y=640)

# -------- json data ---------
# Pulling data from json file to create a dropdown list for country names.
with open("countries.json","r") as data_file:
	contents = json.load(data_file)
	new_list = [x["name"] for x in contents]

print(new_list)

variable = StringVar(my_frame)
variable.set("select") # default value
country_option= OptionMenu(my_frame, variable, new_list)
country_option.config(width=25)
country_option.place(x=200, y=500)






window.mainloop()
