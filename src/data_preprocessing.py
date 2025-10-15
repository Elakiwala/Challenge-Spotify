import pandas as pd
import ast

def extract_first_genre(val):
    """Return the first genre from artist_genres which may be a stringified list or comma-separated string."""
    if pd.isna(val):
        return None
    if isinstance(val, (list, tuple)):
        return val[0] if len(val) > 0 else None
    if isinstance(val, str):
        try:
            parsed = ast.literal_eval(val)
            if isinstance(parsed, (list, tuple)) and len(parsed) > 0:
                return parsed[0]
        except Exception:
            parts = [p.strip() for p in val.split(',') if p.strip()]
            return parts[0] if parts else None
    return None

def parse_genre_list(val):
    """Return a list of genre strings for a cell that may be
       a stringified Python list or a comma-separated string or a real list."""
    if pd.isna(val):
        return []
    if isinstance(val, (list, tuple)):
        return [g.strip().lower() for g in val if isinstance(g, str)]
    if isinstance(val, str):
        # Try to parse stringified list
        try:
            parsed = ast.literal_eval(val)
            if isinstance(parsed, (list, tuple)):
                return [g.strip().lower() for g in parsed if isinstance(g, str)]
        except Exception:
            # fallback: comma-separated
            parts = [p.strip().lower() for p in val.split(',') if p.strip()]
            return parts
    return []
