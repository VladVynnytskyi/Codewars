def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce >= 1 or bounce <= 0 or window >= h:
        return -1
    res = 1
    while h > window:
        if h * bounce > window:
            res += 2
        h = h * bounce
    return res