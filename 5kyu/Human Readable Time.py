def make_readable(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    if seconds > 36000:
        return '%d:%02d:%02d' % (hour, min, sec)
    else:
        return '0%d:%02d:%02d' % (hour, min, sec)