def detect_language(text):
    try:
        text.encode('ascii')
        return "english"
    except:
        return "mixed"