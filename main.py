#######################################################4
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, destination_floor):
        if destination_floor > self.top_floor or destination_floor < self.bottom_floor:
            print("Invalid floor request. The floor is out of range.")
            return

        while self.current_floor != destination_floor:

            if self.current_floor < destination_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")


# Main program
if __name__ == "__main__":
    # Create an elevator
    elevator_h = Elevator(bottom_floor=1, top_floor=10)

    # Move the elevator to floor 5
    elevator_h.go_to_floor(5)

    # Move the elevator back to the bottom floor
    elevator_h.go_to_floor(1)

#######################################################5
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, destination_floor):
        if destination_floor > self.top_floor or destination_floor < self.bottom_floor:
            print("Invalid floor request. The floor is out of range.")
            return

        while self.current_floor != destination_floor:
            if self.current_floor < destination_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            print(f"Running elevator {elevator_number} to floor {destination_floor}")
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number")


# Main program
if __name__ == "__main__":
    # Create a building with 3 elevators, ranging from floor 1 to 10
    building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

    # Run elevators to specific floors
    building.run_elevator(elevator_number=0, destination_floor=7)
    building.run_elevator(elevator_number=1, destination_floor=3)

#######################################################6
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, destination_floor):
        if destination_floor > self.top_floor or destination_floor < self.bottom_floor:
            print("Invalid floor request. The floor is out of range.")
            return

        while self.current_floor != destination_floor:
            if self.current_floor < destination_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            print(f"Running elevator {elevator_number} to floor {destination_floor}")
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number")

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
        print("Fire alarm activated. All elevators moved to the bottom floor.")


# Main program
if __name__ == "__main__":
    # Create a building with 3 elevators, ranging from floor 1 to 10
    building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

    # Run elevators to specific floors
    building.run_elevator(elevator_number=0, destination_floor=7)
    building.run_elevator(elevator_number=1, destination_floor=3)

    # Activate fire alarm, moving all elevators to the bottom floor
    building.fire_alarm()


##############################################################7
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        if change_speed >= 0:
            self.current_speed = min(self.current_speed + change_speed, self.max_speed)
        else:
            self.current_speed = max(self.current_speed + change_speed, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change_speed = random.randint(-10, 15)
            car.accelerate(change_speed)
            car.drive(1)

    def print_status(self):
        print("{:<15} {:<15} {:<15} {:<15}".format("Registration", "Max Speed (km/h)", "Current Speed", "Travelled Distance"))
        print("-" * 60)
        for car in self.cars:
            print("{:<15} {:<15} {:<15} {:<15}".format(
                car.registration_number,
                car.max_speed,
                car.current_speed,
                car.travelled_distance
            ))
        print()

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


# Main program
if __name__ == "__main__":
    # Create a list of ten cars for the race
    cars = [Car(registration_number=f"ABC-{i}", max_speed=random.randint(100, 200)) for i in range(1, 11)]

    # Create the Grand Demolition Derby race with 8000 kilometers distance
    grand_demolition_derby = Race(name="Grand Demolition Derby", distance=8000, cars=cars)

    # Simulate the race progress
    for hour in range(1, 1001):  # Run for a maximum of 1000 hours
        grand_demolition_derby.hour_passes()

        # Print status every 10 hours
        if hour % 10 == 0:
            print(f"Hour {hour}")
            grand_demolition_derby.print_status()

        # Check if the race has finished
        if grand_demolition_derby.race_finished():
            print("Race finished!")
            break

    # Print final status at the end of the race
    print("Final Status:")
    grand_demolition_derby.print_status()
