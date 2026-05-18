# ✈️ AI Tourist Guide & Travel Planning Agent

A mini LangChain + Groq project that acts as your personal AI travel companion.

## What it does

Ask it anything travel-related and it uses a ReAct agent to select the right tool and respond intelligently:

| Tool | What it does |
|------|-------------|
| `get_top_attractions` | Lists must-see spots for a city |
| `plan_itinerary` | Builds a day-by-day trip plan |
| `estimate_budget` | Calculates cost for budget/mid-range/luxury travel |
| `get_packing_list` | Season-aware packing suggestions |
| `get_local_tips` | Insider advice & cultural etiquette |

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the agent
python travel_agent.py
```

Or set your API key as an environment variable to skip the prompt:
```bash
export GROQ_API_KEY="your_key_here"
python travel_agent.py
```

Get a free Groq API key at: https://console.groq.com

## LangChain Concepts Used

- **`@tool` decorator** — wraps plain Python functions as LangChain tools
- **`ChatGroq`** — LangChain-compatible Groq LLM wrapper
- **`create_react_agent`** — builds a ReAct (Reason + Act) agent
- **`AgentExecutor`** — runs the agent loop, handles tool calls & errors
- **`hub.pull`** — loads a standard ReAct prompt from LangChain Hub

## Example Queries

```
What are the top attractions in Kyoto?
Plan a 3-day trip to Paris for someone who loves food and history
What's the budget for 5 days in Tokyo, mid-range style?
What should I pack for Bangalore in monsoon season?
Give me local tips for New York City
```

## Project Structure

```
travel_agent/
├── travel_agent.py    # Agent, tools, and CLI
├── requirements.txt   # Pinned dependencies
└── README.md
```

## Extending It

To add a new tool, just decorate any function with `@tool` and add it to the `tools` list in `build_agent()`:

```python
@tool
def get_visa_info(country: str) -> str:
    """Returns visa requirements for a country."""
    ...
```

The agent will automatically decide when to use it.
