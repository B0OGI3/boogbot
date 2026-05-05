# boogbot

A CLI coding agent powered by Google Gemini 2.5 Flash. Give it a natural language prompt about a codebase and it plans, reads, writes, and runs files autonomously until the task is done — similar in spirit to tools like Cursor or Claude Code, but built from scratch.

## How It Works

The agent runs an iterative loop (up to 20 steps):

1. Sends your prompt + conversation history to Gemini
2. Gemini decides whether to call a tool or respond with a final answer
3. Tools execute and their results feed back into the next iteration
4. Loop ends when Gemini produces a text response with no further tool calls

### Available Tools

| Tool | Description |
|---|---|
| `get_files_info` | List files and sizes in a directory |
| `get_file_content` | Read a file's contents (up to 10,000 chars) |
| `run_python_file` | Execute a Python file and capture output |
| `write_file` | Write or overwrite a file |

All file operations are sandboxed to the working directory — no access outside it.

## Tech Stack

- Python 3.13
- [Google Gemini API](https://ai.google.dev/) (`gemini-2.5-flash`)
- `google-genai` SDK
- `python-dotenv`

## Getting Started

### 1. Clone and install

```bash
git clone https://github.com/B0OGI3/boogbot.git
cd boogbot
pip install -r requirements.txt
```

### 2. Set up your API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_key_here
```

Get a free key at [aistudio.google.com](https://aistudio.google.com).

### 3. Run

```bash
python main.py "your prompt here"
```

Add `--verbose` to see token counts and tool call details:

```bash
python main.py "fix any bugs in main.py" --verbose
```

## Example

```bash
python main.py "look at the calculator project and run its tests, then fix any failing ones"
```

The agent will list files, read the source, run the tests, identify failures, and write fixes — all autonomously.

## Project Structure

```
boogbot/
├── main.py                    # Entry point — argument parsing and agent loop
├── prompts.py                 # System prompt
├── config.py                  # Constants (file read limit, etc.)
├── functions/
│   ├── call_function.py       # Routes Gemini tool calls to Python functions
│   ├── get_file_content.py    # Safe file reader
│   ├── get_files_info.py      # Directory listing
│   ├── run_python_file.py     # Sandboxed Python execution
│   └── write_file.py          # Safe file writer
└── calculator/                # Sample codebase for testing the agent against
```

## Safety

- All file operations are sandboxed to the working directory
- Always commit your code before running the agent so you can `git diff` or revert
- Do not point it at directories containing secrets or credentials
