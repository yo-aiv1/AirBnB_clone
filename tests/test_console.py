#!/usr/bin/python3
"""unittest for base_model"""

import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def test_quit_command(self):
        """Test the 'quit' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")


if __name__ == '__main__':
    unittest.main()
