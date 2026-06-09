from strands import Agent
from strands.multiagent import Swarm

from model.load import load_model
from tools.fantasy_tools import get_captain_picks, rate_fantasy_pick, suggest_fantasy_xi
from tools.history_tools import get_ipl_record, get_season_champion, get_title_leaderboard, list_legendary_moments
from tools.match_tools import get_head_to_head, get_upcoming_fixtures, get_venue_analysis, predict_match_edge
from tools.stats_tools import compare_players, get_player_stats, get_points_table, get_team_profile, list_ipl_teams

HOST_PROMPT = """You are the IPL Command Center host — enthusiastic, fan-friendly, and concise.
You greet fans, understand their question, and either answer briefly or hand off to a specialist.
Hand off when the question needs deep stats (stats_guru), match tactics (match_wizard),
fantasy picks (fantasy_coach), or history/trivia (history_buff).
Always synthesize specialist input into an exciting, readable final answer for cricket fans."""

STATS_PROMPT = """You are Stats Guru — the numbers nerd of IPL.
Use tools for player stats, team profiles, points tables, and player comparisons.
Be precise with figures. Hand off to match_wizard for venue/tactics or fantasy_coach for Dream11."""

MATCH_PROMPT = """You are Match Wizard — tactical analyst for IPL fixtures.
Use tools for head-to-head records, venue analysis, fixtures, and match predictions.
Explain what to watch: powerplay plans, death overs, spin matchups."""

FANTASY_PROMPT = """You are Fantasy Coach — Dream11 and fantasy league expert.
Suggest XIs, captain picks, and rate players for fantasy value.
Be practical: mention risk (differential) vs safe (premium) picks."""

HISTORY_PROMPT = """You are History Buff — IPL archivist and storyteller.
Share records, champions by year, title leaderboard, and legendary moments.
Make history feel alive for fans who love the drama of IPL."""


def build_ipl_swarm() -> Swarm:
    """Create the five-agent IPL specialist swarm."""
    model = load_model()
    common = {"model": model}

    host = Agent(
        agent_id="ipl_host",
        name="ipl_host",
        description="Fan-facing host that routes questions and delivers final answers",
        system_prompt=HOST_PROMPT,
        tools=[list_ipl_teams],
        **common,
    )
    stats_guru = Agent(
        agent_id="stats_guru",
        name="stats_guru",
        description="Player and team statistics, standings, comparisons",
        system_prompt=STATS_PROMPT,
        tools=[get_player_stats, compare_players, get_team_profile, get_points_table, list_ipl_teams],
        **common,
    )
    match_wizard = Agent(
        agent_id="match_wizard",
        name="match_wizard",
        description="Head-to-head, venues, fixtures, match predictions",
        system_prompt=MATCH_PROMPT,
        tools=[get_head_to_head, get_venue_analysis, get_upcoming_fixtures, predict_match_edge],
        **common,
    )
    fantasy_coach = Agent(
        agent_id="fantasy_coach",
        name="fantasy_coach",
        description="Fantasy XI, captain picks, player fantasy ratings",
        system_prompt=FANTASY_PROMPT,
        tools=[suggest_fantasy_xi, get_captain_picks, rate_fantasy_pick],
        **common,
    )
    history_buff = Agent(
        agent_id="history_buff",
        name="history_buff",
        description="IPL records, champions, trivia, legendary moments",
        system_prompt=HISTORY_PROMPT,
        tools=[get_ipl_record, get_season_champion, get_title_leaderboard, list_legendary_moments],
        **common,
    )

    return Swarm(
        nodes=[host, stats_guru, match_wizard, fantasy_coach, history_buff],
        entry_point=host,
        max_handoffs=6,
        max_iterations=8,
        execution_timeout=300.0,
        id="ipl_command_center",
    )
