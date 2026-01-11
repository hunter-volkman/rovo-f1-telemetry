import fastf1


def load_session(year: int, grand_prix: str, session: str):
    """
    Load timing and telemetry data for a given F1 session using FastF1.

    Example:
        load_session(2024, "Monaco", "R")
    """
    fastf1.Cache.enable_cache("cache")
    session_obj = fastf1.get_session(year, grand_prix, session)
    session_obj.load()
    return session_obj


def collect_lap_data(year: int, grand_prix: str, session: str = "R"):
    """
    Load a session and return a small structure with basic lap data context.

    This returns a minimal subset of information that is easy to inspect and
    suitable as an input to downstream analytics.
    
    TODO:
        - Return a pandas DataFrame with lap and sector times.
        - Include basic quality checks on the underlying data.
    """
    session_obj = load_session(year, grand_prix, session)

    # For now, return a minimal subset of fields.
    return {
        "year": year,
        "grand_prix": grand_prix,
        "session": session,
        "laps_available": getattr(session_obj, "laps", None) is not None,
    }


def load_latest_race_session():
    """
    Convenience wrapper that loads lap data for a fixed recent race.

    TODO:
        - Replace the hard-coded values with a lookup for the latest completed
          race in the calendar.
    """
    return collect_lap_data(2024, "Monaco", "R")