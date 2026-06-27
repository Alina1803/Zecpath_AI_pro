def create_alert(metric):

    if metric["failures"] > 5:

        return "ALERT"

    return "OK"
