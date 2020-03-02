# -*- coding: utf-8 -*-

"""
This module contains functions common to various cloud providers.
"""

from time import time
import subprocess


def createWorkerInstanceName(prefix):
    """Return a unique name based on prefix and timestamp."""
    return "%s%s" % (prefix, int(time()))


def _run_or_none(cmd):
    """Execute command. Returns None in case of exception."""
    try:
        return subprocess.Popen(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
    except Exception as e:
        print(e)
    return None


def _check_output_or_none(cmd):
    """Execute command. Returns None in case of exception."""
    try:
        return subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, universal_newlines=True
        )
    except Exception as e:
        print(e)
    return None


# vim: tabstop=4 noexpandtab shiftwidth=4 softtabstop=4 textwidth=79
