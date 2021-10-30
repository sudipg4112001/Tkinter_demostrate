def library():
    kroot = Toplevel(master=dataframe)
    kroot.grab_set()
    kroot.title('library')
    kroot.geometry('200x100+880+500')
    kroot.resizable(False, False)
    infobutton=Button(kroot,text='information',width=20)
    infobutton.pack(side=TOP,expand=True)
    kroot.mainloop()
###########################################################################
def healcontact():
    proot = Toplevel(master=dataframe)
    proot.grab_set()
    proot.title('contact')
    proot.geometry('200x100+880+500')
    proot.resizable(False, False)
    ambubutton = Button(proot, text='AMBULANCE', width=20)
    ambubutton.pack(side=TOP, expand=True)
    medbutton=Button(proot,text='MEDICINE',width=20)
    medbutton.pack(side=TOP,expand=True)
    proot.mainloop()





###################################################
def bookbuy():
    mroot=Toplevel()
    mroot.grab_set()
    mroot.title('bookbuy')
    mroot.geometry('200x100+880+500')
    mroot.resizable(False,False)
    databasebutton=Button(mroot, text='database', width=20)
    databasebutton.pack(side=TOP,expand=True)
    mroot.mainloop()
def booksell():
    sroot = Toplevel()
    sroot.grab_set()
    sroot.title('booksell')
    sroot.geometry('600x250+600+200')
    sroot.resizable(False, False)
    #####################################################labels
    selllabel=Label(sroot,text='bookname:',width=20)
    selllabel.place(x=10,y=10)
    pricelabel = Label(sroot, text='price:', width=20)
    pricelabel.place(x=10, y=60)
    contactlabel = Label(sroot, text='contact:', width=20)
    contactlabel.place(x=10, y=120)
    ################################################################entry
    nentry=Entry(sroot,font=('roman','30','bold'),bd=5,textvariable=StringVar)
    nentry.place(x=150,y=10)
    nentry = Entry(sroot, font=('roman', '30', 'bold'), bd=5, textvariable=StringVar)
    nentry.place(x=150, y=60)
    nentry = Entry(sroot, font=('roman', '30', 'bold'), bd=5, textvariable=StringVar)
    nentry.place(x=150, y=120)
#########################################################################submitbutton
    subbutton=Button(sroot,text='submit',width=20)
    subbutton.place(x=250,y=200)
    sroot.mainloop()
####################################################################################################################
def books():
    zroot = Toplevel()
    zroot.grab_set()
    zroot.title('book')
    zroot.geometry('600x250+600+200')
    zroot.resizable(False, False)
    ##################################################################################333
    bookbuybutton = Button(zroot, text='BOOK BUY', width=20, command=bookbuy)
    bookbuybutton.pack(side=TOP, expand=True)
    booksellbutton = Button(zroot, text='BOOK SELL', width=20, command=booksell)
    booksellbutton.pack(side=TOP, expand=True)
##############################################################################################
    zroot.mainloop()





##################################################################################################
def acedemic():
    sdroot = Toplevel()
    sdroot.grab_set()
    sdroot.title('acedemic')
    sdroot.geometry('200x200+880+200')
    sdroot.resizable(False, False)
    ########################################################3question
    queslabel=Label(sdroot,text='Choose an Option',width=25)
    queslabel.place(x=10,y=10)
    #########################################################buttonsforbook
    libbutton = Button(sdroot, text='LIBRARY', width=20,command=library)
    libbutton.pack(side=TOP, expand=True)
    stationarybutton = Button(sdroot, text='Stationary', width=20,command=books)
    stationarybutton.pack(side=TOP, expand=True)
    ebookbutton = Button(sdroot, text='E-BOOK', width=20)
    ebookbutton.pack(side=TOP, expand=True)
    quesbutton = Button(sdroot, text='Question Paper', width=20)
    quesbutton.pack(side=TOP, expand=True)
    notesbutton = Button(sdroot, text='Notes', width=20)
    notesbutton.pack(side=TOP, expand=True)




    sdroot.mainloop()
##############################################################################################################333
def messinfo():
    aroot = Toplevel()
    aroot.grab_set()
    aroot.title('mess')
    aroot.geometry('600x250+600+200')
    aroot.resizable(False, False)
    #####################################################labels
    loclabel = Label(aroot, text='Location:', width=20)
    loclabel.place(x=10, y=10)
    conlabel = Label(aroot, text='condition+price:', width=20)
    conlabel.place(x=10, y=60)
    contactlabel = Label(aroot, text='contact:', width=20)
    contactlabel.place(x=10, y=120)
    ################################################################entry
    nentry = Entry(aroot, font=('roman', '30', 'bold'), bd=5, textvariable=StringVar)
    nentry.place(x=150, y=10)
    nentry = Entry(aroot, font=('roman', '30', 'bold'), bd=5, textvariable=StringVar)
    nentry.place(x=150, y=60)
    nentry = Entry(aroot, font=('roman', '30', 'bold'), bd=5, textvariable=StringVar)
    nentry.place(x=150, y=120)
    #########################################################################submitbutton
    subbutton = Button(aroot, text='submit', width=20)
    subbutton.place(x=250, y=200)
    aroot.mainloop()


################################################################################################

def canteen():
    print("database")

def helpdesk():
    qroot = Toplevel()
    qroot.grab_set()
    qroot.title('helpdesk')
    qroot.geometry('200x200+880+200')
    qroot.resizable(False, False)

    #########################################################buttonsforbook
    acabutton = Button(qroot, text='ACEDEMIC', width=20)
    acabutton.pack(side=TOP, expand=True)
    nonacabutton = Button(qroot, text='NON-ACEDEMIC', width=20)
    nonacabutton.pack(side=TOP, expand=True)
    sqbutton = Button(qroot, text='SHOW QUERIES', width=20)
    sqbutton.pack(side=TOP, expand=True)
    guidebutton = Button(qroot, text='ABOUT', width=20)
    guidebutton.pack(side=TOP, expand=True)
    qroot.mainloop()


def healthcare():
    droot = Toplevel()
    droot.grab_set()
    droot.title('healthcare')
    droot.geometry('200x200+880+200')
    droot.resizable(False, False)
    ########################################################3question
    quelabel = Label(droot, text='Choose an Option', width=25)
    quelabel.place(x=10, y=10)
    #########################################################buttonsforbook
    availbutton = Button(droot, text='Available Slots', width=20)
    availbutton.pack(side=TOP, expand=True)
    contactbutton = Button(droot, text='contact', width=20,command=healcontact)
    contactbutton.pack(side=TOP, expand=True)
##################################################################3
    droot.mainloop()

def notice():
    print("success notice")

def exit():
    res=messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res==True):
        root.destroy()
#################################################################################
def connectdb():
    dbroot= Toplevel()
    dbroot.grab_set()
    dbroot.title('booking')
    dbroot.geometry('500x200+780+200')
    dbroot.resizable(False,False)
    #########################################box label
    headerlabel=Label(dbroot,text='Choose an option',width=20,anchor='c')
    headerlabel.place(x=200,y=50)
    #########################################button
    canbutton=Button(dbroot,text='CANTEEN',width=20)
    canbutton.place(x=200,y=130)

    hosbutton = Button(dbroot, text='HOSPITAL SLOT', width=20)
    hosbutton.place(x=200, y=170)
    dbroot.mainloop()







############################################################################
from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
import pyttsx3

root = Tk()
root.title('college system')
root.configure(bg='cyan3')
root.geometry('1107x700+200+50')
root.resizable(False,False)
####################################################################frame
dataframe=Frame(root,bg='white',relief=GROOVE,borderwidth=2)
dataframe.place(x=10,y=100,width=500,height=550)
#####################################################################frame1button
accedemicdata=Button(dataframe,text='acedemic ',width=25,command=acedemic)
accedemicdata.pack(side=TOP,expand=True)

messdata=Button(dataframe,text='mess',width=25,command=messinfo)
messdata.pack(side=TOP,expand=True)

canteen=Button(dataframe,text='canteen',width=25,command=canteen)
canteen.pack(side=TOP,expand=True)

helpdesk=Button(dataframe,text='helpdesk',width=25,command=helpdesk)
helpdesk.pack(side=TOP,expand=True)

healthcare=Button(dataframe,text='healthcare',width=25,command=healthcare)
healthcare.pack(side=TOP,expand=True)

notice=Button(dataframe,text='notice',width=25,command=notice)
notice.pack(side=TOP,expand=True)

exit=Button(dataframe,text='exit',width=25,command=exit)
exit.pack(side=TOP,expand=True)








######################################################################secondframe
showframe=Frame(root,bg='white',relief=GROOVE,borderwidth=2)
showframe.place(x=550,y=100,width=550,height=550)
######################################################################heading









######################################################################################33
titlelabel=Label(root,text='COLLEGE SYSTEM',font=('arial',30,'bold'), relief=GROOVE,borderwidth=2,bg='white')
titlelabel.place(x=400,y=10)


fr=pyttsx3.init()
fr.say("welcome to my B C R E C  ")
fr.runAndWait()
########################################################################connectdatabase
connectbutton=Button(root,text='Booking',width=23,height=3,command=connectdb)
connectbutton.place(x=900,y=10)


root.mainloop()


