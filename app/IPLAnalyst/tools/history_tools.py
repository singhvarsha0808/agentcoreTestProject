from strands import tool

from ipl_data.catalogue import LEGENDARY_MOMENTS, RECORDS, SEASON_CHAMPIONS


@tool
def get_ipl_record(record_key: str) -> str:
    """Look up an IPL record. Keys include: highest_team_total, fastest_hundred, orange_cap_2024, final_2024, etc."""
    key = record_key.strip().lower().replace(" ", "_").replace("-", "_")
    for rkey, value in RECORDS.items():
        if key in rkey or rkey in key:
            return f"{rkey.replace('_', ' ').title()}: {value}"
    available = ", ".join(RECORDS.keys())
    return f"Record not found. Try: {available}"


@tool
def get_season_champion(year: int) -> str:
    """Return the IPL champion for a given season year (2008–2024)."""
    if year not in SEASON_CHAMPIONS:
        return f"No champion data for {year}. Range: 2008–2024."
    team = SEASON_CHAMPIONS[year]
    return f"IPL {year} champion: {team}"


@tool
def list_legendary_moments() -> str:
    """Share iconic IPL moments and finals highlights."""
    return "Legendary IPL moments:\n" + "\n".join(f"- {m}" for m in LEGENDARY_MOMENTS)


@tool
def get_title_leaderboard() -> str:
    """Show franchises ranked by IPL titles won."""
    from ipl_data.catalogue import TEAMS

    ranked = sorted(TEAMS.items(), key=lambda x: x[1]["titles"], reverse=True)
    lines = ["IPL Title Leaderboard:"]
    for abbr, info in ranked:
        lines.append(f"- {info['full_name']} ({abbr}): {info['titles']} titles")
    return "\n".join(lines)
