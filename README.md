# Image-Encrypt-Decrypt
A python based simple app for encrypt-decrypt images.

## Used python libraries
Tkinter, Matplotlib, Numpy

### Version 1
Encryption
1. Read Image
2. Convert it to png for better conversion.
3. Reshape 3d numpy array for making it compact with csv.
4. Modify its reshaped data by multiplying given number with it and save it to csv.

Decryption
1. Read any given csv that has reshaped csv data.
2. Demodify by the given number.
3. Reshape to 3d numpy array and convert it to JPG.

### Version 2
Encryption
Same approach but replace all numbers with given character value.

Decryption
Same approach and demodify all numbers with given character value.
Without encryption code, you cannot get the image!




