#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        val = fct(*args)

        return val
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as inst:
        message = "Exception: {}".format(inst)
        sys.stderr.write(message + "\n")
        return None
