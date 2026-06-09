"""Curated IPL knowledge base for demo agents (2024 season focus, evergreen records)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    name: str
    team: str
    role: str
    runs: int = 0
    wickets: int = 0
    strike_rate: float = 0.0
    economy: float = 0.0
    matches: int = 0


TEAMS: dict[str, dict] = {
    "CSK": {
        "full_name": "Chennai Super Kings",
        "captain": "MS Dhoni",
        "home_ground": "MA Chidambaram Stadium, Chennai",
        "titles": 5,
        "colors": "Yellow",
        "strength": "Spin-friendly home, experienced core, death bowling",
    },
    "MI": {
        "full_name": "Mumbai Indians",
        "captain": "Hardik Pandya",
        "home_ground": "Wankhede Stadium, Mumbai",
        "titles": 5,
        "colors": "Blue and Gold",
        "strength": "Pace at Wankhede, explosive top order, tactical depth",
    },
    "RCB": {
        "full_name": "Royal Challengers Bengaluru",
        "captain": "Faf du Plessis",
        "home_ground": "M. Chinnaswamy Stadium, Bengaluru",
        "titles": 0,
        "colors": "Red and Gold",
        "strength": "Batting-friendly Chinnaswamy, star power, high intent",
    },
    "KKR": {
        "full_name": "Kolkata Knight Riders",
        "captain": "Shreyas Iyer",
        "home_ground": "Eden Gardens, Kolkata",
        "titles": 3,
        "colors": "Purple and Gold",
        "strength": "2024 champions, spin at Eden, fearless batting",
    },
    "RR": {
        "full_name": "Rajasthan Royals",
        "captain": "Sanju Samson",
        "home_ground": "Sawai Mansingh Stadium, Jaipur",
        "titles": 1,
        "colors": "Pink",
        "strength": "Youth pipeline, smart auctions, balanced XI",
    },
    "DC": {
        "full_name": "Delhi Capitals",
        "captain": "Rishabh Pant",
        "home_ground": "Arun Jaitley Stadium, Delhi",
        "titles": 0,
        "colors": "Red and Blue",
        "strength": "Aggressive batting, young Indian talent",
    },
    "PBKS": {
        "full_name": "Punjab Kings",
        "captain": "Shreyas Iyer",
        "home_ground": "IS Bindra Stadium, Mohali",
        "titles": 0,
        "colors": "Red",
        "strength": "Power hitters, flat pitches, high-risk high-reward",
    },
    "SRH": {
        "full_name": "Sunrisers Hyderabad",
        "captain": "Pat Cummins",
        "home_ground": "Rajiv Gandhi Stadium, Hyderabad",
        "titles": 1,
        "colors": "Orange",
        "strength": "2024 finalists, record-breaking batting, Cummins leadership",
    },
    "GT": {
        "full_name": "Gujarat Titans",
        "captain": "Shubman Gill",
        "home_ground": "Narendra Modi Stadium, Ahmedabad",
        "titles": 1,
        "colors": "Navy and Gold",
        "strength": "2022 champions, Gill anchor, all-round depth",
    },
    "LSG": {
        "full_name": "Lucknow Super Giants",
        "captain": "KL Rahul",
        "home_ground": "BRSABV Ekana Stadium, Lucknow",
        "titles": 0,
        "colors": "Aqua Blue",
        "strength": "KL Rahul anchor, balanced squad building",
    },
}

PLAYERS: dict[str, Player] = {
    "virat kohli": Player("Virat Kohli", "RCB", "Batter", runs=741, strike_rate=154.7, matches=15),
    "travis head": Player("Travis Head", "SRH", "Batter", runs=567, strike_rate=215.0, matches=15),
    "sunil narine": Player("Sunil Narine", "KKR", "All-rounder", runs=488, wickets=17, strike_rate=180.7, economy=6.79, matches=16),
    "nitish rana": Player("Nitish Rana", "KKR", "Batter", runs=520, strike_rate=142.9, matches=16),
    "heinrich klaasen": Player("Heinrich Klaasen", "SRH", "Wicketkeeper-Batter", runs=479, strike_rate=171.1, matches=15),
    "ruturaj gaikwad": Player("Ruturaj Gaikwad", "CSK", "Batter", runs=583, strike_rate=147.1, matches=14),
    "shubman gill": Player("Shubman Gill", "GT", "Batter", runs=583, strike_rate=147.5, matches=14),
    "rohit sharma": Player("Rohit Sharma", "MI", "Batter", runs=417, strike_rate=150.0, matches=14),
    "hardik pandya": Player("Hardik Pandya", "MI", "All-rounder", runs=268, wickets=11, strike_rate=146.4, economy=9.47, matches=14),
    "jasprit bumrah": Player("Jasprit Bumrah", "MI", "Bowler", wickets=20, economy=6.55, matches=13),
    "harshal patel": Player("Harshal Patel", "PBKS", "Bowler", wickets=24, economy=9.55, matches=14),
    "yuzvendra chahal": Player("Yuzvendra Chahal", "RR", "Bowler", wickets=19, economy=8.64, matches=14),
    "pat cummins": Player("Pat Cummins", "SRH", "All-rounder", wickets=18, economy=8.22, matches=16),
    "mitchell starc": Player("Mitchell Starc", "KKR", "Bowler", wickets=16, economy=9.57, matches=15),
    "andre russell": Player("Andre Russell", "KKR", "All-rounder", runs=222, wickets=8, strike_rate=168.2, economy=9.43, matches=14),
    "ms dhoni": Player("MS Dhoni", "CSK", "Wicketkeeper-Batter", runs=325, strike_rate=142.1, matches=14),
    "faf du plessis": Player("Faf du Plessis", "RCB", "Batter", runs=418, strike_rate=155.0, matches=14),
    "kl rahul": Player("KL Rahul", "LSG", "Wicketkeeper-Batter", runs=583, strike_rate=142.0, matches=14),
    "sanju samson": Player("Sanju Samson", "RR", "Wicketkeeper-Batter", runs=531, strike_rate=153.9, matches=14),
    "rishabh pant": Player("Rishabh Pant", "DC", "Wicketkeeper-Batter", runs=446, strike_rate=156.6, matches=13),
}

POINTS_TABLE_2024: list[dict] = [
    {"rank": 1, "team": "KKR", "played": 14, "won": 9, "lost": 3, "nrr": 0.721, "points": 20},
    {"rank": 2, "team": "SRH", "played": 14, "won": 8, "lost": 5, "nrr": 0.268, "points": 17},
    {"rank": 3, "team": "RR", "played": 14, "won": 8, "lost": 5, "nrr": 0.273, "points": 17},
    {"rank": 4, "team": "RCB", "played": 14, "won": 7, "lost": 7, "nrr": 0.438, "points": 14},
    {"rank": 5, "team": "CSK", "played": 14, "won": 7, "lost": 7, "nrr": 0.131, "points": 14},
    {"rank": 6, "team": "PBKS", "played": 14, "won": 7, "lost": 7, "nrr": -0.185, "points": 14},
    {"rank": 7, "team": "DC", "played": 14, "won": 6, "lost": 8, "nrr": -0.377, "points": 12},
    {"rank": 8, "team": "LSG", "played": 14, "won": 6, "lost": 8, "nrr": -0.667, "points": 12},
    {"rank": 9, "team": "GT", "played": 14, "won": 5, "lost": 7, "nrr": -1.095, "points": 11},
    {"rank": 10, "team": "MI", "played": 14, "won": 4, "lost": 10, "nrr": -1.299, "points": 8},
]

HEAD_TO_HEAD: dict[tuple[str, str], dict] = {
    ("CSK", "MI"): {"played": 36, "csk_wins": 20, "mi_wins": 16, "note": "El Clasico of IPL — Dhoni vs Mumbai legacy"},
    ("RCB", "CSK"): {"played": 32, "rcb_wins": 12, "csk_wins": 20, "note": "RCB chasing first title against yellow army"},
    ("KKR", "SRH"): {"played": 26, "kkr_wins": 15, "srh_wins": 11, "note": "2024 final rematch — explosive batting vs spin"},
    ("MI", "RCB"): {"played": 34, "mi_wins": 19, "rcb_wins": 15, "note": "Wankhede vs Chinnaswamy shootouts"},
    ("RR", "GT"): {"played": 8, "rr_wins": 4, "gt_wins": 4, "note": "New rivalry — young guns vs 2022 champions"},
}

VENUES: dict[str, dict] = {
    "wankhede": {"city": "Mumbai", "avg_first_innings": 172, "favors": "Pace and power hitting", "night_dew": "Moderate"},
    "chinnaswamy": {"city": "Bengaluru", "avg_first_innings": 185, "favors": "Batting paradise, short boundaries", "night_dew": "Low"},
    "eden gardens": {"city": "Kolkata", "avg_first_innings": 165, "favors": "Spinners in second innings", "night_dew": "High"},
    "chepauk": {"city": "Chennai", "avg_first_innings": 158, "favors": "Spin, slower balls, CSK home advantage", "night_dew": "High"},
    "rajiv gandhi": {"city": "Hyderabad", "avg_first_innings": 178, "favors": "SRH 2024 batting carnage", "night_dew": "Moderate"},
}

RECORDS: dict[str, str] = {
    "highest_team_total": "SRH 287/3 vs RCB (2024) — highest ever IPL team score",
    "fastest_hundred": "Chris Gayle — 30 balls (2013) for RCB vs PWI",
    "most_runs_career": "Virat Kohli — 8000+ IPL runs, Orange Cap record holder multiple times",
    "most_wickets_career": "Yuzvendra Chahal — among top wicket-takers in IPL history",
    "most_titles_player": "Rohit Sharma — 6 IPL titles (5 with MI, 1 with DC as coach era overlap)",
    "purple_cap_2024": "Harshal Patel — 24 wickets for Punjab Kings",
    "orange_cap_2024": "Virat Kohli — 741 runs for RCB",
    "final_2024": "KKR beat SRH by 8 wickets — Sunil Narine Player of the Tournament",
}

SEASON_CHAMPIONS: dict[int, str] = {
    2008: "RR", 2009: "DC", 2010: "CSK", 2011: "CSK", 2012: "KKR",
    2013: "MI", 2014: "KKR", 2015: "MI", 2016: "SRH", 2017: "MI",
    2018: "CSK", 2019: "MI", 2020: "MI", 2021: "CSK", 2022: "GT",
    2023: "CSK", 2024: "KKR",
}

LEGENDARY_MOMENTS: list[str] = [
    "2016 final: Ben Cutting's spell helps SRH beat RCB for their first title",
    "2019 final: MI edge CSK by 1 run — Lasith Malinga's last-over heroics",
    "2023 final: MS Dhoni's CSK win 5th title in a rain-affected Ahmedabad thriller",
    "2024: SRH post 287 vs RCB — Travis Head 102 (39) rewrites batting records",
    "2024 final: KKR dismantle SRH for 47 — Mitchell Starc's new-ball masterclass",
]

UPCOMING_FIXTURES: list[dict] = [
    {"match": "MI vs CSK", "venue": "Wankhede", "date": "2025-03-23", "storyline": "El Clasico opener"},
    {"match": "RCB vs KKR", "venue": "Chinnaswamy", "date": "2025-03-24", "storyline": "Kohli vs Narine rematch"},
    {"match": "SRH vs RR", "venue": "Rajiv Gandhi", "date": "2025-03-25", "storyline": "2024 semi-finalists clash"},
    {"match": "GT vs DC", "venue": "Narendra Modi", "date": "2025-03-26", "storyline": "Gill vs Pant leadership battle"},
]

FANTASY_TIERS: dict[str, list[str]] = {
    "premium": ["Virat Kohli", "Travis Head", "Sunil Narine", "Jasprit Bumrah", "Pat Cummins"],
    "value": ["Nitish Rana", "Heinrich Klaasen", "Yuzvendra Chahal", "Ruturaj Gaikwad", "Andre Russell"],
    "differential": ["Mitchell Starc", "Harshal Patel", "Sanju Samson", "Hardik Pandya", "Rishabh Pant"],
}


def normalize_team(name: str) -> str | None:
    """Resolve team abbreviation or partial name."""
    key = name.strip().upper()
    if key in TEAMS:
        return key
    lowered = name.strip().lower()
    for abbr, info in TEAMS.items():
        if lowered in info["full_name"].lower() or lowered in abbr.lower():
            return abbr
    return None


def normalize_player(name: str) -> str | None:
    """Resolve player name case-insensitively."""
    lowered = name.strip().lower()
    for key in PLAYERS:
        if lowered == key or lowered in key:
            return key
    return None
