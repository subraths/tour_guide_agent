from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from deepagents import create_deep_agent

from src.guide_tools import (
    suggest_spots,
    build_itinerary,
    list_previous_trip_suggestions,
    mark_suggested_as_completed,
    list_trips,
    save_trip,
)

SYSTEM_PROMPT = """
You MUST follow these rules without exception:
- NEVER answer questions about saved trips or suggestions from memory
- ALWAYS call list_suggestions() when user asks to list/show/recall anything saved
- ALWAYS call save_trip() before confirming a trip is saved
- If unsure whether to call a tool, call it anyway
"""


def main() -> None:
    load_dotenv()

    # OpenRouter model via init_chat_model using provider:model syntax
    model = init_chat_model(
        model="openrouter:openai/gpt-oss-120b:free",
        temperature=0.1,
    )

    # In-memory checkpointer for session memory
    checkpointer = InMemorySaver()

    agent = create_deep_agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[
            suggest_spots,
            build_itinerary,
            list_previous_trip_suggestions,
            mark_suggested_as_completed,
            list_trips,
            save_trip,
        ],
        checkpointer=checkpointer,
    )

    print("AI Tourist Guide CLI. Type 'exit' to quit.\n")
    thread_id = "tourist-guide-session"

    while True:
        user_text = input("You: ").strip()
        if not user_text or user_text.lower() in {"exit", "quit"}:
            break

        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_text}]},
            config={"configurable": {"thread_id": thread_id}},
        )
        # Deep Agents returns a LangGraph state; messages live in result["messages"]
        final_msg = result["messages"][-1].content
        print(f"\nGuide: {final_msg}\n")


if __name__ == "__main__":
    main()
