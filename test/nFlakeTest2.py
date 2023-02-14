
#imports
from tkinter import Y
import pygame
from math import *
import random
import os
import time
import sys
import colorsys
from PIL import Image

#function definitions
def lerp(a,b,t):
    return ((1 - t) * a[0] + t * b[0],(1 - t) * a[1] + t * b[1])

def getSpaceThing(num,max):
    return (1+max-len(str(num)))*" "

def timeToString(tm,acc=2,acc2=5):
    thing = 10**acc
    if      (tm < 60):
        string = str(round(tm      *thing)/thing)
        return string + getSpaceThing(string,acc2-2+acc) + "seconds"
    elif  (tm < 3600):#60*60
        string = str(round(tm/60   *thing)/thing)
        return string + getSpaceThing(string,acc2-2+acc) + "minutes"
    elif (tm < 86400):#60*60*24
        string = str(round(tm/3600 *thing)/thing)
        return string + getSpaceThing(string,acc2-2+acc) + "hours  "
    else:
        string = str(round(tm/86400*thing)/thing)
        return string + getSpaceThing(string,acc2-2+acc) + "days   "
def finish(name):
    #print total time
    finalTime = time.time()-strtTime
    hrs = floor(finalTime/3600)
    mins = floor((finalTime%3600)/60)
    secs = floor((finalTime-hrs%60))
    print("\n" + str(hrs) + " hrs")
    print(str(mins) + " mins")
    print(str(secs) + " secs")
    print("or " + timeToString(finalTime,4))
    print("\nAverage time per percent: " + timeToString(finalTime/100,4))
    
    #save image and open it
    img0.save(name+"0.png")
    img1.save(name+"1.png")
    img2.save(name+"2.png")
    img3.save(name+"3.png")
    img4.save(name+"4.png")
    img5.save(name+"5.png")
    img6.save(name+"6.png")
    img7.save(name+"7.png")
    img8.save(name+"8.png")
    print("saved images")
    os.system("python combine.py \"" + name + "\" " + str(screensize) + " 3")
    sys.exit()

def set(pos,col):
    x = pos[0]
    y = pos[1]
    col = (int(col[0]),int(col[1]),int(col[2]))
    if (x < screensize):
        if (y < screensize):
            img0.putpixel((x,y), col)
        elif(y < screensize*2):
            img3.putpixel((x,y-screensize), col)
        else:
            img6.putpixel((x,y-screensize*2), col)
    elif(x < screensize*2):
        if (y < screensize):
            img1.putpixel((x-screensize,y), col)
        elif(y < screensize*2):
            img4.putpixel((x-screensize,y-screensize), col)
        else:
            img7.putpixel((x-screensize,y-screensize*2), col)
    else:
        if (y < screensize):
            img2.putpixel((x-screensize*2,y), col)
        elif(y < screensize*2):
            img5.putpixel((x-screensize*2,y-screensize), col)
        else:
            img8.putpixel((x-screensize*2,y-screensize*2), col)
#variables
n = 0
if (len(sys.argv) > 0):
    n = int(sys.argv[1])
else:
    n=6

screensize = 6500
multiplier = screensize*3-50
angleOffset = 180
colors = [(0)*3]*n
num = 100000000
name = "serpinski nGon3_"

#setup
angleOffsetRadians = angleOffset*pi/180
points = [[0]*2]*n
for i in range(n):
    points[i] = [multiplier*(sin(i*(2*pi/n)+angleOffsetRadians)+1)/2,multiplier*(cos(i*(2*pi/n)+angleOffsetRadians)+1)/2]
    colTemp = colorsys.hls_to_rgb(i/n, 0.5, 1)
    colors[i] = (round(colTemp[0]*255),round(colTemp[1]*255),round(colTemp[2]*255))
os.system("cls")
img0 = Image.new("RGB",(screensize, screensize))
img0.paste((255,255,255),(0, 0,screensize, screensize))
img1 = Image.new("RGB",(screensize, screensize))
img1.paste((255,255,255),(0, 0,screensize, screensize))
img2 = Image.new("RGB",(screensize, screensize))
img2.paste((255,255,255),(0, 0,screensize, screensize))
img3 = Image.new("RGB",(screensize, screensize))
img3.paste((255,255,255),(0, 0,screensize, screensize))
img4 = Image.new("RGB",(screensize, screensize))
img4.paste((255,255,255),(0, 0,screensize, screensize))
img5 = Image.new("RGB",(screensize, screensize))
img5.paste((255,255,255),(0, 0,screensize, screensize))
img6 = Image.new("RGB",(screensize, screensize))
img6.paste((255,255,255),(0, 0,screensize, screensize))
img7 = Image.new("RGB",(screensize, screensize))
img7.paste((255,255,255),(0, 0,screensize, screensize))
img8 = Image.new("RGB",(screensize, screensize))
img8.paste((255,255,255),(0, 0,screensize, screensize))

#more variables
strtTime = time.time()
multiplier = n/(n+3)
thing = (5.7182+5.9318+5.8987+5.6474)/4

rand = 0
p2 = [0]*2
point = points[0]
col = (0)*3
PrcntTime = timeToString(thing/100000000*num)
tltTime = timeToString(0)

curTime = strtTime
lastPrcntTime = strtTime
percent = 0
loops = 0

print("%    , time so far  , time/%       , estimated time")
print("0%   , 0.0   seconds, " + PrcntTime + ", " + timeToString(thing/1000000*num))
#loop
try:
    for i in range(num):
        rand = random.randint(0,n-1)
        p2 = points[rand]
        point = lerp(point,p2,multiplier)
        #col = max(surface.get_at((round(point[0]), round(point[1])))[0]-5,0)
        col = colors[rand]
        #col = (0,0,0)
        set((round(point[0]), round(point[1])),col)
        if (((i+1)/num*100)%1==0):
            curTime = time.time()
            PrcntTime = timeToString(curTime-lastPrcntTime)
            tltTime = timeToString(curTime-strtTime)
            percent = round((i+1)/num*100)
            print(str(percent)+ "%" + getSpaceThing(percent,3) + ", " + tltTime + ", " + PrcntTime + ", " + timeToString((curTime-strtTime)/percent*100))
            lastPrcntTime = curTime
        loops = i
            
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    print("got to " + str(loops) + " dots, or " + str(round(loops/num*10000)/100) + "%")
    #finish(name+"Exited"+str(n))
    sys.exit()

finish(name+str(n))
