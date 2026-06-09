from strands.models.bedrock import BedrockModel


def load_model() -> BedrockModel:
    return BedrockModel(model_id="global.anthropic.claude-sonnet-4-5-20250929-v1:0")
