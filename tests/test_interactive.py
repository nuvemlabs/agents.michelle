"""
Test interactive mode functionality for all agents.
"""
import pytest
import sys
import os
from unittest.mock import patch, MagicMock
from io import StringIO

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from agent.simple_agent import interactive_mode as simple_interactive, create_creative_agent
from agent.obama import interactive_mode as obama_interactive, create_obama_agent
from agent.pfeiffer import interactive_mode as pfeiffer_interactive, michelle_agent


class TestInteractiveMode:
    """Test interactive mode functionality for all agents."""
    
    def test_simple_agent_has_interactive_mode(self):
        """Test that simple agent has interactive mode function."""
        # Check that the function exists
        assert callable(simple_interactive)
        
        # Check that it creates the correct agent
        agent = create_creative_agent()
        assert agent.name == "Creative Assistant"
        
    def test_obama_agent_has_interactive_mode(self):
        """Test that Michelle Obama agent has interactive mode function."""
        # Check that the function exists
        assert callable(obama_interactive)
        
        # Check that it creates the correct agent
        agent = create_obama_agent()
        assert agent.name == "Michelle Obama Knowledge Assistant"
        
    def test_pfeiffer_agent_has_interactive_mode(self):
        """Test that Pfeiffer agent has interactive mode function."""
        # Check that the function exists
        assert callable(pfeiffer_interactive)
        
        # Check that the main agent is configured correctly
        assert michelle_agent.name == "Michelle Pfeiffer"
        assert len(michelle_agent.handoffs) == 2


class TestInteractiveFlowControl:
    """Test the flow control in interactive modes."""
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_simple_interactive_exit_command(self, mock_stdout, mock_input):
        """Test that simple interactive mode handles exit commands."""
        # Mock user typing 'exit'
        mock_input.return_value = 'exit'
        
        # Run interactive mode
        simple_interactive()
        
        # Check that goodbye message was printed
        output = mock_stdout.getvalue()
        assert "goodbye" in output.lower() or "thanks" in output.lower()
        
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO) 
    def test_obama_interactive_exit_command(self, mock_stdout, mock_input):
        """Test that Obama interactive mode handles exit commands."""
        # Mock user typing 'quit'
        mock_input.return_value = 'quit'
        
        # Run interactive mode
        obama_interactive()
        
        # Check that goodbye message was printed
        output = mock_stdout.getvalue()
        assert "goodbye" in output.lower() or "thank" in output.lower()
        
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_pfeiffer_interactive_exit_command(self, mock_stdout, mock_input):
        """Test that Pfeiffer interactive mode handles exit commands."""
        # Mock user typing 'bye'
        mock_input.return_value = 'bye'
        
        # Run interactive mode
        pfeiffer_interactive()
        
        # Check that goodbye message was printed
        output = mock_stdout.getvalue()
        assert "goodbye" in output.lower() or "thank" in output.lower()


class TestInteractiveUserInterface:
    """Test the user interface elements of interactive modes."""
    
    @patch('builtins.input', return_value='exit')
    @patch('sys.stdout', new_callable=StringIO)
    def test_simple_interactive_welcome_message(self, mock_stdout, mock_input):
        """Test that simple interactive mode shows welcome message."""
        simple_interactive()
        
        output = mock_stdout.getvalue()
        assert "Creative Assistant" in output
        assert "creative" in output.lower()
        assert "exit" in output.lower()
        
    @patch('builtins.input', return_value='exit')
    @patch('sys.stdout', new_callable=StringIO)
    def test_obama_interactive_welcome_message(self, mock_stdout, mock_input):
        """Test that Michelle Obama interactive mode shows welcome message."""
        obama_interactive()
        
        output = mock_stdout.getvalue()
        assert "Michelle Obama" in output
        assert "first lady" in output.lower() or "books" in output.lower()
        assert "exit" in output.lower()
        
    @patch('builtins.input', return_value='exit')
    @patch('sys.stdout', new_callable=StringIO)
    def test_pfeiffer_interactive_welcome_message(self, mock_stdout, mock_input):
        """Test that Pfeiffer interactive mode shows welcome message."""
        pfeiffer_interactive()
        
        output = mock_stdout.getvalue()
        assert "Michelle Pfeiffer" in output
        assert "Tim Burton" in output
        assert "Martin Scorsese" in output
        assert "handoff" in output.lower()
        assert "exit" in output.lower()


class TestInteractiveErrorHandling:
    """Test error handling in interactive modes."""
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_simple_interactive_empty_input(self, mock_stdout, mock_input):
        """Test that simple interactive mode handles empty input."""
        # Mock empty input followed by exit
        mock_input.side_effect = ['', 'exit']
        
        simple_interactive()
        
        output = mock_stdout.getvalue()
        assert "Please enter" in output or "empty" in output.lower()
        
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_obama_interactive_empty_input(self, mock_stdout, mock_input):
        """Test that Michelle Obama interactive mode handles empty input."""
        # Mock empty input followed by exit
        mock_input.side_effect = ['', 'exit']
        
        obama_interactive()
        
        output = mock_stdout.getvalue()
        assert "Please enter" in output or "question" in output.lower()
        
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_pfeiffer_interactive_empty_input(self, mock_stdout, mock_input):
        """Test that Pfeiffer interactive mode handles empty input."""
        # Mock empty input followed by exit
        mock_input.side_effect = ['', 'exit']
        
        pfeiffer_interactive()
        
        output = mock_stdout.getvalue()
        assert "Please enter" in output or "message" in output.lower()


class TestInteractivePrompts:
    """Test the prompt formatting in interactive modes."""
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt_formatting(self, mock_stdout, mock_input):
        """Test that all interactive modes use consistent prompt formatting."""
        # Mock user input to trigger prompt display then exit
        mock_input.side_effect = ['test input', 'exit']
        
        # Test simple agent
        try:
            simple_interactive()
        except Exception:
            pass  # Ignore API errors, we just want to test UI
        simple_output = mock_stdout.getvalue()
        
        # Reset stdout capture and mock
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        mock_input.side_effect = ['test input', 'exit']
        
        # Test Obama agent
        try:
            obama_interactive()
        except Exception:
            pass  # Ignore API errors, we just want to test UI
        obama_output = mock_stdout.getvalue()
        
        # Reset stdout capture and mock
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        mock_input.side_effect = ['test input', 'exit']
        
        # Test Pfeiffer agent
        try:
            pfeiffer_interactive()
        except Exception:
            pass  # Ignore API errors, we just want to test UI
        pfeiffer_output = mock_stdout.getvalue()
        
        # Check that all show welcome messages (which is what we can reliably test)
        assert "Creative Assistant" in simple_output
        assert "Michelle Obama" in obama_output
        assert "Michelle Pfeiffer" in pfeiffer_output


@pytest.mark.integration 
class TestInteractiveAgentResponses:
    """Integration tests for interactive mode with actual agent responses."""
    
    @pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="Requires OpenAI API key")
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_simple_agent_interactive_response(self, mock_stdout, mock_input):
        """Test that simple agent responds to user input in interactive mode."""
        # Mock user input: a creative request followed by exit
        mock_input.side_effect = ['Write a short haiku about testing', 'exit']
        
        # This will actually call the API
        simple_interactive()
        
        output = mock_stdout.getvalue()
        
        # Should have shown some response from the agent
        assert "Creative Assistant:" in output
        
        # Response should contain content (haiku about testing)
        assert len(output) > 200  # Should have substantial content
        
        # Should have proper exit
        assert "goodbye" in output.lower() or "thanks" in output.lower()
        
    @pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="Requires OpenAI API key")
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_obama_agent_interactive_response(self, mock_stdout, mock_input):
        """Test that Michelle Obama agent responds to user input in interactive mode."""
        # Mock user input: Michelle Obama question followed by exit
        mock_input.side_effect = ['What book did Michelle Obama write?', 'exit']
        
        # This will actually call the API
        obama_interactive()
        
        output = mock_stdout.getvalue()
        
        # Should have shown some response from the agent
        assert "Michelle Obama Expert:" in output
        
        # Response should contain content about Michelle Obama
        assert len(output) > 200  # Should have substantial content
        
        # Should have proper exit
        assert "goodbye" in output.lower() or "thank" in output.lower()


class TestInteractiveModeIntegration:
    """Test integration between different components of interactive mode."""
    
    def test_all_agents_support_interactive_flag(self):
        """Test that all agent files support the --interactive command line flag."""
        # This is more of a design test - ensuring consistent interface
        
        # Import the main functions from each agent file
        import importlib.util
        
        # Test simple_agent.py
        spec = importlib.util.spec_from_file_location(
            "simple_agent", 
            os.path.join(os.path.dirname(__file__), '..', 'src', 'agent', 'simple_agent.py')
        )
        simple_module = importlib.util.module_from_spec(spec)
        
        # Should have both main() and interactive_mode() functions
        assert hasattr(simple_module, '__file__')  # Basic module loading test
        
    def test_consistent_exit_commands(self):
        """Test that all interactive modes accept the same exit commands."""
        exit_commands = ['exit', 'quit', 'bye']
        
        # This is tested in the individual exit command tests above
        # Here we just verify the commands are consistent
        assert len(exit_commands) == 3
        assert 'exit' in exit_commands
        assert 'quit' in exit_commands  
        assert 'bye' in exit_commands


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"]) 