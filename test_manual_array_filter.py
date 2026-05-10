import unittest
from manual_array_filter import array_filter

class TestArrayFilter(unittest.TestCase):

  def test_remove_matching_items(self): 
      data = [
          {"type": "A"},
          {"type": "B"},
          {"type": "A"}
      ]
      result = array_filter(data, "type", "A")
      self.assertEqual(result, [{"type", "B"}])

  def test_no_items_removed(self): 
      data = [
          {"type": "A"}, 
          {"type": "A"}
      ]
      result = array_filter(data, "type", "C")
      self.assertEqual(result, [{"type": "A"}, {"type": "A"}])

  def test_empty_array(self): 
      data = []
      result = array_filter(data, "type", "A")
      self.assertEqual(result, [])

  def test_single_element(self): 
      data = [{"type": "A"}]
      result = array_filter(data, "type", "A")
      self.assertEqual(result, [])

if __name__ == "__main__": 
    unittest.main()
