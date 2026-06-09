from strands import tool

from ipl_data.catalogue import HEAD_TO_HEAD, UPCOMING_FIXTURES, VENUES, normalize_team


@tool
def get_head_to_head(team_a: str, team_b: str) -> str:
    """Get historical head-to-head record between two IPL teams."""
    abbr_a = normalize_team(team_a)
    abbr_b = normalize_team(team_b)
    if not abbr_a or not abbr_b:
        return "Provide two valid team names or abbreviations (e.g. CSK and MI)."
    key = (abbr_a, abbr_b) if (abbr_a, abbr_b) in HEAD_TO_HEAD else (abbr_b, abbr_a)
    if key not in HEAD_TO_HEAD:
        return f"No detailed H2H data for {abbr_a} vs {abbr_b} in local database."
    data = HEAD_TO_HEAD[key]
    wins_a = data.get(f"{abbr_a.lower()}_wins") or data.get(f"{key[0].lower()}_wins", "?")
    wins_b = data.get(f"{abbr_b.lower()}_wins") or data.get(f"{key[1].lower()}_wins", "?")
    return (
        f"{abbr_a} vs {abbr_b}: {data['played']} matches played\n"
        f"Wins — {abbr_a}: {wins_a}, {abbr_b}: {wins_b}\n"
        f"Insight: {data['note']}"
    )


@tool
def get_venue_analysis(venue: str) -> str:
    """Analyze an IPL venue — pitch behavior, average scores, what style of cricket it favors."""
    key = venue.strip().lower().replace(" stadium", "").replace(" ", "")
    matched = None
    for vkey, info in VENUES.items():
        if key in vkey or vkey in key or key in info["city"].lower():
            matched = (vkey, info)
            break
    if not matched:
        venues = ", ".join(VENUES.keys())
        return f"Venue not found. Try one of: {venues}"
    vkey, info = matched
    return (
        f"{vkey.title()} ({info['city']})\n"
        f"Avg 1st innings score: {info['avg_first_innings']}\n"
        f"Favors: {info['favors']}\n"
        f"Night dew factor: {info['night_dew']}"
    )


@tool
def get_upcoming_fixtures() -> str:
    """List sample upcoming IPL fixtures with venue and storyline (demo schedule)."""
    lines = ["Upcoming IPL fixtures (demo schedule):"]
    for fix in UPCOMING_FIXTURES:
        lines.append(f"- {fix['date']}: {fix['match']} @ {fix['venue']} — {fix['storyline']}")
    return "\n".join(lines)


@tool
def predict_match_edge(team_a: str, team_b: str, venue: str = "") -> str:
    """Give a qualitative match prediction based on H2H, form, and venue (not real odds)."""
    abbr_a = normalize_team(team_a)
    abbr_b = normalize_team(team_b)
    if not abbr_a or not abbr_b:
        return "Need two valid teams for a prediction."

    key = (abbr_a, abbr_b) if (abbr_a, abbr_b) in HEAD_TO_HEAD else (abbr_b, abbr_a)
    h2h_note = HEAD_TO_HEAD[key]["note"] if key in HEAD_TO_HEAD else "Limited H2H data available."

    venue_note = ""
    if venue:
        vkey = venue.strip().lower().replace(" stadium", "").replace(" ", "")
        for name, info in VENUES.items():
            if vkey in name or vkey in info["city"].lower():
                venue_note = f"Venue favors: {info['favors']}"
                break

    return (
        f"Match preview: {abbr_a} vs {abbr_b}\n"
        f"H2H insight: {h2h_note}\n"
        f"{venue_note}\n"
        f"Edge: Slight advantage to the team with better recent form and home conditions."
    )
