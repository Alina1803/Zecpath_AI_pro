from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    raw_text: Mapped[str] = mapped_column(Text)

    summary: Mapped[str] = mapped_column(Text, nullable=True)
    skills: Mapped[str] = mapped_column(Text, nullable=True)
    experience: Mapped[str] = mapped_column(Text, nullable=True)
    education: Mapped[str] = mapped_column(Text, nullable=True)
    projects: Mapped[str] = mapped_column(Text, nullable=True)
    certifications: Mapped[str] = mapped_column(Text, nullable=True)