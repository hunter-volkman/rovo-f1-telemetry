import fastf1


def load_session(year: int, grand_prix: str, session: str):
    """
    Load timing and telemetry data for a given F1 session using FastF1.

    Example:
        load_session(2024, "Monaco", "R")
    """
    fastf1.Cache.enable_cache("cache")
    s = fastf1.get_session(year, grand_prix, session)
    s.load()
    return s


def collect_lap_data(year: int, grand_prix: str, session: str = "R"):
    """
    High-level helper that loads a session and returns a simple structure
    focused on lap data.

    This intentionally returns a minimal, easy-to-inspect object for demos,
    not a full analytics-ready dataset.
    """
    session_obj = load_session(year, grand_prix, session)

    # For now, just return a tiny subset of information.
    # You can expand this later if you want richer demo data.
    return {
        "year": year,
        "grand_prix": grand_prix,
        "session": session,
        "laps_available": getattr(session_obj, "laps", None) is not None,
    }


def load_latest_race_session():
    """
    Convenience wrapper for demos: load lap data for a hard-coded recent race.

    TODO: Make this dynamic by looking up the current or last completed race.
    """
    # Pick a stable example; you don't have to actually run this in the demo.
    return collect_lap_data(2024, "Monaco", "R")