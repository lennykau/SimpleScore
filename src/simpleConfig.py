# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
from tkinter import *
from tkinter import ttk
import configparser

def resetDefaults():
    pass

def setupSimpleConfig(ini, myFrame):
    frameRow = 0
    frameCol = 0
    
        # Display the classes and their descriptions
    classRows = 0
    classFrame = ttk.Frame(myFrame)
    classFrame.grid(column=frameCol, row=frameRow, sticky=(N, W, E, S))
    classFrame['borderwidth'] = 1
    classFrame['relief']      = 'sunken'
    ttk.Label(classFrame, text='Shooter Classifications').grid(column=1, row=classRows, sticky=E)
    classRows += 1
    for key in ini['classes']:
        ttk.Label(classFrame, text=key).grid(column=1, row=classRows, sticky=W)
        label = ttk.Label(classFrame, text=ini['classes'][key])
        label.grid(column=2, row=classRows, sticky=E)
        classRows += 1
    for child in classFrame.winfo_children(): child.grid_configure(padx=4, pady=2)

    frameRow += 1
    frameCol  = 0
    #display the penalties
    penRow=0
    something = 0
    penFrame = ttk.Frame(myFrame)
    penFrame.grid(column=frameCol, row=frameRow, sticky=(N, W, E, S))
    penFrame['borderwidth'] = 1
    penFrame['relief']      = 'sunken'
    ttk.Label(penFrame, text='Penalties').grid(column=1, row=penRow, sticky=W)
    penRow += 1
    for key in ini['penalties']: 
        ttk.Label(penFrame, text=key).grid(column=1, row=penRow, sticky=W)
        entry = ttk.Entry(penFrame, width=4, justify=RIGHT )
        entry.grid(column=2, row=penRow, sticky=E)
        entry.insert(0,ini['penalties'][key])
        penRow += 1
    for child in penFrame.winfo_children(): child.grid_configure(padx=4, pady=2)

    
    frameCol += 1

    # Display the match Fees
    feeRow = 0
    feeFrame = ttk.Frame(myFrame)
    feeFrame.grid(column=frameCol, row=frameRow, sticky=(N, W, E, S))
    feeFrame['borderwidth'] = 1
    feeFrame['relief']      = 'sunken'
    ttk.Label(feeFrame, text='Match Fees').grid(column=1, row=feeRow, sticky=W)
    feeRow += 1
    for key in ini['matchFees']:
        ttk.Label(feeFrame, text=key).grid(column=1, row=penRow, sticky=W)
        entry = ttk.Entry(feeFrame, width=4, justify=RIGHT )
        entry.grid(column=2, row=penRow, sticky=E)
        entry.insert(0,ini['matchFees'][key])
        penRow += 1
    for child in feeFrame.winfo_children(): child.grid_configure(padx=4, pady=2)

    frameCol += 1
    # Display the match points
    feeRow = 0
    pointsFrame = ttk.Frame(myFrame)
    pointsFrame.grid(column=frameCol, row=frameRow, sticky=(N, W, E, S))
    pointsFrame['borderwidth'] = 1
    pointsFrame['relief']      = 'sunken'
    ttk.Label(pointsFrame, text='Year End Points').grid(column=1, row=feeRow, sticky=W)
    feeRow += 1
    for key in ini['scoring']: 
        ttk.Label(pointsFrame, text=key).grid(column=1, row=penRow, sticky=W)
        entry = ttk.Entry(pointsFrame, width=4, justify=RIGHT )
        entry.grid(column=2, row=penRow, sticky=E)
        entry.insert(0,ini['scoring'][key])
        penRow += 1
    for child in pointsFrame.winfo_children(): child.grid_configure(padx=4, pady=2)


    frameRow += 3  # pad
    
    defaultsBtn = ttk.Button(myFrame, text="Reset To Defaults", command=resetDefaults)
    defaultsBtn.grid(column=3, row=frameRow, sticky=W)

    for child in myFrame.winfo_children(): child.grid_configure(padx=5, pady=3)

