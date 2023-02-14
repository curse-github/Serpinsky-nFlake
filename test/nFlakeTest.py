
#imports
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
    #pygame.image.save(surfaceTr, name+"Tr.jpg")
    imgTr.save(name+"Tr.jpg")
    print("saved Top right")
    #pygame.image.save(surfaceTl, name+"Tl.jpg")
    imgTl.save(name+"Tl.jpg")
    print("saved Top left")
    #pygame.image.save(surfaceBr, name+"Br.jpg")
    imgBr.save(name+"Br.jpg")
    print("saved Bottom right")
    #pygame.image.save(surfaceBl, name+"Bl.jpg")
    imgBl.save(name+"Bl.jpg")
    print("saved Bottom left")
    os.system("python combine.py \"" + name + "\" " + str(screensize))
    sys.exit()

def set(pos,col):
    x = pos[0]
    y = pos[1]
    col = (int(col[0]),int(col[1]),int(col[2]))
    if (x < 0):
        if (y < 0):
            #surfaceTl.set_at((x+screensize,y+screensize),col)
            #print((x+screensize,y+screensize))
            imgTl.putpixel((x+screensize,y+screensize), col)
        else:
            #surfaceBl.set_at((x+screensize,y),col)
            #print((x+screensize,y))
            imgBl.putpixel((x+screensize,y), col)
    else:
        if (y < 0):
            #surfaceTr.set_at((x,y+screensize),col)
            #print((x,y+screensize))
            imgTr.putpixel((x,y+screensize), col)
        else:
            #surfaceBr.set_at((x,y),col)
            #print((x,y))
            imgBr.putpixel((x,y), col)

#variables
n = 0
if (len(sys.argv) > 0):
    n = int(sys.argv[1])
else:
    n=6

screensize = 9500
multiplier = screensize-50
angleOffset = 180
colors = [(0)*3]*n
num = 1000000000

#setup
angleOffsetRadians = angleOffset*pi/180
points = [[0]*2]*n
for i in range(n):
    points[i] = [multiplier*sin(i*(2*pi/n)+angleOffsetRadians),multiplier*cos(i*(2*pi/n)+angleOffsetRadians)]
    colTemp = colorsys.hls_to_rgb(i/n, 0.5, 1)
    colors[i] = (colTemp[0]*255,colTemp[1]*255,colTemp[2]*255)
os.system("cls")
imgTr = Image.new("RGB",(screensize, screensize))
imgTr.paste((255,255,255),(0, 0,screensize, screensize))
imgTl = Image.new("RGB",(screensize, screensize))
imgTl.paste((255,255,255),(0, 0,screensize, screensize))
imgBr = Image.new("RGB",(screensize, screensize))
imgBr.paste((255,255,255),(0, 0,screensize, screensize))
imgBl = Image.new("RGB",(screensize, screensize))
imgBl.paste((255,255,255),(0, 0,screensize, screensize))
'''
surfaceTr = pygame.Surface((screensize, screensize));
surfaceTr.fill((255,255,255))
surfaceTl = pygame.Surface((screensize-1, screensize));
surfaceTl.fill((255,255,255))
surfaceBr = pygame.Surface((screensize, screensize-1));
surfaceBr.fill((255,255,255))
surfaceBl = pygame.Surface((screensize-1, screensize-1));
surfaceBl.fill((255,255,255))
'''

#more variables
strtTime = time.time()
multiplier = n/(n+3)
thing = (5.7182+5.9318+5.8987+5.6474)/4
name = "serpinski nGon"

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
