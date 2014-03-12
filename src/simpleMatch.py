# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import time
import logging

from dataBase import *

class SimpleMatch(object):
        
    def __init__(self):
        logging.info('SimpleMatch constructor')
        self._matchDate    = time.time()
        self._matchEntries = list()
        
    def addMatchEntry(self,matchEntry):
        self._matchEntries.append(matchEntry)
        
    def delMatchEntry(self,matchEntryId):
        self._matchEntries.remove(matchEntryId)
        
    @property 
    def matchEntries(self):
        return self._matchEntries
    
    @property
    def scores(self):
        return self._scores
    
    @property
    def matchDate(self):
        return self._matchDate
    
    @matchDate.setter
    def matchDate(self,date):
        self._matchDate = date

    def createTable():
        DataBase.dbConn.execute("""
            CREATE TABLE IF NOT EXISTS matches(
	        matchId    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                matchDate  INTEGER NOT NULL      
                    )
               """)
