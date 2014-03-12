# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import logging
from dataBase import *

class ShooterScore(object):
    
    scoreConstants = None
        
    # 
    def __init__(self, scoreId, matchId, shooterId, stage, 
                       time=0.0, miss=0, noShoot=0, procedural=0, bonus=0):
        self._scoreId      = scoreId  # set to None if this is the first creation
        self._matchId      = matchId
        self._shooterId    = shooterId
        self._stage        = stage
        self._time         = time
        self._miss         = miss
        self._noShoot      = noShoot
        self._procedural   = procedural
        self._bonus        = bonus
        self._totalScore   = 0
        
    def __str__(self):
        printString  = 'stage       %d\n' % self._stage
        printString += 'time        %f\n' % self._time
        printString += 'miss        %d\n' % self._miss
        printString += 'no shoot    %d\n' % self._noShoot
        printString += 'procedural  %d\n' % self._procedural
        printString += 'bonus       %d\n' % self._bonus
        printString += 'Total Score %f\n' % self._totalScore
        return printString
 
    @property
    def shooterId(self):
        return self._shooterId
    @property
    def matchId(self):
        return self._matchId
    @property
    def scoreId(self):
        return self._scoreId
    @property
    def stage(self):
        return self._stage
    @property
    def time(self):
        return self._time
    @property
    def miss(self):
        return self._miss
    @property
    def noShoot(self):
        return self._noShoot
    @property
    def procedural(self):
        return self._procedural
    @property
    def totalScore(self):
        self._totalScore = (self._time + 
                           (self._miss        * ShooterScore.scoreConstants.miss) +
                           (self._noShoot     * ShooterScore.scoreConstants.noShoot) +
                           (self._procedural  * ShooterScore.scoreConstants.procedural) -
                           (self._bonus       * ShooterScore.scoreConstants.bonus))
        return self._totalScore

    @time.setter
    def time(self, time):
        self._time = time
    @miss.setter
    def miss(self,miss):
        self._miss = miss
    @noShoot.setter
    def noShoot(self,noShoot):
        self._noShoot = noShoot
    @procedural.setter
    def procedural(self,procedural):
        self._procedural = procedural
        
    def createTable():
        DataBase.dbConn.execute("""
               CREATE TABLE IF NOT EXISTS scores(
	               scoreId    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                       matchId    INTEGER,
                       shooterId  INTEGER,
                       stage      INTEGER,
                       time       REAL,
                       miss       INTEGER,
                       noShoot    INTEGER,
                       procedural INTEGER,
                       bonus      INTEGER,
                       totalScore REAL
                    )
               """)
    
    def writeToDB(self):
        if (self._scoreId == None ):
            sql = 'INSERT INTO scores( matchId, shooterId, \
                 stage, time, miss, noShoot, procedural, bonus, totalScore)     \
                 VALUES(%d, %d, %d, %f, %d, %d, %d, %d, %f)' %                  \
                 ( self._matchId, self._shooterId, self._stage,                 \
                  self._time, self._miss, self._noShoot, self._procedural,      \
                  self._bonus, self._totalScore)
        else:    
            sql = 'INSERT ON CONFLICT IGNORE INTO scores(scoreId, matchId, shooterId, \
                 stage, time, miss, noShoot, procedural, bonus, totalScore)       \
                 VALUES(%d, %d, %d, %d, %f, %d, %d, %d, %d, %f)' %                \
                 (self._scoreId, self._matchId, self._shooterId, self._stage,     \
                  self._time, self._miss, self._noShoot, self._procedural,        \
                  self._bonus, self._totalScore)

        logging.info(sql)
        DataBase.dbConn.execute(sql)
        DataBase.dbConn.commit()
    
        