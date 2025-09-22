# utils.py
def safe_print(*args, **kwargs):
    """Print wrapper that handles unicode errors gracefully."""
    try:
        print(*args, **kwargs)
    except UnicodeEncodeError:
        # fallback
        print(*[str(a).encode("utf-8", "replace") for a in args], **kwargs)
