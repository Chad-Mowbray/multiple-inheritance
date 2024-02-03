import unittest
from employees import *


class TestEmployees(unittest.TestCase):    
    
    def test_employee(self):
        e = Employee("123asd")
        self.assertIsInstance(e, Employee)

    def test_manager(self):
        m = Manager("123asd", "API Team")
        self.assertIsInstance(m, Employee)
        self.assertEqual(m.key_card_no, "123asd")
        self.assertEqual(m.department, "API Team")

    def test_technical(self):
        t = Technical("123asd")
        self.assertIsInstance(t, Employee)
      
    def test_developer(self):
        d = Developer("123asd", ["Java", "Python"])
        self.assertIsInstance(d, Employee) 
        self.assertEqual(d.languages, ["Java", "Python"])
        self.assertEqual(d.key_card_no, "123asd")
   
    def test_project_manager(self):
        pm = ProjectManager("123asd", "external")
        self.assertIsInstance(pm, Employee) 
        self.assertIsNotNone(pm.key_card_no)  
        
    def test_head_engineer(self):
        he = HeadEngineer("123asd", ["Javascript"], "C", "CS")
        self.assertIsInstance(he, Employee)  
        self.assertIsInstance(he, Developer)  
        self.assertIsInstance(he, ProjectManager)  
        self.assertEqual(he.key_card_no, "123asd")

        
        
if __name__ == "__main__":
    unittest.main()