import json
import requests
import base64
import urllib

#  Client Keys
CLIENT_ID = "7ba9cd74b12549a380a2c3e11ec093c7"
CLIENT_SECRET = "9160980bb1fa4be9bb5275247304229b"

# URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Authorization parameters
# TODO: assign CLIENT_SIDE_URL based on config file
CLIENT_SIDE_URL = "http://18.188.140.44"
REDIRECT_URI = CLIENT_SIDE_URL + "/login"
SCOPE = "streaming user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-email user-read-birthdate"
STATE = ""
SHOW_DIALOG = "false"

auth_query_parameters = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    # "state": STATE,
    "scope": SCOPE,
    "show_dialog": SHOW_DIALOG,
}


def get_tokens(auth_token):
    payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }
    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))
    headers = {"Authorization": "Basic {}".format(base64encoded)}
    post_response = requests.post(SPOTIFY_TOKEN_URL, data=payload, headers=headers)
    return json.loads(post_response.text)


def get_profile_me(access_token):
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}
    api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    try:
        resp = requests.get(api_endpoint, headers=authorization_header)
    except requests.exeptions.RequestException as e:
        return {"error": e}
    return json.loads(resp.text)


def search_track(access_token, search_string):
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}
    api_endpoint = "{}/search?q={}&type=track&limit=10".format(SPOTIFY_API_URL, search_string.replace(" ", "+"))
    try:
        resp = requests.get(api_endpoint, headers=authorization_header)
    except requests.exeptions.RequestException as e:
        return {"error": e}
    return json.loads(resp.text)


def search_artist(access_token, search_string):
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}
    api_endpoint = "{}/search?q={}&type=artist&limit=10".format(SPOTIFY_API_URL, search_string.replace(" ", "+"))
    try:
        resp = requests.get(api_endpoint, headers=authorization_header)
    except requests.exeptions.RequestException as e:
        return {"error": e}
    return json.loads(resp.text)


def get_track(access_token, track_id):
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}
    api_endpoint = "{}/tracks/{}".format(SPOTIFY_API_URL, track_id)
    track_object = requests.get(api_endpoint, headers=authorization_header)
    return json.loads(track_object.text)


def get_artists_by_track(track):
    artists = track['artists']
    artists_list = []

    for artist in artists:
        artists_list.append(artist['name'])

    return ", ".join(artists_list)


def get_current_track(access_token):
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}
    api_endpoint = "{}/me/player/currently-playing".format(SPOTIFY_API_URL)
    try:
        current_playing_object = requests.get(api_endpoint, headers=authorization_header)
    except requests.exeptions.RequestException as e:
        return {"error": e}

    if current_playing_object.status_code == 204 or 200:
        return {"error": {"message": "NO CONTENT"}}

    return json.loads(current_playing_object.text)


def get_auth_url():
    url_args = "&".join(["{}={}".format(key, urllib.quote(val)) for key, val in auth_query_parameters.iteritems()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return auth_url
