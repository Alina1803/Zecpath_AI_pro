import re
from typing import Dict, List


SECTION_PATTERNS = {
    "summary": [
        r"\bsummary\b",
        r"\bprofessional summary\b",
        r"\bprofile\b"
    ],
    "skills": [
        r"\bskills\b",
        r"\btechnical skills\b",
        r"\bcore competencies\b"
    ],
    "experience": [
        r"\bwork experience\b",
        r"\bprofessional experience\b",
        r"\bexperience\b",
        r"\bemployment history\b"
    ],
    "education": [
        r"\beducation\b",
        r"\bacademic background\b"
    ],
    "projects": [
        r"\bprojects\b",
        r"\bpersonal projects\b"
    ],
    "certifications": [
        r"\bcertifications\b",
        r"\blicenses\b"
    ]
}

def segment_sections(text):

    sections = {}
    current_section = None

    lines = text.split("\n")

    for line in lines:

        line_clean = line.strip().lower()

        if line_clean in ["skills", "education", "experience", "projects"]:
            current_section = line_clean
            sections[current_section] = ""

        elif current_section:
            sections[current_section] += line + "\n"

    return sections

class ResumeSectionSegmenter:

    def _init_(self):
        self.compiled_patterns = {
            section: [re.compile(p, re.IGNORECASE) for p in patterns]
            for section, patterns in SECTION_PATTERNS.items()
        }

    def detect_section_heading(self, line: str) -> str | None:
        """Detect if a line is a section heading."""
        line_clean = line.strip().lower()

        for section, patterns in self.compiled_patterns.items():
            for pattern in patterns:
                if pattern.search(line_clean):
                    return section
        return None

    def segment(self, text: str) -> Dict[str, str]:
        """
        Split resume text into structured sections.
        """
        lines = text.split("\n")
        current_section = "other"
        sections: Dict[str, List[str]] = {}

        for line in lines:
            detected = self.detect_section_heading(line)

            if detected:
                current_section = detected
                if current_section not in sections:
                    sections[current_section] = []
                continue

            if current_section not in sections:
                sections[current_section] = []

            sections[current_section].append(line)

        # Convert lists to strings
        return {k: "\n".join(v).strip() for k, v in sections.items()}

def clean_text(self, text: str) -> str:
    text = re.sub(r'\r', '', text)
    text = re.sub(r'\n{2,}', '\n', text)
    return text.strip()


def segment(self, text: str) -> dict:
    text = self.clean_text(text)
    lines = text.split("\n")

    sections = {}
    current_section = "other"

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # Detect heading even if uppercase
        if line.isupper() and len(line) < 40:
            detected = self.detect_section_heading(line)
            if detected:
                current_section = detected
                sections[current_section] = []
                continue

        detected = self.detect_section_heading(line)
        if detected:
            current_section = detected
            sections[current_section] = []
            continue

        if current_section not in sections:
            sections[current_section] = []

        sections[current_section].append(line)

    return {k: "\n".join(v).strip() for k, v in sections.items()}
