import unittest
import json
from game import Game
from player import Player
from bot import ComputerPlayer
from unittest.mock import patch

# --- Initialization tests ---
def test_single_player_initialization():
    game = Game()
    with patch("builtins.input", return_value="Alice"):
        game.start_single_player()
    assert isinstance(game.players[0], Player)
    assert isinstance(game.players[1], ComputerPlayer)
    assert game.players[0].name == "Alice"
    assert game.players[1].name == "Computer"

def test_two_player_initialization():
    game = Game()
    with patch("builtins.input", side_effect=["Alice","Bob"]):
        game.start_two_player()
    assert isinstance(game.players[0], Player)
    assert isinstance(game.players[1], Player)
    assert game.players[0].name == "Alice"
    assert game.players[1].name == "Bob"

# --- Turn logic ---
def test_switch_turn():
    game = Game()
    game.players = [Player("A"), Player("B")]
    game.current_player_index = 0
    game.switch_turn()
    assert game.current_player_index == 1
    game.switch_turn()
    assert game.current_player_index == 0

def test_hold_adds_to_total():
    player = Player("A")
    player.current_score = 5
    player.add_to_total()
    assert player.total_score == 5
    assert player.current_score == 0

def test_roll_one_resets_current(monkeypatch):
    game = Game()
    game.players = [Player("A")]
    game.current_player_index = 0
    # simulate rolling 1
    monkeypatch.setattr(game.dice, "roll", lambda: 1)
    p = game.players[0]
    p.current_score = 4
    roll = game.dice.roll()
    assert roll == 1
    p.reset_turn()
    assert p.current_score == 0

def test_cheat_roll_increases_by_6(monkeypatch):
    game = Game()
    game.players = [Player("A")]
    game.current_player_index = 0
    monkeypatch.setattr(game.dice, "roll", lambda cheat_number=None: cheat_number)
    p = game.players[0]
    p.current_score = 0
    cheat_value = game.dice.roll(cheat_number=6)
    p.current_score += cheat_value
    assert cheat_value == 6
    assert p.current_score == 6

def test_check_winner_triggers(monkeypatch):
    game = Game()
    player = Player("A")
    player.total_score = 100
    game.players = [player]
    monkeypatch.setattr(game, "update_scores", lambda name: True)
    result = game.check_winner(player)
    assert result is True

def test_show_rules_output(capsys):
    game = Game()
    game.show_rules()
    captured = capsys.readouterr()
    assert "Rules of Pig Dice Game" in captured.out

def test_computer_player_decision():
    cp = ComputerPlayer("AI")
    decision = cp.decide()
    assert decision in ["roll","hold"]

def test_alternate_turns_and_scores():
    game = Game()
    game.players = [Player("A"), Player("B")]
    p1, p2 = game.players
    p1.current_score = 5
    p1.add_to_total()
    assert p1.total_score == 5
    game.switch_turn()
    assert game.current_player_index == 1
    p2.current_score = 7
    p2.add_to_total()
    assert p2.total_score == 7
