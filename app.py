import tkinter as tk
import tkinter as ttk
from tkinter import *
from tkinter import filedialog, Text
import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import cv2
import scipy
from skimage.filters import threshold_otsu
from skimage import color
from skimage import io
import numpy as np
from tkinter.font import Font
import csv
from skimage.filters import threshold_local
from skimage.filters import try_all_threshold
from skimage.filters import sobel
from skimage.filters import gaussian
from skimage import exposure
from skimage import morphology
import os
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from skimage.restoration import inpaint
from skimage.feature import Cascade
from skimage import data
from skimage.segmentation import slic
from  skimage.color import label2rgb
from skimage.filters import gaussian
from skimage import io
from skimage.feature import Cascade
from skimage import data
import pandas as pd
import decimal
from matplotlib import patches
from tkinter import *
from tkinter.messagebox import *
image1=''
main = Tk()
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
print(cwd)
os.chdir(dir_path)
main.bold_font = Font(family="Helvetica", size=14, weight="bold")
main.title("Image Encrypt Decrypt")
main.minsize(850, 300)
main.maxsize(850, 300)
main.labelFrame = ttk.Label(main, text = "Open File:", font=('Impact', -20), bg='#000', fg='#fff')
main.labelFrame.grid(column = 0, row = 2, padx = 20, pady = 20)
main.configure(background='#263D42')
main.labelFrame.configure(background='#263D42')

Label(main, text = "Enter Encryption Number:").grid(column= 0, row = 4)
Label(main, text = "Enter Decryption Number:").grid(column= 0, row = 5)
num1 = Entry(main)
num1.grid(column= 1, row = 4)
num2 = Entry(main)
num2.grid(column= 1, row = 5)


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
    x = image.reshape(image.shape[0], -1)
    Ans = int(num1.get())
    x=x*Ans

    np.savetxt("shape.csv", x)
    # saving reshaped array to file.

def decryption():
    loaded_arr = np.loadtxt("shape.csv").astype(float)
    shape1 = np.loadtxt("shape1.csv").astype(int)
    Ans = int(num2.get())
    loaded_arr=loaded_arr/As

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

def show_image(image, title='Image', cmap_type='gray'):
    dpi = 80
    im_data = plt.imread('somefilename.jpg')
    height, width, nbands = im_data.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(image, interpolation='nearest')
    ax.set(xlim=[-0.5, width - 0.5], ylim=[height - 0.5, -0.5], aspect=1)
    fig.savefig("foo.jpg", dpi=dpi,transparent=True)

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
    plt.imshow(image)
    plt.show()

def button():
        main.button = ttk.Button(main, text = "Browse File",font=('Impact', -10),command = fileDialog)
        main.button.grid(column=1, row = 2)

def showoriginal():
        main.showoriginal = ttk.Button(main, text = "Original",command = original)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 0, row = 3)

def encrypt():
        main.showoriginal = ttk.Button(main, text = "Encrypt",command = encryption)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 2, row = 4)

def decrypt():
        main.showoriginal = ttk.Button(main, text = "Decrypt",command = decryption)
        main.showoriginal.configure(background='#e28743')
        main.showoriginal.grid(column= 2, row = 5)


button()
showoriginal()
encrypt()
decrypt()



# This defines the Python GUI backend to use for matplotlib
matplotlib.use('TkAgg')


mainloop()
