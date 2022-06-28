import unittest
from subprocess import Popen, PIPE
import subprocess
from autograder import function_test, exact_compare


def custom_list_compare(candidate, gold):
    if len(candidate) != len(gold):
        return False, f"the proposed solution does not have the correct length:\n{candidate}"
    elif tuple(candidate) != tuple(gold):
        return False, f"the proposed solution does not have the correct elements:\n{candidate}"
    return True, "correct"


class TestOne(unittest.TestCase):

    def test_fibs_up_to1(self):
        function_test("hw", "fibs_up_to", (5,),
                      lambda c: exact_compare(c, [1, 1, 2, 3, 5]))


class TestTwo(unittest.TestCase):

    def test_fibs_up_to2(self):
        function_test("hw", "fibs_up_to", (5,),
                      lambda c: custom_list_compare(c, [1, 1, 2, 3]))

    def test_fibs_up_to3(self):
        function_test("hw", "fibs_up_to", (5,),
                      lambda c: custom_list_compare(c, [1, 1, 2, 3, 6]))
