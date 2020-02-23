def enough(cap, on, wait):
    if cap >= on + wait:
        return 0
    elif cap < on + wait:
        return (on+wait) - cap


