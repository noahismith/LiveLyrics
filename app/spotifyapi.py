import json
import requests
import base64
import urllib

#  Client Keys
CLIENT_ID = "91893049176646de8ec8994ea5cd0b27"
CLIENT_SECRET = "9ff3c3b4f73b4420b4243f354cb1a525"

# URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Authorization parameters
# TODO: assign CLIENT_SIDE_URL based on config file
CLIENT_SIDE_URL = "http://127.0.0.1:5000"
REDIRECT_URI = CLIENT_SIDE_URL + "/"
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
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}
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
