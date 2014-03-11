# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import time

class SimpleMatch(object):
    
    def __init__(self):
        self._date     = time.time()
        self._shooters = list()
        self._scores   = list()
        
    def addShooter(self,shooterId):
        self._shooters.append(shooterId)
        
    def delShooter(self,shooterId):
        self._shooters.remove(shooterId)