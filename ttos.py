import os
import sys
import pyttsx3
engine = pyttsx3.init()
fhand = open("Output.txt")
for line in fhand:
    #x = line.split()
    #for word in x:
        print(line)
        engine.say(line)
        engine.runAndWait()
        
import main.py
