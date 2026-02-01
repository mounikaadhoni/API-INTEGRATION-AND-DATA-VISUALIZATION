import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# API CONFIGURATION
# -----------------------------
API_KEY = "98352d5025d55042aac040aa082c7c9e"
CITY = "Hyderabad"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code != 200:
    print("API Error:", data.get("message"))
    exit()

dates = []
temperatures = []
humidity = []
wind_speed = []

for item in data.get("list", []):
    dates.append(item["dt_txt"])
    temperatures.append(item["main"]["temp"])
    humidity.append(item["main"]["humidity"])
    wind_speed.append(item["wind"]["speed"])


df = pd.DataFrame({
    "Date": pd.to_datetime(dates),
    "Temperature (°C)": temperatures,
    "Humidity (%)": humidity,
    "Wind Speed (m/s)": wind_speed
})

sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
sns.lineplot(x="Date", y="Temperature (°C)", data=df)
plt.title("Temperature Forecast")

plt.subplot(3, 1, 2)
sns.lineplot(x="Date", y="Humidity (%)", data=df)
plt.title("Humidity Forecast")

plt.subplot(3, 1, 3)
sns.lineplot(x="Date", y="Wind Speed (m/s)", data=df)
plt.title("Wind Speed Forecast")

plt.tight_layout()
plt.show()