# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class ShooterScore(object):
    
    scoreConstants = 0  
    dbConn         = 0
        
    # 
    def __init__(self,matchId, shooterId, stage, 
                 time=0, miss=0, noShoot=0, procedural=0):
        self._matchId    = matchId
        self._shooterId  = shooterId
        self._stage      = stage
        self._time       = time
        self._miss       = miss
        self._noShoot    = noShoot
        self._procedural = procedural
        self._totalScore = 0
 
    @property
    def matchId(self):
        return self._matchId
    @property
    def shooterId(self):
        return self._shooterId
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
                           (self._procedural  * ShooterScore.scoreConstants.procedural))
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
    