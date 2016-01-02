# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import timeit

BENCH_NUM = 1000
REPEAT_NUM = 100
input = [1,2,3,4]

SETUP = '''

from __main__ import test_iter, test_map, test_compr
words_l = u'Define a default timer, in a platform-specific manner. On Windows, time.clock() has microsecond granularity, but time.time()‘s granularity is 1/60th of a second. On Unix, time.clock() has 1/100th of a second granularity, and time.time() is much more precise. On either platform, default_timer() measures wall clock time, not the CPU time. This means that other processes running on the same computer may interfere with the timing.'.split(' ')

'''
def test_iter(words):
	out = list()
	for word in words:
		out.append(word.capitalize())
	return out

def test_map(words):
	return map(unicode.capitalize, words)

def test_compr(words):
	return [x.capitalize() for x in words]


def _run_test(command):
	min_test_time = min(timeit.repeat(
	command, 
	setup = SETUP,
	number = BENCH_NUM,
	repeat = REPEAT_NUM,
	))

	print 'Time for {}: {}'.format(command, min_test_time)

_run_test('test_iter(words_l)')
_run_test('test_map(words_l)')
_run_test('test_compr(words_l)')