# import matplotlib.pyplot as plt
# import numpy as np
# import math

# def plot_function(func, a_values, b_values, midpoints):
#     """Plots a function and highlights method steps dynamically, with integer axis labels."""
    
#     # Define x range dynamically
#     x_min, x_max = min(a_values + b_values) - 1, max(a_values + b_values) + 1
#     x = np.linspace(x_min, x_max, 400)

#     # Compute y-values safely
#     y = []
#     for val in x:
#         try:
#             if "log" in func and val <= 0:  # Prevent log(x) errors
#                 y.append(float('nan'))
#             else:
#                 y.append(eval(func, {"x": val, "sin": math.sin, "cos": math.cos, "tan": math.tan,
#                                      "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e}))
#         except (ValueError, OverflowError):
#             y.append(float('nan'))

#     # Convert to NumPy array and mask NaN/Inf values
#     y = np.array(y)
#     mask = np.isfinite(y)  # Filter out NaN and Inf values

#     # Set dynamic y-limits ignoring NaN values
#     y_valid = y[mask]
#     if len(y_valid) > 0:
#         y_min, y_max = min(y_valid), max(y_valid)
#         y_margin = (y_max - y_min) * 0.1  # Add 10% margin
#         y_min, y_max = math.floor(y_min - y_margin), math.ceil(y_max + y_margin)  # Round to integers
#     else:
#         y_min, y_max = -1, 1  # Default range

#     # Plot function
#     plt.figure(figsize=(8, 5))
#     plt.plot(x[mask], y[mask], label=f"f(x) = {func}", color='blue')
#     plt.axhline(0, color='black', linewidth=1)
#     plt.axvline(0, color='black', linewidth=1)

#     # Evaluate function values for given points
#     def safe_eval(val):
#         try:
#             return eval(func, {"x": val, "sin": math.sin, "cos": math.cos, "tan": math.tan,
#                                "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e})
#         except (ValueError, OverflowError):
#             return float('nan')

#     a_y = [safe_eval(v) for v in a_values]
#     b_y = [safe_eval(v) for v in b_values]
#     mid_y = [safe_eval(v) for v in midpoints]

#     # Plot points with valid values
#     plt.scatter(a_values, a_y, color='red', label="Lower bound (a)")
#     plt.scatter(b_values, b_y, color='green', label="Upper bound (b)")
#     plt.scatter(midpoints, mid_y, color='purple', marker='x', label="Midpoints (c)")

#     # Round x and y limits to integers
#     x_min, x_max = math.floor(x_min), math.ceil(x_max)

#     # Set limits and labels
#     plt.xlim(x_min, x_max)
#     plt.ylim(y_min, y_max)

#     # Set integer ticks
#     plt.xticks(range(x_min, x_max + 1))  # Integer ticks for x-axis
#     plt.yticks(range(y_min, y_max + 1))  # Integer ticks for y-axis

#     plt.xlabel("x")
#     plt.ylabel("f(x)")
#     plt.title("Bisection & False Position Method Iterations")
#     plt.legend()
#     plt.grid()
#     plt.show()
import matplotlib.pyplot as plt
import numpy as np
import math

def plot_function(func, a_values, b_values, midpoints):
    """Plots a function and highlights method steps dynamically with interactive tooltips."""
    
    # Define x range dynamically
    x_min, x_max = min(a_values + b_values) - 1, max(a_values + b_values) + 1
    x = np.linspace(x_min, x_max, 400)

    # Compute y-values safely
    y = []
    for val in x:
        try:
            if "log" in func and val <= 0:  # Prevent log(x) errors
                y.append(float('nan'))
            else:
                y.append(eval(func, {"x": val, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                                     "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e}))
        except (ValueError, OverflowError):
            y.append(float('nan'))

    # Convert to NumPy array and mask NaN/Inf values
    y = np.array(y)
    mask = np.isfinite(y)

    # Set y-limits ignoring NaN values
    y_valid = y[mask]
    if len(y_valid) > 0:
        y_min, y_max = min(y_valid), max(y_valid)
        y_margin = (y_max - y_min) * 0.1  # 10% margin
        y_min, y_max = math.floor(y_min - y_margin), math.ceil(y_max + y_margin)
    else:
        y_min, y_max = -1, 1  # Default range

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x[mask], y[mask], label=f"f(x) = {func}", color='blue')
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    # Safe function evaluation
    def safe_eval(val):
        try:
            return eval(func, {"x": val, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                               "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e})
        except (ValueError, OverflowError):
            return float('nan')

    # Compute valid y-values for points
    a_y = [safe_eval(v) for v in a_values]
    b_y = [safe_eval(v) for v in b_values]
    mid_y = [safe_eval(v) for v in midpoints]

    # Scatter points
    a_scatter = ax.scatter(a_values, a_y, color='red', label="Lower bound (a)", picker=True)
    b_scatter = ax.scatter(b_values, b_y, color='green', label="Upper bound (b)", picker=True)
    mid_scatter = ax.scatter(midpoints, mid_y, color='purple', marker='x', label="Midpoints (c)", picker=True)

    # Set integer ticks
    ax.set_xlim(math.floor(x_min), math.ceil(x_max))
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(range(math.floor(x_min), math.ceil(x_max) + 1))
    ax.set_yticks(range(y_min, y_max + 1))

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Bisection & False Position Method Iterations")
    ax.legend()
    ax.grid()

    # Add hover annotation
    tooltip = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
                          bbox=dict(boxstyle="round", fc="w"),
                          arrowprops=dict(arrowstyle="->"))
    tooltip.set_visible(False)

    # Hover event handler
    def on_hover(event):
        if event.inaxes == ax:
            for scatter, label in [(a_scatter, "a"), (b_scatter, "b"), (mid_scatter, "c")]:
                cont, ind = scatter.contains(event)
                if cont:
                    index = ind["ind"][0]
                    x_val, y_val = scatter.get_offsets()[index]
                    tooltip.set_text(f"{label}: ({x_val:.4f}, {y_val:.4f})")
                    tooltip.set_position((event.xdata, event.ydata))
                    tooltip.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        tooltip.set_visible(False)
        fig.canvas.draw_idle()

    # Connect event
    fig.canvas.mpl_connect("motion_notify_event", on_hover)

    plt.show()
