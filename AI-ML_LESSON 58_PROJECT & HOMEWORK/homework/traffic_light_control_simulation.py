import time

class TrafficLight:
    def __init__(self):
        self.color = "Red"

    def change_color(self):
        if self.color == "Red":
            self.color = "Green"
        elif self.color == "Green":
            self.color = "Yellow"
        elif self.color == "Yellow":
            self.color = "Red"

    def display(self):
        print(f"Traffic Light Color: {self.color}")

def main():
    traffic_light = TrafficLight()

    while True:
        traffic_light.display()
        traffic_light.change_color()
        time.sleep(3)  # Change traffic light color every 3 seconds

if __name__ == "__main__":
    main()
