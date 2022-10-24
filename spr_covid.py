from tkinter import *
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

def click(self):
    print("all is ok")

url="http://103.247.238.92/webportal/pages/covid19.php"
html = urlopen(url)
bsObj = BeautifulSoup(html.read())

lab_tests=bsObj.body.findAll("div",{"class":"callout bg-success"})
lab_test=lab_tests[0].get_text()


confirme=bsObj.body.findAll("div",{"class":"callout bg-warning"})
confirmed=confirme[0].get_text()


recover=bsObj.body.findAll("div",{"class":"callout bg-success"})
recovered=recover[1].get_text()


death=bsObj.body.findAll("div",{"class":"callout bg-danger"})
deathd=death[0].get_text()



# def hello():
#     print("Button is working")
# def name():
#     print("Md Shamim Hasan")
# def id():
#     print("201936032")



root = Tk()
root.geometry("700x500")
root.configure(bg="dodger blue")
# root.maxsize(600,425)
root.title('Simple Work')
# C = Canvas(root, bg="blue", height=250, width=300)
# root.configure(background="Black")

canvas = Canvas(
    root,
    bg="#dddddd",
    height=500,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

canvas.create_rectangle(
    0, 0, 0 + 330, 0 + 500,
    fill="dodger blue",
    outline="")

canvas.create_text(
    165.0, 235.5,
    text="Hey!\n“Be safe, be smart, be kind”\n\nHope you find it useful!\nThank you.",
    fill="#dddddd",
    font=("Montserrat-MediumItalic", int(14.0)))



canvas.create_rectangle(
    330, 0,700,500,
    fill="gray99",
    outline="")

sv = StringVar()


#command=lambda:[funcA(), funcB(), funcC()]

Current_Date_Formatted = datetime.datetime.today().strftime ('%d-%b-%Y')
datee=str(Current_Date_Formatted)
sv.set(f"{datee}")

f2 = Frame(root, bg='gray99', borderwidth=2)
f2.place(x=330, y=0, width=370,
         height=70)
p = Label(f2, text=f'COVID-19 in Bangladesh', font=('Helvetica', 20, 'bold'), fg='Black', bg='gray99')
p.pack(side=TOP)
datt = Label(f2, textvariable=sv, font=('Helvetica', 10), fg='Black', bg='gray99')
datt.pack(side=TOP)


f8 = Frame(canvas, bg='gray99', relief=SUNKEN)
f8.place(x=330, y=70,
         width=370,
         height=430)

scv1 = StringVar()
scv1.set(f"{lab_test}")

scv2 = StringVar()
scv2.set(f"{confirmed}")

scv3 = StringVar()
scv3.set(f"{recovered}")

scv4 = StringVar()
scv4.set(f"{deathd}")

daily_cases = Label(f8, textvariable=scv1, font=('Helvetica', 15, 'bold'), fg='dodger blue', bg='gray99')
daily_cases.pack()

daily_confirmed = Label(f8, textvariable=scv2, font=('Helvetica', 15, 'bold'), fg='Orange', bg='gray99')
daily_confirmed.pack()

daily_recovered= Label(f8, textvariable=scv3, font=('Helvetica', 15, 'bold'), fg='Green', bg='gray99')
daily_recovered.pack()

daily_death= Label(f8, textvariable=scv4, font=('Helvetica', 15, 'bold'), fg='Red', bg='gray99')
daily_death.pack()

# # f8.pack_propagate(0)
# # scb=Scrollbar(f8)
# scb.pack(fill=Y,side=RIGHT)
# mnb = Menu(root)
# m4 = Menu(mnb, tearoff=0)
# m4.add_command(label='Print', command=hello())
# mnb.add_cascade(label='File', menu=m4)
# root.config(menu=mnb)
mnb = Menu(root)
m4 = Menu(mnb, tearoff=0)
m4.add_command(label='Print', command=click)
m4.add_command(label='About', command=click)
m4.add_command(label='Feedback', command=click)
mnb.add_cascade(label='File', menu=m4)
root.config(menu=mnb)


root.resizable(False, False)
root.mainloop()
