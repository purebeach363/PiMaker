
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button


def darts_thrower(darts):
    hits_x, hits_y = [], []
    misses_x, misses_y = [], []

    for _ in range(darts):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)

        if x**2 + y**2 <= 100:
            hits_x.append(x)
            hits_y.append(y)
        else:
            misses_x.append(x)
            misses_y.append(y)

    return hits_x, hits_y, misses_x, misses_y


# Create figure and plot
fig, ax = plt.subplots(figsize=(9, 9))
fig.canvas.manager.set_window_title("Pi M   aker")

# Leave space at the bottom for our widgets
plt.subplots_adjust(bottom=0.20)

# Create input box
axbox = fig.add_axes([0.20, 0.08, 0.35, 0.06])
text_box = TextBox(axbox, "Number of darts: ", initial="1000")

# Create button
axbutton = fig.add_axes([0.62, 0.08, 0.20, 0.06])
button = Button(axbutton, "Throw darts!")

# Status message
status = fig.text(0.5, 0.02, "Enter a number greater than 1.",
                  ha="center")


def update_plot(darts):
    hits_x, hits_y, misses_x, misses_y = darts_thrower(darts)

    hit = len(hits_x)
    total = darts

    pi_estimate = 4 * hit / total

    # Clear previous graph
    ax.clear()

    # Draw hits and misses
    ax.scatter(hits_x, hits_y, s=5, color="green",
               label="Hits (inside circle)")

    ax.scatter(misses_x, misses_y, s=5, color="red",
               label="Misses (outside circle)")

    # Draw circle
    circle = plt.Circle((0, 0), 10, fill=False,
                        color="blue", linewidth=2)

    ax.add_patch(circle)

    # Configure plot
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect("equal")

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.set_title(
        f"Pi maker = {pi_estimate:.6f}\n"
        f"Number of darts: {total}"
    )

    ax.legend()
    ax.grid(alpha=0.2)

    status.set_text(
        f"Hits: {hit} | Misses: {total-hit} | Estimated pi: {pi_estimate:.6f}"
    )

    fig.canvas.draw_idle()


def throw_darts(event):
    user_input = text_box.text.strip()

    try:
        darts = int(user_input)

        if darts <= 1:
            status.set_text("Please enter a number greater than 1!")
            fig.canvas.draw_idle()
            return

        update_plot(darts)

    except ValueError:
        status.set_text("Invalid input! Please enter a whole number.")
        fig.canvas.draw_idle()


# Connect button and Enter key to the same function
button.on_clicked(throw_darts)
text_box.on_submit(throw_darts)

# Draw initial circle
ax.add_patch(plt.Circle((0, 0), 10, fill=False,
                        color="blue", linewidth=2))

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect("equal")
ax.set_title("Pi Maker")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(alpha=0.2)

# Start application
plt.show()
