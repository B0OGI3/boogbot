# BOOGBOT – LLM Code Debugging Agent

This project is a small “agentic” developer tool inspired by editors like Cursor, Zed, and Claude Code. It uses a large language model (LLM) plus a set of tool functions to:

- Analyze and debug code
- Propose fixes and refactors
- Optionally run tests or commands to verify changes

> ⚠️ This is a **toy** agent for learning. Don’t point it at sensitive code or give it broad system access.

---

## Features

- Summarizes and analyzes code files
- Proposes bug fixes and improvements
- Can call tools such as:
  - `read_file` / `write_file` (or your equivalents)
  - `run_tests` or `run_command`
- Iterative “plan + act + reflect” loop to refine changes

---

## Tech Stack

- Language: Python [3.13]
- LLM Provider: [Gemini / OpenAI / Anthropic / etc.]
- Dependencies:
  - `python-dotenv` (optional, for environment variables)
  - `[your LLM SDK]`
  - `[any test frameworks: pytest, etc.]`

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/B0OGI3/boogbot.git
cd boogbot
```

2. Install Dependencies
pip install -r requirements.txt

(or your poetry/pipenv/uv command.)

3. Environment Variables
Create a .env file (or otherwise set env vars) with your LLM credentials:

LLM_API_KEY=your_key_here
LLM_MODEL_NAME=your_model_here

Adjust names as needed to match your code.

Usage
Typical usage:

python main.py path/to/your/codebase

Or, if you have CLI flags:

python main.py \
  --root ./my_project \
  --entry main.py \
  --max-iterations 5

The agent will:

Scan the code (or the specified file/directory)
Ask the LLM to analyze and propose a plan
Use tools to read/write files or run tests
Iterate until done or a limit is reached
Check your git diff after the run to review all changes.

Project Structure
.
├─ main.py            # Entry point for the agent
├─ agent.py           # Core agent loop and reasoning
├─ tools.py           # Tool function definitions
├─ tests/             # Optional: tests for the agent itself
└─ requirements.txt   # Python dependencies

Adjust this section to match your actual layout.

Safety Notes
Commit your code before running the agent so you can easily revert.
Avoid giving it write access to:
Home directory
Secrets/configs
Production systems
Review all changes before pushing to GitHub.
Future Improvements
Ideas for extending the project:

Better planning / reflection steps
Support for more tools (e.g., search, static analysis)
Multi-file refactors
Richer CLI or TUI interface
License
[MIT / Apache-2.0 / etc.]

Acknowledgements
Built as part of the Boot.dev “LLM Prompt Engineering & Agents” course.


If you paste your repo structure and how you actually run the agent, I can tailor this README so it fits your project perfectly.
