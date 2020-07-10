from googleapiclient.discovery import build
import requests

api_key = "AIzaSyAthkU8lXJc0nHLv_HSOeQR8XiVAYPz0xE"
channel_id = "UCCezIgC97PvUuR4_gbFUs5g"
lists_id= "PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p"

youtube = build("youtube", "v3", developerKey=api_key)

# request = youtube.playlistItems().list(
#     part='contentDetails,snippet,status',
#     playlistId=lists_id
# )

# response = request.execute()
# nextPageToken = response.get('nextPageToken')
# while 'nextPageToken' in response :
#     nextPage = youtube.playlistItems().list(
#         part="contentDetails",
#         playlistId=lists_id,
#         pageToken=nextPageToken
#     ).execute()
#     response['items'] = response['items'] + nextPage['items']
#     if 'nextPageToken' not in nextPage:
#         response.pop('nextPageToken',None)
#     else:
#         nextPageToken = nextPage['nextPageToken']

# #response = "type of ..."
# # r = requests.

# #print(response)
# print()
# for item in response['items']:
#     print(item)
#     print(len(response['items']))

nextPageToken = None
response = None
i = 0
while True :
    nextPage = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=lists_id,
        pageToken=nextPageToken,
        maxResults=50
    ).execute()
    i += 1
    print(i,list(nextPage))
    if response is None :
        response = nextPage['items']
    else:
        response = response + nextPage['items']
    if 'nextPageToken' not in nextPage:
        break
    else:
        nextPageToken = nextPage['nextPageToken']

#response = "type of ..."
# r = requests.

#print(response)
print()
for item in response:
    print(item)
    print(len(response))
