# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:28:56 2021

@author: Ganesh
"""

from tkinter import *
from tkinter import messagebox,simpledialog
import tkinter as tk
import pymysql


db = pymysql.connect(host='localhost',user='root',password='',database='stud_info')
cursor = db.cursor()

root = tk.Tk()

root.geometry('1300x600+0+0')
root.title('Student Information System')
root.config(bg ='#8aa624')



#=================
#Creating a Frame
#=================
top_frame = tk.Frame(root,bg ='#ba2b0f')
top_frame.place(x = 5, y = 5,width = 1290, height = 70)
left_frame = tk.Frame(root,bg ='#ba2b0f')
left_frame.place(x = 5,y=80 ,width = 640, height =420)
right_frame = tk.Frame(root,bg ='#ba2b0f')
right_frame.place(x = 655,y=80 ,width = 640, height =420)
button_frame = tk.Frame(root,bg ='#ba2b0f')
button_frame.place(x = 5,y = 505, width = 1290, height = 70)



def update():
    if (sid_E.get()=='' or fname_e.get()=='' ) or (lname_e.get()=='' or stream_e.get()=='') or (python_E.get()==''or java_e.get()=='') or (c_e.get()==''or android_e.get()=='') or (total_e.get()==''or per_e.get()==''):
        tk.messagebox.showerror('ERROR','All fields Are Mandatory')
    else:
        
    
    
        cursor.execute("UPDATE results SET sid='"
                       + str(sid_E.get()) +"', fname ='" 
                       +fname_e.get() +"', lname ='"
                       + lname_e.get() +"', class ='"
                       + cls_e.get() +"', stream ='"
                       + stream_e.get() +"', python ='"
                       + python_E.get() +"', java ='"
                       + java_e.get() +"', c ='"
                       + c_e.get() +"', android = '"
                       + android_e.get() +"', total ='"
                       + total_e.get() +"', persentage ='"
                       + per_e.get() +"' where sid ='" + sid_E.get() + "'")
        db.commit()
        tk.messagebox.showinfo('Update','Data Updated')
        clrbtn()
    
    

 
def deleterecord():
    clrbtn()
    esid = tk.simpledialog.askinteger('DeleteRecord', 'Enter sid of information which You want to Delete')
    del_rec = "delete from results where sid = '%s'"%(esid)
    delr = cursor.execute(del_rec)
    db.commit()
   
    
    if delr ==1:
        tk.messagebox.showinfo('Delete','Information Deleted Successfully')
    else:
        tk.messagebox.showinfo('Info','Data Not Found')
        
def showallrecord():
    root1 = tk.Tk()
    root1.title('Data')
    root1.config(bg ='#8aa624')
    root1.geometry('')
    
    cursor.execute("select * from results ") 
    data = cursor.fetchall()
    
    db_e1 = tk.Entry(root1,width = 10)
    db_e1.grid(row =0 , column =0)
    db_e1.insert('0', 'SID')
    
    db_e2 = tk.Entry(root1,width = 10)
    db_e2.grid(row =0 , column =1)
    db_e2.insert('0', 'First Name')
    
    db_e3 = tk.Entry(root1,width = 10)
    db_e3.grid(row =0 , column =2)
    db_e3.insert('end', 'Last Name')
    
    db_e4 = tk.Entry(root1,width = 10)
    db_e4.grid(row =0 , column =3)
    db_e4.insert('end', 'Class')
    
    db_e5 = tk.Entry(root1,width = 10)
    db_e5.grid(row =0 , column =4)
    db_e5.insert('end', 'Stream')
    
    db_e6= tk.Entry(root1,width = 10)
    db_e6.grid(row =0 , column =5)
    db_e6.insert('end', 'Python')
    
    db_e7= tk.Entry(root1,width = 10)
    db_e7.grid(row =0 , column =6)
    db_e7.insert('end', 'Java')
    
    db_e8= tk.Entry(root1,width = 10)
    db_e8.grid(row =0 , column =7)
    db_e8.insert('end', 'C')
    
    db_e9= tk.Entry(root1,width = 10)
    db_e9.grid(row =0 , column =8)
    db_e9.insert('end', 'Android')
    
    db_e10= tk.Entry(root1,width = 10)
    db_e10.grid(row =0 , column =9)
    db_e10.insert('end', 'Total')
    
    db_e11 = tk.Entry(root1,width = 10)
    db_e11.grid(row =0 , column =10)
    db_e11.insert('end', 'Persentage')
    
   
    i = 1
    for results in data:
        for j in range(len(results)):
            
            db_e = tk.Entry(root1,width = 10)
            db_e.grid(row =i , column =j)
            db_e.insert(0,results[j])
        i=i+1
    root1.mainloop()
''' cursor.execute("SELECT * FROM results limit 0,10")
    i=0 
    for results in cursor: 
        for j in range(len(results)):
            e = Entry(root1, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, results[j])
        i=i+1'''
    

def ShowRecord():
    clrbtn() 
    
    esid = tk.simpledialog.askinteger('Search', 'Enter sid of information which You want to search')

    Select1="select sid,fname,lname,class,stream,python,java,c,android,total,persentage from results where sid='%s'" %(esid)
    chk1=cursor.execute(Select1)
    result2=cursor.fetchall()
    print(result2)
   
    if(chk1 == 1):
        for i in result2:
            sid_E.insert(0, i[0])
            fname_e.insert(0,i[1])
            lname_e.insert(0, i[2])
            cls_e.insert(0, i[3])
            stream_e.insert(0, i[4])
            python_E.insert(0, i[5])
            java_e.insert(0, i[6])
            c_e.insert(0, i[7])
            android_e.insert(0, i[8])
            total_e.insert(0, i[9])
            per_e.insert(0, i[10])
        
    else:
        tk.messagebox.askokcancel("Information","No Record exists")    
def saveinfotodb():
    if (sid_E.get()=='' or fname_e.get()=='' ) or (lname_e.get()=='' or stream_e.get()=='') or (python_E.get()==''or java_e.get()=='') or (c_e.get()==''or android_e.get()=='') or (total_e.get()==''or per_e.get()==''):
        tk.messagebox.showerror('ERROR','All fields Are Mandatory')
    else:
        esid1 = int(sid_E.get())
        Select="select sid from results where sid='%s'" %(esid1)
        chk=cursor.execute(Select)
        
        if (chk == 1):
            tk.messagebox.showerror('ERROR','Student Already Registered For this Sid')
        
            
            
        else:
            cursor.execute ("insert into results values('"
                            + str(sid_E.get()) +"','" 
                            +fname_e.get() +"','"
                            + lname_e.get() +"','"
                            + cls_e.get() +"','"
                            + stream_e.get() +"','"
                            + str(python_E.get()) +"','"
                            + str(java_e.get()) +"','"
                            + str(c_e.get()) +"','"
                            + str(android_e.get()) +"','"
                            + str(total_e.get()) +"','"
                            + str(per_e.get()) +"')")
            db.commit()
            tk.messagebox.showinfo("Save","Information Saved in Database Successfully")
            clrbtn()
            
def clrbtn():
    sid_E.delete(0,'end')
    fname_e.delete(0,'end')
    lname_e.delete(0,'end')
    stream_e.delete(0,'end')
    cls_e.delete(0,'end')
    python_E.delete(0,'end')
    java_e.delete(0,'end')
    c_e.delete(0,'end')
    android_e.delete(0,'end')
    total_e.delete(0,'end')
    per_e.delete(0,'end') 
    
    
def quitbtn():
    ask = tk.messagebox.askyesno('Quit','Do You Really Want to Quit')
    if ask==1:
        root.destroy()
        
def calculate():
    if (sid_E.get()=='' or fname_e.get()=='' ) or (lname_e.get()=='' or stream_e.get()=='') or (python_E.get()==''or java_e.get()=='') or (c_e.get()==''or android_e.get()==''):
        tk.messagebox.showerror('ERROR','All fields Are Mandatory')
    else:
        total_e.delete(0,'end')
        per_e.delete(0,'end') 
        abc = int(python_E.get())+int(java_e.get())+int(c_e.get())+int(android_e.get())
        efg = (int(python_E.get())+int(java_e.get())+int(c_e.get())+int(android_e.get()))/4
        total_e.insert(0, abc)
        per_e.insert(0, efg)
    
    
    
    
#=================
#Creating a Label
#=================
title_lbl = tk.Label(top_frame,text = 'Student information System', font = ('Times New Roman', 40 ,'bold'),bg='#ba2b0f',fg='white')
title_lbl.place(x = 320, y = 1)
title_lf = tk.Label(left_frame,text = 'Student Info :',font = ('Times New Roman',30,'bold'),bg='#ba2b0f',fg='white')
title_lf.grid(row = 0 ,column = 0,padx =10,pady =10,sticky='w')
sid_lbl = tk.Label(left_frame,text = 'Student Id :', font = ('Times New Roman', 20 ,'bold'),bg='#ba2b0f',fg='white')
sid_lbl.grid(row = 1 , column= 0 ,padx =15, pady=10,sticky='w')
sid_E = tk.Entry(left_frame,textvariable = "st_id",font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
sid_E.grid(row = 1 , column= 1 ,padx =10, pady=10,sticky='w')
fname_lbl = tk.Label(left_frame,text = 'First Name :', font = ('Times New Roman', 20 ,'bold'),bg='#ba2b0f',fg='white')
fname_lbl.grid(row = 2 , column= 0 ,padx =5, pady=10,sticky='w')
fname_e = tk.Entry(left_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
fname_e.grid(row = 2 , column= 1 ,padx =10, pady=10,sticky='w')
lname_lbl = tk.Label(left_frame,text = 'Last Name :',font = ('Times New Roman', 20 ,'bold'),bg='#ba2b0f',fg='white')
lname_lbl.grid(row = 3 , column= 0 ,padx =10, pady=10,sticky='w')
lname_e = tk.Entry(left_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
lname_e.grid(row = 3 , column= 1 ,padx =10, pady=10,sticky='w')
stream_lbl = tk.Label(left_frame,text = 'Stream :', font = ('Times New Roman', 20 ,'bold'),bg='#ba2b0f',fg='white')
stream_lbl.grid(row = 4 , column= 0 ,padx =53, pady=10,sticky='w')
stream_e = tk.Entry(left_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
stream_e.grid(row = 4 , column= 1 ,padx =10, pady=10,sticky='w')
cls_lbl = tk.Label(left_frame,text = 'Class :', font = ('Times New Roman', 20 ,'bold'),bg='#ba2b0f',fg='white')
cls_lbl.grid(row = 5 , column= 0 ,padx =72, pady=10,sticky='w')
cls_e = tk.Entry(left_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
cls_e.grid(row = 5 , column= 1 ,padx =10, pady=10,sticky='w')

title_rf = tk.Label(right_frame,text = 'Marks :',font = ('Times New Roman',30,'bold'),bg='#ba2b0f',fg='white')
title_rf.grid(row = 0 ,column = 0,padx =10,pady =10,sticky='w')
python_lbl = tk.Label(right_frame,text = 'Python :', font = ('Times New Roman', 20 ,'bold'),bg='#ba2b0f',fg='white')
python_lbl.grid(row = 1 , column= 0 ,padx =15, pady=10,sticky='w')
python_E = tk.Entry(right_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
python_E.grid(row = 1 , column= 1 ,padx =10, pady=10,sticky='w')
java_lbl = tk.Label(right_frame,text = 'Java :', font = ('Times New Roman', 20 ,'bold'),bg='#ba2b0f',fg='white')
java_lbl.grid(row = 2 , column= 0 ,padx =42, pady=10,sticky='w')
java_e = tk.Entry(right_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
java_e.grid(row = 2 , column= 1 ,padx =10, pady=10,sticky='w')
c_lbl = tk.Label(right_frame,text = 'C :',font = ('Times New Roman', 20 ,'bold'),bg='#ba2b0f',fg='white')
c_lbl.grid(row = 3 , column= 0 ,padx =80, pady=10,sticky='w')
c_e = tk.Entry(right_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
c_e.grid(row = 3 , column= 1 ,padx =10, pady=10,sticky='w')
android_lbl = tk.Label(right_frame,text = 'Android :', font = ('Times New Roman', 20 ,'bold',),bg='#ba2b0f',fg='white')
android_lbl.grid(row = 4 , column= 0 ,padx =1, pady=10,sticky='w')
android_e = tk.Entry(right_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
android_e.grid(row = 4 , column= 1 ,padx =10, pady=10,sticky='w')
btn_cal = tk.Button(right_frame,text ='Calculate',font = ('Times New Roman',10,'bold'),bg='#ba2b0f',fg='white',command=calculate)
btn_cal.grid(row = 4 , column= 2 ,padx =10, pady=10,sticky='w')
total_lbl = tk.Label(right_frame,text = 'Total :', font = ('Times New Roman', 20 ,'bold',),bg='#ba2b0f',fg='white')
total_lbl.grid(row = 5 , column= 0 ,padx =40, pady=10,sticky='w')
total_e = tk.Entry(right_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
total_e.grid(row = 5 , column= 1 ,padx =10, pady=10,sticky='w')
per_lbl = tk.Label(right_frame,text = 'Persentage :', font = ('Times New Roman', 20 ,'bold',),bg='#ba2b0f',fg='white')
per_lbl.grid(row = 6 , column= 0 ,padx =1, pady=10,sticky='w')
per_e = tk.Entry(right_frame,font = ('Times New Roman',20,'bold'),bg='#ba2b0f',fg='white')
per_e.grid(row = 6 , column= 1 ,padx =10, pady=10,sticky='w')

quitb = tk.Button(button_frame ,text ='Quit',bg ='gray' ,fg = 'white', font=('Times New Roman',20,'bold'),command =quitbtn)
quitb.pack(side="right",pady =5,padx =5)
btn_delete = tk.Button(button_frame ,text ='Delete',bg ='#70cf32' ,fg = 'white',font=('Times New Roman',20,'bold'),command =deleterecord)
btn_delete.pack(side="right",pady =5,padx =5)
update = tk.Button(button_frame ,text ='Update',bg ='#70cf32' ,fg = 'white',font=('Times New Roman',20,'bold'),command = update)
update.pack(side="right",pady =5,padx =5)
search = tk.Button(button_frame ,text ='Search',bg ='#6b7009' ,fg = 'white',command = ShowRecord,font=('Times New Roman',20,'bold'))
search.pack(side="right",pady =5,padx =5)
clear = tk.Button(button_frame ,text ='Clear',bg ='orange' ,fg = 'white', font=('Times New Roman',20,'bold'),command =clrbtn)
clear.pack(side="right",pady =5,padx =5)
save = tk.Button(button_frame ,text ='Save',bg ='green' ,fg = 'white',command = saveinfotodb,font=('Times New Roman',20,'bold'))
save.pack(side="right",pady =5,padx =5)
all_rec = tk.Button(button_frame ,text ='Alldata',bg ='green' ,fg = 'white',command = showallrecord,font=('Times New Roman',20,'bold'))
all_rec.pack(side="left",pady =5,padx =5)



root.mainloop()
