import json
import os
import uuid

SCORE_FILE = os.path.join("data", "scores.json")


def ensure_score_file():
    """Ensure that the data folder and the score JSON file exist."""
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "w") as f:
            json.dump({"players": {}}, f)


def _load_data():
    """Load scoreboard data from file. Return dict with 'players' key."""
    ensure_score_file()
    with open(SCORE_FILE, "r") as f:
        try:
            data = json.load(f)
            if "players" not in data:
                data = {"players": {}}
            return data
        except Exception:
            return {"players": {}}


def _save_data(data):
    """Save scoreboard data to the JSON file with indentation."""
    ensure_score_file()
    with open(SCORE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def _find_player_id_by_name(data, name):
    """Return the unique player ID for a given name, or None if not found."""
    for pid, entry in data.get("players", {}).items():
        if entry.get("name") == name:
            return pid
    return None


def _create_player_entry(data, name):
    """Create a new player entry with a UUID and initial stats."""
    pid = str(uuid.uuid4())
    data["players"][pid] = {"name": name, "games": 0, "wins": 0, "losses": 0}
    return pid


def update_score(winner_name, players):
    """
    Update wins/losses/total games for a completed round.

    Args:
        winner_name (str): Name of the winning player.
        players (list): List of Player objects in the round.
    """
    data = _load_data()
    for player in players:
        name = player.name
        pid = _find_player_id_by_name(data, name)
        if not pid:
            pid = _create_player_entry(data, name)
        data["players"][pid]["games"] = data["players"][pid].get("games", 0) + 1
        if name == winner_name:
            data["players"][pid]["wins"] = data["players"][pid].get("wins", 0) + 1
        else:
            data["players"][pid]["losses"] = data["players"][pid].get("losses", 0) + 1
    _save_data(data)


def show_scores():
    """Print all players' wins, losses, and total games to the terminal."""
    data = _load_data()
    players = data.get("players", {})
    if not players:
        print("No scores yet!")
        return
    print("\n🏅 High Scores 🏅")
    for pid, stats in players.items():
        name = stats.get("name", pid)
        print(f"{name}: {stats.get('wins', 0)} wins / {stats.get('losses', 0)} losses / {stats.get('games', 0)} games")


def rename_player(old_name, new_name):
    """
    Rename or merge stats from old_name to new_name.

    If new_name exists, merge old stats into new and remove old entry.

    Args:
        old_name (str): Current player name to rename.
        new_name (str): New player name.
    """
    data = _load_data()
    players = data.setdefault("players", {})

    old_pid = _find_player_id_by_name(data, old_name)
    new_pid = _find_player_id_by_name(data, new_name)

    if not old_pid:
        if not new_pid:
            _create_player_entry(data, new_name)
        _save_data(data)
        return

    if not new_pid:
        data["players"][old_pid]["name"] = new_name
    else:
        old = players.get(old_pid, {})
        new = players.get(new_pid, {})
        new["games"] = new.get("games", 0) + old.get("games", 0)
        new["wins"] = new.get("wins", 0) + old.get("wins", 0)
        new["losses"] = new.get("losses", 0) + old.get("losses", 0)
        players.pop(old_pid, None)

    _save_data(data)


def list_players():
    """Return a list of all player names currently in the scoreboard."""
    data = _load_data()
    return [entry.get("name") for entry in data.get("players", {}).values()]
