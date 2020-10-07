from Tkinter import Tk, Text, Scrollbar
from Tkinter import*

root = Tk()
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
l1=[]
aicte=open("out.csv","r")
# open file
tem=aicte.read()
for i in tem.split('\n'):
    l1.append(i.split(','))
aicte.close()
r = 0
for i in range(100):
    for col in l1:
      c = 0
      for row in col:
         # i've added some styling
         label = Label(txt, width = 10, height = 2, \
                               text = row, relief = RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1
# make the text look like a label
txt.configure(state="disabled", relief="flat", bg=root.cget("bg"))

root.mainloop()
