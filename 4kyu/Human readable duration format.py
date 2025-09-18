def format_duration(seconds):
    if seconds == 0:
        return "now"

    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    units = [
        ("year", years),
        ("day", days),
        ("hour", hours),
        ("minute", minutes),
        ("second", sec),
    ]

    parts = []
    for name, value in units:
        if value > 0:
            if value == 1:
                parts.append(f"{value} {name}")
            else:
                parts.append(f"{value} {name}s")

    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return " and ".join(parts)
    else:
        return ", ".join(parts[:-1]) + " and " + parts[-1]
