import time
import random

class AutonomousVehicle:
    def __init__(self, lane):
        self.speed = 0
        self.position = 0
        self.lane = lane

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

    def move(self):
        self.position += self.speed

    def change_lane(self):
        self.lane = (self.lane + 1) % 3  # Assuming there are 3 lanes

class Environment:
    def __init__(self):
        self.obstacles = []
        self.generate_obstacles()

    def generate_obstacles(self):
        for _ in range(5):
            lane = random.randint(0, 2)
            position = random.randint(0, 99)
            self.obstacles.append((lane, position))

    def move_obstacles(self):
        for i in range(len(self.obstacles)):
            lane, position = self.obstacles[i]
            position = (position + 1) % 100  # Move obstacle forward by one step
            self.obstacles[i] = (lane, position)

    def display(self, vehicles):
        print("-" * 80)
        for lane in range(3):
            for i in range(100):
                if (lane, i) in vehicles:
                    print("A", end="")
                elif (lane, i) in self.obstacles:
                    print("X", end="")
                else:
                    print("-", end="")
            print("\n" + "-" * 80)

def main():
    vehicles = [AutonomousVehicle(lane=0), AutonomousVehicle(lane=1), AutonomousVehicle(lane=2)]
    environment = Environment()

    for _ in range(100):
        environment.display({(vehicle.lane, vehicle.position) for vehicle in vehicles})
        time.sleep(0.5)
        environment.move_obstacles()
        for vehicle in vehicles:
            if (vehicle.lane, vehicle.position) in environment.obstacles:
                print("Obstacle ahead! Decelerating...")
                vehicle.decelerate()
                time.sleep(1)
                if vehicle.speed == 0:
                    vehicle.change_lane()
            else:
                print("No obstacle ahead. Accelerating...")
                vehicle.accelerate()
                time.sleep(1)
                vehicle.move()

if __name__ == "__main__":
    main()
