# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import sqlite3
import logging

from shooter import *

class  CreateTestDBTestCase(unittest.TestCase):
    
    def setUp(self):
        logging.basicConfig(filename='test.log',level=logging.DEBUG)
        logging.info('CreateTestDBTestCase starting')

    def tearDown(self):
        self._dbConn.close()

    def test_createTestDB(self):
        #assert x != y;
        #self.assertEqual(x, y, "Msg");
        try:
            self._dbConn = sqlite3.connect('test.db')
            Shooter.dbConn = self._dbConn
            
        except:
            logging.warning('Failed to open database')
            self.fail("Error: Failed to open database")

        logging.info('creating table shooters')
        self._dbConn.execute('''CREATE TABLE SHOOTERS
                        (ID   INTEGER  PRIMARY KEY AUTOINCREMENT,
                         NAME TEXT             NOT NULL)''')

        
        self._names = ['Ken Lau', 'Mike Colbert', 'Allison Cutsinger']

        for name in self._names:
            shooter = Shooter(name, None)
            shooter.saveShooter()

        
        self.fail("TODO: Write test")

if __name__ == '__main__':
    unittest.main()

