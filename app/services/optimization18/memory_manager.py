import gc

def clear_memory():
    """
    Force garbage collection
    """
    gc.collect()


def process_large_text(text, chunk_size=1000):
    """
    Yield chunks instead of loading everything at once
    """
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]