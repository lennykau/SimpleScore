# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="lenny"
__date__ ="$Mar 9, 2014 4:48:32 PM$"

class Shooter(object):
    
    def __init__(self, name, id):
        __name       = name
        __shooter_id = id
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._shooter_id