# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="lenny"
__date__ ="$Mar 9, 2014 12:44:14 PM$"

import sys
import configparser
from tkinter        import *
from tkinter        import ttk
from shooterScore   import *
from startMatch     import *
from scoreConstants import *
from simpleMatch    import *
from simpleConfig   import *

def exitAll():
    quit()
    pass



if __name__ == "__main__":
    
    try:
        ini = configparser.ConfigParser()
        ini.read('simpleScore.ini')
    except:
        print("Unexpected error:", sys.exc_info()[0])
    
    #match = SimpleMatch()
    root = Tk()
    root.title(ini['lables']['matchName'])
    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    tabs = ttk.Notebook(mainframe)
    startFrame  = ttk.Frame(tabs, padding="3 3 12 12"); # first page, which would get widgets gridded into it
    configFrame = ttk.Frame(tabs); # Sets variables for running match
    tabs.add(startFrame,  text='Start Here')
    tabs.add(configFrame, text='Configure')
    tabs.grid(column=1, row=1, sticky=(N,W))
    
    setupSimpleConfig(ini, configFrame)
    setupStartMatch(startFrame)
    
    button = ttk.Button(mainframe, text="Exit", command=exitAll)
    button.grid(column=3, row=3, sticky=W)
    button.bind('<Enter>', lambda e: button.configure(text='Press To Quit!'))
    button.bind('<Leave>', lambda e: button.configure(text='Exit'))
    
    exitBtn = ttk.Button()
    
    # add padding around all elements
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


    root.mainloop()
    
    