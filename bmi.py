from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import random

gok = [8,9,9,10,10,11,11,12,12,13,14,14,15,16]
u_ju = 0
u_jung = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,]
veg = [6,6,7,7,8,8,8,8,9,9,9,9,9,9]
fat = [3,3,4,4,5,5,5,5,6,6,6,7,7,7]
milk = [0,0,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
fruit = [1,1,1,1,2,2,2,2,3,3,3,3,3,3]

global gun_num
gun_num = 0

gok_list = {"쌀밥" : 70, "보리밥" : 70, "현미밥" : 70, "쌀죽" : 140, "식빵" : 35}
u_ju_list = {"광어" : 50, "조기" : 50, "코다리" : 50, "오리고기" : 40, "참치" : 50}
u_jung_list = {"돼지고기 안심" : 40, "소고기 등심" : 40, "갈치" : 50, "두부" : 80, "꽁치" : 50}
veg_list = {"단호박" : 40, "애호박" : 70, "도라지" : 40, "연근" : 40, "시금치" : 70}
fat_list = {'잣' : 8, '호두' : 8, "땅콩" : 8, "아몬드" : 8, "캐슈넛" : 8}
milk_list = {"우유" : 200, "두유" : 200}
fruit_list = {"귤" : 120, "바나나": 50, "배" : 110, "단감" : 50, "수박" : 150}

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

your_bmi = 'hello'
######################################################################################
#                                harris benedict시작                                 #
######################################################################################

def man0(): 

    global your_bmi
    global weight

    weight = float(weight_insert0.get())
    height = float(height_insert0.get())
    age = float(age_insert0.get())
    
    bmi_man = 66.47 + (13.75*weight) + (5*height) - (6.76*age)
    bmi_woman = 655.1 + (9.56*weight) + (1.85*height) - (4.68*age)

    bmi_man = round(bmi_man,2) 
    bmi_woman = round(bmi_woman,2)

    your_bmi = bmi_man 
    bmi_out0.insert(0, str(your_bmi))

    return your_bmi

def woman0():

    global your_bmi
    global weight

    weight = float(weight_insert0.get())
    height = float(height_insert0.get())
    age = float(age_insert0.get())
    
    bmi_man = 66.47 + (13.75*weight) + (5*height) - (6.76*age)
    bmi_woman = 655.1 + (9.56*weight) + (1.85*height) - (4.68*age)

    bmi_man = round(bmi_man,2) 
    bmi_woman = round(bmi_woman,2) 

    your_bmi = bmi_woman
    bmi_out0.insert(0, str(your_bmi))

    return your_bmi

l1 = Label(fixed, text="몸무게") #입력받을 값들의 이름을 tkinter내에 나오게 하는 코드들
l2 = Label(fixed, text="키")
l3 = Label(fixed, text="나이") 
l4 = Label(fixed, text="성별")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)

weight_insert0 = Entry(fixed)#입력창을 만드는 함수
height_insert0 = Entry(fixed)
age_insert0 = Entry(fixed)

weight_insert0.grid(row=0, column=1)
height_insert0.grid(row=1, column=1)
age_insert0.grid(row=2, column=1)

b_man = Button(fixed, text="남성", command=man0, height = 1, width = 3, bg = 'azure')
b_man.grid(row=3, column=1)

b_woman = Button(fixed, text="여성", command=woman0, height = 1, width = 3, bg = 'azure')
b_woman.grid(row=4, column=1)

################################################################################
#                                활동대사량 시작                                #
################################################################################


def one():
    global real_bmi

    real_bmi = your_bmi * 1.2
    real_bmi = round(real_bmi,2)
    real_bmi_output.insert(0, str(real_bmi))

def two():
    global real_bmi

    real_bmi = your_bmi * 1.375
    real_bmi = round(real_bmi,2)
    real_bmi_output.insert(0, str(real_bmi))

def three():
    global real_bmi

    real_bmi = your_bmi * 1.55
    real_bmi = round(real_bmi,2)
    real_bmi_output.insert(0, str(real_bmi))

def four():
    global real_bmi

    real_bmi = your_bmi * 1.725
    real_bmi = round(real_bmi,2)
    real_bmi_output.insert(0, str(real_bmi))

def five():
    global real_bmi

    real_bmi = your_bmi * 1.9
    real_bmi = round(real_bmi,2)
    real_bmi_output.insert(0, str(real_bmi))

l1 = Label(fixed, text="    많이 적음") 
l2 = Label(fixed, text="    약간 적음")
l3 = Label(fixed, text="    보통") 
l4 = Label(fixed, text="    약간 많음")
l5 = Label(fixed, text="    많이 많음") 

l1.grid(row=0, column=3)
l2.grid(row=1, column=3)
l3.grid(row=2, column=3)
l4.grid(row=3, column=3)
l5.grid(row=4, column=3)

blank_text0 = Label(fixed, text="   ")
blank_text0.grid(row=0, column=4)


blank_text1 = Label(fixed, text="    ")
blank_text1.grid(row=1, column=4)

blank_text2 = Label(fixed, text="    ")
blank_text2.grid(row=0, column=6)

blank_text3 = Label(fixed, text="    ")
blank_text3.grid(row=1, column=6)

bmi_out0_text = Label(fixed, text="추천 BMI")#출력시킬 값들의 이름을 적고 출력창을 tkinter내에 만드는 코드들
bmi_out0_text.grid(row=0, column=7)
bmi_out0 = Entry(fixed)
bmi_out0.grid(row=0, column=8)

real_bmi_output_text = Label(fixed, text="활동량 고려 BMI")
real_bmi_output_text.grid(row=1, column=7)
real_bmi_output = Entry(fixed)
real_bmi_output.grid(row=1, column=8)

# b_0 = Button(fixed,text="그림", command=zero,height = 1, width = 3, bg = 'azure')
# b_0.grid(row=7, column=5)

b_1 = Button(fixed,text="계산", command=one,height = 1, width = 3, bg = 'azure')
b_1.grid(row=0, column=5)

b_2 = Button(fixed,text="계산", command=two,height = 1, width = 3, bg = 'azure')
b_2.grid(row=1, column=5)

b_3 = Button(fixed,text="계산", command=three,height = 1, width = 3, bg = 'azure')
b_3.grid(row=2, column=5)

b_4 = Button(fixed,text="계산", command=four,height = 1, width = 3, bg = 'azure')
b_4.grid(row=3, column=5)

b_5 = Button(fixed,text="계산", command=five,height = 1, width = 3, bg = 'azure')
b_5.grid(row=4, column=5)

################################################################################
#                                감량기간 설정                                  #
################################################################################

def process3():
    global can_eat_kcal
    global gun_num

    want_kg = float(kg_insert2.get())
    want_day = float(day_insert2.get())

    can_eat_kcal = real_bmi - ((weight - want_kg)*7700 / want_day)
    can_eat_kcal = round(can_eat_kcal,2)
    vc_out2.insert(0, str(can_eat_kcal))
    
    if can_eat_kcal >= 1200 and can_eat_kcal < 1300:
        gun_num = 0
        gun_num = int(gun_num)

    elif can_eat_kcal >= 1300 and can_eat_kcal < 1400:
        gun_num = 1
        gun_num = int(gun_num)

    elif can_eat_kcal >= 1400 and can_eat_kcal < 1500:
        gun_num = 2
        gun_num = int(gun_num)

    elif can_eat_kcal >= 1500 and can_eat_kcal < 1600:
        gun_num = 3
        gun_num = int(gun_num)

    elif can_eat_kcal >= 1600 and can_eat_kcal < 1700:
        gun_num = 4
        gun_num = int(gun_num)

    elif can_eat_kcal >= 1700 and can_eat_kcal < 1800:
        gun_num = 5
        gun_num = int(gun_num)

    elif can_eat_kcal >= 1800 and can_eat_kcal < 1900:
        gun_num = 6
        gun_num = int(gun_num)

    elif can_eat_kcal >= 1900 and can_eat_kcal < 2000:
        gun_num = 7
        gun_num = int(gun_num)

    elif can_eat_kcal >= 2000 and can_eat_kcal < 2100:
        gun_num = 8
        gun_num = int(gun_num)

    elif can_eat_kcal >= 2100 and can_eat_kcal < 2200:
        gun_num = 9
        gun_num = int(gun_num)

    elif can_eat_kcal >= 2200 and can_eat_kcal < 2300:
        gun_num = 10
        gun_num = int(gun_num)

    elif can_eat_kcal >= 2300 and can_eat_kcal < 2400:
        gun_num = 11
        gun_num = int(gun_num)

    elif can_eat_kcal >= 2400 and can_eat_kcal < 2500:
        gun_num = 12
        gun_num = int(gun_num)
    
    elif can_eat_kcal >= 2500 and can_eat_kcal < 2600:
        gun_num = 13
        gun_num = int(gun_num)

    
    gok_out.insert(0, str(gok[gun_num]))
    u_ju_out.insert(0, str(u_ju))
    u_jung_out.insert(0, str(u_jung[gun_num]))
    veg_out.insert(0, str(veg[gun_num]))
    fat_out.insert(0, str(fat[gun_num]))
    milk_out.insert(0, str(milk[gun_num]))
    fruit_out.insert(0, str(fruit[gun_num]))

l1 = Label(emiter, text="원하는 몸무게")
l2 = Label(emiter, text="예상 감량기간") 

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

kg_insert2 = Entry(emiter)
day_insert2 = Entry(emiter)

kg_insert2.grid(row=0, column=1)
day_insert2.grid(row=1, column=1)

vc_out2_text = Label(emiter, text="하루 섭취칼로리")
vc_out2_text.grid(row=0, column=3)
vc_out2 = Entry(emiter)
vc_out2.grid(row=0, column=4)

blank_text4 = Label(emiter, text="   ")
blank_text4.grid(row=2, column=0)

gok_out_text = Label(emiter, text="곡류군")
gok_out_text.grid(row=3, column=0)
gok_out = Entry(emiter)
gok_out.grid(row=3, column=1)

u_ju_out_text = Label(emiter, text="어육류 저지방")
u_ju_out_text.grid(row=4, column=0)
u_ju_out = Entry(emiter)
u_ju_out.grid(row=4, column=1)

u_jung_out_text = Label(emiter, text="어육류 고지방")
u_jung_out_text.grid(row=5, column=0)
u_jung_out = Entry(emiter)
u_jung_out.grid(row=5, column=1)

veg_out_text = Label(emiter, text="채소군")
veg_out_text.grid(row=6, column=0)
veg_out = Entry(emiter)
veg_out.grid(row=6, column=1)

fat_out_text = Label(emiter, text="지방군")
fat_out_text.grid(row=7, column=0)
fat_out = Entry(emiter)
fat_out.grid(row=7, column=1)

milk_out_text = Label(emiter, text="우유군")
milk_out_text.grid(row=8, column=0)
milk_out = Entry(emiter)
milk_out.grid(row=8, column=1)

fruit_out_text = Label(emiter, text="과일군")
fruit_out_text.grid(row=9, column=0)
fruit_out = Entry(emiter)
fruit_out.grid(row=9, column=1)

b_01 = Button(emiter,text="계산", command=process3,height = 1, width = 3, bg = 'azure')
b_01.grid(row=12, column=2)

################################################################################
#                                   식단추천                                    #
################################################################################

def chuchun():
    
    name0 = list(gok_list.keys())
    ran0 = random.randrange(0,len(name0))
    gok_out2.insert(0, str(name0[ran0]))
    gok_out_weight.insert(0, str(gok_list['{0}'.format(name0[ran0])] * gok[gun_num] / 3))

    name1 = list(u_ju_list.keys())
    ran1 = random.randrange(0,len(name1))
    u_ju_out2.insert(0, str(name1[ran1]))
    u_ju_out_weight.insert(0, str(u_ju_list['{0}'.format(name1[ran1])] * u_ju / 3))

    name2 = list(u_jung_list.keys())
    ran2 = random.randrange(0,len(name2))
    u_jung_out2.insert(0, str(name2[ran2]))
    u_jung_out_weight.insert(0, str(u_jung_list['{0}'.format(name2[ran2])] * u_jung[gun_num] / 3))

    name3 = list(veg_list.keys())
    ran3 = random.randrange(0,len(name3))
    veg_out2.insert(0, str(name3[ran3]))
    veg_out_weight.insert(0, str(veg_list['{0}'.format(name3[ran3])] * veg[gun_num] / 3))

    name4 = list(fat_list.keys())
    ran4 = random.randrange(0,len(name4))    
    fat_out2.insert(0, str(name4[ran4]))
    fat_out_weight.insert(0, str(fat_list['{0}'.format(name4[ran4])] * fat[gun_num] / 3))

    name5 = list(milk_list.keys())
    ran5 = random.randrange(0,len(name5))
    milk_out2.insert(0, str(name5[ran5]))
    milk_out_weight.insert(0, str(milk_list['{0}'.format(name5[ran5])] * milk[gun_num] / 3))

    name6 = list(fruit_list.keys())
    ran6 = random.randrange(0,len(name6))
    fruit_out2.insert(0, str(name6[ran6]))
    fruit_out_weight.insert(0, str(fruit_list['{0}'.format(name6[ran6])] * fruit[gun_num] / 3))

gok_out2_text = Label(voltage_divider, text="곡류 추천")
gok_out2_text.grid(row=3, column=3)
gok_out2 = Entry(voltage_divider)
gok_out2.grid(row=3, column=4)
gok_out_weight = Entry(voltage_divider)
gok_out_weight.grid(row=3, column=5)

u_ju_out2_text = Label(voltage_divider, text="어육류 저지방 추천")
u_ju_out2_text.grid(row=4, column=3)
u_ju_out2 = Entry(voltage_divider)
u_ju_out2.grid(row=4, column=4)
u_ju_out_weight = Entry(voltage_divider)
u_ju_out_weight.grid(row=4, column=5)

u_jung_out2_text = Label(voltage_divider, text="어육류 고지방 추천")
u_jung_out2_text.grid(row=5, column=3)
u_jung_out2 = Entry(voltage_divider)
u_jung_out2.grid(row=5, column=4)
u_jung_out_weight = Entry(voltage_divider)
u_jung_out_weight.grid(row=5, column=5)

veg_out2_text = Label(voltage_divider, text="채소군 추천")
veg_out2_text.grid(row=6, column=3)
veg_out2 = Entry(voltage_divider)
veg_out2.grid(row=6, column=4)
veg_out_weight = Entry(voltage_divider)
veg_out_weight.grid(row=6, column=5)

fat_out2_text = Label(voltage_divider, text="지방군 추천")
fat_out2_text.grid(row=7, column=3)
fat_out2 = Entry(voltage_divider)
fat_out2.grid(row=7, column=4)
fat_out_weight = Entry(voltage_divider)
fat_out_weight.grid(row=7, column=5)

milk_out2_text = Label(voltage_divider, text="우유군 추천")
milk_out2_text.grid(row=8, column=3)
milk_out2 = Entry(voltage_divider)
milk_out2.grid(row=8, column=4)
milk_out_weight = Entry(voltage_divider)
milk_out_weight.grid(row=8, column=5)

fruit_out2_text = Label(voltage_divider, text="과일군 추천")
fruit_out2_text.grid(row=9, column=3)
fruit_out2 = Entry(voltage_divider)
fruit_out2.grid(row=9, column=4)
fruit_out_weight = Entry(voltage_divider)
fruit_out_weight.grid(row=9, column=5)

blank_text5 = Label(voltage_divider, text="   ")
blank_text5.grid(row=11, column=2)

blank_text6 = Label(voltage_divider, text="   ")
blank_text6.grid(row=11, column=3)

b_01 = Button(voltage_divider,text="변환", command=chuchun,height = 1, width = 3, bg = 'azure')
b_01.grid(row=12, column=3)

window.mainloop() 