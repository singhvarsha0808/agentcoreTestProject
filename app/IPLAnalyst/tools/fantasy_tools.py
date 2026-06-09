from strands import tool

from ipl_data.catalogue import FANTASY_TIERS, PLAYERS, normalize_player, normalize_team


@tool
def suggest_fantasy_xi(match_context: str = "balanced", budget_tier: str = "premium") -> str:
    """Suggest a sample Dream11-style XI for IPL fantasy. budget_tier: premium, value, or differential."""
    tier = budget_tier.strip().lower()
    if tier not in FANTASY_TIERS:
        tier = "premium"
    picks = FANTASY_TIERS[tier][:7]
    return (
        f"Fantasy XI suggestion ({tier} picks) for '{match_context}':\n"
        f"Batters/AR: {', '.join(picks[:4])}\n"
        f"Bowlers: {', '.join(picks[4:])}\n"
        f"Captain pick: {picks[0]} | Vice-captain: {picks[1]}\n"
        f"Tip: Stack SRH/KKR batters on flat pitches; pick Narine/Bumrah on turning tracks."
    )


@tool
def get_captain_picks(teams_playing: str) -> str:
    """Recommend fantasy captain/vice-captain for a match involving given teams (e.g. 'RCB vs CSK')."""
    teams = [normalize_team(t.strip()) for t in teams_playing.replace("vs", " ").split() if t.strip()]
    teams = [t for t in teams if t]
    if not teams:
        return "Specify teams playing, e.g. 'SRH vs KKR'."
    captains = {
        "RCB": "Virat Kohli",
        "CSK": "Ruturaj Gaikwad",
        "MI": "Rohit Sharma",
        "KKR": "Sunil Narine",
        "SRH": "Travis Head",
        "RR": "Sanju Samson",
        "GT": "Shubman Gill",
        "DC": "Rishabh Pant",
        "PBKS": "Shreyas Iyer",
        "LSG": "KL Rahul",
    }
    picks = [captains.get(t, "Top run-scorer from lineup") for t in teams]
    return (
        f"Captain options for {' vs '.join(teams)}:\n"
        f"Primary: {picks[0]}\n"
        f"Alternate: {picks[-1] if len(picks) > 1 else picks[0]}\n"
        f"Differential: Andre Russell or Heinrich Klaasen if chasing"
    )


@tool
def rate_fantasy_pick(player_name: str) -> str:
    """Rate a player's fantasy value for IPL based on 2024 form."""
    key = normalize_player(player_name)
    if not key:
        return f"Player '{player_name}' not in database."
    p = PLAYERS[key]
    score = 5
    if p.strike_rate >= 170:
        score += 2
    if p.wickets >= 15:
        score += 2
    if p.runs >= 500:
        score += 1
    tier = "Must-pick" if score >= 8 else "Strong pick" if score >= 6 else "Situational"
    return f"{p.name}: {tier} (fantasy score {score}/10) — {p.role} for {p.team}"
