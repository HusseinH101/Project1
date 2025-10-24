
import json
import os
import uuid

SCORE_FILE = os.path.join("data", "scores.json")


def ensure_score_file():
    """Ensure data directory and file exist."""
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "w") as f:
            json.dump({"players": {}}, f)


def _load_data():
    """Load scoreboard safely."""
    ensure_score_file()
    try:
        with open(SCORE_FILE, "r") as f:
            data = json.load(f)
            if "players" not in data:
                data["players"] = {}
            return data
    except Exception:
        return {"players": {}}


def _save_data(data):
    ensure_score_file()
    with open(SCORE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def _find_player_id_by_name(data, name):
    for pid, entry in data["players"].items():
        if entry.get("name") == name:
            return pid
    return None


def _create_player_entry(data, name):
    pid = str(uuid.uuid4())
    data["players"][pid] = {"name": name, "games": 0, "wins": 0, "losses": 0}
    return pid


def update_score(winner_name, players):
    """Update wins/losses and total games."""
    data = _load_data()
    for player in players:
        name = player.name
        pid = _find_player_id_by_name(data, name)
        if not pid:
            pid = _create_player_entry(data, name)
        data["players"][pid]["games"] += 1
        if name == winner_name:
            data["players"][pid]["wins"] += 1
        else:
            data["players"][pid]["losses"] += 1
    _save_data(data)


def show_scores():
    """Display scoreboard."""
    data = _load_data()
    players = data.get("players", {})
    if not players:
        print("No scores yet!")
        return
    print("\n🏅 High Scores 🏅")
    for stats in players.values():
        print(f"{stats['name']}: {stats['wins']}W / {stats['losses']}L / {stats['games']}G")


def rename_player(old_name, new_name):
    """Rename or merge players."""
    data = _load_data()
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
        old = data["players"][old_pid]
        new = data["players"][new_pid]
        new["games"] += old["games"]
        new["wins"] += old["wins"]
        new["losses"] += old["losses"]
        data["players"].pop(old_pid, None)

    _save_data(data)


def list_players():
    """List all players."""
    data = _load_data()
    return [p["name"] for p in data["players"].values()]

