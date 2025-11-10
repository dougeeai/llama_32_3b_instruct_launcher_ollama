# Llama 3.2 3B Instruct Ollama Launcher

Quick and dirty launcher script for running Llama-3.2-3B-Instruct through Ollama API.

## Description

Simple Python script to chat with Llama 3.2 3B Instruct model using Ollama's local API. Ollama handles all the model management, quantization, and hardware optimization automatically.

## Requirements

- Python 3.13
- Ollama installed and running
- ~2GB disk space for model

## Setup

1. Install Ollama:
```bash
# Windows: Download from https://ollama.ai
# Linux: curl -fsSL https://ollama.ai/install.sh | sh
# Mac: brew install ollama
```

2. Start Ollama service:
```bash
ollama serve
```

3. Pull the model:
```bash
ollama pull llama3.2:3b
```

4. Create conda environment:
```bash
conda env create -f environment.yml
conda activate llama_32_3b_instruct_launcher_ollama
```

5. Run:
```bash
python llama_32_3b_instruct_launcher_ollama.py
```

## Files

- `llama_32_3b_instruct_launcher_ollama.py` - Ollama API client with streaming chat
- `environment.yml` - Minimal conda environment (just requests library)

## Configuration

Key settings in the script:
- `MODEL` - Model name in Ollama (default: "llama3.2:3b")
- `HOST` - Ollama API endpoint (default: "http://localhost:11434")
- `TEMP` - Temperature for generation (default: 0.7)

## Usage

Type messages at the prompt. Commands:
- `quit` - Exit the chat

## Notes

- Ollama manages all GGUF files internally
- Automatic GPU/CPU detection and optimization
- No manual model path configuration needed
- Streaming output enabled by default
