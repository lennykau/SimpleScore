# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class ScoreConstants(object):
    
    def __init__(self):
        __miss       = 20
        __noShoot    = 40
        __procedural = 60
        
    @property
    def miss(self):
        return __miss
    
    @property
    def noShoot(self):
        return __noShoot
    
    @property
    def procedural(self):
        return __procedural