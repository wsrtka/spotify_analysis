"""Module for extracting Spotify data."""

import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def authenticate():
    """Authenticate to Spotify API.

    Returns:
        spotipy.Spotify: Spotify API w
    """
    client_id = os.environ.get("SPOTIPY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")

    credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    spoti = spotipy.Spotify(client_credentials_manager=credentials_manager)
    return spoti


if __name__ == "__main__":
    authenticate()
