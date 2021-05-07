import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import cv2
import scipy
import numpy as np
from tkinter.font import Font
import csv
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from skimage import io
import pandas as pd
from matplotlib import patches
from tkinter.messagebox import *
import time
image1=''
main = Tk()
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
print(cwd)
os.chdir(dir_path)
main.bold_font = Font(family="Helvetica", size=14, weight="bold")
main.title("Image Encrypt Decrypt")
main.minsize(800, 400)
main.maxsize(800, 400)
main.labelFrame = Label(main, text = "Open File:", font=('Impact', -20), bg='#000', fg='#000')
main.labelFrame.grid(column = 0, row = 2, padx = 20, pady = 20)
main.configure(background='#dfdddd')
main.labelFrame.configure(background='#dfdddd')

Label(main, text = "Enter Encryption Character for 0:").grid(column= 0, row = 4)
Label(main, text = "Enter Encryption Character for 1:").grid(column= 0, row = 5)
Label(main, text = "Enter Encryption Character for 2:").grid(column= 0, row = 6)
Label(main, text = "Enter Encryption Character for 3:").grid(column= 0, row = 7)
Label(main, text = "Enter Encryption Character for 4:").grid(column= 0, row = 8)
Label(main, text = "Enter Encryption Character for 5:").grid(column= 0, row = 9)
Label(main, text = "Enter Encryption Character for 6:").grid(column= 0, row = 10)
Label(main, text = "Enter Encryption Character for 7:").grid(column= 0, row = 11)
Label(main, text = "Enter Encryption Character for 8:").grid(column= 0, row = 12)
Label(main, text = "Enter Encryption Character for 9:").grid(column= 0, row = 13)


Label(main, text = "Enter Decryption Character for 0:").grid(column= 6, row = 4)
Label(main, text = "Enter Decryption Character for 1:").grid(column= 6, row = 5)
Label(main, text = "Enter Decryption Character for 2:").grid(column= 6, row = 6)
Label(main, text = "Enter Decryption Character for 3:").grid(column= 6, row = 7)
Label(main, text = "Enter Decryption Character for 4:").grid(column= 6, row = 8)
Label(main, text = "Enter Decryption Character for 5:").grid(column= 6, row = 9)
Label(main, text = "Enter Decryption Character for 6:").grid(column= 6, row = 10)
Label(main, text = "Enter Decryption Character for 7:").grid(column= 6, row = 11)
Label(main, text = "Enter Decryption Character for 8:").grid(column= 6, row = 12)
Label(main, text = "Enter Decryption Character for 9:").grid(column= 6, row = 13)
num1 = Entry(main)
num1.grid(column= 1, row = 4)
num2 = Entry(main)
num2.grid(column= 1, row = 5)
num3 = Entry(main)
num3.grid(column= 1, row = 6)
num4 = Entry(main)
num4.grid(column= 1, row = 7)
num5 = Entry(main)
num5.grid(column= 1, row = 8)
num6 = Entry(main)
num6.grid(column= 1, row = 9)
num7 = Entry(main)
num7.grid(column= 1, row = 10)
num8 = Entry(main)
num8.grid(column= 1, row = 11)
num9 = Entry(main)
num9.grid(column= 1, row = 12)
num10 = Entry(main)
num10.grid(column= 1, row = 13)

num1a = Entry(main)
num1a.grid(column= 7, row = 4)
num2a = Entry(main)
num2a.grid(column= 7, row = 5)
num3a = Entry(main)
num3a.grid(column= 7, row = 6)
num4a = Entry(main)
num4a.grid(column= 7, row = 7)
num5a = Entry(main)
num5a.grid(column= 7, row = 8)
num6a = Entry(main)
num6a.grid(column= 7, row = 9)
num7a = Entry(main)
num7a.grid(column= 7, row = 10)
num8a = Entry(main)
num8a.grid(column= 7, row = 11)
num9a = Entry(main)
num9a.grid(column= 7, row = 12)
num10a = Entry(main)
num10a.grid(column= 7, row = 13)

def button_pressed():
    # put text
    label=Label(main, text = "Encryption Done!")
    label.grid(column= 0, row = 14)
    # run clear_label after 2000ms (2s)
    main.after(2000,destroy_widget, label)

def button_pressed1():
    # put text
    label=Label(main, text = "Decryption Done!")
    label.grid(column= 6, row = 14)
    # run clear_label after 2000ms (2s)
    main.after(2000,destroy_widget, label)

def button_pressed2():
    label=Label(main, text = "Loading...")
    label.grid(column= 0, row = 8)
    main.after(32000,destroy_widget, label)

def destroy_widget(widget):
    widget.destroy()

def fileDialog():
    main.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
    (("jpeg files","*.jpg"),("all files","*.*")) )
    #main.label = ttk.Label(main.labelFrame, text = "")

    #main.label.configure(text = main.filename)
    img = Image.open(main.filename)
    file="imagepath.csv"
    with open(file, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([main.filename])
    img2 = io.imread(main.filename, plugin='matplotlib')


def encryption():

    image1=""
    file="imagepath.csv"
    with open(file, 'r',) as file:
        reader = csv.reader(file, delimiter = '\t')
        for row in reader:
            image1=row[0]
            break
    image = mpimg.imread(image1)
    #os.remove("imagewrite.csv");
    # reshaping the array from 3D
    # matrice to 2D matrice.
    from PIL import Image
    im = Image.open(image1)
    im.save('Foto.png')
    image = mpimg.imread('Foto.png')
    imageshape=np.asarray(image.shape)
    np.savetxt("shape1.csv", imageshape, delimiter=",",fmt='%.3e')
    arr_reshaped = image.reshape(image.shape[0], -1)

    arr_reshaped=arr_reshaped.astype(str)
    Ans = str(num1.get())
    arr_reshaped=np.char.replace(arr_reshaped,"0", Ans)
    Ans = str(num2.get())
    arr_reshaped=np.char.replace(arr_reshaped,"1", Ans)
    Ans = str(num3.get())
    arr_reshaped=np.char.replace(arr_reshaped,"2", Ans)
    Ans = str(num4.get())
    arr_reshaped=np.char.replace(arr_reshaped,"3", Ans)
    Ans = str(num5.get())
    arr_reshaped=np.char.replace(arr_reshaped,"4", Ans)
    Ans = str(num6.get())
    arr_reshaped=np.char.replace(arr_reshaped,"5", Ans)
    Ans = str(num7.get())
    arr_reshaped=np.char.replace(arr_reshaped,"6", Ans)
    Ans = str(num8.get())
    arr_reshaped=np.char.replace(arr_reshaped,"7", Ans)
    Ans = str(num9.get())
    arr_reshaped=np.char.replace(arr_reshaped,"8", Ans)
    Ans = str(num10.get())
    arr_reshaped=np.char.replace(arr_reshaped,"9", Ans)


    # saving reshaped array to file.


    np.savetxt("shape.csv", arr_reshaped, delimiter=" ", fmt="%s")
    # saving reshaped array to file.

    command = button_pressed()


def decryption():
    filename = filedialog.askopenfilename()
    loaded_arr = np.genfromtxt(filename,dtype='str')

    Ans = str(num1a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"0")
    Ans = str(num2a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"1")
    Ans = str(num3a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"2")
    Ans = str(num4a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"3")
    Ans = str(num5a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"4")
    Ans = str(num6a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"5")
    Ans = str(num7a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"6")
    Ans = str(num8a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"7")
    Ans = str(num9a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"8")
    Ans = str(num10a.get())
    loaded_arr=np.char.replace(loaded_arr,Ans,"9")

    loaded_arr=loaded_arr.astype(float)
    shape1 = np.loadtxt("shape1.csv").astype(int)

    load_original_arr = loaded_arr.reshape(loaded_arr.shape[0], loaded_arr.shape[1] // shape1[2], shape1[2])
    # This loadedArr is a 2D array, therefore
    # we need to convert it to the original
    # array shape.reshaping to get original
    # matrice with original shape.
    dpi = 80
    image2=load_original_arr
    im_data = load_original_arr
    height, width, nbands = im_data.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(image2, interpolation='nearest')
    ax.set(xlim=[-0.5, width - 0.5], ylim=[height - 0.5, -0.5], aspect=1)
    fig.savefig("foo.jpg", dpi=dpi,transparent=True)
    os.remove("shape.csv")
    os.remove("shape1.csv")
    command = button_pressed1()


def original():
    image1=""
    file="imagepath.csv"
    with open(file, 'r',) as file:
        reader = csv.reader(file, delimiter = '\t')
        for row in reader:
            image1=row[0]
            break
    image = cv2.imread(image1)
    image = mpimg.imread(image1)
    dpi = 80
    im_data = plt.imread(image1)
    height, width, nbands = im_data.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(image, interpolation='nearest')
    ax.set(xlim=[-0.5, width - 0.5], ylim=[height - 0.5, -0.5], aspect=1)
    fig.show()

def button():
        main.button = Button(main, text = "Browse for image",font=('Impact', -10),command = fileDialog)
        main.button.grid(column=1, row = 2)


def showoriginal():
        main.showoriginal = Button(main, text = "Original",command = original)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 0, row = 3)

def encrypt():
        #command = lambda:[encryption(),button_pressed2()]
        main.showoriginal = Button(main, text = "Encrypt",command = lambda:[encryption()])
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 2, row = 13)

def decrypt():
        main.showoriginal = Button(main, text = "Decrypt",command = decryption)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 8, row = 13)


button()
showoriginal()
encrypt()
decrypt()

# This defines the Python GUI backend to use for matplotlib
matplotlib.use('TkAgg')
mainloop()
