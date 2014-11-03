'''
Created on 01/11/2014

@author: Elloa
'''
import unittest
from src.ca import RuleNumber

class Test(unittest.TestCase):


    def testRuleNumber(self):
        rule30 = RuleNumber.RuleNumber(30)
        self.assertEqual(rule30.getNext(0, 0, 0), 0)
        self.assertEqual(rule30.getNext(0, 0, 1), 1)
        self.assertEqual(rule30.getNext(0, 1, 0), 1)
        self.assertEqual(rule30.getNext(0, 1, 1), 1)
        self.assertEqual(rule30.getNext(1, 0, 0), 1)              
        self.assertEqual(rule30.getNext(1, 0, 1), 0)
        self.assertEqual(rule30.getNext(1, 1, 0), 0)
        self.assertEqual(rule30.getNext(1, 1, 1), 0)
        
        rule45 = RuleNumber.RuleNumber(45)
        self.assertEqual(rule45.getNext(0, 0, 0), 1)
        self.assertEqual(rule45.getNext(0, 0, 1), 0)
        self.assertEqual(rule45.getNext(0, 1, 0), 1)
        self.assertEqual(rule45.getNext(0, 1, 1), 1)
        self.assertEqual(rule45.getNext(1, 0, 0), 0)              
        self.assertEqual(rule45.getNext(1, 0, 1), 1)
        self.assertEqual(rule45.getNext(1, 1, 0), 0)
        self.assertEqual(rule45.getNext(1, 1, 1), 0)
        
        rule200 = RuleNumber.RuleNumber(200)
        self.assertEqual(rule200.getNext(0, 0, 0), 0)
        self.assertEqual(rule200.getNext(0, 0, 1), 0)
        self.assertEqual(rule200.getNext(0, 1, 0), 0)
        self.assertEqual(rule200.getNext(0, 1, 1), 1)
        self.assertEqual(rule200.getNext(1, 0, 0), 0)              
        self.assertEqual(rule200.getNext(1, 0, 1), 0)
        self.assertEqual(rule200.getNext(1, 1, 0), 1)
        self.assertEqual(rule200.getNext(1, 1, 1), 1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRuleNumber']
    unittest.main()