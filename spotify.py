
from os import access
import requests
import base64, json
from secrets import *


class TSpotify:
     def __init__(self, clientID, clientSecret):
          self.authUrl = "https://accounts.spotify.com/api/token"
          self.clientID = clientID
          self.clientSecret = clientSecret

     def getAccessToken(self):
          authHeader = {}
          authData = {}
          message = f"{self.clientID}:{self.clientSecret}"
          message_bytes = message.encode('ascii')
          base64_bytes = base64.b64encode(message_bytes)
          base64_message = base64_bytes.decode('ascii')

          authHeader['Authorization'] = "Basic " + base64_message
          authData['grant_type'] = "client_credentials"

          res = requests.post(self.authUrl, headers=authHeader, data=authData)
          responseObject = res.json()

          accessToken = responseObject['access_token']
          return accessToken
                      
     def 	getArtist(self, token, ID):
          endpoint = f"https://api.spotify.com/v1/artists/{ID}"

          getHeader = {
               "Authorization": "Bearer " + token
          }

          res = requests.get(endpoint, headers=getHeader)
          playlistObject = res.json()
          return playlistObject

     def getPlayList(self, token, ID):
          endpoint = f"https://api.spotify.com/v1/playlists/{ID}"

          getHeader = {
               "Authorization": "Bearer " + token
          }

          res = requests.get(endpoint, headers=getHeader)
          playlistObject = res.json()
          return playlistObject

     def getTracks(self, token, ID):
          playlistendpoint = f"https://api.spotify.com/v1/tracks/{ID}"

          getHeader = {
               "Authorization": "Bearer " + token
          }

          res = requests.get(playlistendpoint, headers=getHeader)
          playlistObject = res.json()
          return playlistObject
