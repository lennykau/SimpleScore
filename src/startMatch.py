# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="lenny"
__date__ ="$Mar 9, 2014 6:12:35 PM$"

from tkinter import *
from tkinter import ttk

import datetime

def setupStartMatch(myFrame):
    frameRow = 0
    frameCol = 0
    newMatchFrame = ttk.Frame(myFrame)
    newMatchFrame.grid(column=frameCol, row=frameRow, sticky=(N, W, E, S))
    newMatchFrame['borderwidth'] = 1
    newMatchFrame['relief']      = 'sunken'
    ttk.Label(newMatchFrame, text='Start a new match.').grid(column=0, row=0, sticky=W)
    ttk.Label(newMatchFrame, text='Match Date').grid(column=0, row=1, sticky=W)

    
    frameCol += 1
    
    existingMatchFrame = ttk.Frame(myFrame)
    existingMatchFrame = ttk.Frame(myFrame)
    existingMatchFrame.grid(column=frameCol, row=frameRow, sticky=(N, W, E, S))
    existingMatchFrame['borderwidth'] = 1
    existingMatchFrame['relief']      = 'sunken'
    ttk.Label(existingMatchFrame, text='Open an existing match.').grid(column=0, row=0, sticky=E)
    ttk.Label(existingMatchFrame, text='Match Date').grid(column=0, row=1, sticky=W)

    scrollbar = Scrollbar(existingMatchFrame, orient=VERTICAL)
    dateBox = Listbox(existingMatchFrame, yscrollcommand=scrollbar.set)
    dateBox.insert(END, "a list entry")
#    
    for item in ['Jan 7, 2014', 'Feb 6, 2014', 'March 5, 2014']:
        dateBox.insert(END, item)
        
    Lb1 = Listbox(existingMatchFrame)
    Lb1.insert(1, "Python")
    Lb1.insert(2, "Perl")
    Lb1.insert(3, "C")
    Lb1.insert(4, "PHP")
    Lb1.insert(5, "JSP")
    Lb1.insert(6, "Ruby")

#    Lb1.pack()

#
#    dateBox.pack(side=LEFT, fill=BOTH, expand=1)


