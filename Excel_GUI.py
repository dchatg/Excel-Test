# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:04:51 2022

@author: dchat
"""
import os as os
import pandas as pd
import tkinter as tk


pand = tk.Tk()
pand.title('Pandas')
pand.geometry('400x400+700+300')
pand.resizable(0,0)

class Pads():
    
    def __init__(self):
        "初始化"
        self.kpassw={'a':'a'}
        self.file_read=None

        
    def login(self,name,password):
        """登录页面"""
        if name in self.kpassw:
            if self.kpassw[name] == password:
                tk.messagebox.showinfo(title = '成功',message = '成功登录')
                pand.destroy()
                self.__user__()
            else:
                tk.messagebox.showinfo(title = '错误',message = '密码错误')
        else:
            tk.messagebox.showinfo(title = '错误',message = '账号错误')
            
    def __user__(self):
        """操作主页面"""
        users=tk.Tk()
        users.title('JUNS主页面')
        users.geometry('900x400+400+250')
        users.resizable(0,0)
        
        user_L = tk.Label(users,text='1、请将文件的相关目录粘贴在下方',font=('Arical',15))
        user_L.place(x=30,y=30)
        user_E = tk.Entry(users,width=100)
        user_E.place(x=30,y=70)
        
        #查询文件格式
        def checkstr():
            namelist=['xls','xlsx','csv','txt','json','sql','html']
            strring=user_E.get()
            strring=strring.replace('\\','=').replace('=','/')
            string=strring.split('.')[-1].lower()
            if string == '':
                tk.messagebox.showinfo(title = '错误',message = '不支持的文件类型')
            #如果文件/文件夹不存在
            if string in namelist and  os.path.isfile(strring):
                tk.messagebox.showinfo(title = '文件格式',message = f'文件格式为{string}')
            else:
                tk.messagebox.showinfo(title = '错误',message = '地址请指向具体文件')
        
        def exit_users():
            users.destroy()
                
        #确定&按钮
        y_but = tk.Button(users,text='确定', width=5, height=2,command=checkstr)
        y_but.place(x=700,y=100)
        
        exit_user = tk.Button(users,text='退出',width=5,height=2,command=exit_users)
        exit_user.place(x=830,y=20)
        
        def file_read():
            strring=user_E.get()
            strring=strring.replace('\\','=').replace('=','/')
            string=strring.split('.')[-1].lower()
            if string == 'xls' or string == 'xlsx':
                file=pd.read_excel(strring,index_col=0)
            elif string == 'csv':
                file = pd.read_csv(strring,index_col=0)
            elif string == 'txt':
                file = pd.read_txt(strring,index_col=0)
            elif string == 'json':
                file = pd.read_txt(strring,index_col=0)
            elif string == 'html':
                file = pd.read_txt(strring,index_col=0)
            elif string == 'sql':
                file = pd.read_txt(strring,index_col=0)
            self.file_read = file
            tk.messagebox.showinfo(title = '文件',message = f'文件格式为{type(self.file_read)}')
            
        #查看文件
        file_b = tk.Button(users,text='查看文件大致信息',command=file_read)
        file_b.place(x=700,y=170)
        
        #对文件进行操作
        file_doit = tk.StringVar()
        file_doit.set('xlsx')
        
        filedoitchoice = tk.Label(users,text='2、请选择需要进行操作',font=('Arical',15))
        filedoitchoice.place(x=30,y=110)
        
        filedo1 = tk.Radiobutton(users,text='操作1',variable = file_doit,value = 'xlsx1')
        filedo1.place(x=50,y=150)
        filedo2 = tk.Radiobutton(users,text='操作2',variable = file_doit,value = 'xlsx2')
        filedo2.place(x=50,y=180)
        filedo3 = tk.Radiobutton(users,text='操作3',variable = file_doit,value = 'xlsx3')
        filedo3.place(x=50,y=210)
        filedo4 = tk.Radiobutton(users,text='操作4',variable = file_doit,value = 'xlsx4')
        filedo4.place(x=50,y=240)
        filedo5 = tk.Radiobutton(users,text='操作5',variable = file_doit,value = 'xlsx5')
        filedo5.place(x=50,y=270)
        filedo6 = tk.Radiobutton(users,text='操作6',variable = file_doit,value = 'xlsx6')
        filedo6.place(x=50,y=300)
        filedo7 = tk.Radiobutton(users,text='操作7',variable = file_doit,value = 'xlsx7')
        filedo7.place(x=50,y=330)
        
        def pri_file():
            #占位函数，后续将用来编写操作选择
            tk.messagebox.showinfo(title = '占位',message = f'当前占位为选择的操作方式\n{file_doit.get()}')
        
        file_pri = tk.Button(users,text='按钮测试',width=8,height=2,command=pri_file)
        file_pri.place(x=400,y=100)
        
        users.mainloop()
        
            
whcom = tk.Label(pand,text='登录页面',font=('Arical',25),width=8,height=2).place(x=140,y=100)
enc_name = tk.Entry(pand,width = 20)
enc_name.place(x=140,y=170)
enc_password = tk.Entry(pand,width = 20,show='*')
enc_password.place(x=140,y=200)
name = tk.Label(pand,text='账号',width=4,height=1).place(x=100,y=170)
password = tk.Label(pand,text='密码',width=4,height=1).place(x=100,y=200)

def test_login():
    name=enc_name.get()
    password=enc_password.get()
    pads=Pads()
    pads.login(name,password)

def exit_pand():
    pand.destroy()
    
logbut_name=tk.Button(pand,text='登录',font=('Arical',15),width = 5,height = 1,command=test_login)
logbut_name.place(x=220,y=250)

exit_pand = tk.Button(pand,text='退出',font=('Arical',15),width = 5,height = 1,command=exit_pand)
exit_pand.place(x=110,y=250)
        

pand.mainloop()