#!/usr/bin/env python
# encoding: utf-8

import functools
import sys


def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    print('*  %s line %s' % (func_name, line_no))


def trace_calls(frame, event, arg, to_be_traced):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from printing
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    print('* Call to %s on line %s of %s' %
          (func_name, line_no, filename))
    if func_name in to_be_traced:
        # Trace into this function
        return trace_lines
    return


def c(input):
    print('input =', input)
    print('Leaving c()')


def b(arg):
    val = arg * 5
    c(val)
    print('Leaving b()')


def a():
    b(2)
    print('Leaving a()')


tracer = functools.partial(trace_calls, to_be_traced=['b'])
sys.settrace(tracer)
a()