from Tkinter import*
import csv,coll,roll,all_
class home:
    def __init__(self,qq):
        self.home=qq
        self.d=qq
        self.photo1 = PhotoImage(file="0001.gif")
        self.a=Label(self.d,image=self.photo1)
        self.a.place(x=0,y=0)
        self.photo = PhotoImage(file="00003.gif")
        self.photo2 = PhotoImage(file="00002.gif")
        self.photo3 = PhotoImage(file="00001.gif") 
        #self.d=Canvas(self.home, bg="blue", height=250, width=300)place(relx=1, x=-2, y=2, anchor=NE)
        self.b11=Button(self.d,command= self.call)#text="get all unverified",width=30,height=1,command= self.call )
        self.b11.config(image=self.photo)
        self.b11.place(x=100,y=25)
        self.b2=Button(self.d,image= self.photo2,command= self.caall)#,text="get all unverified of a college",width=30,height=1,command= self.caall)
        self.b3=Button(self.d,image= self.photo3,command= self.caaall)#,text="verify a singel student",width=30,height=1,command= self.caaall)
        #self.b11.place(x=100,y=25)
        self.b2.place(x=100,y=120)
        self.b3.place(x=100,y=215)
    def destrohy(self):
        self.check1q.destroy()
    def call(self):
        app = al()
    def caall(self):
        coll2()
    def caaall(self):
        coll3()
    def usercall(self):
        qt=Toplevel()
        app=login(qt)
        qt.mainloop()
    def hellp(self):
        
        app=Help()

class coll2():
    def __init__(self):
        self.d1=Tk()
        self.d1.geometry('150x120+10+50')
        self.l0= Label(self.d1,text="ENTER COLLEGE NAME")
        self.l0.pack()
        self.e01= Entry(self.d1)
        self.e01.pack()
        #print "ffffffffffffff",e01
        self.b00= Button(self.d1,width=17,height=1,text='Verify',command=self.get)
        self.b00.pack()
        self.d1.mainloop()
    def get(self):
        tej= self.e01.get()
        self.d1.destroy()
        #al_(self.e01.get())
        l1=[]
        tem=coll.coll(tej)
        #print tem
        for i in tem.split('\n'):
            l1.append(i.split(','))
        root = Tk()
        root.geometry('1000x300+10+50')
        # only the column containing the text is resized when the window size changes:
        root.columnconfigure(0, weight=1) 
        # resize row 0 height when the window is resized
        root.rowconfigure(0, weight=1)

        txt = Text(root)
        txt.grid(row=0, column=0, sticky="eswn")

        scroll_y = Scrollbar(root, orient="vertical", command=txt.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        # bind txt to scrollbar
        txt.configure(yscrollcommand=scroll_y.set)
        s=""+str('-'*122)+"\n"
        for i1 in l1:
            s+="|"
            for j in i1:
                #print i1,j
                s+=j+"|"
            s+='\n'
            #print s
        print"fvdfvf"
        very_long_list = s
        #very_long_list = "\n".join([str(i) for i in range(100)])
        #print very_long_list.split("\n")
        
        print"266"
        txt.insert("1.0", very_long_list)
        # make the text look like a label
        txt.configure(state="disabled", relief="flat", bg=root.cget("bg"))
        print"done"
        root.mainloop()
class coll3():
    def __init__(self):
        self.v=Tk()
        self.v.geometry('150x120+10+50')
        self.l0= Label(self.v,text="ENTER COLLEGE NAME")
        self.l0.pack()
        self.e011= Entry(self.v)
        self.e011.pack()
        #print "ffffffffffffff",e01
        self.b00= Button(self.v,width=17,height=1,text='Verify',command=self.get)
        self.b00.pack()
        self.v.mainloop()
    def get(self):
        tej= self.e011.get()
        self.v.destroy()
        #al_(self.e01.get())
        l1=[]
        tem=roll.roll(tej)
        #print tem
        for i in tem.split('\n'):
            l1.append(i.split(','))
        root = Tk()
        root.geometry('1000x300+10+50')
        # only the column containing the text is resized when the window size changes:
        root.columnconfigure(0, weight=1) 
        # resize row 0 height when the window is resized
        root.rowconfigure(0, weight=1)

        txt = Text(root)
        txt.grid(row=0, column=0, sticky="eswn")

        scroll_y = Scrollbar(root, orient="vertical", command=txt.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        # bind txt to scrollbar
        txt.configure(yscrollcommand=scroll_y.set)
        s=""+str('-'*122)+"\n"
        for i1 in l1:
            s+="|"
            for j in i1:
                #print i1,j
                s+=j+"|"
            s+='\n'
            #print s
        print"fvdfvf"
        very_long_list = s
        #very_long_list = "\n".join([str(i) for i in range(100)])
        #print very_long_list.split("\n")
        
        print"266"
        txt.insert("1.0", very_long_list)
        # make the text look like a label
        txt.configure(state="disabled", relief="flat", bg=root.cget("bg"))
        print"done"
        root.mainloop()
def update(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
def al():
    l1=[]
    tem=all_.all_()
    #print tem
    for i in tem.split('\n'):
        l1.append(i.split(','))
    root = Tk()
    root.geometry('1000x300+10+50')
    # only the column containing the text is resized when the window size changes:
    root.columnconfigure(0, weight=1) 
    # resize row 0 height when the window is resized
    root.rowconfigure(0, weight=1)

    txt = Text(root)
    txt.grid(row=0, column=0, sticky="eswn")

    scroll_y = Scrollbar(root, orient="vertical", command=txt.yview)
    scroll_y.grid(row=0, column=1, sticky="ns")
    # bind txt to scrollbar
    txt.configure(yscrollcommand=scroll_y.set)
    s=""+str('-'*122)+"\n"
    for i1 in l1:
        s+="|"
        for j in i1:
            #print i1,j
            s+=j+"|"
        s+='\n'
        #print s
    print"fvdfvf"
    very_long_list = s
    #very_long_list = "\n".join([str(i) for i in range(100)])
    #print very_long_list.split("\n")
    
    print"266"
    txt.insert("1.0", very_long_list)
    # make the text look like a label
    txt.configure(state="disabled", relief="flat", bg=root.cget("bg"))
    print"done"
    root.mainloop()
#u()
qqq= Tk()
app= home(qqq.geometry('500x300+10+50'))
qqq.mainloop()

