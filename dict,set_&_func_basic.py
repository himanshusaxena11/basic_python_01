# -*- coding: utf-8 -*-
"""Dict,Set & Func Basic

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18yenc2pghBy8a9IouCzfiW5rkneWXxNs
"""

x={'name':'q',
   'age':12
   }

x

type(x)

# Dict having emp name,id and salary
q={
    'name':('e','r','y','g'),
    'id':[342,23,56,134],
    'salary':(6382,738,9392,3738)
}

q

q['salary'][1]

q['id'][2]=929

q

# Empty dict
y={

}

type(y)

# Single element dict
p={'age':12}

type(p)

#FUNCTION

# Add 2 nos using fn
def add():
  a=4
  b=3
  c=a+b
  print(c)

add()

def add(a,b):
  c=a+b
  print(c)

add(4,1)

#NO ARG NO RETURN
def divide():
  w=9
  s=3
  q=w//s
  print(q)

divide()

#NO RETURN WITH ARG
def multiply(x,y):
  z=x*y
  print(z)

multiply(2,8)

#NO ARG WITH RETURN
def mul():
  a=4
  b=5
  z=a*b
  return z

mul()

def s(r,t):
  w=r=t
  return w

s(2.9,'ji')

#WITH ARG WITH RETURN
def addn(p,q):
  w=p+q
  return w

addn(3,8)

#SET

d={4,2,-8,3.6,True,'hey'}

d

type(d)

v=[73,92,1,6,-12,1]

v

f=(73,92,1,6,-12,1)

f

j={-1,True,'hi',34,-1}

j

def ad(a=2,b=4):
  s=a+b
  return s

ad(3,7)

ad(1)

def ad(a,b=4,c=8):
  s=a+b+c
  return s

ad(1)

def sb(a=5,b=4,c=8):
  s=a+b-c
  return s

sb(8,3,6)
sb(7,2)

