# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class ScoreConstants(object):
    
    def __init__(self, miss=20, noShoot=40, procedural=60):
        self._miss       = miss
        self._noShoot    = noShoot
        self._procedural = procedural
        
    @property
    def miss(self):
        return self._miss
    
    @property
    def noShoot(self):
        return self._noShoot
    
    @property
    def procedural(self):
        return self._procedural