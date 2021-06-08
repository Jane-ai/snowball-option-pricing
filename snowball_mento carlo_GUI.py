# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:39:07 2021

@author: mac
"""

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib import cm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from PIL import Image, ImageTk
# from tkinter import messagebox
from datetime import datetime
# import statsmodels.api as sm
from sklearn import linear_model
from statsmodels.graphics.tsaplots import plot_acf
from mpl_toolkits.axisartist.axislines import SubplotZero
import statsmodels.api as sm
from tqdm import tqdm
import time
import datetime
import math;
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
# import other modules
#from load_data import *



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
    # return relative_path


# 主窗口
def overview(window):
    global n,s
    root0 = window
    # 将之前界面里的所有控件摧毁
    while assembly != []:
        a = assembly.pop()
        a.destroy()

    # 窗口命名
    root0.title('[期权与期货]基于蒙特卡洛的雪球产品定价')

    #########################################窗口布局#########################################

    # 获得屏幕分辨率
    screenWidth = root0.winfo_screenwidth()
    print('screenWidth is:',screenWidth)
    screenHeight = root0.winfo_screenheight()
    print('screenHeight is:',screenHeight)
    # 根据分辨率调节窗口尺寸
    n = 3 * screenHeight / 3200#3

    # 各控件之间的相对距离，窗口示意图及各参数意义参见说明文档的示意图

    x1 = int(20 * n)
    print('x1 is:',x1)
    x2 = int(x1 + 350 * n)
    x3 = int(x2 + 5 * n)
    x4 = int(x3 + 40 * n)
    x5 = int(x4 + 350 * n)
    x6 = int(x5 + 5 * n)
    x7 = int(x6 + 80 * n)
    x8 = int(x7 + 5 * n)
    x9 = int(x8 + 20 * n)
    x10 = int(x9 + 400 * n)
    x11 = int(x10 + 20 * n)

    y1 = int(90 * n)
    print('y1 is:',y1)
    y2 = int(y1 + 60 * n)
    y3 = int(y2 + 5 * n)
    y4 = int(y3 + 200 * n)
    y5 = int(y4 + 5 * n)
    y6 = int(y5 + 5 * n)
    y7 = int(y6 + 80 * n)
    y8 = int(y7 + 5 * n)
    y9 = int(y8 + 400 * n)
    y10 = int(y9 + 20 * n)

    y11 = int(y8 + 80 * n)
    y12 = int(y11 + 100 * n)
    y13 = int(y12 + 40 * n)
    y14 = int(y13 + 100 * n)
    y15 = int(y8 + 70 * n)
    y16 = int(y15 + 160 * n)
    y17 = int(y8 + 250*n)
    y18 = int(y17 + 20*n)

    winWidth = x11#int(4193*n)
    winHeight = y10#int(1305*n)
    # 窗口距电脑屏幕边缘空出的距离
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    # 放置窗口
    root0.geometry("%sx%s+%s+%s" % (int(winWidth), int(winHeight), x, y))
    # root.geometry("1070x800+200+20")第一个数横大小，第二个数纵大小，第三个数离左屏幕边界距离，第四个数离上面屏幕边界距离。

    # 设置窗口不可缩放
    root0.resizable(0, 0)

    #########################################标签初始化#########################################

    # 设置标签宽度、字体大小、高度
    label_width = int(15 * n)
    fontsize = int(15 * n)
    label_height = int(20 * n)

    # 放置第一行标签
    index_class01 = Label(root0, anchor=W, text='测试开始时间(YY-MM-DD)', font=('KaiTi', fontsize))
    index_class01.place(x=20 * n, y=30 * n, width=4*(x2 - x1), height=(y2 - y1) / 2)

    start = StringVar()
    entry_start = Entry(root0, textvariable=start, font=('KaiTi', int(15 * n)))
    entry_start.place(x=260 * n, y=30 * n, width=120*n, height=(y2 - y1) / 2)
    start.set('2019-12-31')

    index_class02 = Label(root0, anchor=W, text='测试结束时间(YY-MM-DD)', font=('KaiTi', fontsize))
    index_class02.place(x=380 * n, y=30 * n, width=4*(x2 - x1), height=(y2 - y1) / 2)

    end = StringVar()
    entry_end = Entry(root0, textvariable=end, font=('KaiTi', int(15 * n)))
    entry_end.place(x=620 * n, y=30 * n, width=120*n, height=(y2 - y1) / 2)
    end.set('2020-3-31')
    
    knockout = Label(root0, anchor=W, text='敲出倍数', font=('KaiTi', fontsize))
    knockout.place(x=740 * n+5, y=30 * n, width=(x2 - x1), height=(y2 - y1) / 2)

    knock_out = StringVar()
    entry_knockout = Entry(root0, textvariable=knock_out, font=('KaiTi', int(15 * n)))
    entry_knockout.place(x=830 * n+5, y=30 * n, width=60*n, height=(y2 - y1) / 2)
    knock_out.set('1.0')
    #a = knock_out.get()
    
    knockin = Label(root0, anchor=W, text='敲入倍数', font=('KaiTi', fontsize))
    knockin.place(x=900 * n+5, y=30 * n, width=(x2 - x1), height=(y2 - y1) / 2)

    knock_in = StringVar()
    entry_knockin = Entry(root0, textvariable=knock_in, font=('KaiTi', int(15 * n)))
    entry_knockin.place(x=990 * n+5, y=30 * n, width=60*n, height=(y2 - y1) / 2)
    knock_in.set('1.0')
    
    timeup = Label(root0, anchor=W, text='到期时长(月)', font=('KaiTi', fontsize))
    timeup.place(x=1060 * n+5, y=30 * n, width=(x2 - x1), height=(y2 - y1) / 2)

    time_up = StringVar()
    entry_timeup = Entry(root0, textvariable=time_up, font=('KaiTi', int(15 * n)))
    entry_timeup.place(x=1190 * n+5, y=30 * n, width=60*n, height=(y2 - y1) / 2)
    time_up.set('1')
    
    # 放置标签
    volwrite = Label(root0, width=x7 - x4, anchor=CENTER, text='可以手动输入波动率', justify='center', font=('KaiTi', fontsize))
    volwrite.place(x=x1, y=y1, width=x7 - x4, height=y2 - y1)
    
    vol_write = StringVar()
    entry_vol_write = Entry(root0, textvariable=vol_write, font=('KaiTi', int(15 * n)))
    entry_vol_write.place(x=5*x1, y=y3-15, width=3*(x2 - x1)/4, height=3*(y2 - y1)/4)#x1+60
    vol_write.set('original')
    
    index_class = Label(root0, width=x2 - x1, anchor=CENTER, text='全部时间的波动率', font=('KaiTi', fontsize))
    index_class.place(x=x1+30, y=y1+135, width=x2 - x1, height=y2 - y1)

    index_option = Label(root0, width=x2 - x1, anchor=CENTER, text='对数差分股价走势', justify='center', font=('KaiTi', fontsize))
    index_option.place(x=x1+30, y=y6+140, width=x2 - x1, height=y7 - y6)#y=y6
    
    # 显示预测股价曲线
    time_choose_curve = Label(root0, width=x10 - x9, anchor=CENTER, text='预测股价波动图', justify='center', font=('KaiTi', fontsize))
    time_choose_curve.place(x=x9-10, y=y1, width=x10 - x9, height=y2 - y1)

    productpc = Label(root0, width=x7 - x4, anchor=CENTER, text='请输入股指价格', justify='center', font=('KaiTi', fontsize))
    productpc.place(x=x4+20, y=y1, width=x7 - x4, height=y2 - y1)
    
    product_pc = StringVar()
    entry_productpc = Entry(root0, textvariable=product_pc, font=('KaiTi', int(15 * n)))
    entry_productpc.place(x=x4+120, y=y3-15, width=(x2 - x1)/2, height=3*(y2 - y1)/4)
    product_pc.set('1')
    
    return1 = Label(root0, width=x7 - x4, anchor=CENTER, text='请输入情形一时的投资收益率', justify='center', font=('KaiTi', fontsize))
    return1.place(x=x4+20, y=y3+25, width=x7 - x4, height=y2 - y1)
    
    return_1 = StringVar()
    entry_return1 = Entry(root0, textvariable=return_1, font=('KaiTi', int(15 * n)))
    entry_return1.place(x=x4+120, y=y3+60, width=(x2 - x1)/2, height=3*(y2 - y1)/4)
    return_1.set('1')
    
    return2 = Label(root0, width=x7 - x4, anchor=CENTER, text='请输入情形二时的投资收益率', justify='center', font=('KaiTi', fontsize))
    return2.place(x=x4+20, y=y3+95, width=x7 - x4, height=y2 - y1)
    
    return_2 = StringVar()
    entry_return2 = Entry(root0, textvariable=return_2, font=('KaiTi', int(15 * n)))
    entry_return2.place(x=x4+120, y=y3+130, width=(x2 - x1)/2, height=3*(y2 - y1)/4)
    return_2.set('1')
    
    return3 = Label(root0, width=x7 - x4, anchor=CENTER, text='请输入情形三时的投资收益率', justify='center', font=('KaiTi', fontsize))
    return3.place(x=x4+20, y=y3+165, width=x7 - x4, height=y2 - y1)
    
    return_3 = StringVar()
    entry_return3 = Entry(root0, textvariable=return_3, font=('KaiTi', int(15 * n)))
    entry_return3.place(x=x4+120, y=y3+200, width=(x2 - x1)/2, height=3*(y2 - y1)/4)
    return_3.set('1')
    
    productet = Label(root0, width=x7 - x4, anchor=CENTER, text='产品预测价格', justify='center', font=('KaiTi', fontsize))
    productet.place(x=x4+20, y=y3+310, width=x7 - x4, height=y2 - y1)
    
    product_et = StringVar()
    entry_productet = Entry(root0, textvariable=product_et, font=('KaiTi', int(15 * n)))
    entry_productet.place(x=x4+120, y=y3+345, width=(x2 - x1)/2, height=3*(y2 - y1)/4)
    product_et.set('1')
    
    producter = Label(root0, width=x7 - x4, anchor=CENTER, text='产品价格标准差', justify='center', font=('KaiTi', fontsize))
    producter.place(x=x4+20, y=y3+380, width=x7 - x4, height=y2 - y1)
    
    product_er = StringVar()
    entry_producter = Entry(root0, textvariable=product_er, font=('KaiTi', int(15 * n)))
    entry_producter.place(x=x4+120, y=y3+415, width=(x2 - x1)/2, height=3*(y2 - y1)/4)
    product_er.set('1')
    
    productr = Label(root0, width=x7 - x4, anchor=CENTER, text='产品预测收益率', justify='center', font=('KaiTi', fontsize))
    productr.place(x=x5+60, y=y3+310, width=x7 - x4, height=y2 - y1)
    
    product_r = StringVar()
    entry_productr = Entry(root0, textvariable=product_r, font=('KaiTi', int(15 * n)))
    entry_productr.place(x=x5+160, y=y3+345, width=(x2 - x1)/2, height=3*(y2 - y1)/4)
    product_r.set('1')
    
    productre = Label(root0, width=x7 - x4, anchor=CENTER, text='产品预测收益', justify='center', font=('KaiTi', fontsize))
    productre.place(x=x5+60, y=y3+380, width=x7 - x4, height=y2 - y1)
    
    product_re = StringVar()
    entry_productre = Entry(root0, textvariable=product_re, font=('KaiTi', int(15 * n)))
    entry_productre.place(x=x5+160, y=y3+415, width=(x2 - x1)/2, height=3*(y2 - y1)/4)
    product_re.set('1')
    
    pro = Label(root0, width=x7 - x4, anchor=CENTER, text='三种情形发生的预测概率', justify='center', font=('KaiTi', fontsize))
    pro.place(x=x5+60, y=y3+165, width=x7 - x4, height=y2 - y1)
    
    pro1 = Label(root0, width=x7 - x4, anchor=CENTER, text='情形一', justify='center', font=('KaiTi', fontsize))
    pro1.place(x=x5+80, y=y3+200, width=50, height=y2 - y1)
    
    pro1_pre = StringVar()
    entry_pro1_pre = Entry(root0, textvariable=pro1_pre, font=('KaiTi', int(15 * n)))
    entry_pro1_pre.place(x=x5+70, y=y3+235, width=70, height=3*(y2 - y1)/4)
    pro1_pre.set('1')
    
    pro2 = Label(root0, width=x7 - x4, anchor=CENTER, text='情形二', justify='center', font=('KaiTi', fontsize))
    pro2.place(x=x5+190, y=y3+200, width=50, height=y2 - y1)
    
    pro2_pre = StringVar()
    entry_pro2_pre = Entry(root0, textvariable=pro2_pre, font=('KaiTi', int(15 * n)))
    entry_pro2_pre.place(x=x5+180, y=y3+235, width=70, height=3*(y2 - y1)/4)
    pro2_pre.set('1')
    
    pro3 = Label(root0, width=x7 - x4, anchor=CENTER, text='情形三', justify='center', font=('KaiTi', fontsize))
    pro3.place(x=x5+300, y=y3+200, width=50, height=y2 - y1)
    
    pro3_pre = StringVar()
    entry_pro3_pre = Entry(root0, textvariable=pro3_pre, font=('KaiTi', int(15 * n)))
    entry_pro3_pre.place(x=x5+290, y=y3+235, width=70, height=3*(y2 - y1)/4)
    pro3_pre.set('1')
    
    
    

    
    
    ##############################蒙特卡洛_部分###################################

    global or_data,data
    #start_date = 
    #end_date = 
    
    
    #############################################图片留空白区域#############################################

    blank_img1 = Image.open(resource_path('blank.png')).resize((int(n * 400), int(n * 230)), Image.ANTIALIAS)
    blank_img2 = Image.open(resource_path('blank.png')).resize((int(n * 400), int(n * 200)), Image.ANTIALIAS)
    
    acf_pimg = ImageTk.PhotoImage(blank_img1)
    acf_label = Label(root0, image=acf_pimg)
    acf_label.image = acf_pimg
    acf_label.place(x=x1+30, y=y3+120, width=x2-x1, height=y4 - y3)
    
    q_pimg = ImageTk.PhotoImage(blank_img2)
    q_label = Label(root0, image=q_pimg)
    q_label.image = q_pimg
    q_label.place(x=x1+30, y=y7+120, width=x2-x1, height=y4 - y3)
    
    pre_pimg = ImageTk.PhotoImage(blank_img2)
    pre_label = Label(root0, image=pre_pimg)
    pre_label.image = pre_pimg
    pre_label.place(x=x8, y=y3-15)
    
    ##########################################对图片进行大致的统计分析#############################################
    def function():
        global n,data,or_data#,start_date,end_date
        
        start_date = start.get()
        end_date = end.get()
        # 选择特定时间区间的参考数据
        np.random.seed(10)
        
 
        #计算区间的分位数
        # 区间股价图
        data = or_data.loc[start.get():end.get()]
        len_data = len(data)
        print('data1 is:',data)
        
        stock = data['Clsprc']
        stock_r = np.log(stock).diff().dropna()
            
        stock_vol = stock_r.std()/np.sqrt(1/252)
        
        backtest_pictureWidth = int(n * 400)
        backtest_pictureHeight = int(n * 240)
        
        #定义出图路径
        plot_name1 = '区间'+start_date+'到'+end_date+'Quantiles'
        outpath_plot1 = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))+'\\'+plot_name1+'.png'
            
        #出图
        fig1 = plt.figure(figsize=(15, 6))
        ax2 = fig1.add_subplot(1, 1, 1)
        plt.rcParams.update({'font.size': 12})
        plt.tick_params(labelsize=12)
        plt.subplots_adjust(top=0.90, bottom=0.10, right=1.00, left=0.08, hspace=0, wspace=0)#0.9,0.1,0.95,0.95,0.05,0,0
        sm.qqplot(stock_r,line='q').savefig(outpath_plot1)
            
        #读取Quantiles结果图    
        q_img = Image.open(resource_path(outpath_plot1)).resize((backtest_pictureWidth, backtest_pictureHeight), Image.ANTIALIAS)#
        q_pimg = ImageTk.PhotoImage(q_img)
        q_label = Label(root0, image=q_pimg)
        q_label.image = q_pimg
        q_label.place(x=x1, y=y7+120)#y=y7-10       
 
        #计算中证500自成立以来的日已实现波动率
        daily_volatility(or_data['Clsprc'])
        

    def daily_volatility(or_data):
        # 求每日已实现波动率
        TRADING_DAYS = 252
        returns = np.log(or_data/or_data.shift(1))
        print('returns is:',returns)
        returns.fillna(0, inplace=True)
        volatility = returns.rolling(window=TRADING_DAYS).std()*np.sqrt(TRADING_DAYS)
        print(' volatility is:',  volatility)
        
        #定义出图路径
        plot_name = '全部时间的已实现波动率'
        outpath_plot = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))+'\\'+plot_name+'.png'
        
        fig = plt.figure(figsize=(15, 7))
        ax1 = fig.add_subplot(1, 1, 1)
        volatility.plot(ax=ax1)
        ax1.set_xlabel('Date',size= 24)
        ax1.set_ylabel('Volatility',size=24)
        ax1.set_title('Annualized volatility for Apple Inc')
        plt.rcParams.update({'font.size': 24})
        plt.tick_params(labelsize=20)
        plt.subplots_adjust(top=0.90, bottom=0.10, right=0.98, left=0.08, hspace=0, wspace=0)#0.9,0.1,0.95,0.95,0.05,0,0
        plt.savefig(outpath_plot)
        
        #读取已实现波动率结果图
        backtest_pictureWidth = int(n * 400)
        backtest_pictureHeight = int(n * 240)
            
        acf_img = Image.open(resource_path(outpath_plot)).resize((backtest_pictureWidth, backtest_pictureHeight), Image.ANTIALIAS)#
        acf_pimg = ImageTk.PhotoImage(acf_img)
        acf_label = Label(root0, image=acf_pimg)
        acf_label.image = acf_pimg
        acf_label.place(x=x1, y=y3+120)#y=y7-10
        
        
 
    style_02 = Style()
    style_02.configure('PLot.TButton', font=('KaiTi', fontsize, 'bold'), foreground='black', backgroud='black')
    Plot_base = Button(root0, text='所选指标\n  作图', command=function, style='PLot.TButton')
    Plot_base.place(x=x1+30, y=y1+85, width=x2 - x1, height=y2 - y1)
    
    
    
 
    #计算两个日期相差天数，自定义函数名，和两个日期的变量名。
    def Caltime(date1,date2):
        #%Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
        #date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S") 
        #date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
        date1=time.strptime(date1,"%Y-%m-%d")
        date2=time.strptime(date2,"%Y-%m-%d")
        #根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
        #date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
        #date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
        date1=datetime.datetime(date1[0],date1[1],date1[2])
        date2=datetime.datetime(date2[0],date2[1],date2[2])
        #返回两个变量相差的值，就是相差天数
        return date2-date1
    
    #蒙特卡洛主函数
    def mento():
        global or_data, data#,s
        
        data = or_data.loc[start.get():end.get()]#将数据定义为[有数据的最后一日: 预计的结算日]
        vol_len = len(data)
        #data = data.drop(['Trddt'], axis=1)
        print('data2 is:',data)
        
        stock = data['Clsprc']
        stock_r = np.log(stock).diff().dropna()
        stock_vol = stock_r.std()/np.sqrt(1/vol_len)#original is 252
        #vol_write.set(round(stock_vol,4))
        
        if vol_write.get() != 'original':
            if round(float(vol_write.get()),4) == round(stock_vol,4):
                meishi = 0
            else:
                stock_vol = round(float(vol_write.get()),4)
                print('now stock_vol is:',stock_vol)
        
        
        n = len(data)
        d = 100000                      #模拟轨迹
        m = int(time_up.get())          #到期时间(月)
        
        ##########################计算距离产品到期时间长度###########################3
        start_date = start.get()
        end_date = end.get()
        year = end_date[0:4]
        month = end_date[5:7]
        day = end_date[8:10]
        
        if int(month)+m<=12:
            expir_month = str(int(month)+m)
            if len(expir_month)==1:
                expir_date =  year+'-0'+expir_month+'-'+day
            else:
                expir_date =  year+'-'+expir_month+'-'+day
        else:
            k = int(month)+m
            year_d = k/12
            year = year + year_d
            month = int(month)+m-year_d*12
            expir_month = str(month)
            if len(expir_month)==1:
                expir_date =  year+'-0'+expir_month+'-'+day
            else:
                expir_date =  year+'-'+expir_month+'-'+day
                
        print('end date is:',end_date)
        print('expir date is:',expir_date)
            
        dis_length = len(or_data.loc[end_date:expir_date])#Caltime(expir_date-start_date)
        #这个地方有一个问题，那就是expir_date可能超越现在的时点，可能无法定位，所以需要在excel中做长时间的交易日时间序列，归值为0.
        #只要end_date没有超越现有的时点即可，最好再加一个控件，告诉大家当前日期是多少。
        
        T = float(dis_length/252.)          #到期时间（以年为单位）original
        
        ############################蒙特卡洛参数设置##############################
        delta_t = 1./252.         #每个区间的时间长度,设1天为时间间隔
        r = 0.05            #利率
        cupoun_r1 = float(return_1.get())    #cupoun rate
        cupoun_r2 = float(return_2.get())
        cupoun_r3 = float(return_3.get())
        option = float(product_pc.get())    #产品价格
            
        s = np.zeros(dis_length)#array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])本来是dis_length+1
        f = np.zeros(d)
        f1 = np.zeros(d)
        f2 = np.zeros(d)
        f3 = np.zeros(d)
        condition1 = np.zeros(d)
        condition2 = np.zeros(d)
        condition3 = np.zeros(d)
        s.shape,f.shape
            
        s[0] = stock[n-1]   #最后一天的股价，即最原始价格
        K_out = s[0]*float(knock_out.get())
        K_in = s[0]*float(knock_in.get())
        
        ####################敲出观察日，np.arrange(起点，终点，步长)###############
        #obs_date = np.arange(1,m,12)+11  
        observe = []
        obs_date = []
        
        index_datelist = list(or_data.loc[end_date:expir_date].index)   
        print('index_datelist is:',index_datelist)
        
        for date in index_datelist[1:]:
            print('date is:',date)
            date1 = time.strptime(date,"%Y-%m-%d")
            date1_end = time.strptime(end_date,"%Y-%m-%d")
            
            if datetime.datetime(date1[0],date1[1],date1[2])==datetime.datetime(date1_end[0],date1_end[1],date1_end[2]):
                o=0
            else:
                date1_delta = str(datetime.datetime(date1[0],date1[1],date1[2])-datetime.datetime(date1_end[0],date1_end[1],date1_end[2]))
                date1_deltavalue = int(date1_delta[0:2])
                print('date1_deltavalue1 is:',date1_deltavalue)
                print('date1[2] is:',date1[2])
                print('dis_length is:',dis_length)
                if (date1[2]==11) :
                    if date1_deltavalue < dis_length:
                        print('date1_deltavalue2 is:',date1_deltavalue)
                        observe.append(date)
                        date1_deltavalue = date1_deltavalue-1
                        obs_date.append(date1_deltavalue)
                    #这个观察日序列是观察日-原始即检验的最后一天的日期的值。
        
        print('observe is:',observe)
        
        ############################开始蒙特卡洛##############################
        all_s = pd.DataFrame()
        
        for j in tqdm(range(0,100000)):#
            k_in = False
            k_out = False
            k = 0
            for i in range(1,dis_length):#总长是[1:dis_length]，是dis_length
                
                W = np.sqrt(delta_t) * np.random.randn(1)
                ret = (r - (1/2)*stock_vol**2) * delta_t + stock_vol * W
                s[i] = s[i-1]* np.e**ret
                    
                if s[i]>=K_out and i in obs_date:
                    if k_out == False:#保证在在第一次敲出的时候产品就结束了。
                        k_out = True
                        k=i
                    
                if s[i]<=K_in:
                    k_in = True
                        
            if k_out==True:
                f[j] = np.e**(-r*(k/252.))  * float(cupoun_r1) * k/252. *1000#option#k douwn change into 365
                f1[j] = float(cupoun_r1) * k/252.#option#k douwn change into 365
                condition1[j] = 1
            else:
                if k_in==False:
                    f[j] = np.e**(-r*T)  * float(cupoun_r2) * 60./360. * 1000#option#(T+180./360.)
                    f2[j] = float(cupoun_r2) * 60./360.#option#k douwn change into 365
                    condition2[j] = 1
                else:
                    f[j] = np.e**(-r*T)  * -max(0, float(s[0])-float(s[k]))/float(s[0]) * 1000#option
                    f3[j] =  -max(0, float(s[0])-float(s[k]))/float(s[0]) #option
                    condition3[j] = 1
            
            all_s[j]=s
            
        print('all_s is:',all_s)
            
        print('Product Price Estimate:',round(np.mean(f),4))
        print('Standard Error:',round(pd.np.std(f)/pd.np.sqrt(d),4))
       
        #产品价格及标准差统计
        product_et.set(round(np.mean(f),4))
        product_er.set(round(np.sqrt(d),4))
        
        #产品收益率统计
        sum1 = sum(condition1)
        sum2 = sum(condition2)
        sum3 = sum(condition3)
        
        ratio1 = sum1/100000.
        ratio2 = sum2/100000.
        ratio3 = sum3/100000.
        
        pro1_pre.set(round(ratio1,2))
        pro2_pre.set(round(ratio2,2))
        pro3_pre.set(round(ratio3,2))
        
        #每种情况的公平收益率为
        print('情况一的公平收益率为：',float(sum(f1))/sum1)
        print('情况二的公平收益率为：',float(sum(f2))/sum2)
        print('情况三的公平收益率为：',float(sum(f3))/sum3)
        
        all_r = cupoun_r1*ratio1 + cupoun_r2*ratio2 + -max(0, float(s[0])-float(s[k]))/float(s[0]) * (360./dis_length)*ratio3 
        product_r.set(round(all_r,4))
        product_re.set(round(all_r*(60./360.)*1000,4))
        
        '''
        predict_price = pd.DataFrame()
        predict_price['date'] = index_datelist
        predict_price['price'] = s
        
        csv_name2 = '区间'+end_date+'到'+expir_date+'predict_price'
        outpath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))+'\\'+csv_name2+'.csv'
        predict_price.to_csv(outpath)
        '''
        
        #stocklist = list(stock.values)
        #print('min is:',list(all_s.min(axis=0).min())[1])
        min_price = min(float(list(all_s.min(axis=0))[1]),float(list(all_s.min(axis=1))[1]))-1000.0
        max_price = max(float(list(all_s.max(axis=0))[1]),float(list(all_s.max(axis=1))[1]))+1000.0
        print('min price is:',min_price)
        print('max price is:',max_price)
        
        #plot_price(index_datelist,all_s,min_price,max_price,end_date,expir_date,stock[n-1])
        
    #function()
    
    def plot_price(xaxis,yaxis,minp,maxp,date1,date2,stocks):
        
        plt.rcParams['text.usetex']=True
        plt.rcParams['text.latex.preamble']=r'\makeatletter \newcommand*{\rom}[1]{\expandafter\@slowromancap\romannumeral #1@} \makeatother'
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.style.use('mystyle.mplstyle')
        
        #plt.style.use('mystyle.mplstyle')
        
        dates = xaxis

        xs = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
        
        for j in range(0,100000):#d
            ys = list(yaxis[j].values)
            plt.plot(xs, ys,  linewidth=0.7, linestyle='-')#color='c',
        #ys = yaxis
        plt.figure(num=1, figsize=(10,6))
        #plt.rcParams.update({'font.size': 20})
        #plt.tick_params(labelsize=24)
        # 配置横坐标
        #设置x y坐标轴范围
        plt.ylim( (minp, maxp) )#maxp(3000,7000)
        
        #设置x y坐标轴名称
        plt.xlabel("Data", fontsize=8)
        plt.ylabel("Predicted Price", fontsize=8 )
        
        plt.axhline(y=stocks,c="red", ls="-", lw="1");
        plt.gcf().autofmt_xdate() # 自动旋转日期标记
        #plt.show()
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.subplots_adjust(top=0.90, bottom=0.10, right=0.98, left=0.08, hspace=0, wspace=0)#0.9,0.1,0.95,0.95,0.05,0,0
        plt.margins(0, 0)
        #plt.savefig('flutter.pdf', dpi=600)
        #plt.savefig('flutter.png', dpi=600)
        #plt.savefig('flutter.svg', dpi=600)
        
        #定义出图路径
        backtest_pictureWidth = int(n * 420)
        backtest_pictureHeight = int(n * 252)
        plot_name2 = '区间'+date1+'到'+date2+'股价波动'
        outpath_plot2 = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))+'\\'+plot_name2+'.png'
            
        #出图
        plt.savefig(outpath_plot2,dpi=600)
        
        #读取est_price结果图    
        p_img = Image.open(resource_path(outpath_plot2)).resize((backtest_pictureWidth, backtest_pictureHeight), Image.ANTIALIAS)#
        p_pimg = ImageTk.PhotoImage(p_img)
        p_label = Label(root0, image=p_pimg)
        p_label.image = p_pimg
        p_label.place(x=x8, y=y3-15)#y=y7-10
    
    style_03 = Style()
    style_03.configure('Backtest.TButton', font=('KaiTi', fontsize, 'bold'), foreground='black', backgroud='black')
    backtest = Button(root0, text='所选指标\n  计算', command=mento, style='Backtest.TButton')
    backtest.place(x=x4+120, y=y3+245, width=(x2 - x1)/2, height=(y16 - y15)/2)
    
###########################################登陆界面#####################################
def mainwindow():
    window = Tk()  # Toplevel()
    # 窗口命名
    window.title('[期权与期货]基于蒙特卡洛的雪球产品定价')
    #########################################窗口布局#########################################
    # 获取屏幕分辨率
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    # 根据分辨率调节窗口和图片尺寸
    n = 3 * screenHeight / 4000
    winWidth = int(n * 650)
    winHeight = int(n * 770)
    pictureWidth = int(n * 650)
    pictureHeight = int(n * 770)
    # 各控件之间的相对距离，窗口示意图及各参数意义参见说明文档的示意图
    x1 = int(n * 150)
    x2 = int(n * 280)
    x3 = int(n * 250)
    x4 = int(n * 450)
    x5 = int(n * 470)
    x6 = int(n * 505)

    y1 = int(n * 550)
    y2 = int(n * 600)
    y3 = int(n * 650)
    y4 = int(n * 700)
    y5 = int(n * 720)
    y6 = int(n * 740)
    # 设置输入框宽度，按钮宽度和高度以及字体大小
    entryWidth = int(n * 200)
    buttonWidth = int(n * 150)
    buttonHeight = int(n * 45)
    fontsize = int(n * 20)
    fontsize2 = int(n * 10)
    # 窗口距电脑屏幕边缘空出的距离
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    # 放置窗口
    window.geometry("%sx%s+%s+%s" % (int(winWidth), int(winHeight), x, y))
    # 大小不可变
    window.resizable(0, 0)

    #########################################控件初始化#########################################
    #用logo作为封面，打开保存路径下的图片文件，resize调整尺寸，再转化为PhotoImage对象放在Label上
    img = Image.open(resource_path('menu_logo.png')).resize((pictureWidth, pictureHeight), Image.ANTIALIAS)
    pimg = ImageTk.PhotoImage(img)
    label = Label(window, image=pimg)
    label.image = pimg
    label.place(x=0, y=0)
    # 每创建一个控件就将其引用放入assembly列表
    assembly.append(label)
    
    # 放置标签：用户名和密码
    l1 = Label(window, text='用户名:', font=('KaiTi', fontsize))
    l1.place(x=x1, y=y1)
    l2 = Label(window, text='密码:', font=('KaiTi', fontsize))
    l2.place(x=x1, y=y2)
    assembly.append(l1)
    assembly.append(l2)

    # 放置标签：出品团队和出品时间
    l3 = Label(window, text='投资学18', font=('KaiTi', fontsize))#2
    l3.place(x=x6+2, y=y4-25)#4
    l4 = Label(window, text='只想搞钱组', font=('KaiTi', fontsize))
    l4.place(x=x6-5, y=y5-15)
    l5 = Label(window, text='2021年5月', font=('KaiTi', fontsize))
    l5.place(x=x6, y=y6-5)
    assembly.append(l3)
    assembly.append(l4)
    assembly.append(l5)

    # 用可变文字类型StringVar存放输入值
    var_usr_name = StringVar()
    var_usr_pwd = StringVar()
    # 放置输入框
    e1 = Entry(window, textvariable=var_usr_name)
    e1.place(x=x2, y=y1, width=entryWidth)
    e2 = Entry(window, textvariable=var_usr_pwd, show='*')
    e2.place(x=x2, y=y2, width=entryWidth)
    assembly.append(e1)
    assembly.append(e2)

    # 登录按钮
    def usr_login():
        # 获得StringVar存放的值
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()

        if usr_name == '' and usr_pwd == '':
            overview(window)
        else:
            messagebox.showerror(message='请检查您的用户名和密码是否输入正确。')

    # Style()类用来给文字设置字体颜色、大小、粗细、背景色等，但用于ttk自身的bug，有些功能无法实现。
    # 注意Style的命名规则，如果是用于Button的文字，命名需要用"xxx.TButton"形式，否则无法识别
    style = Style()
    style.configure('Login.TButton', font=('KaiTi', fontsize), foreground='black', backgroud='white')
    # 放置按钮
    Button_login = Button(window, text='登录', command=usr_login, style='Login.TButton')
    Button_login.place(x=x3, y=y3, width=buttonWidth, height=buttonHeight)
    assembly.append(Button_login)

    mainloop()


if __name__ == '__main__':
    global assembly, result, or_data, data,s#,start_date,end_date#,time_up,
    print('数据读取中...')
    # min_num, max_num = 0, 1
    
    path_way = os.getcwd()
    or_data = pd.read_excel(resource_path('data.xlsx'))#
    or_data.index = or_data['Trddt']
    or_data = or_data.drop(['Trddt'], axis=1)
    # 调整字体，显示负号
    mpl.rcParams['font.sans-serif'] = ['KaiTi']
    mpl.rcParams['font.serif'] = ['KaiTi']
    mpl.rcParams['axes.unicode_minus'] = False
    
    def remove_same(old_list):
        new_list = []
        for i in old_list:
            if i not in new_list:
                new_list.append(i)
        return new_list

    # 全局变量，创建控件时用于存放控件的引用，当切换界面时，删除对应页面上的控件
    
    print('数据读取完毕。')
    assembly = []
    result = []

    mainwindow()
