from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import random

window = tk.Tk()         
window.title("BMI측정 및 식단추천")  
tabControl = ttk.Notebook(window)         

tab1 = ttk.Frame(tabControl)           
tabControl.add(tab1, text='Harris-Benedict') #첫번째 탭 fixed bias 생성

tab2 = ttk.Frame(tabControl)           
tabControl.add(tab2, text='활동 대샤랑') #두번째 탭 emiter bias 생성 

tab3 = ttk.Frame(tabControl)           
tabControl.add(tab3, text='식단추천') #세번째 탭 voltage divider 생성

tabControl.pack(expand=1, fill="both")  

fixed = ttk.LabelFrame(tab1, text='Harris-Benedict')
fixed.grid(column=0, row=0, padx=8, pady=4)

emiter = ttk.LabelFrame(tab2, text='활동 대샤랑')
emiter.grid(column=0, row=0, padx=8, pady=4)

voltage_divider = ttk.LabelFrame(tab3, text='식단추천')
voltage_divider.grid(column=0, row=0, padx=8, pady=4)

a_label = ttk.Label(fixed)
a_label.grid(column=0, row=0)

gok_ = 0
uju_ = 0
ujung_ = 0
veg_ = 0#입력창을 만드는 함수
fat_ = 0
milk_ = 0
fruit_ = 0#입력창을 만드는 함수

gok0_ = 0
uju0_ = 0
ujung0_ = 0
veg0_ = 0#입력창을 만드는 함수
fat0_ = 0
milk0_ = 0
fruit0_ = 0#입력창을 만드는 함수

tan = 0
dan = 0
ji = 0

tan_ = 0
dan_ = 0
ji_ = 0
######################################################################################
#                                harris benedict시작                                 #
######################################################################################

def plus0():

    global gok_
    global gok0_ 
    global tan
    global dan
    global ji

    gok.delete("0","end")
    gok0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    tan = tan + 23
    dan = dan + 2
    ji = ji + 0

    gok_ = gok_ + 1
    gok0_ = gok0_ + 100

    gok.insert(0, str(gok_))
    gok0.insert(0, str(gok0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))

def plus1():

    global uju_
    global uju0_ 
    global tan
    global dan
    global ji

    tan = tan + 0
    dan = dan + 8
    ji = ji + 2

    uju.delete("0","end")
    uju0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    uju_ = uju_ + 1
    uju0_ = uju0_ + 50

    uju.insert(0, str(uju_))
    uju0.insert(0, str(uju0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))


def plus2():

    global ujung_
    global ujung0_ 
    global tan
    global dan
    global ji

    tan = tan + 0
    dan = dan + 8
    ji = ji + 5

    ujung.delete("0","end")
    ujung0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    ujung_ = ujung_ + 1
    ujung0_ = ujung0_ + 75

    ujung.insert(0, str(ujung_))
    ujung0.insert(0, str(ujung0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))


def plus3():

    global veg_
    global veg0_ 
    global tan
    global dan
    global ji

    tan = tan + 3
    dan = dan + 2
    ji = ji + 0

    veg.delete("0","end")
    veg0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    veg_ = veg_ + 1
    veg0_ = veg0_ + 20

    veg.insert(0, str(veg_))
    veg0.insert(0, str(veg0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))

def plus4():

    global fat_
    global fat0_ 
    global tan
    global dan
    global ji

    tan = tan + 0
    dan = dan + 0
    ji = ji + 5

    fat.delete("0","end")
    fat0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    fat_ = fat_ + 1
    fat0_ = fat0_ + 45

    fat.insert(0, str(fat_))
    fat0.insert(0, str(fat0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))


def plus5():

    global milk_
    global milk0_ 
    global tan
    global dan
    global ji

    tan = tan + 10
    dan = dan + 6
    ji = ji + 2

    milk.delete("0","end")
    milk0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    milk_ = milk_ + 0.5
    milk0_ = milk0_ + 40

    milk.insert(0, str(milk_))
    milk0.insert(0, str(milk0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))


def plus6():

    global fruit_
    global fruit0_ 
    global tan
    global dan
    global ji

    fruit.delete("0","end")
    fruit0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    tan = tan + 12
    dan = dan + 0
    ji = ji + 0
    
    yung_sum = tan + dan + ji
    tan_ = tan / yung_sum * 100
    dan_ = dan / yung_sum * 100
    ji_ = ji / yung_sum * 100

    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))

    fruit_ = fruit_ + 1
    fruit0_ = fruit0_ + 50

    fruit.insert(0, str(fruit_))
    fruit0.insert(0, str(fruit0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    

############################
#          빼기
############################

def minus0():

    global gok_
    global gok0_ 
    global tan
    global dan
    global ji

    gok.delete("0","end")
    gok0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    tan = tan - 23
    dan = dan - 2
    ji = ji - 0

    gok_ = gok_ - 1
    gok0_ = gok0_ - 100

    gok.insert(0, str(gok_))
    gok0.insert(0, str(gok0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))

def minus1():

    global uju_
    global uju0_ 
    global tan
    global dan
    global ji

    tan = tan - 0
    dan = dan - 8
    ji = ji - 2

    uju.delete("0","end")
    uju0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    uju_ = uju_ - 1
    uju0_ = uju0_ - 50

    uju.insert(0, str(uju_))
    uju0.insert(0, str(uju0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))


def minus2():

    global ujung_
    global ujung0_ 
    global tan
    global dan
    global ji

    tan = tan - 0
    dan = dan - 8
    ji = ji - 5

    ujung.delete("0","end")
    ujung0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    ujung_ = ujung_ - 1
    ujung0_ = ujung0_ - 75

    ujung.insert(0, str(ujung_))
    ujung0.insert(0, str(ujung0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))


def minus3():

    global veg_
    global veg0_ 
    global tan
    global dan
    global ji

    tan = tan - 3
    dan = dan - 2
    ji = ji - 0

    veg.delete("0","end")
    veg0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    veg_ = veg_ - 1
    veg0_ = veg0_ - 20

    veg.insert(0, str(veg_))
    veg0.insert(0, str(veg0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))

def minus4():

    global fat_
    global fat0_ 
    global tan
    global dan
    global ji

    tan = tan - 0
    dan = dan - 0
    ji = ji - 5

    fat.delete("0","end")
    fat0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    fat_ = fat_ - 1
    fat0_ = fat0_ - 45

    fat.insert(0, str(fat_))
    fat0.insert(0, str(fat0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))


def minus5():

    global milk_
    global milk0_ 
    global tan
    global dan
    global ji

    tan = tan - 10
    dan = dan - 6
    ji = ji - 2

    milk.delete("0","end")
    milk0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    milk_ = milk_ - 0.5
    milk0_ = milk0_ - 40

    milk.insert(0, str(milk_))
    milk0.insert(0, str(milk0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

    yung_sum = tan + dan + ji
    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))


def minus6():

    global fruit_
    global fruit0_ 
    global tan
    global dan
    global ji

    fruit.delete("0","end")
    fruit0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    tan = tan - 12
    dan = dan - 0
    ji = ji - 0
    
    yung_sum = tan + dan + ji
    tan_ = tan / yung_sum * 100
    dan_ = dan / yung_sum * 100
    ji_ = ji / yung_sum * 100

    tan_ = round((tan / yung_sum )* 100,2)
    dan_ = round((dan / yung_sum )* 100,2)
    ji_ = round((ji / yung_sum )* 100,2)

    tan0.insert(0, str(tan_))
    dan0.insert(0, str(dan_))
    ji0.insert(0, str(ji_))

    fruit_ = fruit_ - 1
    fruit0_ = fruit0_ - 50

    fruit.insert(0, str(fruit_))
    fruit0.insert(0, str(fruit0_))
    Sum = gok0_ + uju0_ + ujung0_ + veg0_ + fat0_ + milk0_ + fruit0_ 
    sum0.insert(0, str(Sum))

def clear():

    global tan
    global dan
    global ji
    global tan_
    global dan_
    global ji_

    global gok_
    global uju_
    global ujung_
    global veg_
    global fat_
    global milk_
    global fruit_

    global gok0_ 
    global uju0_ 
    global ujung0_
    global veg0_ 
    global fat0_ 
    global milk0_ 
    global fruit0_ 

    gok.delete("0","end")
    gok0.delete("0","end")
    uju.delete("0","end")
    uju0.delete("0","end")
    ujung.delete("0","end")
    ujung0.delete("0","end")
    veg.delete("0","end")
    veg0.delete("0","end")
    fat.delete("0","end")
    fat0.delete("0","end")
    milk.delete("0","end")
    milk0.delete("0","end")
    fruit.delete("0","end")
    fruit0.delete("0","end")
    sum0.delete("0","end")
    tan0.delete("0","end")
    dan0.delete("0","end")
    ji0.delete("0","end")

    gok.insert(0,0)
    gok0.insert(0,0)
    uju.insert(0,0)
    uju0.insert(0,0)
    ujung.insert(0,0)
    ujung0.insert(0,0)
    veg.insert(0,0)
    veg0.insert(0,0)
    fat.insert(0,0)
    fat0.insert(0,0)
    milk.insert(0,0)
    milk0.insert(0,0)
    fruit.insert(0,0)
    fruit0.insert(0,0)
    sum0.insert(0,0)
    tan0.insert(0,0)
    dan0.insert(0,0)
    ji0.insert(0,0)

    tan = 0
    dan = 0
    ji = 0

    tan_ = 0
    dan_ = 0
    ji_ = 0

    gok_ = 0
    uju_ = 0
    ujung_ = 0
    veg_ = 0#입력창을 만드는 함수
    fat_ = 0
    milk_ = 0
    fruit_ = 0#입력창을 만드는 함수

    gok0_ = 0
    uju0_ = 0
    ujung0_ = 0
    veg0_ = 0#입력창을 만드는 함수
    fat0_ = 0
    milk0_ = 0
    fruit0_ = 0#입력창을 만드는 함수


############################
#          교환단위
############################

l1 = Label(fixed, text="곡류") #입력받을 값들의 이름을 tkinter내에 나오게 하는 코드들
l2 = Label(fixed, text="어육류 저")
l3 = Label(fixed, text="어육류 중") 
l4 = Label(fixed, text="채소")
l5 = Label(fixed, text="지방")
l6 = Label(fixed, text="어유")
l7 = Label(fixed, text="과일")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)
l5.grid(row=4, column=0)
l6.grid(row=5, column=0)
l7.grid(row=6, column=0)

gok = Entry(fixed)#입력창을 만드는 함수
uju = Entry(fixed)
ujung = Entry(fixed)
veg = Entry(fixed)#입력창을 만드는 함수
fat = Entry(fixed)
milk = Entry(fixed)
fruit = Entry(fixed)#입력창을 만드는 함수

gok.grid(row=0, column=1)
uju.grid(row=1, column=1)
ujung.grid(row=2, column=1)
veg.grid(row=3, column=1)
fat.grid(row=4, column=1)
milk.grid(row=5, column=1)
fruit.grid(row=6, column=1)

############################
#           kcal
############################

l10 = Label(fixed, text="곡류") #입력받을 값들의 이름을 tkinter내에 나오게 하는 코드들
l20 = Label(fixed, text="어육류 저")
l30 = Label(fixed, text="어육류 중") 
l40 = Label(fixed, text="채소")
l50 = Label(fixed, text="지방")
l60 = Label(fixed, text="어유")
l70 = Label(fixed, text="과일")
l80 = Label(fixed, text="합계")

l100 = Label(fixed, text="탄수화물")
l200 = Label(fixed, text="단백질")
l300 = Label(fixed, text="지방")

l10.grid(row=0, column=3)
l20.grid(row=1, column=3)
l30.grid(row=2, column=3)
l40.grid(row=3, column=3)
l50.grid(row=4, column=3)
l60.grid(row=5, column=3)
l70.grid(row=6, column=3)
l80.grid(row=7, column=3)

l100.grid(row=0, column=5)
l200.grid(row=1, column=5)
l300.grid(row=2, column=5)

gok0 = Entry(fixed)#입력창을 만드는 함수
uju0 = Entry(fixed)
ujung0 = Entry(fixed)
veg0 = Entry(fixed)#입력창을 만드는 함수
fat0 = Entry(fixed)
milk0 = Entry(fixed)
fruit0 = Entry(fixed)#입력창을 만드는 함수
sum0 = Entry(fixed)#입력창을 만드는 함수
tan0 = Entry(fixed)
dan0 = Entry(fixed)
ji0 = Entry(fixed)

gok0.grid(row=0, column=4)
uju0.grid(row=1, column=4)
ujung0.grid(row=2, column=4)
veg0.grid(row=3, column=4)
fat0.grid(row=4, column=4)
milk0.grid(row=5, column=4)
fruit0.grid(row=6, column=4)
sum0.grid(row=7, column=4)

tan0.grid(row=0, column=6)
dan0.grid(row=1, column=6)
ji0.grid(row=2, column=6)

############################
#          더하기
############################

b_man0 = Button(fixed, text="곡+", command=plus0, height = 1, width = 5, bg = 'azure')
b_man0.grid(row=7, column=0)

b_man1 = Button(fixed, text="어저+", command=plus1, height = 1, width = 5, bg = 'azure')
b_man1.grid(row=8, column=0)

b_man2 = Button(fixed, text="어중+", command=plus2, height = 1, width = 5, bg = 'azure')
b_man2.grid(row=9, column=0)

b_man3 = Button(fixed, text="채소+", command=plus3, height = 1, width = 5, bg = 'azure')
b_man3.grid(row=10, column=0)

b_man4 = Button(fixed, text="지방+", command=plus4, height = 1, width = 5, bg = 'azure')
b_man4.grid(row=11, column=0)

b_man5 = Button(fixed, text="우유+", command=plus5, height = 1, width = 5, bg = 'azure')
b_man5.grid(row=12, column=0)

b_man6 = Button(fixed, text="과일+", command=plus6, height = 1, width = 5, bg = 'azure')
b_man6.grid(row=13, column=0)

############################
#          빼기
############################

b_man0 = Button(fixed, text="곡-", command=minus0, height = 1, width = 5, bg = 'azure')
b_man0.grid(row=7, column=1)

b_man1 = Button(fixed, text="어저-", command=minus1, height = 1, width = 5, bg = 'azure')
b_man1.grid(row=8, column=1)

b_man2 = Button(fixed, text="어중-", command=minus2, height = 1, width = 5, bg = 'azure')
b_man2.grid(row=9, column=1)

b_man3 = Button(fixed, text="채소-", command=minus3, height = 1, width = 5, bg = 'azure')
b_man3.grid(row=10, column=1)

b_man4 = Button(fixed, text="지방-", command=minus4, height = 1, width = 5, bg = 'azure')
b_man4.grid(row=11, column=1)

b_man5 = Button(fixed, text="우유-", command=minus5, height = 1, width = 5, bg = 'azure')
b_man5.grid(row=12, column=1)

b_man6 = Button(fixed, text="과일-", command=minus6, height = 1, width = 5, bg = 'azure')
b_man6.grid(row=13, column=1)

b_man7 = Button(fixed, text="클리어-", command=clear, height = 1, width = 5, bg = 'azure')
b_man7.grid(row=14, column=1)

window.mainloop() 