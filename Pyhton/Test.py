import pyautogui
import math
import time

def draw_circle(radius):
    # Calculate the circumference of the circle
    circumference = 2 * math.pi * radius

    # Set the number of steps to draw the circle
    steps = int(circumference)

    # Set the angle increment
    angle_increment = 360 / steps

    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Calculate the center of the screen
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Move the mouse to the starting point
    pyautogui.moveTo(center_x + radius, center_y)

    # Simulate drawing the circle
    for _ in range(steps):
        angle_rad = math.radians(angle_increment)
        x = center_x + radius * math.cos(angle_rad)
        y = center_y + radius * math.sin(angle_rad)
        pyautogui.dragTo(x, y, duration=1)

# Example usage
radius = 100
time.sleep(5)  # Give some time to focus on the drawing area
draw_circle(radius) 