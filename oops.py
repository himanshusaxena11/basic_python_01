# -*- coding: utf-8 -*-
"""OOPS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nFR_0da4mO-CB_aKliO8fy7GpM99cin5
"""

#Make class of students having name and marks and make an object to get the output

#class
class student:
  name='jf'
  marks=73

#object
s=student()
s.name

s.marks

s.name,s.marks

class student:                            #jab class me koi func banta he to self use karte he
  def info(self,name,marks):              #self se func ki properties ka access class ko milta he
    return (name,marks)

s=student()
s.info('d',23)

class colleague:
  def info(self,name,marks):                     #class me define ki hui properties pehle chalti he
    name='y'                                      # agar object me properties define ki hui he fir bhi class ki properties phle chlengi
    marks=56
    return (name,marks)

c=colleague()
c.info('h',83)

c.info('k',93)

#max no in list using func
def maxm():
  a=[4,8,89,12,23,68,-3,56]
  max=a[0]
  for i in a:
    if i>max:
      max=i
  print('max is',max)

maxm()

#Wap to make a class of simplified arithmetic operator and try to get o/p of that class through object
class arith:
  def oprtn(self,a,b):
    add=a+b
    sub=a-b
    mult=a*b
    div=a/b
    return ('add--',add,'sub--',sub,'mult--',mult,'div---',div)     #return not used bcz it gives single o/p of code in func while print is used to print operations in code

a=arith()
a.oprtn(6,3)

#Wap to make a class of simplified arithmetic operator and try to get o/p of that class through object
class arith:
  def oprtn(self,a,b):
    add=a+b
    sub=a-b
    mult=a*b
    div=a/b
    print ('add--',add,'sub--',sub,'mult--',mult,'div---',div)

a=arith()
a.oprtn(6,3)

#Wap to make a class of simplified arithmetic operator and try to get o/p of that class through object   #USER INPUT
class arit:
  def oprn(self,a=int(input('enter no')),b=int(input('enter no'))):
    add=a+b
    sub=a-b
    mult=a*b
    div=a/b
    print ('add--',add,'sub--',sub,'mult--',mult,'div---',div)

r=arit()
r.oprn()

#Wap to make a class of simplified arithmetic operator and try to get o/p of that class through object      #USER INPUT
class arit:
  def oprn(self):
    a=int(input('enter no'))
    b=int(input('enter no'))
    add=a+b
    sub=a-b
    mult=a*b
    div=a/b
    print ('add--',add,'sub--',sub,'mult--',mult,'div---',div)

r=arit()
r.oprn()

## wap to make a class of car and find its actual price if the car is of more than 10 lakh then there is a tax of 14% on the car and if the cost is less than 10 lakh then
#there is a discount of 7.8 % on the car.find the actual price of the car paid by the user
class car():
  def info(self,price):
    if price>1000000:
      act_price=price+((14/100)*price)
      print('actual price is',act_price)
    else:
      act_price=price-((7.8/100)*price)
      print('actual price is',act_price)

t=car()
t.info(1100000)

# Find max no with the help of func
v=[5,3,8,2,7]
def fun(v):
  max=v[0]
  for i in v:
    if i>max:
      max=i
      print('max is',max)

fun(v)

#Find 2nd highest no
v=[5,3,8,2,7]
v.sort()
v[-2]

