# import requests

# def get_weather(city):
#     api_key = '10239cd5e130220a7e977787afaeaa1b'  # Replace with your OpenWeatherMap API key
#     base_url = 'http://api.openweathermap.org/data/2.5/weather?'
#     complete_url = base_url + 'q=' + city + '&appid=' + api_key + '&units=metric'
    
#     response = requests.get(complete_url)
#     data = response.json()
    
#     if data['cod'] != '404':
#         main = data['main']
#         weather = data['weather'][0]
#         temperature = main['temp']
#         pressure = main['pressure']
#         humidity = main['humidity']
#         description = weather['description']
        
#         print(f"Temperature: {temperature}°C")
#         print(f"Pressure: {pressure} hPa")
#         print(f"Humidity: {humidity}%")
#         print(f"Weather description: {description}")
#     else:
#         print("City not found.")

# if __name__ == "__main__":
#     city = input("Enter city name: ")
#     get_weather(city)


import tkinter as tk
import requests
from tkinter import messagebox

class WeatherApp:
    def __init__(self, master):
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
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return

        api_key = '10239cd5e130220a7e977787afaeaa1b'
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        complete_url = base_url + 'q=' + city + '&appid=' + api_key + '&units=metric'

        try:
            response = requests.get(complete_url)
            data = response.json()

            if data['cod'] != '404':
                main = data['main']
                weather = data['weather'][0]
                
                # Update labels
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

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()