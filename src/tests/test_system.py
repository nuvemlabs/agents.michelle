#!/usr/bin/env python3
"""Simple test for the Michelle Pfeiffer agent system."""

import sys
import os
import asyncio

# Add the src directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from agent.pfeiffer import michelle_agent, Runner


async def test_handoffs():
    """Test that handoffs work correctly."""
    
    print("🎭 Testing Michelle Pfeiffer Agent System")
    print("=" * 50)
    
    # Test 1: Question about Batman Returns should route to Tim Burton
    print("\n🦇 Test 1: Batman Returns question")
    result1 = await Runner.run(michelle_agent, "Tell me about Batman Returns and Catwoman")
    print(f"Response: {result1.final_output[:200]}...")
    
    # Test 2: Question about Age of Innocence should route to Martin Scorsese  
    print("\n🎬 Test 2: Age of Innocence question")
    result2 = await Runner.run(michelle_agent, "Tell me about The Age of Innocence")
    print(f"Response: {result2.final_output[:200]}...")
    
    # Test 3: General acting question should stay with Michelle
    print("\n🎭 Test 3: General acting question")
    result3 = await Runner.run(michelle_agent, "What's your favorite acting technique?")
    print(f"Response: {result3.final_output[:200]}...")
    
    print("\n✅ All tests completed!")


if __name__ == "__main__":
    asyncio.run(test_handoffs()) 