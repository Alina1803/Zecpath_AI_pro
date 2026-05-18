from datetime import datetime


class InterviewState:

    def __init__(self, role, experience):

        # =====================================================
        # BASIC CANDIDATE INFO
        # =====================================================

        self.role = role
        self.experience = experience

        # =====================================================
        # INTERVIEW FLOW
        # =====================================================

        self.current_phase = "introduction"

        self.current_question_id = 0

        self.followup_count = 0

        # =====================================================
        # STORAGE
        # =====================================================

        self.history = []

        self.transcripts = []

        self.audio_files = []

        # =====================================================
        # DUPLICATE QUESTION TRACKING
        # =====================================================

        self.asked_questions = set()

        # =====================================================
        # SCORE TRACKING
        # =====================================================

        self.total_score = 0

        self.communication_score = 0

        self.confidence_score = 0

        self.technical_score = 0

        self.behavioral_score = 0

        # =====================================================
        # INTERVIEW ANALYTICS
        # =====================================================

        self.total_questions = 0

        self.failed_answers = 0

        self.interview_start_time = datetime.now()

        self.interview_end_time = None

    # =========================================================
    # CHECK DUPLICATE QUESTION
    # =========================================================

    def has_asked_question(self, question):

        if not question:

            return False

        return (
            question.strip().lower()
            in self.asked_questions
        )

    # =========================================================
    # GET ALL PREVIOUS QUESTIONS
    # =========================================================

    def get_previous_questions(self):

        return list(self.asked_questions)

    # =========================================================
    # UPDATE STATE AFTER EACH ANSWER
    # =========================================================

    def update(
        self,
        question_data=None,
        q_data=None,
        answer="",
        transcript=None,
        audio_path=None,
        communication_score=0,
        confidence_score=0,
        technical_score=0,
        behavioral_score=0,
        followup=False
    ):

        try:

            # =================================================
            # SUPPORT BOTH question_data AND q_data
            # =================================================

            if q_data is not None:

                question_data = q_data

            if question_data is None:

                question_data = {}

            # =================================================
            # SAFE SCORE HANDLING
            # =================================================

            communication_score = (
                communication_score or 0
            )

            confidence_score = (
                confidence_score or 0
            )

            technical_score = (
                technical_score or 0
            )

            behavioral_score = (
                behavioral_score or 0
            )

            # =================================================
            # QUESTION EXTRACTION
            # =================================================

            question_text = question_data.get(
                "question",
                ""
            ).strip()

            question_type = question_data.get(
                "type",
                "general"
            )

            # =================================================
            # PREVENT DUPLICATE STORAGE
            # =================================================

            normalized_question = (
                question_text.lower()
            )

            if normalized_question in self.asked_questions:

                print(
                    f"\nWARNING: Duplicate Question Detected:\n"
                    f"{question_text}"
                )

            else:

                self.asked_questions.add(
                    normalized_question
                )

            # =================================================
            # FINAL QUESTION SCORE
            # =================================================

            final_score = (
                communication_score +
                confidence_score +
                technical_score +
                behavioral_score
            ) / 4

            # =================================================
            # FAILED ANSWER DETECTION
            # =================================================

            if (
                not transcript or
                not answer or
                "STT Error" in str(answer)
            ):

                self.failed_answers += 1

            # =================================================
            # STORE QUESTION + ANSWER
            # =================================================

            response_data = {

                "id": self.current_question_id,

                "type": question_type,

                "question": question_text,

                "answer": answer,

                "transcript": transcript,

                "audio_path": audio_path,

                "communication_score": round(
                    communication_score,
                    2
                ),

                "confidence_score": round(
                    confidence_score,
                    2
                ),

                "technical_score": round(
                    technical_score,
                    2
                ),

                "behavioral_score": round(
                    behavioral_score,
                    2
                ),

                "final_score": round(
                    final_score,
                    2
                ),

                "followup": followup,

                "timestamp": str(
                    datetime.now()
                )
            }

            self.history.append(
                response_data
            )

            # =================================================
            # STORE TRANSCRIPTS
            # =================================================

            if transcript:

                self.transcripts.append(
                    transcript
                )

            # =================================================
            # STORE AUDIO FILES
            # =================================================

            if audio_path:

                self.audio_files.append(
                    audio_path
                )

            # =================================================
            # TRACK TOTAL SCORES
            # =================================================

            self.total_score += final_score

            self.communication_score += (
                communication_score
            )

            self.confidence_score += (
                confidence_score
            )

            self.technical_score += (
                technical_score
            )

            self.behavioral_score += (
                behavioral_score
            )

            # =================================================
            # FOLLOWUP TRACKING
            # =================================================

            if followup:

                self.followup_count += 1

            # =================================================
            # QUESTION TRACKING
            # =================================================

            self.total_questions += 1

            self.current_question_id += 1

            # =================================================
            # AUTO PHASE MANAGEMENT
            # =================================================

            self._auto_update_phase()

        except Exception as e:

            print(
                f"\nInterviewState Update Error: {e}"
            )

    # =========================================================
    # AUTO UPDATE PHASE
    # =========================================================

    def _auto_update_phase(self):

        if self.total_questions >= 2:

            self.current_phase = "core"

        if self.total_questions >= 5:

            self.current_phase = "evaluation"

        if self.total_questions >= 8:

            self.current_phase = "closing"

    # =========================================================
    # MANUAL NEXT PHASE
    # =========================================================

    def next_phase(self):

        phases = [
            "introduction",
            "core",
            "evaluation",
            "closing"
        ]

        current_index = phases.index(
            self.current_phase
        )

        if current_index < len(phases) - 1:

            self.current_phase = (
                phases[current_index + 1]
            )

    # =========================================================
    # GET CURRENT PHASE
    # =========================================================

    def get_current_phase(self):

        return self.current_phase

    # =========================================================
    # GET TOTAL QUESTIONS
    # =========================================================

    def get_total_questions(self):

        return self.total_questions

    # =========================================================
    # GET LAST RESPONSE
    # =========================================================

    def get_last_response(self):

        if not self.history:

            return None

        return self.history[-1]

    # =========================================================
    # VALIDATE INTERVIEW STATE
    # =========================================================

    def validate_state(self):

        print("\n=================================")

        print("INTERVIEW STATE VALIDATION")

        print("=================================")

        print(f"Total Questions : {self.total_questions}")

        print(f"Current Phase   : {self.current_phase}")

        print(f"Failed Answers  : {self.failed_answers}")

        print(f"Asked Questions :")

        for q in self.asked_questions:

            print(f" - {q}")

    # =========================================================
    # FINAL RESULTS
    # =========================================================

    def get_results(self):

        if self.total_questions == 0:

            return {

                "message": (
                    "No interview data available"
                )
            }

        # =====================================================
        # END TIME
        # =====================================================

        self.interview_end_time = datetime.now()

        duration = (
            self.interview_end_time -
            self.interview_start_time
        )

        # =====================================================
        # AVERAGE SCORES
        # =====================================================

        avg_score = (
            self.total_score /
            self.total_questions
        )

        avg_communication = (
            self.communication_score /
            self.total_questions
        )

        avg_confidence = (
            self.confidence_score /
            self.total_questions
        )

        avg_technical = (
            self.technical_score /
            self.total_questions
        )

        avg_behavioral = (
            self.behavioral_score /
            self.total_questions
        )

        # =====================================================
        # FINAL DECISION
        # =====================================================

        decision = self._final_decision(
            avg_score
        )

        # =====================================================
        # RETURN FINAL REPORT
        # =====================================================

        return {

            "role": self.role,

            "experience": self.experience,

            "phase": self.current_phase,

            "total_questions": (
                self.total_questions
            ),

            "followups_asked": (
                self.followup_count
            ),

            "failed_answers": (
                self.failed_answers
            ),

            "interview_duration": str(
                duration
            ),

            "average_score": round(
                avg_score,
                2
            ),

            "communication_score": round(
                avg_communication,
                2
            ),

            "confidence_score": round(
                avg_confidence,
                2
            ),

            "technical_score": round(
                avg_technical,
                2
            ),

            "behavioral_score": round(
                avg_behavioral,
                2
            ),

            "decision": decision,

            "responses": self.history
        }

    # =========================================================
    # FINAL DECISION LOGIC
    # =========================================================

    def _final_decision(self, avg_score):

        # =====================================================
        # SYSTEM FAILURE CHECK
        # =====================================================

        if self.failed_answers >= 2:

            return "INCOMPLETE"

        # =====================================================
        # NORMAL DECISION LOGIC
        # =====================================================

        if avg_score >= 8:

            return "STRONG SELECT"

        elif avg_score >= 7:

            return "SELECTED"

        elif avg_score >= 5:

            return "HOLD"

        else:

            return "REJECTED"