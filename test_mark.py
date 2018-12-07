#!/usr/bin/python3 

class I:
    'imported objects'
    import unittest
    import mark

class Test_Marked(I.unittest.TestCase):    
    def test(self):  
        obj = 't'
        m = I.mark.Marked(obj)
        m.mark('first')
        m.mark('short')
        self.assertTrue(m.Is('first'))
        self.assertFalse(m.Is('second'))
        self.assertEqual(m.marks, ['first', 'short'])
        m.unmark('first')
        m.unmark('none')
        self.assertFalse(m.Is('first'))

if __name__ == '__main__':
    ttr = I.unittest.TextTestRunner(tb_locals=True)
    I.unittest.main(testRunner=ttr, verbosity=2)
