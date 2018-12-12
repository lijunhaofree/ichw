#!/usr/bin/env python3

"""tile.py:对如何用砖铺墙的认识。

__author__ = "Li Junhao"
__pkuid__  = "1800011726"
__email__  = "lijunhao@pku.edu.cn"
"""



def brick(m,n,a,b):
    '''在m*n的墙中横着摆a*b的砖的所有可能性'''
    x=min(a,b)
    l=[]
    for i in range(n-b+1):
        if (x<=i<=n-x-b or i==n-b or i==0):
            for j in range(m-a+1):
                if (x<=j<=m-x-a or j==m-a or j==0):
                    g=[]
                    for z in range(a*b):
                        g=g+[(i+z//a)*m+j+z%a]    
                    l=l+[g]
    return l




def sum_brick(m,n,a,b):
    '''将竖着摆和横着摆的情况总结在一起，建立一个列表，
如3*2,2*1会输出[[0, 1], [1, 2], [3, 4], [4, 5], [0, 3], [1, 4], [2, 5]]'''
    if a==b:
        return brick(m,n,a,b)
    else:
        return brick(m,n,a,b)+brick(m,n,b,a)



lst=[]
def scheme(lis,l,n,a):
    '''输出出所有的铺法，原理是对列表进行有条件的组合，把所有情况打印出来，
同时输出一个总列表，便于画图函数引用其中的一项'''
    global lst
    if len(l)==n:
        l.sort()
        print(l)
        lst=lst+[l.copy()]
    else:
        for i in range(a,len(lis)):  
            if not conflict(lis[i],l):
                l=l+[lis[i]]               
                scheme(lis,l,n,i)
                del l[-1]




def conflict(x,lis):
    '''判断位置是否已经有砖摆过'''
    n=0
    for i in x:
        for j in lis:
            for g in j:
                if i==g:
                    n=n+1
    if n>0:
        return True
    else:
        return False



m=int(input('墙的长度'))
n=int(input('墙的宽度'))
a=int(input('砖的长度'))
b=int(input('砖的宽度'))




from turtle import*
speed(9)
'''此后为画图函数，将计算出的列表的第一种情况可视化'''


def table(m,n):
    '''画出m*n的墙的框架'''
    pencolor('red')
    for i in range(n+1):
        up()
        goto(-50*m/2,-50*(i-n/2))
        down()
        goto(50*m/2,-50*(i-n/2))
    for i in range(m+1):
        up()
        goto(-50*(i-m/2),50*(n/2))
        down()
        goto(-50*(i-m/2),-50*n/2)




mydict={}
def fill(m,n):
    '''往每一格中填入数字标号，同时建立一个字典，将数字与坐标对应，
便于对某个数字进行调用'''
    x=0
    global mydict
    for j in range(n):
        for i in range(m):
            up()
            goto(50*i-50*m/2+20,50*j-50*n/2+20)
            down()
            write(x)
            mydict[x]=[50*i-50*m/2,50*j-50*n/2]
            x+=1




def size(l,m,n,a,b):
    '''判断砖是横着摆还是竖着摆'''
    i=min(l)
    j=max(l)
    z=mydict[i]
    if i+m*(b-1)+a-1==j:
        bricks(a,b,z[0],z[1])
    else:
        bricks(b,a,z[0],z[1])
            



def bricks(a,b,x,y):
    '''画出其中的一块砖'''
    pencolor('black')
    pensize(7)
    up()
    goto(x,y)
    down()
    goto(x+a*50,y)
    goto(x+a*50,y+b*50)
    goto(x,y+b*50)
    goto(x,y)


def main1():
    '''定义一个main函数，对所有函数进行调用，输出所有情况，并用turtle进行绘图'''
    l1=sum_brick(m,n,a,b)
    scheme(l1,[],(m*n)/(a*b),0)
    table(m,n)
    fill(m,n)
    for i in lst[0]:
        size(i,m,n,a,b)

if __name__ == '__main__':
    main1()


