def find_secret_number(low, high, guess_bot):
    while low <= high:
        mid = (low + high)//2
        result = guess_bot.guess_number(mid)

        if result == 'Correct':
            return mid
        elif result == 'Larger':
            low = mid + 1
        elif result == 'Smaller':
            high = mid - 1
