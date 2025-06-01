"""
Test individual agent functionality and configuration.
"""
import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from agent.settings import settings, AgentConfig
from agent.simple_agent import create_creative_agent
from agent.obama import create_obama_agent
from agent.pfeiffer import michelle_agent, tim_burton_agent, martin_scorsese_agent


class TestSettings:
    """Test the configuration system."""
    
    def test_settings_loading(self):
        """Test that settings load properly from YAML."""
        assert settings.model_name == "gpt-4o-2024-11-20"
        assert settings.model_temperature == 0.7
        assert settings.model_max_tokens == 2000
        
    def test_agent_configs_loaded(self):
        """Test that agent configurations are loaded."""
        assert "michelle" in settings.agent_configs
        assert "tim_burton" in settings.agent_configs
        assert "martin_scorsese" in settings.agent_configs
        
    def test_agent_config_structure(self):
        """Test that agent configs have required fields."""
        michelle_config = settings.get_agent_config("michelle")
        assert isinstance(michelle_config, AgentConfig)
        assert michelle_config.name == "Michelle Pfeiffer"
        assert michelle_config.emoji == "🎭"
        assert "actress" in michelle_config.instructions.lower()
        
    def test_agent_config_emojis(self):
        """Test that all agents have emojis."""
        agents = ["michelle", "tim_burton", "martin_scorsese"]
        for agent_key in agents:
            config = settings.get_agent_config(agent_key)
            assert config.emoji  # Should not be empty
            assert len(config.emoji) > 0
            
    def test_default_agent_config(self):
        """Test fallback for unknown agent type."""
        unknown_config = settings.get_agent_config("unknown_agent")
        assert unknown_config.name == "Default Agent"
        assert unknown_config.emoji == "🤖"


class TestAgentCreation:
    """Test agent creation and basic properties."""
    
    def test_creative_agent_creation(self):
        """Test creating the creative assistant agent."""
        agent = create_creative_agent()
        assert agent.name == "Creative Assistant"
        assert agent.model == settings.model_name
        
    def test_obama_agent_creation(self):
        """Test creating the Michelle Obama knowledge agent."""
        agent = create_obama_agent()
        assert agent.name == "Michelle Obama Knowledge Assistant"
        assert agent.model == settings.model_name
        assert "michelle obama" in agent.instructions.lower()
        
    def test_michelle_agent_creation(self):
        """Test creating the Michelle Pfeiffer agent."""
        assert michelle_agent.name == "Michelle Pfeiffer"
        assert michelle_agent.model == settings.model_name
        assert len(michelle_agent.handoffs) == 2  # Tim Burton + Martin Scorsese
        
    def test_tim_burton_agent_creation(self):
        """Test creating the Tim Burton agent."""
        assert tim_burton_agent.name == "Tim Burton"
        assert tim_burton_agent.model == settings.model_name
        assert "batman returns" in tim_burton_agent.instructions.lower()
        
    def test_martin_scorsese_agent_creation(self):
        """Test creating the Martin Scorsese agent."""
        assert martin_scorsese_agent.name == "Martin Scorsese"
        assert martin_scorsese_agent.model == settings.model_name
        assert "age of innocence" in martin_scorsese_agent.instructions.lower()


class TestAgentInstructions:
    """Test agent instructions contain expected content."""
    
    def test_michelle_instructions(self):
        """Test Michelle's instructions mention key collaborators."""
        instructions = michelle_agent.instructions.lower()
        assert "michelle pfeiffer" in instructions
        assert "actress" in instructions
        assert "batman returns" in instructions
        assert "age of innocence" in instructions
        assert "handoff" in instructions
        
    def test_tim_burton_instructions(self):
        """Test Tim Burton's instructions mention key films and style."""
        instructions = tim_burton_agent.instructions.lower()
        assert "tim burton" in instructions
        assert "batman returns" in instructions
        assert "catwoman" in instructions
        assert "gothic" in instructions
        assert "michelle pfeiffer" in instructions
        
    def test_martin_scorsese_instructions(self):
        """Test Martin Scorsese's instructions mention key films and approach."""
        instructions = martin_scorsese_agent.instructions.lower()
        assert "martin scorsese" in instructions
        assert "age of innocence" in instructions
        assert "ellen olenska" in instructions
        assert "michelle pfeiffer" in instructions
        assert "film" in instructions or "cinema" in instructions


class TestHandoffConfiguration:
    """Test handoff system configuration."""
    
    def test_michelle_has_handoffs(self):
        """Test that Michelle agent has handoffs configured."""
        assert hasattr(michelle_agent, 'handoffs')
        assert michelle_agent.handoffs is not None
        assert len(michelle_agent.handoffs) == 2
        
    def test_handoff_agents_are_correct(self):
        """Test that handoff agents are Tim Burton and Martin Scorsese."""
        handoff_names = [agent.name for agent in michelle_agent.handoffs]
        assert "Tim Burton" in handoff_names
        assert "Martin Scorsese" in handoff_names
        
    def test_director_agents_no_handoffs(self):
        """Test that director agents don't have handoffs (they're endpoints)."""
        # Tim Burton shouldn't have handoffs
        assert not hasattr(tim_burton_agent, 'handoffs') or not tim_burton_agent.handoffs
        # Martin Scorsese shouldn't have handoffs  
        assert not hasattr(martin_scorsese_agent, 'handoffs') or not martin_scorsese_agent.handoffs


@pytest.mark.integration
class TestAgentResponses:
    """Integration tests that actually call the agents (requires API key)."""
    
    @pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="Requires OpenAI API key")
    def test_creative_agent_response(self):
        """Test that creative agent can generate a response."""
        from agents import Runner
        
        agent = create_creative_agent()
        result = Runner.run_sync(agent, "Write a short haiku about testing.")
        
        assert result.final_output
        assert len(result.final_output) > 10  # Should be more than just a few characters
        
    @pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="Requires OpenAI API key")
    def test_obama_agent_response(self):
        """Test that Michelle Obama agent can answer questions."""
        from agents import Runner
        
        agent = create_obama_agent()
        result = Runner.run_sync(agent, "What book did Michelle Obama write?")
        
        assert result.final_output
        assert "becoming" in result.final_output.lower() or "light we carry" in result.final_output.lower()


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"]) 