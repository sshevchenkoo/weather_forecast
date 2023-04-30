import requests

API_key = "8808628127260ef18ffbeaba46ae68da"
def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    nr_values = 8 * forecast_days
    filter_data = filter_data[:nr_values]
    return filter_data

