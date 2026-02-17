def categorize(ref):
    ref = ref.upper()

    if "MISSION" in ref:
        return "MISSION"
    elif "TITHE" in ref:
        return "TITHE"
    elif "OFFERING" in ref:
        return "OFFERING"
    else:
        return "GENERAL"
