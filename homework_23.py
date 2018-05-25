# ------------------------ Task 23 -------------------------


def chess_reward():
    """
    Counts grains until it reaches above 1 million
    :return: cell number, total amount of grains on this cell
    """
    cell = 0
    grain_total = 1
    while True:
        cell += 1
        grain_total = grain_total*2
        if grain_total > int(1e6):
            return cell, grain_total - 1


print(chess_reward())
