# Coin Denominations: 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p
# How many different ways can 200p be made using any number of coins?


def change_maker(total):
    combos = [[1] * total]
    while combos[-1][0] < total:
        last = combos[-1]
        print(last)
        if len(last) == 2:
            finisher(combos)
        elif last[-2] == 1:
            add_ones(combos)
        elif last[-1] == 1:
            twos_and_one(combos)
        elif last[-1] == 2:
            twos_and_two(combos)
        elif last[-1] == 5:
            fives_and_fives(combos)
        elif last[-2] == 10:
            tens_and_tens(combos)
        elif last[-1] == 10:
            twenty_and_ten(combos)
        elif last[-1] == 20:
            twenty_and_twenty(combos)
        elif last[-1] == 50:
            fifty_and_fifty(combos)
    return len(combos)


def finisher(list):
    new = [2 * list[-1][0]]
    list.append(new)
    print(list[-1])
    return list


def add_ones(list):
    new = list[-1]
    new.pop()
    new.pop()
    new.append(2)
    new.sort(reverse=True)
    list.append(new)
    return list


def twos_and_one(list):
    new = list[-1]
    count = new.count(2)
    position = new.index(2)
    # Remove all the 2's and the 1
    for _ in range(len(new[position:])):
        new.pop()
    # Add a 5
    new.append(5)
    # Add sum of count * 2 + 1 - 5 1's
    total = count * 2 - 4
    if total > 0:
        for _ in range(total):
            new.append(1)
    new.sort(reverse=True)
    list.append(new)
    return list


def twos_and_two(list):
    new = list[-1]
    count = new.count(2)
    position = new.index(2)
    # Remove all the 2's and the 1
    for _ in range(len(new[position:])):
        new.pop()
    # Add a 5
    new.append(5)
    # Add sum of count * 2 - 5 1's
    total = count * 2 - 5
    if total > 0:
        for _ in range(total):
            new.append(1)
    new.sort(reverse=True)
    list.append(new)
    return list


def fives_and_fives(list):
    new = list[-1]
    count = new.count(5)
    position = new.index(5)
    # Remove all the 2's and the 1
    for _ in range(len(new[position:])):
        new.pop()
    # Add a 5
    new.append(10)
    # Add sum of count * 2 - 5 1's
    total = count * 5 - 10
    if total > 0:
        for _ in range(total):
            new.append(1)
    new.sort(reverse=True)
    list.append(new)
    return list


def tens_and_tens(list):
    new = list[-1]
    count = new.count(10)
    position = new.index(10)
    # Remove all the 2's and the 1
    for _ in range(len(new[position:])):
        new.pop()
    # Add a 5
    new.append(20)
    # Add sum of count * 2 - 5 1's
    total = count * 10 - 20
    if total > 0:
        for _ in range(total):
            new.append(1)
    new.sort(reverse=True)
    list.append(new)
    return list


def twenty_and_ten(list):
    new = list[-1]
    count = new.count(20)
    position = new.index(20)
    # Remove all the 2's and the 1
    for _ in range(len(new[position:])):
        new.pop()
    # Add a 5
    new.append(50)
    # Add sum of count * 2 + 1 - 5 1's
    total = count * 20 - 40
    if total > 0:
        for _ in range(total):
            new.append(1)
    new.sort(reverse=True)
    list.append(new)
    return list


def twenty_and_twenty(list):
    new = list[-1]
    count = new.count(20)
    position = new.index(20)
    # Remove all the 2's and the 1
    for _ in range(len(new[position:])):
        new.pop()
    # Add a 5
    new.append(50)
    # Add sum of count * 2 - 5 1's
    total = count * 20 - 50
    if total > 0:
        for _ in range(total):
            new.append(1)
    new.sort(reverse=True)
    list.append(new)
    print(list[-1])
    return list


def fifty_and_fifty(list):
    new = list[-1]
    count = new.count(50)
    position = new.index(50)
    # Remove all the 2's and the 1
    for _ in range(len(new[position:])):
        new.pop()
    # Add a 5
    new.append(100)
    # Add sum of count * 2 - 5 1's
    total = count * 50 - 100
    if total > 0:
        for _ in range(total):
            new.append(1)
    new.sort(reverse=True)
    list.append(new)
    return list


total = 20

print("There are", change_maker(total), "ways to make change for", total, "cents")
