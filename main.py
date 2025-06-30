import tkinter as tk
from tkinter import messagebox
import requests
from config import API_KEY  

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            result_label.config(
                text=f"🌡 Temp: {temp}°C\n☁️ Condition: {condition}\n💧 Humidity: {humidity}%"
            )
        else:
            messagebox.showerror("Error", f"City '{city}' not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

label = tk.Label(root, text="Enter City:", font=("Arial", 12))
label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack(pady=5)

get_weather_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_weather_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=20)

root.mainloop()
