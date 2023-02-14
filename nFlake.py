
#imports
import pygame
from math import *
import random
import os
import time
import sys
import colorsys
import io

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
    #save image and open it
    pygame.image.save(surface, name+".png")
    os.system("\""+name+".png\"")

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

#variables
n = 6
screensize = 10000
multiplier = screensize-50
angleOffset = 180
yOffset = 0
colors = [(0)*3]*n
num = 30000000

#setup
angleOffsetRadians = angleOffset*pi/180
points = [[0]*2]*n
for i in range(n):
    points[i] = [multiplier*sin(i*(2*pi/n)+angleOffsetRadians)/2+screensize/2,multiplier*cos(i*(2*pi/n)+angleOffsetRadians)/2+screensize/2-yOffset]
    colTemp = colorsys.hls_to_rgb(i/n, 0.5, 1)
    colors[i] = (colTemp[0]*255,colTemp[1]*255,colTemp[2]*255)
pygame.init()
pygame.display.set_caption("Test")

surface = pygame.Surface((round(screensize*16/9), screensize));# 16/9 aspect ratio
surface.fill((255,255,255))
os.system("cls")
strtTime = time.time()
print("filling screen with black")
for x in range(round(screensize*16/9)):# fill with black
    for y in range(screensize):
        surface.set_at((x,y),(0,0,0))
print("done.\n")
print("time took: " + str((time.time()-strtTime)/60) + "mins")

#more variables
strtTime = time.time()
multiplier = n/(n+3)
thing = (5.7182+5.9318+5.8987+5.6474)/4
name = "Preview"

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
        surface.set_at((round(screensize*(16/9-1)/2 + point[0]), round(point[1])),col)
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
    finish(name+"Exited"+str(n))
    sys.exit()

finish(name)
