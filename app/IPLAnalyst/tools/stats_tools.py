from strands import tool

from ipl_data.catalogue import PLAYERS, POINTS_TABLE_2024, TEAMS, normalize_player, normalize_team


@tool
def list_ipl_teams() -> str:
    """List all 10 IPL franchises with captains and title counts."""
    lines = ["IPL Franchises (2024 era):"]
    for abbr, info in TEAMS.items():
        lines.append(
            f"- {abbr}: {info['full_name']} | Captain: {info['captain']} | "
            f"Titles: {info['titles']} | Home: {info['home_ground']}"
        )
    return "\n".join(lines)


@tool
def get_team_profile(team_name: str) -> str:
    """Get detailed profile for an IPL team by name or abbreviation (e.g. CSK, Mumbai)."""
    abbr = normalize_team(team_name)
    if not abbr:
        return f"Team '{team_name}' not found. Use list_ipl_teams for valid teams."
    info = TEAMS[abbr]
    return (
        f"{info['full_name']} ({abbr})\n"
        f"Captain: {info['captain']}\n"
        f"Home: {info['home_ground']}\n"
        f"IPL Titles: {info['titles']}\n"
        f"Kit: {info['colors']}\n"
        f"Key strength: {info['strength']}"
    )


@tool
def get_points_table(season: int = 2024) -> str:
    """Return IPL league standings. Currently supports 2024 season."""
    if season != 2024:
        return f"Standings for {season} not in local database. Try season=2024."
    lines = [f"IPL {season} Points Table:"]
    for row in POINTS_TABLE_2024:
        lines.append(
            f"{row['rank']}. {row['team']} — {row['points']} pts "
            f"({row['won']}W/{row['lost']}L, NRR {row['nrr']:+.3f})"
        )
    return "\n".join(lines)


@tool
def get_player_stats(player_name: str) -> str:
    """Get IPL 2024 stats for a player by name (e.g. Virat Kohli, Bumrah)."""
    key = normalize_player(player_name)
    if not key:
        return f"Player '{player_name}' not found in 2024 database."
    p = PLAYERS[key]
    parts = [
        f"{p.name} ({p.team}) — {p.role}",
        f"Matches: {p.matches}",
    ]
    if p.runs:
        parts.append(f"Runs: {p.runs} @ SR {p.strike_rate}")
    if p.wickets:
        parts.append(f"Wickets: {p.wickets} @ Econ {p.economy}")
    return " | ".join(parts)


@tool
def compare_players(player_a: str, player_b: str) -> str:
    """Compare two IPL players head-to-head on 2024 stats."""
    key_a = normalize_player(player_a)
    key_b = normalize_player(player_b)
    if not key_a or not key_b:
        missing = []
        if not key_a:
            missing.append(player_a)
        if not key_b:
            missing.append(player_b)
        return f"Could not find: {', '.join(missing)}"
    a, b = PLAYERS[key_a], PLAYERS[key_b]
    verdict = []
    if a.runs and b.runs:
        verdict.append(f"Runs: {a.name} {a.runs} vs {b.name} {b.runs}")
    if a.wickets and b.wickets:
        verdict.append(f"Wickets: {a.name} {a.wickets} vs {b.name} {b.wickets}")
    if a.strike_rate and b.strike_rate:
        faster = a.name if a.strike_rate >= b.strike_rate else b.name
        verdict.append(f"Higher strike rate: {faster}")
    return f"Comparison ({a.team} vs {b.team}):\n" + "\n".join(verdict)
