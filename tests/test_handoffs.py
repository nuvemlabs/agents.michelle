"""
Test handoff functionality between Michelle, Tim Burton, and Martin Scorsese agents.
"""
import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from agent.pfeiffer import michelle_agent, tim_burton_agent, martin_scorsese_agent


class TestHandoffSystem:
    """Test the handoff system configuration and behavior."""
    
    def test_michelle_handoff_configuration(self):
        """Test that Michelle agent has the correct handoffs configured."""
        assert hasattr(michelle_agent, 'handoffs')
        assert michelle_agent.handoffs is not None
        assert len(michelle_agent.handoffs) == 2
        
        # Check that handoffs include the right agents
        handoff_names = [agent.name for agent in michelle_agent.handoffs]
        assert "Tim Burton" in handoff_names
        assert "Martin Scorsese" in handoff_names
        
    def test_director_agents_are_endpoints(self):
        """Test that director agents don't have further handoffs."""
        # Tim Burton should be an endpoint (no handoffs)
        tim_handoffs = getattr(tim_burton_agent, 'handoffs', None)
        assert tim_handoffs is None or len(tim_handoffs) == 0
        
        # Martin Scorsese should be an endpoint (no handoffs)
        martin_handoffs = getattr(martin_scorsese_agent, 'handoffs', None)
        assert martin_handoffs is None or len(martin_handoffs) == 0
        
    def test_handoff_agents_have_unique_names(self):
        """Test that all agents in the handoff system have unique names."""
        all_agents = [michelle_agent, tim_burton_agent, martin_scorsese_agent]
        names = [agent.name for agent in all_agents]
        assert len(names) == len(set(names))  # All names should be unique
        
    def test_handoff_agents_use_same_model(self):
        """Test that all agents use the same model for consistency."""
        all_agents = [michelle_agent, tim_burton_agent, martin_scorsese_agent]
        models = [agent.model for agent in all_agents]
        assert len(set(models)) == 1  # All should use the same model


class TestHandoffTriggers:
    """Test the content that should trigger handoffs."""
    
    def test_batman_keywords_in_instructions(self):
        """Test that Michelle's instructions mention Batman-related keywords."""
        instructions = michelle_agent.instructions.lower()
        batman_keywords = ["batman returns", "catwoman", "tim burton"]
        
        for keyword in batman_keywords:
            assert keyword in instructions, f"'{keyword}' should be in Michelle's instructions for Tim Burton handoff"
            
    def test_age_of_innocence_keywords_in_instructions(self):
        """Test that Michelle's instructions mention Age of Innocence keywords."""
        instructions = michelle_agent.instructions.lower()
        innocence_keywords = ["age of innocence", "martin scorsese"]
        
        for keyword in innocence_keywords:
            assert keyword in instructions, f"'{keyword}' should be in Michelle's instructions for Martin Scorsese handoff"
            
    def test_tim_burton_specialization(self):
        """Test that Tim Burton's instructions focus on his collaboration with Michelle."""
        instructions = tim_burton_agent.instructions.lower()
        
        # Should mention their collaboration
        assert "batman returns" in instructions
        assert "catwoman" in instructions
        assert "michelle pfeiffer" in instructions
        
        # Should mention his style
        tim_style_keywords = ["gothic", "visual", "character"]
        for keyword in tim_style_keywords:
            assert keyword in instructions
            
    def test_martin_scorsese_specialization(self):
        """Test that Martin Scorsese's instructions focus on his collaboration with Michelle."""
        instructions = martin_scorsese_agent.instructions.lower()
        
        # Should mention their collaboration
        assert "age of innocence" in instructions
        assert "ellen olenska" in instructions
        assert "michelle pfeiffer" in instructions
        
        # Should mention his approach
        scorsese_keywords = ["film", "cinema", "character", "method"]
        found_keywords = [keyword for keyword in scorsese_keywords if keyword in instructions]
        assert len(found_keywords) >= 2, f"Should mention at least 2 of {scorsese_keywords}"


@pytest.mark.integration
class TestHandoffBehavior:
    """Integration tests for actual handoff behavior (requires API key)."""
    
    @pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="Requires OpenAI API key")
    def test_batman_returns_handoff(self):
        """Test that Batman Returns questions trigger handoff to Tim Burton."""
        from agents import Runner
        
        # This should trigger a handoff to Tim Burton
        result = Runner.run_sync(michelle_agent, "Tell me about working with Tim Burton on Batman Returns.")
        
        assert result.final_output
        # The result should come from Tim Burton, not Michelle
        # We can check if Tim Burton-specific content appears in the response
        response_lower = result.final_output.lower()
        
        # Should contain Tim Burton's perspective, not just Michelle's
        tim_indicators = ["gothic", "visual", "batman returns", "catwoman"]
        found_indicators = [indicator for indicator in tim_indicators if indicator in response_lower]
        assert len(found_indicators) >= 1, f"Expected Tim Burton's perspective, got: {result.final_output[:200]}..."
        
    @pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="Requires OpenAI API key") 
    def test_age_of_innocence_handoff(self):
        """Test that Age of Innocence questions trigger handoff to Martin Scorsese."""
        from agents import Runner
        
        # This should trigger a handoff to Martin Scorsese
        result = Runner.run_sync(michelle_agent, "Tell me about The Age of Innocence and working with Martin Scorsese.")
        
        assert result.final_output
        response_lower = result.final_output.lower()
        
        # Should contain Martin Scorsese's perspective
        scorsese_indicators = ["age of innocence", "scorsese", "film", "cinema", "edith wharton"]
        found_indicators = [indicator for indicator in scorsese_indicators if indicator in response_lower]
        assert len(found_indicators) >= 1, f"Expected Scorsese's perspective, got: {result.final_output[:200]}..."
        
    @pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="Requires OpenAI API key")
    def test_general_question_stays_with_michelle(self):
        """Test that general acting questions stay with Michelle."""
        from agents import Runner
        
        # This should stay with Michelle
        result = Runner.run_sync(michelle_agent, "What's your favorite acting technique?")
        
        assert result.final_output
        response_lower = result.final_output.lower()
        
        # Should be from Michelle's perspective, not redirected
        # General acting advice should come from Michelle herself
        michelle_indicators = ["acting", "technique", "performance", "character", "experience"]
        found_indicators = [indicator for indicator in michelle_indicators if indicator in response_lower]
        assert len(found_indicators) >= 1, f"Expected Michelle's acting advice, got: {result.final_output[:200]}..."


class TestHandoffSystemIntegrity:
    """Test the overall integrity and consistency of the handoff system."""
    
    def test_all_agents_have_instructions(self):
        """Test that all agents have non-empty instructions."""
        agents = [michelle_agent, tim_burton_agent, martin_scorsese_agent]
        
        for agent in agents:
            assert hasattr(agent, 'instructions')
            assert agent.instructions
            assert len(agent.instructions.strip()) > 50  # Should be substantial instructions
            
    def test_instructions_are_persona_appropriate(self):
        """Test that each agent's instructions match their persona."""
        # Michelle should sound like an actress
        michelle_instructions = michelle_agent.instructions.lower()
        assert any(word in michelle_instructions for word in ["actress", "acting", "performance", "character"])
        
        # Tim Burton should sound like a director
        tim_instructions = tim_burton_agent.instructions.lower()
        assert any(word in tim_instructions for word in ["director", "film", "visual", "gothic"])
        
        # Martin Scorsese should sound like a filmmaker
        martin_instructions = martin_scorsese_agent.instructions.lower()
        assert any(word in martin_instructions for word in ["director", "filmmaker", "cinema", "film"])
        
    def test_cross_references_exist(self):
        """Test that agents reference each other appropriately."""
        # Michelle should reference both directors
        michelle_instructions = michelle_agent.instructions.lower()
        assert "tim burton" in michelle_instructions
        assert "martin scorsese" in michelle_instructions
        
        # Directors should reference Michelle
        tim_instructions = tim_burton_agent.instructions.lower()
        martin_instructions = martin_scorsese_agent.instructions.lower()
        
        assert "michelle pfeiffer" in tim_instructions
        assert "michelle pfeiffer" in martin_instructions


class TestHandoffErrorCases:
    """Test error handling and edge cases in the handoff system."""
    
    def test_agents_exist(self):
        """Test that all required agents are properly instantiated."""
        agents = [michelle_agent, tim_burton_agent, martin_scorsese_agent]
        
        for agent in agents:
            assert agent is not None
            assert hasattr(agent, 'name')
            assert hasattr(agent, 'instructions')
            assert hasattr(agent, 'model')
            
    def test_model_consistency(self):
        """Test that all agents use a valid model."""
        agents = [michelle_agent, tim_burton_agent, martin_scorsese_agent]
        
        for agent in agents:
            assert agent.model
            assert isinstance(agent.model, str)
            assert "gpt" in agent.model.lower()  # Should be a GPT model


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"]) 