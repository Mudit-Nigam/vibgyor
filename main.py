o=0
while(o!=5):
    o = int(input("Enter 1 for shape,2 for level1 colors,3 for level2 colors,4 for taking image text to audio,5 for exit"))
    if(o==1):
      import sh.py
    elif(o==2):
      import level1.py
    elif(o==3):
      import level2.py
    elif(o==4):
      import ocr_func_check.py
    elif(o==5):
      quit()
    else:
      print("Enter correct choice")
