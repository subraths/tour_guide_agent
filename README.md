# AI Tourist Guide and Travel Planning Agent

A minimal LangChain + LangGraph + DeepAgents project that acts as a tourist guide and travel planner.  
It uses OpenRouter (`openai/gpt-oss-120b:free`) and supports in-memory trip history.

---

## ✨ Features

- Suggest must-see spots for a city
- Build quick multi-day itineraries
- Save and list trip history (session only)
- CLI interface for quick interaction

---

## ✅ Requirements

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- OpenRouter API key

---

## 🚀 Setup

```bash
uv init ai-tourist-guide
cd ai-tourist-guide
uv add langchain langchain-openrouter langgraph deepagents python-dotenv
```

Create `.env`:

```
OPENROUTER_API_KEY=your_openrouter_key_here
```

---

## 📂 Project Structure

```
ai-tourist-guide/
├─ app/
│  └─ main.py
├─ tools/
│  └─ guide_tools.py
├─ .env
└─ README.md
```

---

## ▶️ Run

```bash
uv run python app/main.py
```

Example prompts:

```
Plan a 3-day foodie trip to Tokyo
Save this trip: 3-day Tokyo foodie itinerary
List my trips
```

---

## 🧠 Model

Uses:

```
openrouter:openai/gpt-oss-120b:free
```

---

## ✅ Notes

- Trip history is stored **in-memory only** (reset on restart).
- You can extend tools to include real data sources (maps, weather, events, etc.).

---

## 📌 Next Ideas

- Persistent trip history (SQLite / JSON)
- Live POI search (Places API)
- Weather-aware itinerary planning
- Budget-based optimization
