def countWays(target, power, num):
    value = num ** power

    # Agar exact target mil gaya
    if target == 0:
        return 1

    # Agar target se bada ho gaya
    if value > target:
        return 0

    # Include current number
    include = countWays(target - value, power, num + 1)

    # Skip current number
    exclude = countWays(target, power, num + 1)

    return include + exclude

cnt = countWays(100, 2, 5)
print(cnt)