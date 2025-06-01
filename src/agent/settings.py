"""Settings for agents.michelle."""

import os
from typing import Dict, Any, Optional

import yaml
from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AgentConfig(BaseModel):
    """Configuration for individual agents."""
    name: str
    emoji: str
    instructions: str


class CreativeConfig(BaseModel):
    """Configuration for creative tasks."""
    enable_poetry: bool = True
    enable_storytelling: bool = True
    default_task: str = "Write a roses are red, violets are blue, poem."


class Settings(BaseSettings):
    """Application settings loaded from environment and config files."""

    # API Keys
    openai_api_key: str = Field(..., alias="OPENAI_API_KEY")
    openai_org_id: Optional[str] = Field(None, alias="OPENAI_ORG_ID")

    # Environment
    env: str = Field("development", alias="ENV")
    log_level: str = Field("INFO", alias="LOG_LEVEL")

    # Model settings
    model_name: str = "gpt-4o-2024-11-20"
    model_temperature: float = 0.7
    model_max_tokens: int = 2000

    # Agent settings
    agent_verbose: bool = True
    agent_default_instructions: str = "You are a helpful assistant."

    # Creative settings
    creative_config: CreativeConfig = CreativeConfig()

    # Agent configurations
    agent_configs: Dict[str, AgentConfig] = {}

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_file_encoding="utf-8",
    )

    @classmethod
    def load_from_yaml(cls, config_path: str = "config/settings.yaml"):
        """Load settings from YAML file and environment."""
        settings_dict = {}

        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                config = yaml.safe_load(f)

            # Flatten the nested config
            if "model" in config:
                settings_dict.update(
                    {
                        "model_name": config["model"].get("name", "gpt-4o-2024-11-20"),
                        "model_temperature": config["model"].get("temperature", 0.7),
                        "model_max_tokens": config["model"].get("max_tokens", 2000),
                    }
                )

            if "agent" in config:
                settings_dict.update(
                    {
                        "agent_verbose": config["agent"].get("verbose", True),
                        "agent_default_instructions": config["agent"].get(
                            "default_instructions", "You are a helpful assistant."
                        ),
                    }
                )

            if "creative" in config:
                settings_dict["creative_config"] = CreativeConfig(**config["creative"])

            if "agents" in config:
                agent_configs = {}
                for key, agent_config in config["agents"].items():
                    agent_configs[key] = AgentConfig(**agent_config)
                settings_dict["agent_configs"] = agent_configs

        return cls(**settings_dict)

    def get_agent_config(self, agent_type: str) -> AgentConfig:
        """Get configuration for a specific agent type."""
        return self.agent_configs.get(
            agent_type,
            AgentConfig(
                name="Default Agent",
                emoji="🤖",
                instructions=self.agent_default_instructions
            ),
        )


# Global settings instance
settings = Settings.load_from_yaml() 