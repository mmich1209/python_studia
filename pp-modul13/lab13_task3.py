import random


# kod znaku A to 65
# ord("A")
def draw_letter():
    return chr(random.randint(ord("A"), ord("E")))


def draw_row():
    return [draw_letter() for _ in range(3)]


def check(row):
    if row[0] == row[1] == row[2]:
        return True
    else:
        return False


counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1

