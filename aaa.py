from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Yummy:
    def __init__(self,root):
        self.root=root
        self.root.title("yummy not yummy informations")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="bisque")
        title=Label(self.root,text="DO YOU KNOW WHAT YOU'RE EATING?",bd=10,relief=GROOVE,font=("lucida calligraphy",40,"bold"),bg="lavender",fg="lightcoral")
        title.pack(side=TOP,fill=X)

    
        #______________________________manage_frames__________________
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="mediumpurple")
        Manage_Frame.place(x=20,y=100,width=450,height=650)

        m_title=Label(Manage_Frame,text="food supplements",bg="mediumpurple",fg="white",font=("harlow solid italic",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_code=Label(Manage_Frame,text="Code:",bg="mediumpurple",fg="white",font=("harrington",20,"bold"))
        lbl_code.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_code=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_code.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name:",bg="mediumpurple",fg="white",font=("harrington",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_approved=Label(Manage_Frame,text="Approved:",bg="mediumpurple",fg="white",font=("harrington",20,"bold"))
        lbl_approved.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_approved=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_approved.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_from=Label(Manage_Frame,text="From:",bg="mediumpurple",fg="white",font=("harrington",20,"bold"))
        lbl_from.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        combo_from=ttk.Combobox(Manage_Frame,font=("times new roman",15,"bold"),state='readonly')
        combo_from['values']=("animal","plant","other")
        combo_from.grid(row=4,column=1,pady=10,padx=10)
        
        lbl_badfor=Label(Manage_Frame,text="Bad for:",bg="mediumpurple",fg="white",font=("harrington",20,"bold"))
        lbl_badfor.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_badfor=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_badfor.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_goodfor=Label(Manage_Frame,text="Good for:",bg="mediumpurple",fg="white",font=("harrington",20,"bold"))
        lbl_goodfor.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_dob=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_general=Label(Manage_Frame,text="General:",bg="mediumpurple",fg="white",font=("harrington",20,"bold"))
        lbl_general.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txt_general=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_general.grid(row=7,column=1,pady=10,padx=20,sticky="w")



        #___________________________button_frames____________________
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="thistle")
        btn_Frame.place(x=15,y=530,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10,font=("forte",10)).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10,font=("forte",10)).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10,font=("forte",10)).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,font=("forte",10)).grid(row=0,column=3,padx=10,pady=10)
        


        
        #______________________________detail_frames__________________
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="palevioletred")
        Detail_Frame.place(x=500,y=100,width=800,height=650)

        lbl_search=Label(Detail_Frame,text="Search by",bg="palevioletred",fg="lavenderblush",font=("harlow solid italic",30,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values']=("code","name","approved")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=Entry(Detail_Frame,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        Searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        Showallbtn=Button(Detail_Frame,text="Show all",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        #__________________________________table______________________________

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=750,height=490)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Yummy_table=ttk.Treeview(Table_Frame,columns=("code","name","approved","from","badfor","goodfor","general"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=Yummy_table.xview)
        scroll_y.config(command=Yummy_table.yview)

        Yummy_table.heading("code",text="CODE")
        Yummy_table.heading("name",text="NAME")
        Yummy_table.heading("approved",text="APPROVED")
        Yummy_table.heading("from",text="FROM")
        Yummy_table.heading("badfor",text="BAD FOR")
        Yummy_table.heading("goodfor",text="GOOD FOR")
        Yummy_table.heading("general",text="GENERAL")
        Yummy_table['show']='headings'
        Yummy_table.column("code",width=75)
        Yummy_table.column("name",width=75)
        Yummy_table.column("approved",width=75)
        Yummy_table.column("from",width=75)
        Yummy_table.column("badfor",width=100)
        Yummy_table.column("goodfor",width=100)
        Yummy_table.column("general",width=300)
        Yummy_table.pack(fill=BOTH,expand=1)
        

            
if __name__=='__main__':
    root=Tk()
    application=Yummy(root)
    root.mainloop()
