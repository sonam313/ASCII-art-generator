# Firstly import all the relevant libraries needed 
from PIL import ImageFont, Image, ImageDraw, ImageOps, ImageFilter
import numpy as np
import cv2
import math

# the video to be converted
videocap ="./data/exhib2.mp4"

# the character set : 
character_list=list(" .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
interval=(len(character_list))/256

char_width=10
char_height=10
scale=0.07

# capturing from video
capture=cv2.VideoCapture(videocap)

# font to be used
Font_use=ImageFont.truetype("./fonts/cour.ttf",15)

def get_characters(i):
    return character_list[math.floor(interval*i)]

# infinite while loop to be exited when the user presses q 
while True:
    _,scan=capture.read()
    scan=Image.fromarray(scan)  

    # width and height of frame
    width,height=scan.size
    # resizing  
    scan=scan.resize((int(scale*width),int(scale*height*(char_width/char_height))),Image.NEAREST)
    # new width and height now
    width,height=scan.size
    
    pixel=scan.load()
    out_scan=Image.new("RGB",(char_width*width,char_height*height),color=(0,0,0))
    final=ImageDraw.Draw(out_scan)

    # looping across the whole height and width
    for i in range(height):
        for j in range(width):
            # r,g,b at ith height and jth width
            r,g,b=pixel[j,i]
            # weighted method or also called as luminosity method
            # it weighs red, green, and blue according to their wavelengths
            k=int(0.299*r+0.587*g+0.114*b)
            pixel[j,i]=(k,k,k)
            final.text((char_width*j,char_height*i),get_characters(k),font=Font_use,fill=(r,g,b))

    ascii_video=np.array(out_scan)
    # if keyboard stroke by user then wait
    stroke=cv2.waitKey(1)
    # if stroke is 'q' then exit
    if stroke == ord("q"):
        break
    # displaying the asciified video in a gui window
    cv2.imshow("ascii_video",ascii_video)

capture.release()
cv2.destroyAllWindows()