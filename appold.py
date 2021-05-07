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

image1=''
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cwd = os.getcwd()
        print(cwd)
        os.chdir(dir_path)
        self.bold_font = Font(family="Helvetica", size=14, weight="bold")
        self.title("Image Encrypt Decrypt")
        self.minsize(850, 300)
        self.maxsize(850, 300)
        self.labelFrame = ttk.Label(self, text = "Open File:", font=('Impact', -20), bg='#000', fg='#fff')
        self.labelFrame.grid(column = 0, row = 2, padx = 20, pady = 20)
        self.configure(background='#263D42')
        self.labelFrame.configure(background='#263D42')
        self.button()
        self.showoriginal()
        self.encrypt()
        self.decrypt()

    def button(self):
            self.button = ttk.Button(self, text = "Browse File",font=('Impact', -10),command = self.fileDialog)
            self.button.grid(column=1, row = 2)

    def showoriginal(self):
            self.showoriginal = ttk.Button(self, text = "Original",command = self.original)
            self.showoriginal.configure(background='#e28743')
            self.showoriginal.grid(column= 0, row = 3)

    def encrypt(self):
            self.showoriginal = ttk.Button(self, text = "Encrypt",command = self.encryption)
            self.showoriginal.configure(background='#e28743')
            self.showoriginal.grid(column= 0, row = 4)

    def decrypt(self):
            self.showoriginal = ttk.Button(self, text = "Decrypt",command = self.decryption)
            self.showoriginal.configure(background='#e28743')
            self.showoriginal.grid(column= 0, row = 5)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        #self.label = ttk.Label(self.labelFrame, text = "")

        #self.label.configure(text = self.filename)
        img = Image.open(self.filename)
        file="imagepath.csv"
        with open(file, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([self.filename])
        img2 = io.imread(self.filename, plugin='matplotlib')

    def original(self):
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

    def encryption(self):
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

        imageshape=np.asarray(image.shape)
        np.savetxt("shape.csv", imageshape, delimiter=",",fmt='%.3e')
        arr_reshaped = image.reshape(image.shape[0], -1)
        # saving reshaped array to file.
        np.savetxt("imagewrite.csv", arr_reshaped)

    def decryption(self):
        # retrieving data from file.
        loaded_arr = np.loadtxt("imagewrite.csv").astype(int)
        shape = np.loadtxt("shape.csv").astype(int)

        # This loadedArr is a 2D array, therefore
        # we need to convert it to the original
        # array shape.reshaping to get original
        # matrice with original shape.
        load_original_arr = loaded_arr.reshape(loaded_arr.shape[0], loaded_arr.shape[1] // shape[2], shape[2])
        load_original_arr=load_original_arr

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

from matplotlib import patches

# This defines the Python GUI backend to use for matplotlib
matplotlib.use('TkAgg')


root = Root()

# Create a tkinter button at the bottom of the window and link it with the updateGraph function
#tk.Button(root,text="Update",command=show_image).grid(row=1, column=0)

root.mainloop()
