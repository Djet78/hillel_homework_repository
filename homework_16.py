# ---------------------- homework_16 ------------------------


def have_trains_crashed(first_train_speed, second_train_speed, sidetrack=4, path=10):
    """
    Shows will be collision of two trains at given speeds
    :param path: starting distance between two trains
    :param sidetrack: takes distance until first train can turn from main path
    :param first_train_speed: takes speed of 1st train
    :param second_train_speed: takes speed of 2nd train
    :return: True if trains crashes or False if not
    """
    first_train_road_time = sidetrack / first_train_speed
    second_train_road_time = (path - sidetrack) / second_train_speed
    if first_train_road_time == second_train_road_time or second_train_road_time < first_train_road_time:
        return True
    elif first_train_road_time < second_train_road_time:
        return False


print(have_trains_crashed(4, 6))
