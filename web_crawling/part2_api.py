import requests
import json

city = "Seoul"
API = "b22f3d8da2533174d1ad7a988ffa8bc4"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)
print(data)

print("---------------------------")

print(data["name"], "의 날씨 입니다.")
print("날씨는", data["weather"][0]["description"], "입니다.")
print("현재 온도는", data["main"]["temp"], "입니다.")
print("하지만 체감", data["main"]["feels_like"], "일 거에요.")
print("최저 기온은", data["main"]["temp_min"], "입니다.")
print("최고 기온은", data["main"]["temp_max"], "입니다.")
print("습도는", data["main"]["humidity"], "입니다.")
print("기압은", data["main"]["pressure"], "입니다.")
print("풍향은", data["wind"]["deg"], "입니다.")
print("풍속은", data["wind"]["speed"], "입니다.")
