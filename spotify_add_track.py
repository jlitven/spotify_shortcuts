"""Script to add a track to your Spotify music collection"""
import sys
import spotipy
import spotipy.util as util

def get_user_token(username='1212629687',  # your username here
                   scope='user-library-modify'):
    """Get the token for the given user and scope"""
    token = util.prompt_for_user_token(username, scope)
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
