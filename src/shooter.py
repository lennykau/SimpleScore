
__author__="lenny"
__date__ ="$Mar 9, 2014 4:48:32 PM$"

import logging

class Shooter(object):
    
    dbConn = 0
    
    def __init__(self, name, id):
        self._name       = name
        self._shooter_id = id
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._shooter_id
    
    @name.setter
    def name(self):
        self._name = name
        
    def saveShooter(self):
        sql = 'INSERT INTO SHOOTERS(NAME) VALUES("%s")' % self._name
        logging.info('SQL :: %s' % sql)
        try:
           Shooter.dbConn.execute(sql)
           Shooter.dbConn.commit()
        except:
            logging.error("insert failed")
    