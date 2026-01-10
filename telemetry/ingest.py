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