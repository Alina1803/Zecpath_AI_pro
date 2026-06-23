from app.services.JD_Parser.role_detector import detect_roles

from app.services.JD_Parser.ca_roles import CA_ROLES


class RoleMapper:

    @staticmethod
    def detect(text):

        detected = detect_roles(text, CA_ROLES)

        if not detected:
            return None

        return detected[0]
