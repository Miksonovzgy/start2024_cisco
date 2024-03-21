import tkinter as tk
import json

def update_room_data():
    global room_data
    room_data = room_data2


room_data = {
    "Office 4": {"Temperature (Celsius)": 22, "Humidity (%)": 45, "Air Quality Index": 30, "People Count": 5},
    "Office 3": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 2": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 1": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Reception": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 5": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 6": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 7": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Toilets": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Kitchen": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Meeting Room": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
}

room_data2 = {
    "Office 4": {"Temperature (Celsius)": 22, "Humidity (%)": 45, "Air Quality Index": 30, "People Count": 5},
    "Office 3": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 2": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 1": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Reception": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 5": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 6": {"Temperature (Celsius)": 50, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Office 7": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Toilets": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Kitchen": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},
    "Meeting Room": {"Temperature (Celsius)": 21, "Humidity (%)": 50, "Air Quality Index": 25, "People Count": 1},

}


class Room:
    def __init__(self, canvas, x1, y1, x2, y2, name, hover_color='red'):
        self.canvas = canvas
        self.name = name
        self.default_color = 'white'
        self.hover_color = hover_color
        self.rect = canvas.create_rectangle(x1, y1, x2, y2, fill=self.default_color, outline='black', tags=name)
        # Adjust the font size as needed
        self.text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=name, font=('TkDefaultFont', 8), tags=f"{name}_text")

        self.update_color_by_temp()  # Update color based on the initial temperature

        # Bind hover events
        self.canvas.tag_bind(self.rect, '<Enter>', self.on_hover)
        self.canvas.tag_bind(self.rect, '<Leave>', self.on_leave)

    def on_hover(self, event):
        room_info = room_data.get(self.name, {})
        # Display only critical information to fit in the box
        info_text = f"Temp: {room_info.get('Temperature (Celsius)', 'N/A')}°C\nPeople: {room_info.get('People Count', 'N/A')}"
        self.canvas.itemconfig(self.text, text=info_text)

    def on_leave(self, event):
        self.canvas.itemconfig(self.text, text=self.name)

    def update_color_by_temp(self):
        room_info = room_data.get(self.name, {})
        temp = room_info.get('Temperature (Celsius)', 0)
        if temp > 35:
            self.canvas.itemconfig(self.rect, fill='red')
        else:
            self.canvas.itemconfig(self.rect, fill=self.default_color)

def update_room_data():
    global room_data
    room_data = room_data2
    for room in rooms:  # Assume 'rooms' is a list of all Room instances
        room.update_color_by_temp()

# Create the main window
root = tk.Tk()
root.title("Interactive Floor Plan")
root.configure(bg='light grey')

root.geometry("1920x1080")


# Create a canvas widget and info box
canvas_width, canvas_height = 1920, 1080
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
# canvas.pack(side='left', fill='y', expand=False)
canvas.pack(side='left', fill='both', expand=True)

# info_box = tk.Label(root, text="Hover over a room", justify='left', bg='lightgrey', anchor='nw')
# info_box.pack(side='right', fill='both', expand=True)

# canvas.create_line(185, 175, 225, 175, fill='green', width=5),
# canvas.create_line(175, 190, 175, 230, fill='green', width=5),
# canvas.create_line(240, 300, 280, 300, fill='green', width=5),
# canvas.create_line(350, 220, 390, 220, fill='green', width=5),
# canvas.create_line(420, 365, 460, 365, fill='green', width=5),
# canvas.create_line(430, 220, 470, 220, fill='green', width=5),
# canvas.create_line(690, 220, 730, 220, fill='green', width=5),
# canvas.create_line(840, 220, 880, 220, fill='green', width=5),
# canvas.create_line(980, 220, 1020, 220, fill='green', width=5),
# canvas.create_line(1140, 240, 1140, 260, fill='green', width=5),
# canvas.create_line(840, 300, 880, 300, fill='green', width=5),
# canvas.create_line(1050, 300, 1090, 300, fill='green', width=5),
# canvas.create_line(650, 520, 650, 560, fill='green', width=5),
# canvas.create_line(550, 590, 590, 590, fill='green', width=5),
# canvas.create_line(1140, 600, 1140, 640, fill='green', width=5),
# canvas.create_line(1140, 200, 1140, 300, fill='black', width=1),

# Create room instances
# rooms = [
#     Room(canvas, 0, 175, 240, 0, 'Office 4', info_box),
#     Room(canvas, 0, 175, 175, 350, 'Office 3', info_box),
#     Room(canvas, 0, 350, 175, 520, 'Office 2', info_box),
#     Room(canvas, 175, 300, 375, 520, 'Office 1', info_box),
#     Room(canvas, 375, 365, 490, 590, 'Reception', info_box),
#     Room(canvas, 240, 0, 410, 220, 'Office 5', info_box),
#     Room(canvas, 410, 0, 580, 220, 'Office 6', info_box),
#     Room(canvas, 580, 0, 750, 220, 'Office 7', info_box),
#     Room(canvas, 750, 0, 970, 220, 'Toilets', info_box),
#     Room(canvas, 970, 0, 1140, 220, 'Kitchen', info_box),
#     Room(canvas, 800, 300, 1140, 520, 'Meeting Room', info_box),
#     Room(canvas, 650, 300, 800, 520, 'Staircase', info_box),
#     Room(canvas, 650, 300, 800, 590, 'Staircase', info_box),
#     Room(canvas, 490, 590, 1140, 640, 'Hallway', info_box),

# ]

# rooms = [
#     Room(canvas, 0, 175, 240, 0, 'Office 4'),
#     Room(canvas, 0, 175, 175, 350, 'Office 3'),
#     Room(canvas, 0, 350, 175, 520, 'Office 2'),
#     Room(canvas, 175, 300, 375, 520, 'Office 1'),
#     Room(canvas, 375, 365, 490, 590, 'Reception'),
#     Room(canvas, 240, 0, 410, 220, 'Office 5'),
#     Room(canvas, 410, 0, 580, 220, 'Office 6'),
#     Room(canvas, 580, 0, 750, 220, 'Office 7'),
#     Room(canvas, 750, 0, 970, 220, 'Toilets'),
#     Room(canvas, 970, 0, 1140, 220, 'Kitchen'),
#     Room(canvas, 800, 300, 1140, 520, 'Meeting Room'),
#     Room(canvas, 650, 300, 800, 520, 'Staircase'),
#     Room(canvas, 650, 300, 800, 590, 'Staircase'),
#     Room(canvas, 490, 590, 1140, 640, 'Hallway'),

# ]

label = tk.Label(root, text="Floor 0", bg='light grey')
label.place(x=1280, y=50)  # Position the label at (1720, 50)


rooms = [
    Room(canvas, 0 + 750,   175 + 100, 240 + 750, 0 + 100, 'Office 4'),
    Room(canvas, 0 + 750,   175 + 100, 175 + 750, 350 + 100, 'Office 3'),
    Room(canvas, 0 + 750,   350 + 100, 175 + 750, 520 + 100, 'Office 2'),
    Room(canvas, 175 + 750, 300 + 100, 375 + 750, 520 + 100, 'Office 1'),
    Room(canvas, 375 + 750, 365 + 100, 490 + 750, 590 + 100, 'Reception'),
    Room(canvas, 240 + 750, 0 + 100,   410 + 750, 220 + 100, 'Office 5'),
    Room(canvas, 410 + 750, 0 + 100,   580 + 750, 220 + 100, 'Office 6'),
    Room(canvas, 580 + 750, 0 + 100,   750 + 750, 220 + 100, 'Office 7'),
    Room(canvas, 750 + 750, 0 + 100,   970 + 750, 220 + 100, 'Toilets'),
    Room(canvas, 970 + 750, 0 + 100,   1140 + 750, 220 + 100, 'Kitchen'),
    Room(canvas, 800 + 750, 300 + 100, 1140 + 750, 520 + 100, 'Meeting Room'),
    Room(canvas, 650 + 750, 300 + 100, 800 + 750, 520 + 100, 'Staircase'),
    Room(canvas, 650 + 750, 300 + 100, 800 + 750, 590 + 100, 'Staircase'),
    Room(canvas, 490 + 750, 590 + 100, 1140 + 750, 640 + 100, 'Hallway'),
]


canvas.create_line(185 + 750, 175 + 100, 225 + 750, 175 + 100, fill='green', width=5)
canvas.create_line(175 + 750, 190 + 100, 175 + 750, 230 + 100, fill='green', width=5)
canvas.create_line(240 + 750, 300 + 100, 280 + 750, 300 + 100, fill='green', width=5)
canvas.create_line(350 + 750, 220 + 100, 390 + 750, 220 + 100, fill='green', width=5)
canvas.create_line(420 + 750, 365 + 100, 460 + 750, 365 + 100, fill='green', width=5)
canvas.create_line(430 + 750, 220 + 100, 470 + 750, 220 + 100, fill='green', width=5)
canvas.create_line(690 + 750, 220 + 100, 730 + 750, 220 + 100, fill='green', width=5)
canvas.create_line(840 + 750, 220 + 100, 880 + 750, 220 + 100, fill='green', width=5)
canvas.create_line(980 + 750, 220 + 100, 1020 + 750, 220 + 100, fill='green', width=5)
canvas.create_line(1140 + 750, 240 + 100, 1140 + 750, 260 + 100, fill='green', width=5)
canvas.create_line(840 + 750, 300 + 100, 880 + 750, 300 + 100, fill='green', width=5)
canvas.create_line(1050 + 750, 300 + 100, 1090 + 750, 300 + 100, fill='green', width=5)
canvas.create_line(650 + 750, 520 + 100, 650 + 750, 560 + 100, fill='green', width=5)
canvas.create_line(550 + 750, 590 + 100, 590 + 750, 590 + 100, fill='green', width=5)
canvas.create_line(1140 + 750, 600 + 100, 1140 + 750, 640 + 100, fill='green', width=5)
canvas.create_line(1140 + 750, 200 + 100, 1140 + 750, 300 + 100, fill='black', width=1)


# rect = canvas.create_rectangle(0, 980,)


# Schedule the room_data update after 10000 milliseconds (10 seconds)
root.after(10000, update_room_data)
# screenshot = pyautogui.screenshot()
# screenshot.save('screenshot.png')





root.mainloop()
