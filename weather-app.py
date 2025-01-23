# Import for the necessary libraries
import tkinter as tk
import requests
from tkinter import messagebox

# Define the WeatherApp class
class WeatherApp:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        master.title("Weather Information")
        master.geometry("400x500")

        # City Input
        self.city_label = tk.Label(master, text="Enter City Name:")
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(master, width=30)
        self.city_entry.pack(pady=5)

        # Search Button
        self.search_button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.search_button.pack(pady=10)

        # Weather Information Display
        self.weather_frame = tk.Frame(master)
        self.weather_frame.pack(pady=20)

        # Labels for weather details
        self.temp_label = tk.Label(self.weather_frame, text="", font=("Arial", 12))
        self.temp_label.pack()

        self.desc_label = tk.Label(self.weather_frame, text="", font=("Arial", 10))
        self.desc_label.pack()

        self.pressure_label = tk.Label(self.weather_frame, text="", font=("Arial", 10))
        self.pressure_label.pack()

        self.humidity_label = tk.Label(self.weather_frame, text="", font=("Arial", 10))
        self.humidity_label.pack()

    def get_weather(self):
        # Get the city name from the entry widget
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return

        # Define the API key and URL
        api_key = '10239cd5e130220a7e977787afaeaa1b'
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        complete_url = base_url + 'q=' + city + '&appid=' + api_key + '&units=metric'

        try:
            # Make the API request
            response = requests.get(complete_url)
            data = response.json()

            if data['cod'] != '404':
                # Extract weather data
                main = data['main']
                weather = data['weather'][0]
                
                # Update labels with weather data
                self.temp_label.config(text=f"Temperature: {main['temp']}°C")
                self.desc_label.config(text=f"Description: {weather['description']}")
                self.pressure_label.config(text=f"Pressure: {main['pressure']} hPa")
                self.humidity_label.config(text=f"Humidity: {main['humidity']}%")
            else:
                messagebox.showerror("Error", "City not found")
        except requests.RequestException:
            messagebox.showerror("Error", "Network error. Check your connection.")
        except KeyError:
            messagebox.showerror("Error", "Unable to retrieve weather information")

# Define the main function to run the application
def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
    
    
    
