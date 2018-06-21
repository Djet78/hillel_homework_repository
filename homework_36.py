# ------------------------ Task 36 -------------------------


class Vehicle:
    """
    Max_speed (kmh)
    Acceleration (seconds)
    """

    def __init__(self, passenger_capacity, max_speed, acceleration):
        self.passenger_cap = passenger_capacity
        self.max_speed = max_speed
        self.acceleration = acceleration

    def percentage_of_occupancy(self, passengers):
        if passengers > self.passenger_cap:
            raise ValueError("Too much passengers for this vehicle")
        else:
            return round(((passengers * 100) / self.passenger_cap), 2)


class Train(Vehicle):

    WAGON_CARGO_CAPACITY = 80

    def __init__(self, passenger_capacity, max_speed, acceleration, quantity_of_wagons):
        super().__init__(passenger_capacity, max_speed, acceleration)
        self.quantity_of_wagons = quantity_of_wagons

    def possible_total_cargo_calc(self):
        return self.WAGON_CARGO_CAPACITY * self.quantity_of_wagons


class Airplane(Vehicle):
    """
    In_air_time (in hours)
    """
    def __init__(self, passenger_capacity, max_speed, acceleration, in_air_time):
        super().__init__(passenger_capacity, max_speed, acceleration)
        self.in_air_time = in_air_time

    def possible_fly_distance_calc(self):
        return self.max_speed * self.in_air_time


cargo_train_1 = Train(0, 200, 30, 100)
print("Possible cargo amount: ", cargo_train_1.possible_total_cargo_calc())

passenger_train_1 = Train(300, 180, 80, 10)
print("Percentage of occupancy: ", passenger_train_1.percentage_of_occupancy(190))

airplane_1 = Airplane(130, 350, 120, 18)
print("Possible fly distance: ", airplane_1.possible_fly_distance_calc())
