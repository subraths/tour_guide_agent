from langchain.tools import tool

# Simple in-memory trip store (session-only)
_TRIP_HISTORY: dict[str, str] = {}

_SUGGESTION_CACHE: dict[str, str] = {}


@tool
def suggest_spots(city: str) -> str:
    """Suggest must-see spots in a city with short descriptions."""
    city_lower = city.lower()
    if "paris" in city_lower:
        return (
            "Paris highlights: Eiffel Tower (iconic views), Louvre (world-class art), "
            "Montmartre (arts district), Seine river walk, and Le Marais (cafes + shopping)."
        )
    if "tokyo" in city_lower:
        return (
            "Tokyo highlights: Senso-ji (Asakusa), Shibuya Crossing, Meiji Shrine, "
            "Tsukiji Outer Market, and teamLab exhibits."
        )
    suggestion = f"""
        Top spots in {city}: central old town, a major museum, a riverfront or scenic park,
        a local market, and a sunset viewpoint.
        """

    _SUGGESTION_CACHE[city] = suggestion
    return suggestion


@tool
def list_previous_trip_suggestions() -> str:
    """List cached previous trip suggestions"""
    if not _SUGGESTION_CACHE:
        return "No city suggestions cached yet."
    lines = [f"{city}: {desc}" for city, desc in _SUGGESTION_CACHE.items()]
    return "Cached City Suggestions:\n" + "\n".join(lines)


@tool
def build_itinerary(destination: str, days: int, interests: str) -> str:
    """Create a compact day-by-day itinerary based on destination, trip length, and interests."""
    itinerary = (
        f"{days}-day itinerary for {destination} focused on {interests}:\n"
        f"Day 1: City orientation + signature landmark + local food tour.\n"
        f"Day 2: Museum/heritage block + neighborhood walk + evening market.\n"
        f"Day 3: Nature/parks + shopping + sunset viewpoint.\n"
        f"Adjust based on opening hours and travel time."
    )
    return itinerary


@tool
def mark_suggested_as_completed(city: str) -> str:
    """Mark a city's suggestions as completed (for tracking)."""
    if city in _SUGGESTION_CACHE:
        _TRIP_HISTORY[city] = _SUGGESTION_CACHE[city]
        return f"Marked suggestions for {city} as completed and saved to trip history."
    return f"No suggestions found for {city} to mark as completed."


@tool
def save_trip(city: str, summary: str) -> str:
    """Save a trip summary to history."""
    _TRIP_HISTORY[city] = summary.strip()
    return "Trip saved to history."


@tool
def list_trips() -> str:
    """List all saved trips."""
    if not _TRIP_HISTORY:
        return "No trips saved yet."
    lines = [f"{i + 1}. {t}" for i, t in enumerate(_TRIP_HISTORY)]
    return "Trip History:\n" + "\n".join(lines)
