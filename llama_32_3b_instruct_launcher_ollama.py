# %% [0.0] Launcher Script Info
# Script metadata and documentation for version tracking
# Ollama Llama 3.2 3B Launcher - Bare Bones Version
# Description: Minimal launcher for Llama 3.2 3B using Ollama API
# Author: dougeeai
# Created: 2025-11-09
# Last Updated: 2025-11-11
# Note: Uses Ollama API instead of direct GGUF loading

# %% [0.1] Model Card & Summary
# Quick reference for model capabilities and requirements
# MODEL: Llama-3.2-3B via Ollama
# Architecture: Llama 3.2 (3.21B parameters)
# Size: ~2GB download (Ollama handles quantization)
# Requirements: Ollama installed and running
# Note: Ollama manages GGUF files internally

# %% [1.0] Core Imports
# Essential imports for Ollama API interaction
import json
import requests
import sys

# %% [1.1] Utility Imports
# Bare Version: Utility imports skipped

# %% [2.0] Base Directory Configuration
# Not applicable - Ollama manages all file storage internally

# %% [2.1] Model Source Configuration
# Not applicable - Models downloaded via: ollama pull llama3.2:3b

# %% [2.2] User Configuration - All Settings
# Central location for all user-modifiable settings

MODEL = "llama3.2:3b"  # Ollama model name
HOST = "http://localhost:11434"  # Ollama API endpoint
TEMP = 0.7  # Temperature for generation
SYSTEM_MSG = "You are a helpful AI assistant."  # System prompt

# %% [2.3] Model Configuration Dataclass
# Bare Version: Dataclass skipped - using direct variables

# %% [3.0] Hardware Auto-Detection
# Not applicable - Ollama handles hardware optimization automatically

# %% [3.1] Hardware Detection
# Not applicable - Ollama manages hardware

# %% [3.2] Environment Validation
# Simple check if Ollama service is running
def check_ollama():
    """Check if Ollama service is running"""
    try:
        requests.get(f"{HOST}/api/tags")
        return True
    except:
        return False

# %% [4.0] Model Loader
# Not applicable - Ollama loads models automatically

# %% [4.1] Model Validation
# Not applicable - Ollama validates models

# %% [5.0] Model Initialization
# Not applicable - Models initialized per request

# %% [6.0] Inference Test
# Not applicable - Test happens naturally with first chat message

# %% [6.1] Terminal Chat Interface
# Interactive chat loop with Ollama streaming
def chat():
    """Interactive chat with Ollama"""
    print(f"Chat with {MODEL} - Type 'quit' to exit")
    print("-" * 40)
    
    messages = [{"role": "system", "content": SYSTEM_MSG}]
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            break
        if not user_input:
            continue
        
        messages.append({"role": "user", "content": user_input})
        
        # Send to Ollama API
        response = requests.post(
            f"{HOST}/api/chat",
            json={
                "model": MODEL,
                "messages": messages,
                "stream": True,
                "options": {"temperature": TEMP}
            },
            stream=True
        )
        
        print("\nAssistant: ", end="", flush=True)
        full_response = ""
        
        # Stream response chunks
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                if 'message' in data and 'content' in data['message']:
                    chunk = data['message']['content']
                    print(chunk, end="", flush=True)
                    full_response += chunk
        
        print()
        messages.append({"role": "assistant", "content": full_response})
        
        # Keep history manageable
        if len(messages) > 20:
            messages = [messages[0]] + messages[-18:]

# %% [7.0] Optional Features
# Bare Version: Optional features skipped

# %% [8.0] Main Entry Point
# Simple main function - check Ollama and start chat
def main():
    """Main entry point - check Ollama and start chat"""
    # Check if Ollama is running
    if not check_ollama():
        print("Error: Ollama not running. Start with 'ollama serve'")
        sys.exit(1)
    
    # Start chat interface
    chat()

if __name__ == "__main__":
    main()
