# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class MatchEntry(object):
    
    def __init__(self, matchId, shooterId, shooterClass, 
                       matchFee, scores, powerFactor=None ):
        self._scores       = list()
        self._matchId      = matchId
        self._shooterId    = shooterId
        self._shooterClass = shooterClass
        self._matchFee     = matchFee
        self._scores       = list(scores)
        self._powerFactor  = powerFactor
        
    def __str__(self):
        printString  = 'matchId       %d\n' % self._matchId
        printString += 'shooterId     %d\n' % self._shooterId
        printString += 'shooter Class %s\n' % self._shooterClass
        printString += 'match fee     %d\n' % self._matchFee
        printString += 'power factor  %s\n' % self._powerFactor
        
        for score in self._scores:
            score.writeToDB()
        return printString
        
        
    @property
    def matchId(self):
        return self._matchId
    
    @property
    def shooterId(self):
        return self._shooterId
    
    @property
    def shooterClass(self):
        return self._shooterClass
    
    @property
    def matchFee(self):
        return self._matchFee
    
    @property
    def powerFactor(self):
        return self._powerFactor
    
    @property
    def scores(self):
        return self._scores
