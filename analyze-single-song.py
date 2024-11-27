import requests

# Your access token
ACCESS_TOKEN = "BQAUPZg3SoOideXu5F9QlBCll3vLhDyv6lsrThudO_6H8kidCowOcsXlOTAFAX2zc6fJq8vOFJGsZ9W7h_5DDJR3OH8guuV7SyXXn-6txDbeyuabkEM"
TRACK_ID = "spotify_track_id"

# Spotify Audio Analysis API URL
url = f"https://api.spotify.com/v1/audio-analysis/{TRACK_ID}"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url, headers=headers)
audio_analysis = response.json()

# Extracting the bars, beats, and tatums data
bars = audio_analysis['bars']
beats = audio_analysis['beats']
tatums = audio_analysis['tatums']

# Print some bars, beats, and tatums data
print("Bars:", bars)
print("Beats:", beats)
print("Tatums:", tatums)
