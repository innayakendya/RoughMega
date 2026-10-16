# test_roughmega.py
"""
Tests for RoughMega module.
"""

import unittest
from roughmega import RoughMega

class TestRoughMega(unittest.TestCase):
    """Test cases for RoughMega class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughMega()
        self.assertIsInstance(instance, RoughMega)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughMega()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
