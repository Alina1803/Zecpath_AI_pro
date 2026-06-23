# --------------------------------------
# File-Based Task Engine
# --------------------------------------


def file_task_quality(files_processed):

    if files_processed >= 10:
        return "Advanced File Handling"

    elif files_processed >= 5:
        return "Intermediate Handling"

    return "Basic Handling"
