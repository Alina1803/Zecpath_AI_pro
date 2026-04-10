from functools import lru_cache

# Cache JD processing
@lru_cache(maxsize=100)
def cached_jd_processing(jd_text: str):
    from app.utils.text_utils import preprocess_text
    return preprocess_text(jd_text)


# Cache resume processing
@lru_cache(maxsize=200)
def cached_resume_processing(resume_text: str):
    from app.utils.text_utils import preprocess_text
    return preprocess_text(resume_text)