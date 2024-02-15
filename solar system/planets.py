import tkinter as tk
import threading
import time
import math
import random

class Planet:
    def __init__(self, canvas, color, radius, distance, angular_velocity):
        self.canvas = canvas
        self.color = color
        self.radius = radius
        self.distance = distance
        self.angular_velocity = angular_velocity
        self.angle = 0
        self.x = 0
        self.y = 0
        self.draw()

    def draw(self):
        self.planet_item = self.canvas.create_oval(0, 0, 0, 0, fill=self.color)
        self.update_position()

    def update_position(self):
        self.x = self.canvas.winfo_width() / 2 + self.distance * math.cos(self.angle)
        self.y = self.canvas.winfo_height() / 2 + self.distance * math.sin(self.angle)
        self.canvas.coords(self.planet_item,
                           self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius)

    def move(self):
        self.angle += self.angular_velocity
        self.update_position()

class SolarSystemSimulation:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height
        self.planets = []

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='black')
        self.canvas.pack()

    def create_planets(self):
        planets_data = [
            ("yellow", 40, 0, 0, 0),  # Sun
            ("gray", 5, 80, 0.01, 0),  # Mercury
            ("orange", 8, 120, 0.008, 0),  # Venus
            ("blue", 10, 160, 0.005, 0),  # Earth
            ("red", 9, 200, 0.004, 0),  # Mars
            ("brown", 15, 280, 0.002, 0),  # Jupiter
            ("purple", 12, 360, 0.0015, 0),  # Saturn
            ("cyan", 10, 420, 0.001, 0),  # Uranus
            ("green", 8, 480, 0.0008, 0)  # Neptune
        ]

        for data in planets_data:
            color, radius, distance, angular_velocity, _ = data
            planet = Planet(self.canvas, color, radius, distance, angular_velocity)
            self.planets.append(planet)

    def start_simulation(self):
        self.create_planets()
        for planet in self.planets:
            threading.Thread(target=self.move_planet, args=(planet,)).start()

    def move_planet(self, planet):
        while True:
            planet.move()
            time.sleep(0.01)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Solar System Simulation")

    width, height = 1200, 800

    app = SolarSystemSimulation(root, width, height)
    app.start_simulation()

    root.mainloop()
