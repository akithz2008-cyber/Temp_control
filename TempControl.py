import tkinter as tk
from tkinter import END


FONT_MAIN_TITLE = "Verdana 16 bold"
FONT_HEADING = "Verdana 12 bold"
FONT_DEFAULT = "Verdana 12"

COLOR_YELLOW = "#FFFF00"
COLOR_PINK = "#FFC0CB"
COLOR_ERROR = "red"
COLOR_TEXT = "black"


ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67



class TemperatureConverter:
    """
    Handles all conversion mathematics and string formatting validations.
    This class contains absolutely NO Tkinter code.
    """

    def calculate_to_c(self, f_string):
        """Converts Fahrenheit string input to Celsius."""
        # 1. Check if input is a valid number
        try:
            f_val = float(f_string)
        except ValueError:
            return "Please enter a number"

        # 2. Check against absolute zero
        if f_val < ABS_ZERO_FAHRENHEIT:
            return "Temperature too low"

        # 3. Calculate and format response
        c_val = (f_val - 32) * 5 / 9
        return f"{c_val:.1f} degrees Centigrade"

    def calculate_to_f(self, c_string):
        """Converts Celsius string input to Fahrenheit."""
        # 1. Check if input is a valid number
        try:
            c_val = float(c_string)
        except ValueError:
            return "Please enter a number"

        # 2. Check against absolute zero
        if c_val < ABS_ZERO_CELSIUS:
            return "Temperature too low"

        # 3. Calculate and format response
        f_val = (c_val * 9 / 5) + 32
        return f"{f_val:.1f} degrees Fahrenheit"



class ConverterGUI:
    """Sets up the GUI layout, frame switching, and widget behaviors."""

    def __init__(self, root):

        self.converter = TemperatureConverter()


        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x175")


        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)


        self.container = tk.Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)


        self.frames = {}


        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()


        self.show_frame("MainFrame")

    def show_frame(self, name):
        """Brings the chosen frame to the top of the stack layer."""
        frame = self.frames[name]
        frame.tkraise()


    def create_main_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")


        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)


        lbl_title = tk.Label(
            frame, text="Temperature Converter", font=FONT_MAIN_TITLE
        )
        lbl_title.grid(row=0, column=0, columnspan=2, pady=10)


        btn_to_c = tk.Button(
            frame,
            text="to Centigrade",
            font=FONT_HEADING,
            bg=COLOR_YELLOW,
            command=lambda: self.show_frame("to_cFrame"),
        )
        btn_to_c.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")


        btn_to_f = tk.Button(
            frame,
            text="to Fahrenheit",
            font=FONT_HEADING,
            bg=COLOR_PINK,
            command=lambda: self.show_frame("to_fFrame"),
        )
        btn_to_f.grid(row=1, column=1, padx=10, pady=15, sticky="nsew")

        return frame


    def create_to_c_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")


        for r in range(4):
            frame.rowconfigure(r, weight=1)
        for c in range(3):
            frame.columnconfigure(c, weight=1)

        # Main Heading
        lbl = tk.Label(
            frame, text="Enter the temperature in Fahrenheit", font=FONT_HEADING
        )
        lbl.grid(row=0, column=0, columnspan=3, pady=5)

        # Input Box
        self.temp_entry_c = tk.Entry(frame, font=FONT_DEFAULT, justify="center")
        self.temp_entry_c.grid(row=1, column=0, columnspan=3, padx=20, sticky="ew")

        # Output label
        self.result_c_label = tk.Label(
            frame, text="Converted temperature goes here", font=FONT_DEFAULT
        )
        self.result_c_label.grid(row=3, column=0, columnspan=3, pady=5)

        # Operation Buttons
        btn_calc = tk.Button(
            frame,
            text="Calculate",
            font=FONT_DEFAULT,
            command=self.to_centigrade,
        )
        btn_calc.grid(row=2, column=0, padx=5, sticky="nsew")

        btn_back = tk.Button(
            frame,
            text="Back",
            font=FONT_DEFAULT,
            command=lambda: self.show_frame("MainFrame"),
        )
        btn_back.grid(row=2, column=1, padx=5, sticky="nsew")

        btn_reset = tk.Button(
            frame,
            text="Reset",
            font=FONT_DEFAULT,
            command=lambda: self.reset(self.temp_entry_c, self.result_c_label),
        )
        btn_reset.grid(row=2, column=2, padx=5, sticky="nsew")

        return frame


    def create_to_f_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")


        for r in range(4):
            frame.rowconfigure(r, weight=1)
        for c in range(3):
            frame.columnconfigure(c, weight=1)

        # Main Heading
        lbl = tk.Label(
            frame, text="Enter the temperature in Centigrade", font=FONT_HEADING
        )
        lbl.grid(row=0, column=0, columnspan=3, pady=5)

        # Input Box
        self.temp_entry_f = tk.Entry(frame, font=FONT_DEFAULT, justify="center")
        self.temp_entry_f.grid(row=1, column=0, columnspan=3, padx=20, sticky="ew")

        # Output label
        self.result_f_label = tk.Label(
            frame, text="Converted temperature goes here", font=FONT_DEFAULT
        )
        self.result_f_label.grid(row=3, column=0, columnspan=3, pady=5)

        # Operation Buttons
        btn_calc = tk.Button(
            frame,
            text="Calculate",
            font=FONT_DEFAULT,
            command=self.to_fahrenheit,
        )
        btn_calc.grid(row=2, column=0, padx=5, sticky="nsew")

        btn_back = tk.Button(
            frame,
            text="Back",
            font=FONT_DEFAULT,
            command=lambda: self.show_frame("MainFrame"),
        )
        btn_back.grid(row=2, column=1, padx=5, sticky="nsew")

        btn_reset = tk.Button(
            frame,
            text="Reset",
            font=FONT_DEFAULT,
            command=lambda: self.reset(self.temp_entry_f, self.result_f_label),
        )
        btn_reset.grid(row=2, column=2, padx=5, sticky="nsew")

        return frame


    def to_centigrade(self):
        """Passes data to logic class and displays Fahrenheit -> Celsius conversion."""
        raw_input = self.temp_entry_c.get()
        result = self.converter.calculate_to_c(raw_input)


        if "degrees" in result:
            self.result_c_label.configure(text=result, fg=COLOR_TEXT)
        else:
            self.result_c_label.configure(text=result, fg=COLOR_ERROR)

    def to_fahrenheit(self):
        """Passes data to logic class and displays Celsius -> Fahrenheit conversion."""
        raw_input = self.temp_entry_f.get()
        result = self.converter.calculate_to_f(raw_input)


        if "degrees" in result:
            self.result_f_label.configure(text=result, fg=COLOR_TEXT)
        else:
            self.result_f_label.configure(text=result, fg=COLOR_ERROR)

    def reset(self, entry, label):
        """Clears target Entry widget values and resets standard placeholder labels."""
        entry.delete(0, END)
        label.configure(text="Converted temperature goes here", fg=COLOR_TEXT)



if __name__ == "__main__":
    window = tk.Tk()
    app = ConverterGUI(window)
    window.mainloop()