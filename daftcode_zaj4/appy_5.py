# -*- coding: utf-8 -*-

import cProfile
import time

def lol():
	time.sleep(1)
	print 'lol'

cProfile.run('lol(); lol()')


####pycallgraph graphviz lineprofiler!!!!!!!!!!!!!!!!!!
####