from re import X
from tkinter import Y


str = 'X-DSPAM-Confidence:0.8475'

x = str.find(":")
y = float((str[x+1:]))
print (y)