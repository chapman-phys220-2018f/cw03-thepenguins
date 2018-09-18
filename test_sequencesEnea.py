#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Note: See python_module_template.py first

###
# Name: Enea Dodi
# Student ID: 2296306
# Email: dodi@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW03
###

import sequencesEnea
import nose.tools
import numpy.testing



"""There are two tests in this file, both testing sequencesEnea.
    The first test names test_five() checks if the correct 5 terms 
    printed by the fibonacci method in "sequencesEnea" are correct
    the second term named test_term_thousand() checks if the thousandth 
    term printed by the fibonacci method in "sequencesEnea" is correct.
"""

def test_five():
    """Verify if the first 5 numbers printed by fibonacci() are correct
    """
    assert sequencesEnea.fibonacci(5) == [1,1,2,3,5]
    
def test_term_thousand():
    """Verify if the thousandth term printed by fibonacci() is correct
    """
    assert sequencesEnea.fibonacci(1000)[-1] == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    
