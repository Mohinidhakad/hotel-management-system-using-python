from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random
from time import strftime
from datetime import datetime
from customer import Cust_win
from Room import Roombooking
from Details import DetailsRoom
from Hotel import HotelManagementSystem



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\pc\Desktop\hotel\Images\image1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\pc\Desktop\hotel\Images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #=====Icon Images=============
        img2=Image.open(r"C:\Users\pc\Desktop\hotel\Images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)



        img3=Image.open(r"C:\Users\pc\Desktop\hotel\Images\LoginIconAppl.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        #LoginButton

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.login,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forget button
        loginbtn=Button(frame,text="Forget Password", command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=20,y=370,width=160)

    #def register_window(self):
    #3   self.new_window=Toplevel(self.root)
    #  self.app=Register(self.new_window)




    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All  Field  Required")
        elif  self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("success","Welcome to our Hotel")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpass.get(),
                                                                                ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    #=============reset password==============
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)


                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login new password",parent=self.root2)
                self.root2.destroy()





#===========================forget password==============

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My error","Please enter the valid user name")
            else:
                conn.close()
                self.root2==Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")


                l=Label(self.root2,text="Forget password",font=("times new roman",15,"bold"),fg="white",bg="black")
                l.place(x=0,y=0,relwidth=1)


                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)


                self.combo_securiy_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly") 
                self.combo_securiy_Q["values"]=("select","Your Birth Place","your Girlfriend name","Your pet Name")
                self.combo_securiy_Q.place(x=50,y=110,width=250)
                self.combo_securiy_Q.current(0)



                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.new_password=ttk.Entry(self.root2,font=("times new roman",15))
                self.new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),bg="white",fg="green")
                btn.place(x=100,y=290)

class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

     #============ hotel img===================
        img1 = Image.open(r"C:\Users\pc\Desktop\hotel\Images\water.jpg")
        img1 = img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
     
     #===============logo========================
        img2 = Image.open(r"C:\Users\pc\Desktop\hotel\Images\avg.jpeg")
        img2 = img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
     
     #============title====================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new romen",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
     
     #====================main frame=================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

     #==================menu===================
        lbl_menu=Label(main_frame,text="MENU",font=("times new romen",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

      #=================Button frame====================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
    
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
   
   #==============Right side image hotel===============
        img3 = Image.open(r"C:\Users\pc\Desktop\hotel\Images\dreamland.jpg")
        img3 = img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

   #===============second image=======================
        img4 = Image.open(r"C:\Users\pc\Desktop\hotel\Images\seoul.jpg")
        img4 = img4.resize((230,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=190)
    
    #=============second image-1=====================
        img5 = Image.open(r"C:\Users\pc\Desktop\hotel\Images\khana1.jpg")
        img5 = img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window) 

    
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
     












                                                                                




if __name__ == "__main__":
    main()