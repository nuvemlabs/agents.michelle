#!/usr/bin/env python3
"""
Test runner for the Michelle Pfeiffer agent handoff system.
This script tests the core functionality without requiring API calls.
"""
import sys
import os

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from agent.settings import settings
from agent.pfeiffer import michelle_agent, tim_burton_agent, martin_scorsese_agent
from agent.simple_agent import create_creative_agent
from agent.obama import create_obama_agent


def test_configuration():
    """Test that configuration is loaded correctly."""
    print("🔧 Testing Configuration...")
    
    # Test settings loading
    assert settings.model_name == "gpt-4o-2024-11-20"
    assert settings.model_temperature == 0.7
    print("  ✓ Settings loaded correctly")
    
    # Test agent configurations
    michelle_config = settings.get_agent_config("michelle")
    tim_config = settings.get_agent_config("tim_burton")
    martin_config = settings.get_agent_config("martin_scorsese")
    
    assert michelle_config.name == "Michelle Pfeiffer"
    assert michelle_config.emoji == "🎭"
    assert tim_config.name == "Tim Burton"
    assert tim_config.emoji == "🎨"
    assert martin_config.name == "Martin Scorsese"
    assert martin_config.emoji == "🎬"
    print("  ✓ Agent configurations loaded with emojis")


def test_agent_creation():
    """Test that all agents are created correctly."""
    print("🤖 Testing Agent Creation...")
    
    # Test Michelle Pfeiffer agent
    assert michelle_agent.name == "Michelle Pfeiffer"
    assert michelle_agent.model == settings.model_name
    assert len(michelle_agent.handoffs) == 2
    print("  ✓ Michelle Pfeiffer agent created with handoffs")
    
    # Test Tim Burton agent
    assert tim_burton_agent.name == "Tim Burton"
    assert tim_burton_agent.model == settings.model_name
    print("  ✓ Tim Burton agent created")
    
    # Test Martin Scorsese agent
    assert martin_scorsese_agent.name == "Martin Scorsese"
    assert martin_scorsese_agent.model == settings.model_name
    print("  ✓ Martin Scorsese agent created")
    
    # Test other agents
    creative_agent = create_creative_agent()
    assert creative_agent.name == "Creative Assistant"
    print("  ✓ Creative Assistant agent created")
    
    obama_agent = create_obama_agent()
    assert obama_agent.name == "Michelle Obama Knowledge Assistant"
    print("  ✓ Michelle Obama Knowledge Assistant agent created")


def test_handoff_configuration():
    """Test the handoff system configuration."""
    print("🔗 Testing Handoff Configuration...")
    
    # Test that Michelle has handoffs to both directors
    handoff_names = [agent.name for agent in michelle_agent.handoffs]
    assert "Tim Burton" in handoff_names
    assert "Martin Scorsese" in handoff_names
    print("  ✓ Michelle has handoffs to both directors")
    
    # Test that directors don't have handoffs (they're endpoints)
    tim_handoffs = getattr(tim_burton_agent, 'handoffs', None)
    martin_handoffs = getattr(martin_scorsese_agent, 'handoffs', None)
    assert tim_handoffs is None or len(tim_handoffs) == 0
    assert martin_handoffs is None or len(martin_handoffs) == 0
    print("  ✓ Directors are endpoints (no further handoffs)")


def test_agent_instructions():
    """Test that agent instructions contain expected content."""
    print("📝 Testing Agent Instructions...")
    
    # Test Michelle's instructions
    michelle_instructions = michelle_agent.instructions.lower()
    assert "michelle pfeiffer" in michelle_instructions
    assert "actress" in michelle_instructions
    assert "batman returns" in michelle_instructions
    assert "age of innocence" in michelle_instructions
    assert "handoff" in michelle_instructions
    print("  ✓ Michelle's instructions mention key films and handoffs")
    
    # Test Tim Burton's instructions
    tim_instructions = tim_burton_agent.instructions.lower()
    assert "tim burton" in tim_instructions
    assert "batman returns" in tim_instructions
    assert "catwoman" in tim_instructions
    assert "michelle pfeiffer" in tim_instructions
    print("  ✓ Tim Burton's instructions mention collaboration with Michelle")
    
    # Test Martin Scorsese's instructions
    martin_instructions = martin_scorsese_agent.instructions.lower()
    assert "martin scorsese" in martin_instructions
    assert "age of innocence" in martin_instructions
    assert "ellen olenska" in martin_instructions
    assert "michelle pfeiffer" in martin_instructions
    print("  ✓ Martin Scorsese's instructions mention collaboration with Michelle")


def test_interactive_mode_availability():
    """Test that all agents have interactive mode capability."""
    print("💬 Testing Interactive Mode Availability...")
    
    # Import interactive mode functions
    from agent.simple_agent import interactive_mode as simple_interactive
    from agent.obama import interactive_mode as obama_interactive
    from agent.pfeiffer import interactive_mode as pfeiffer_interactive
    
    # Test that functions exist
    assert callable(simple_interactive)
    assert callable(obama_interactive)
    assert callable(pfeiffer_interactive)
    print("  ✓ All agents have interactive mode functions")


def test_model_consistency():
    """Test that all agents use the same model."""
    print("🎯 Testing Model Consistency...")
    
    all_agents = [michelle_agent, tim_burton_agent, martin_scorsese_agent]
    models = [agent.model for agent in all_agents]
    
    # All should use the same model
    assert len(set(models)) == 1
    assert models[0] == settings.model_name
    print(f"  ✓ All agents use {settings.model_name}")


def run_all_tests():
    """Run all tests and provide a summary."""
    print("🎭 Michelle Pfeiffer Agent System - Test Suite")
    print("=" * 50)
    
    tests = [
        test_configuration,
        test_agent_creation,
        test_handoff_configuration,
        test_agent_instructions,
        test_interactive_mode_availability,
        test_model_consistency,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"  ❌ {test.__name__} failed: {str(e)}")
            failed += 1
    
    print("=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! The handoff system is working correctly.")
        print("\n🚀 Try the interactive mode:")
        print("   make interactive")
        print("   python src/agent/pfeiffer.py --interactive")
    else:
        print("❌ Some tests failed. Please check the configuration.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code) 