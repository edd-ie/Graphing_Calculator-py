from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import GraphingCalc as graphFx
from matplotlib import pyplot as plt
import customtkinter


# Appearance and colour scheme
customtkinter.set_appearance_mode("system")  # system, dark, light
customtkinter.set_default_color_theme('green')

# Window creation
root = customtkinter.CTk()
root.title("Graphing calculator")
root.geometry("1200x630")  # pixels height & width

# Configure grid columns to expand
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Display
plot_frame = customtkinter.CTkFrame(master=root, width=820)
plot_frame.grid(row=0, column=0, pady=25, padx=(30, 20), sticky="nsew")  # Padding and resizing

frame = customtkinter.CTkFrame(master=root, width=280)  # parent element root
frame.grid(row=0, column=1, pady=25, padx=(30, 20), sticky="nsew")

# Data input and controls

# ----> Function
label1 = customtkinter.CTkLabel(master=frame, text="Graph type")
label1.pack(pady=12, padx=10)


def fx_callback(choice):
    fx_var.set(choice)


fx_var = customtkinter.StringVar(value="linear")
fx = customtkinter.CTkComboBox(master=frame, values=["linear", "quadratic", "cubic"],
                               command=fx_callback, variable=fx_var)
fx.pack(pady=12, padx=10)

# ----> Inverse
label2 = customtkinter.CTkLabel(master=frame, text="Inverse Function")
label2.pack(pady=12, padx=10)
inv_var = customtkinter.StringVar(value="no")


def inv_callback(choice):
    inv_var.set(choice)


inv = customtkinter.CTkComboBox(master=frame, values=["yes", "no"],
                                command=inv_callback, variable=inv_var)
inv.pack(pady=12, padx=10)

# ----> Coefficient
label3 = customtkinter.CTkLabel(master=frame, text="Coefficient")
label3.pack(pady=12, padx=10)
coefficient = customtkinter.CTkEntry(master=frame, placeholder_text="number")
coefficient.pack(pady=12, padx=10)

# ----> Constant
label4 = customtkinter.CTkLabel(master=frame, text="Constant")
label4.pack(pady=12, padx=10)
constant = customtkinter.CTkEntry(master=frame, placeholder_text="number")
constant.pack(pady=12, padx=10)

# ----> Range
label5 = customtkinter.CTkLabel(master=frame, text="Range")
label5.pack(pady=12, padx=10)
range_x = customtkinter.CTkEntry(master=frame, placeholder_text="max x-value")
range_x.pack(pady=12, padx=10)


def submit():
    print("Calculating...")
    dataset = [fx.get(), inv_var.get(), coefficient.get(), constant.get(), range_x.get()]

    # Create a new figure and subplot
    fig = plt.Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Get the data from graphFx.plot()
    graph = graphFx.plot(dataset[0], dataset[1], int(dataset[2]), int(dataset[3]), int(dataset[4]))

    # Plot the data on the subplot
    ax.plot(graph[0], graph[1], marker='s')

    # Set labels
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_title(dataset[0] + ' graph')

    print("...plotting...")
    # Create a canvas for the plot and add it to your customtkinter.CTkFrame
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True)

    coefficient.delete(0, 'end')
    constant.delete(0, 'end')
    range_x.delete(0, 'end')
    print("...Done")


# ----> Button
button = customtkinter.CTkButton(master=frame, text="Graph", command=submit)
button.pack(pady=12, padx=10)

root.mainloop()
