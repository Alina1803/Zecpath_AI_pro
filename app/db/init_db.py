from app.db.connection import engine, Base
from app.models.transcript_models import CATranscript, CATranscriptSegment

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully")


if __name__ == "__main__":
    init_db()