import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0

        
class HighScoresTest(unittest.TestCase):

    def setUp(self):
        self.scores = [1000, 2000, 3000, 5000]

    # Tests

    # Test latest score (the last thing in the list)
    def test_latest(self):
        self.assertEqual(5000, latest(self.scores))    

    # Test personal best (the highest score in the list)

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
