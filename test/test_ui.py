import unittest
from io import StringIO
from unittest.mock import patch
from ui import UI


class DummyPlayer:
    def __init__(self,name,total, current):
        self.name = name
        self.total_score = total
        self.current_score = current

class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = UI()
        self.players = [ 
            DummyPlayer("Jeyson", 80,10),
            DummyPlayer("Hussein", 65, 5)
        ]

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice(self, mock_stdout):
        self.ui.show_dice(5)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch ('sys.stdout', new_callable=StringIO)
    def test_print_title(self, mock_stdout):
        self.ui.show_dice(4)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_1(self, mock_stdout):
        self.ui.show_dice(1)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_2(self, mock_stdout):
        self.ui.show_dice(2)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_3(self, mock_stdout):
        self.ui.show_dice(3)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_4(self, mock_stdout):
        self.ui.show_dice(4)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_5(self, mock_stdout):
        self.ui.show_dice(5)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_6(self, mock_stdout):
        self.ui.show_dice(6)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_scores_prints_scoreboard(self, mock_stdout):
        self.ui.show_scores(self.players)
        output = mock_stdout.getvalue()
        self.assertIn("SCOREBOARD", output)
        self.assertIn("Jeyson", output)
        self.assertIn("Hussein", output)
        self.assertIn("10",output)
        self.assertIn("Hussein",output)
        self.assertIn("65",output)
        self.assertIn("5",output)
        self.assertIn("-",output)
        self.assertIn(".",output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_winner_prints_congratulations(self, mock_stdout):
        self.ui.winner(self.players[0])
        output = mock_stdout.getvalue()
        self.assertIn("CONGRATULATIONS", output)
        self.assertIn("Jeyson", output)
        self.assertIn("80",output)
       
if __name__=='__main__':
    unittest.main()
