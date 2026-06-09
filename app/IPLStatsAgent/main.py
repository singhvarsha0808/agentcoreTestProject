from strands import Agent, tool
from bedrock_agentcore.runtime import BedrockAgentCoreApp

from ipl_data.catalogue import PLAYERS, POINTS_TABLE_2024, TEAMS, normalize_player, normalize_team
from memory.session import get_memory_session_manager
from model.load import load_model

app = BedrockAgentCoreApp()
log = app.logger

SYSTEM_PROMPT = """You are IPL Stats Agent — a dedicated statistics specialist.
Answer with precise numbers from your tools. Cover players, teams, standings, and comparisons.
You do not do fantasy advice or historical storytelling — stay in the stats lane."""


@tool
def get_player_stats(player_name: str) -> str:
    """Get IPL 2024 stats for a player."""
    key = normalize_player(player_name)
    if not key:
        return f"Player '{player_name}' not found."
    p = PLAYERS[key]
    parts = [f"{p.name} ({p.team}) — {p.role}", f"Matches: {p.matches}"]
    if p.runs:
        parts.append(f"Runs: {p.runs} @ SR {p.strike_rate}")
    if p.wickets:
        parts.append(f"Wickets: {p.wickets} @ Econ {p.economy}")
    return " | ".join(parts)


@tool
def get_points_table() -> str:
    """Return IPL 2024 league standings."""
    lines = ["IPL 2024 Points Table:"]
    for row in POINTS_TABLE_2024:
        lines.append(
            f"{row['rank']}. {row['team']} — {row['points']} pts "
            f"({row['won']}W/{row['lost']}L, NRR {row['nrr']:+.3f})"
        )
    return "\n".join(lines)


@tool
def get_team_profile(team_name: str) -> str:
    """Get team profile by name or abbreviation."""
    abbr = normalize_team(team_name)
    if not abbr:
        return f"Team '{team_name}' not found."
    info = TEAMS[abbr]
    return (
        f"{info['full_name']} ({abbr}) | Captain: {info['captain']} | "
        f"Titles: {info['titles']} | {info['strength']}"
    )


tools = [get_player_stats, get_points_table, get_team_profile]


def agent_factory():
    cache = {}

    def get_or_create_agent(session_id, user_id):
        key = f"{session_id}/{user_id}"
        if key not in cache:
            cache[key] = Agent(
                model=load_model(),
                session_manager=get_memory_session_manager(session_id, user_id),
                system_prompt=SYSTEM_PROMPT,
                tools=tools,
            )
        return cache[key]

    return get_or_create_agent


get_or_create_agent = agent_factory()


@app.entrypoint
async def invoke(payload, context):
    log.info("Invoking IPL Stats Agent...")
    session_id = getattr(context, "session_id", "default-session")
    user_id = getattr(context, "user_id", "default-user")
    agent = get_or_create_agent(session_id, user_id)

    async for event in agent.stream_async(payload.get("prompt")):
        if "data" in event and isinstance(event["data"], str):
            yield event["data"]


if __name__ == "__main__":
    app.run()
