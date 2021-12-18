import tkinter as tk
from tkinter.constants import ANCHOR, BOTTOM, INSERT, LEFT, RIGHT, TOP, X
import caesar_cypher_functions as cc

gui = tk.Tk()

screen_width = gui.winfo_screenwidth()
print(screen_width)
screen_height = gui.winfo_screenheight()
print(screen_height)
gui.geometry(str(int(screen_width/2)) + "x" + str(int(screen_height/2)))
userInput = ""
gui.title('Caesar Cypher Bruteforcer')
e0 = tk.Label(gui, text='Message to Bruteforce').pack(side=TOP)


e1 = tk.Entry(gui, width=100)
e1.pack(side=TOP)
mesRes = ""

def beginOp():
    userInput = e1.get()
    global mesRes
    mesRes = cc.bruteforce(userInput)
    refresh()

def refresh():
    tk.Message(gui, text = mesRes, width=screen_width).pack(side=TOP)
    print(gui.pack_slaves())

def rmMes():
    list = gui.pack_slaves()
    print(list)
    for x in range(4):
        print("Popping " + str(list[0]))
        list.pop(0)
        print("Pop successful")
    for x in list:
        print("Destroying " + str(x))
        x.destroy()
        print("Destroy Successeful")
    
    

tk.Button(gui, text ="BruteForce", command = beginOp).pack(side=TOP)
tk.Button(gui, text ="Delete decrypted messages", command = rmMes).pack(side=TOP)

gui.mainloop()