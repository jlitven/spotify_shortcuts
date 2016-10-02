"""Script to add a track to your Spotify music collection"""
import sys
import spotipy
import spotipy.util as util

SCOPE = 'user-library-modify'
USERNAME = 'your_username_goes_here'
SPOTIPY_CLIENT_ID = 'your_client_id_goes_here'
SPOTIPY_SECRET = 'your_secret_id_goes_here'
SPOTIPY_REDIRECT_URI = 'your_redirect_id_goes_here'

def get_user_token():
    """Get the token for the given user and scope"""
    token = util.prompt_for_user_token(username=USERNAME,
                                       scope=SCOPE,
                                       client_id=SPOTIPY_CLIENT_ID,
                                       client_secret=SPOTIPY_SECRET,
                                       redirect_uri=SPOTIPY_REDIRECT_URI)
    return token

def add_track_to_saved_tracks(track_uri):
    """Add the track to the current user's collection"""
    token = get_user_token()
    spotify = spotipy.Spotify(auth=token)
    print 'Adding track {} to collection...'.format(track_uri)
    spotify.current_user_saved_tracks_add([track_uri])

def main():
    """Get the track uri from stdin and add to saved tracks"""
    if len(sys.argv) > 1:
        track_uri = sys.argv[1]
    else:
        print "Usage: %s track_uri" % (sys.argv[0])
        sys.exit()

    add_track_to_saved_tracks(track_uri)

if __name__ == '__main__':
    main()
