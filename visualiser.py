import tkinter as tk
import time
from algorithms.bubblesort import bubble_sort

root = tk.Tk()
root.title("Algorithm Visualiser")
root.geometry('850x500')
root.option_add("*Font", "Helvetica 10")

# Frame for top controls
controls = tk.Frame(root)
controls.grid(row=0, column=0, columnspan=4, pady=10)

# Entry
tk.Label(controls, text="Enter values:").grid(row=0, column=0, padx=5)
entry = tk.Entry(controls, width=30)
entry.grid(row=0, column=1, padx=5)

# Sort button
sort_button = tk.Button(controls, text="Sort", fg="white", bg="#4CAF50", command=lambda: run_sort())
sort_button.grid(row=0, column=2, padx=5)

# Algorithm dropdown
selected_algorithm = tk.StringVar()
selected_algorithm.set("Bubble Sort")
algo_menu = tk.OptionMenu(controls, selected_algorithm, "Bubble Sort", "Insertion Sort")
algo_menu.grid(row=0, column=3, padx=5)

# Canvas for visualisation
canvas = tk.Canvas(root, width=800, height=300, bg="#f8f8f8")
canvas.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Status label
status_label = tk.Label(root, text="Status: Waiting", fg="#2d3436", font=("Helvetica", 11, "bold"))
status_label.grid(row=2, column=0, columnspan=4)

# Speed slider
speed_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Speed (1 = Slow, 10 = Fast)")
speed_slider.set(5)
speed_slider.grid(row=3, column=0, columnspan=4, pady=10)

# Draw function
def draw_array(arr, highlight_indices=[]):
    canvas.delete("all")
    width = 800
    height = 300
    bar_width = width / len(arr)
    is_numeric = all(isinstance(x, (int, float)) for x in arr)
    max_val = max(arr) if is_numeric else len(max(arr, key=len))

    for i, val in enumerate(arr):
        x0 = i * bar_width + 2
        x1 = (i + 1) * bar_width - 2

        if is_numeric:
            y0 = height - (val / max_val) * 250
        else:
            y0 = height - (len(val) / max_val) * 250

        y1 = height

        color = "#ff7675" if i in highlight_indices else "#74b9ff"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
        canvas.create_text((x0 + x1) / 2, y0 - 5, anchor=tk.S, text=str(val), font=("Helvetica", 10))

    root.update()

# Sorting logic
def run_sort():
    speed = speed_slider.get()
    delay = 1.1 - (speed * 0.1)
    raw = entry.get()
    items = [x.strip() for x in raw.split(",")]

    is_numeric = all(item.replace("-", "").isnumeric() for item in items)
    arr = [int(x) for x in items] if is_numeric else items

    algorithm = selected_algorithm.get()

    if algorithm == "Bubble Sort":
        steps = bubble_sort(arr.copy())
    elif algorithm == "Insertion Sort":
        try:
            from algorithms.insertionsort import insertion_sort
            steps = insertion_sort(arr.copy())
        except ImportError:
            status_label.config(text="Insertion Sort not implemented.")
            return
    else:
        status_label.config(text="Unknown algorithm")
        return

    for state, highlights in steps:
        status_label.config(text=f"Swapping: {highlights[0]} ↔ {highlights[1]}")
        draw_array(state, highlight_indices=highlights)
        time.sleep(delay)

    draw_array(steps[-1][0])  # Draw final sorted state
    status_label.config(text="Status: Completed!")

root.mainloop()
