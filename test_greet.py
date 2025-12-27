#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for MiAI Greeting Application
"""

import unittest
from greet import greet_user


class TestGreeting(unittest.TestCase):
    """Test cases for greeting functionality"""
    
    def test_greet_without_name(self):
        """Test greeting without providing a name"""
        result = greet_user()
        self.assertEqual(result, "Chào bạn!")
    
    def test_greet_with_name(self):
        """Test greeting with a name"""
        result = greet_user("Minh")
        self.assertEqual(result, "Chào bạn Minh!")
    
    def test_greet_with_different_names(self):
        """Test greeting with different names"""
        test_cases = [
            ("An", "Chào bạn An!"),
            ("Hương", "Chào bạn Hương!"),
            ("Phong", "Chào bạn Phong!"),
        ]
        
        for name, expected in test_cases:
            with self.subTest(name=name):
                result = greet_user(name)
                self.assertEqual(result, expected)
    
    def test_greet_with_empty_string(self):
        """Test greeting with empty string behaves like no name"""
        result = greet_user("")
        # Empty string is falsy, so should return basic greeting
        self.assertEqual(result, "Chào bạn!")


if __name__ == "__main__":
    unittest.main()
