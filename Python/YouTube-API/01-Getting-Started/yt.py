from googleapiclient.discovery import build
import requests

api_key = "AIzaSyAthkU8lXJc0nHLv_HSOeQR8XiVAYPz0xE"

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.channels().list(part="contentOwnerDetails", forUsername="schafer5")

response = request.execute()
# r = requests.

print(response)
