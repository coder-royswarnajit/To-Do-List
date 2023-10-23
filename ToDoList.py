from tkinter import *
from tkinter.font import Font 
from tkinter import filedialog
import pickle


root = Tk()
root.title("TO DO LIST")
root.geometry("500x500")

fnt = Font(family="Ink Free",size=26,weight='bold')

frame = Frame(root)
frame.pack(pady=10)

lists = Listbox(frame,font=fnt,width=25,height=5,bg='SystemButtonFace',bd=0,fg='black',highlightthickness=0,selectbackground="grey",activestyle='none')
lists.pack()

#stuff = ["eat",'sleep','run','study','cook']
#for item in stuff:
    #lists.insert(END,item)


#lists.config(yscrollcommand=scroll.set)
#scroll.config(command=lists.yview)

#ADD ITEMS
e = Entry(root,font=26)
e.pack(pady=20)

btn_frame = Frame(root)
btn_frame.pack(pady=20)

def deleted():
    lists.delete(ANCHOR)

def added():
    lists.insert(END,e.get())
    e.delete(0,END)

def cross_off():
    lists.itemconfig(lists.curselection(),fg="#dedede")
    lists.selection_clear(0,END)

def delete_crossed():
    ctr=0
    while ctr < lists.size():
        if lists.itemcget(ctr,"fg") == '#dedede':
            lists.delete(lists.index(ctr))
        else:
            ctr+=1


def cross_on():
    lists.itemconfig(lists.curselection(),fg="black")

def clearall():
    lists.delete(0,END)

#FUNCTION BUTTONS
btn_delete = Button(btn_frame,text="DELETE",command=deleted)
btn_delete.grid(row=0,column=0,padx=20)
btn_add = Button(btn_frame,text="ADD",command=added)
btn_add.grid(row=0,column=1,padx=20)
btn_cross_off = Button(btn_frame,text="CROSS OFF",command=cross_off)
btn_cross_off.grid(row=0,column=2,padx=20)
btn_cross_on = Button(btn_frame,text="UN-CROSS",command=cross_on)
btn_cross_on.grid(row=0,column=3,padx=20)
delete_cross = Button(btn_frame,text="DELETE CROSSED",command=delete_crossed)
delete_cross.grid(row=1,column=2,padx=30,pady=20)
clear_btn = Button(btn_frame,text="Clear All",command=clearall)
clear_btn.grid(row=1,column=3,padx=30,pady=20)

#MENU OPTIONS
def save():
    file_name = filedialog.asksaveasfilename(initialdir="C:\Python Programs\GUI\data",
                                             title="Save File", filetypes=(("Dat Files","*.dat"),("All Files","*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        #DELETE CROSSED OFF ITEMS FROM THE LIST
        ctr=0
        while ctr < lists.size():
            if lists.itemcget(ctr,"fg") == '#dedede':
                lists.delete(lists.index(ctr))
            else:
                ctr+=1
        
        #GRABBING THE THINGS FROM LIST
        stuff = lists.get(0,END)
        #OPEN THE FILE
        output_file = open(file_name,'wb')
        #ADD THE STUFF TO THE FILE
        pickle.dump(stuff,output_file)


def Open():
    file_name = filedialog.askopenfilename(initialdir="C:\Python Programs\GUI\data",
                                             title="Open File", filetypes=(("Dat Files","*.dat"),("All Files","*.*")))

    if file_name:
        lists.delete(0,END) #DELETE CURRENTLY OPEN LIST
        input_file = open(file_name,'rb') #OPEN FILE
        stuff = pickle.load(input_file) #LOAD DATA FROM THE FILE
        #OUTPUT stuff TO THE SCREEN
        for item in stuff:
            lists.insert(END,item)



def clear():
    lists.delete(0,END)

menus = Menu(root)
root.config(menu=menus)

file = Menu(menus,tearoff=False)
menus.add_cascade(label="File",menu=file)
file.add_command(label="Save List",command=save)
file.add_command(label="Open List",command=Open)
file.add_separator()
file.add_command(label="Clear List",command=clear)
file.add_separator()
file.add_command(label="Exit....",command=root.quit)


root.mainloop()