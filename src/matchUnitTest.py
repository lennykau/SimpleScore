# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import sqlite3
import logging

from simpleMatch  import *
from shooterScore import *
from matchEntry   import *
from dataBase     import *
from shooter      import *


class  MatchUnitTestCase(unittest.TestCase):
    def setUp(self):
#        self.foo = MatchUnit()
        logging.basicConfig(filename='matchTest.log',level=logging.DEBUG)
        logging.info('Match Unit Test Starting')


    def tearDown(self):
        logging.info('Match Unit Test Complete')
        DataBase.dbConn.close()

#        self.foo.dispose()
#        self.foo = None

    def test_matchUnit(self):
        #assert x != y;
        #self.assertEqual(x, y, "Msg");
        numStages = 4
        
        try:
#            self._dbConn        = sqlite3.connect('test.db')
            DataBase.dbConn     = sqlite3.connect('test.db')
            DataBase.cursor     = DataBase.dbConn.cursor()
            
            Shooter.createTable()
            SimpleMatch.createTable()
            ShooterScore.createTable()
            
        except:
            logging.warning('Failed to open database')
            self.fail("Error: Failed to open database")
            
        match = SimpleMatch()
        
            
        for i in range(5):
            scores = list()
            for j in range(numStages):
                scores.append(ShooterScore(None, 1, i, j+1))
            match.addMatchEntry(MatchEntry(1, i, 'A', 15, scores))
        
        print( 'Match Date %f' % match.matchDate )
#        self.fail("TODO: Write test")

        matchEntries = match.matchEntries
        
        print ('number of entries %d' % len(matchEntries))
        
        for me in matchEntries:
            print(me)
            for score in me.scores:
                print(score)

            print('---------------------------------')
if __name__ == '__main__':
    unittest.main()

