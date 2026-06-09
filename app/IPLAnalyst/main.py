from typing import Any

from bedrock_agentcore.runtime import BedrockAgentCoreApp

from agents.swarm_team import build_ipl_swarm

app = BedrockAgentCoreApp()
log = app.logger


def swarm_factory():
    cache: dict[str, Any] = {}

    def get_or_create_swarm(session_id: str, user_id: str):
        key = f"{session_id}/{user_id}"
        if key not in cache:
            # AgentCore Memory session manager does not support Strands Swarm
            # persistence (create_multi_agent is not implemented). The swarm
            # runs statelessly; short-term context is handled within each turn.
            cache[key] = build_ipl_swarm()
        return cache[key]

    return get_or_create_swarm


get_or_create_swarm = swarm_factory()


def _extract_text(event: dict) -> str | None:
    """Pull streamable text from agent or swarm events."""
    if event.get("type") == "multiagent_node_stream":
        inner = event.get("event", {})
        if "data" in inner and isinstance(inner["data"], str):
            return inner["data"]
        return None
    if "data" in event and isinstance(event["data"], str):
        return event["data"]
    return None


@app.entrypoint
async def invoke(payload, context):
    log.info("Invoking IPL Command Center swarm...")

    session_id = getattr(context, "session_id", "default-session")
    user_id = getattr(context, "user_id", "default-user")
    swarm = get_or_create_swarm(session_id, user_id)
    prompt = payload.get("prompt", "")

    async for event in swarm.stream_async(prompt):
        text = _extract_text(event)
        if text:
            yield text


if __name__ == "__main__":
    app.run()
