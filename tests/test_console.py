#!/usr/bin/python3
"""Test the console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class test console"""

    def create(self):
        """create the instance"""
        return HBNBCommand()

    def test_quit(self):
        """ test for the method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """test for the method EOF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
