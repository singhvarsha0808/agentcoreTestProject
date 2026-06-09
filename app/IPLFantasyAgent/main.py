from strands import Agent, tool
from bedrock_agentcore.runtime import BedrockAgentCoreApp

from ipl_data.catalogue import FANTASY_TIERS, PLAYERS, normalize_player, normalize_team
from memory.session import get_memory_session_manager
from model.load import load_model

app = BedrockAgentCoreApp()
log = app.logger

SYSTEM_PROMPT = """You are IPL Fantasy Coach — Dream11 and fantasy league specialist.
Build XIs, pick captains, and rate players. Explain risk vs reward clearly.
Use tools for data-backed picks. Be opinionated but honest about differentials."""


@tool
def suggest_fantasy_xi(match_context: str = "balanced", budget_tier: str = "premium") -> str:
    """Suggest a Dream11-style XI. budget_tier: premium, value, or differential."""
    tier = budget_tier.strip().lower()
    if tier not in FANTASY_TIERS:
        tier = "premium"
    picks = FANTASY_TIERS[tier][:7]
    return (
        f"Fantasy XI ({tier}) for '{match_context}':\n"
        f"Core: {', '.join(picks[:4])}\n"
        f"Bowlers: {', '.join(picks[4:])}\n"
        f"C/VC: {picks[0]} / {picks[1]}"
    )


@tool
def get_captain_picks(teams_playing: str) -> str:
    """Captain picks for a fixture (e.g. 'RCB vs CSK')."""
    captains = {
        "RCB": "Virat Kohli", "CSK": "Ruturaj Gaikwad", "MI": "Rohit Sharma",
        "KKR": "Sunil Narine", "SRH": "Travis Head", "RR": "Sanju Samson",
        "GT": "Shubman Gill", "DC": "Rishabh Pant", "PBKS": "Shreyas Iyer", "LSG": "KL Rahul",
    }
    teams = [normalize_team(t.strip()) for t in teams_playing.replace("vs", " ").split() if t.strip()]
    teams = [t for t in teams if t]
    if not teams:
        return "Specify teams, e.g. 'SRH vs KKR'."
    return f"Captain: {captains.get(teams[0])} | Vice: {captains.get(teams[-1])}"


@tool
def rate_fantasy_pick(player_name: str) -> str:
    """Rate a player's fantasy value from 2024 form."""
    key = normalize_player(player_name)
    if not key:
        return f"Player '{player_name}' not found."
    p = PLAYERS[key]
    score = 5 + (2 if p.strike_rate >= 170 else 0) + (2 if p.wickets >= 15 else 0) + (1 if p.runs >= 500 else 0)
    tier = "Must-pick" if score >= 8 else "Strong pick" if score >= 6 else "Situational"
    return f"{p.name}: {tier} ({score}/10) — {p.role} for {p.team}"


tools = [suggest_fantasy_xi, get_captain_picks, rate_fantasy_pick]


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
    log.info("Invoking IPL Fantasy Agent...")
    session_id = getattr(context, "session_id", "default-session")
    user_id = getattr(context, "user_id", "default-user")
    agent = get_or_create_agent(session_id, user_id)

    async for event in agent.stream_async(payload.get("prompt")):
        if "data" in event and isinstance(event["data"], str):
            yield event["data"]


if __name__ == "__main__":
    app.run()
