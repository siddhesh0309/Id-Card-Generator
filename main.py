from databasedemo import firebase
from PIL import Image, ImageDraw, ImageFont
image = Image.new( 'RGB', (1000,900), (255, 255, 255))
draw = ImageDraw.Draw( image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import cv2
import textwrap
import qrcode
os. system ("title ID CARD Generaator")

def photo_capture():
    cap = cv2.VideoCapture(0)
    while True:
        ret, photo = cap.read()
        cv2.imshow('hi', photo)
        if cv2.waitKey(1) == 13:
            break
    cv2. destroyAllWindows ()
    cap.release()
    return photo

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime(" %d-%n-%Y\t\t\t\t\t ID CARD Generator \t\t\t\t\t %I:%M:%S %p")
print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (reg_format_date)
print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('\n\nAll Fields are Mandatory')
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters ')
(x, y) = (50, 50)
message = input('\nEnter Your College Name: ')
company = message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=40)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (600, 75)
idno=random.randint(1000000,90000000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)


(x, y) = (50, 150)
name = 'Name'
color = 'rgb(255, 0, 0)'
draw.text((x, y), name, fill=color, font=font)

(x, y) = (50, 220)
message = input('Enter Your Full Nane: ')
name = message

color = 'rgb(0, 0, 0)' #black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (45, 300)
gen = 'Branch'
color = 'rgb(255, 0, 0)'
draw.text((x, y), gen, fill=color, font=font)

(x, y) = (50, 350)
branch = input('Enter Your Branch:  ')
color = 'rgb(0, 0, 0)' #black color
draw. text((x, y), branch, fill=color, font=font)

(x, y) = (250, 300)
sem = 'Semester'
color = 'rgb(255, 0, 0)'
draw.text((x, y), sem, fill=color, font=font)

(x, y) = (250, 350)
age = input ("Enter Your Semester: ")
color = 'rgb(0, 0, 0)' #black color
draw. text((x, y), age, fill=color, font=font)

(x, y) = (50, 410)
dob = 'DOB'
color = 'rgb(255, 0, 0)'
draw.text((x, y), dob, fill=color, font=font)

(x, y) = (50, 470)
dobir = input('Enter Your Date of Birth: ')
color = 'rgb(0, 0, 0)' #black color
draw.text((x, y), dobir, fill=color, font=font)

(x, y) = (50, 530)
bd = 'Blood Group'
color = 'rgb(255, 0, 0)'
draw.text((x, y), bd, fill=color, font=font)

(x, y) = (50, 580)
bgrp = input ('Enter Your Blood Group: ')
color = 'rgb(0, 0, 0)' #black color
draw. text((x, y), bgrp, fill=color, font=font)

(x, y) = (50, 640)
mb = 'Mobile No'
color = 'rgb(255, 0, 0)'
draw. text((x, y), mb, fill=color, font=font)

(x, y) = (50, 690)
mo = input ('Enter Your Mobile Number: ')
temp = mo
color = 'rgb(0, 0, 0)' #black color
draw.text((x, y), mo, fill=color, font=font)

(x, y) = (50, 740)
ad = 'Address'
color = 'rgb(255, 0, 0)'
draw.text((x, y), ad, fill=color, font=font)

(x, y) = (50, 800)
addr = input ('Enter Your Address: ')
color = 'rgb(0, 0, 0)' #black color
draw.text((x, y), addr, fill=color, font=font)

image.save(str (name) +'.jpg')

val_input = int (input ('Press 1 to capture image'))
if val_input == 1:
    photo = photo_capture()

newing = cv2.resize(photo, (350, 350))

newing. shape
gray = cv2.cvtColor (newing,cv2.COLOR_BGR2BGRA)
gray.shape
cv2.imwrite(str(idno)+'.bmp',gray)

til = Image.open(name+'.jpg')
im = Image.open(str(idno)+'.bmp')
im = til.paste(im, (600, 200))
til.save(name+'.jpg')

QR = qrcode.make(str(company) +'\n' + str(idno)+'\n' + str(name)+'\n' + str(branch))
QR.save(str(idno) + '.bmp')

ID = Image.open(name + '.jpg')
QR = Image.open(str(idno) + '.bmp')  # 25x25
ID.paste(QR, (575, 550))
ID.save(name + '.jpg')

import csv
row = [str(idno), str(name), str(gen), str(age), str(dobir), str(bgrp), str(mo), str(addr)]
with open('data.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()

