"""Module for extracting Spotify data."""

import os
import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def authenticate():
    """Authenticate to Spotify API.

    Returns:
        spotipy.Spotify: Spotify API wrapper.
    """
    client_id = os.environ.get("SPOTIPY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")

    credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    spoti = spotipy.Spotify(client_credentials_manager=credentials_manager)

    return spoti


def get_audio_analysis(spoti, uri):
    """Get audio analysis for track.

    Args:
        spoti (spotipy.Spotify): Spotify API wrapper.
        uri (str): Song URI.

    Returns:
        dict: dictionary of song features.
    """
    analysis = spoti.audio_features([uri])[0]
    result = {
        k: v
        for k, v in analysis.items()
        if k not in ["analysis_url", "id", "track_href", "type", "uri"]
    }
    return result


if __name__ == "__main__":
    sp = authenticate()
    an = get_audio_analysis(sp, "0y60itmpH0aPKsFiGxmtnh")
    pprint.pprint(an)
