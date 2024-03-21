import tkinter as tk
import json

# Placeholder for your JSON data loading
room_data = {
    "Conference Room": {"Temperature (Celsius)": 22, "Humidity (%)": 45, "Air Quality Index": 30, "People Count": 5},
    "Executive Office": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Break": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Lobby": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Reception": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "OPEN 1": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Open 2": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "IT": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Meet 1": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "meet 2": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "CEO": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},

    # Add other rooms data from your JSON file here...
}

class Room:
    def __init__(self, canvas, x1, y1, x2, y2, name, info_box, hover_color='red'):
        self.canvas = canvas
        self.name = name
        self.info_box = info_box  # Pass the reference to the info box where details will be displayed
        self.default_color = 'white'
        self.hover_color = hover_color
        self.rect = canvas.create_rectangle(x1, y1, x2, y2, fill=self.default_color, outline='black', tags=name)
        self.text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=name)

        # Bind hover events to the room
        self.canvas.tag_bind(self.rect, '<Enter>', self.on_hover)
        self.canvas.tag_bind(self.rect, '<Leave>', self.on_leave)

    def on_hover(self, event):
        # Display room information in the info box
        room_info = room_data.get(self.name, {})
        info_text = f"{self.name}\nTemp: {room_info.get('Temperature (Celsius)', 'N/A')}°C\n" \
                    f"Humidity: {room_info.get('Humidity (%)', 'N/A')}%\n" \
                    f"Air Quality: {room_info.get('Air Quality Index', 'N/A')}\n" \
                    f"People Count: {room_info.get('People Count', 'N/A')}"
        self.info_box.config(text=info_text)

    def on_leave(self, event):
        # Clear the info box
        self.info_box.config(text="Hover over a room")

# Create the main window
root = tk.Tk()
root.title("Interactive Floor Plan")

# Create a canvas widget
canvas_width, canvas_height = 1200, 650
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(side='left', fill='both', expand=True)

# Create an info box to display room details
info_box = tk.Label(root, text="Hover over a room", justify='left', bg='lightgrey', anchor='nw')
info_box.pack(side='right', fill='both', expand=True)

# Example room coordinates based on the provided image (you will need to adjust these)
rooms = [
    Room(canvas, 0, 175, 240, 0, 'Conference Room', info_box),
    Room(canvas, 0, 175, 175, 350, 'Executive Office', info_box),
    Room(canvas, 0, 350, 175, 520, 'Break Room', info_box),
    Room(canvas, 175, 300, 375, 520, 'Lobby', info_box),
    Room(canvas, 375, 365, 490, 590, 'Reception', info_box),
    Room(canvas, 240, 0, 410, 220, 'Open Office Area 1', info_box),
    Room(canvas, 410, 0, 580, 220, 'Open Office Area 2', info_box),
    Room(canvas, 580, 0, 750, 220, 'IT Room', info_box),
    Room(canvas, 750, 0, 970, 220, 'Meeting Room 1', info_box),
    Room(canvas, 970, 0, 1140, 220, 'Meeting Room 2', info_box),
    Room(canvas, 800, 300, 1140, 520, 'CEO Office', info_box),
]

root.mainloop()
