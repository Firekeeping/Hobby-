import requests
import geocoder
import openai
from PIL import Image, ImageDraw, ImageFont
import datetime

# Get latitude and longitude
g = geocoder.ip('me')
latitude, longitude = g.latlng

# API setup to get current weather conditions
api_key = "f5670863efe47929c7d10d1cc693b9ce"
url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
data = requests.get(url).json()

# Get weather information
temperature = (data["main"]["temp"] - 273.15) * 9/5 + 32
wind_speed = data["wind"]["speed"] * 2.23694
description = data["weather"][0]["description"]

# Get the Unix time from the API and convert it to a human-readable format
unix_time = data["dt"]
time_of_day = datetime.datetime.fromtimestamp(unix_time).strftime('%I:%M %p')


# Print the information to the shell
print("Temperature: ", temperature)
print("Wind Speed: ", wind_speed)
print("Description: ", description)
print("Time of day: ", time_of_day)

# Set OpenAI API key
openai.api_key = "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"

# Use Op


# Use OpenAI API to generate an image based on the weather description and additional texts
response = openai.Image.create(
  prompt=f" {time_of_day}{description} pixel dragon ",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

# Open image using Pillow
im = Image.open(requests.get(image_url, stream=True).raw)

# Draw text on the image to display temperature, wind speed, and time information
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 20)
draw.text((5, 5), f"Temperature: {temperature:.2f}°F", (0, 0, 0), font=font)
draw.text((5, 30), f"Wind Speed: {wind_speed:.2f}mph", (0, 0, 0), font=font)
draw.text((5, 55), f"Time: {time_of_day}", (0, 0, 0), font=font)

# Display the image with the text
im.show()

