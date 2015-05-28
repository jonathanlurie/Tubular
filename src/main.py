import sys
import argparse

from gooey import Gooey, GooeyParser

from SettingFileReader import *

from PafyWrapper import *


@Gooey(advanced=True , show_config=True, program_name='Tubular', default_size=(500, 600), required_cols=1, optional_cols=1, dump_build_config=False )

def main():

    # get some settings from setting file
    settings = SettingFileReader()
    defaultOutput = settings.getSetting("defaultSettings", "output")
    defaultWidth = settings.getSetting("defaultSettings", "width")
    defaultFramerate = settings.getSetting("defaultSettings", "framerate")
    defaultBitrateKb = settings.getSetting("defaultSettings", "bitratekb")



    description = "Download tracks and playlists from Youtube."

    #parser = argparse.ArgumentParser(description=description)
    parser = GooeyParser(description=description)

    parser.add_argument('-output', required=True, help='Folder to save the tracks' , widget="DirChooser")

    parser.add_argument('-track', required=False, default=None, help='Youtube track ID' )
    parser.add_argument('-playlist', required=False, default=None, help='Youtube playlist ID' )
    parser.add_argument('-audio', action="store_true", default=False, help="Download only the audio part (usualy m4a format)")

    args = parser.parse_args()


    # the user must have chosen between a track and a Playlist.
    # Though none of them is mandatory, so we have to check.
    if(not args.track and not args.playlist):
        print("[ERROR] You must fill at least one of those fields:\n\t- Track - to download a single track\n\t- Playlist - to download a entire playlist")


    else:
        pw = PafyWrapper()

        # download a track
        if(args.track):
            try:
                pw.downloadTrack(args.track, path=args.output, audio=args.audio)
            except ValueError as e:
                print("[INVALID URL]" + e)

        if(args.playlist):
            #try:
            print(args.playlist)
            pw.downloadPlaylist(args.playlist,  path=args.output, audio=args.audio)
            #    print("DEBUG01")
            #except ValueError as e:
            #    print("[INVALID URL]" + e)










if __name__ == '__main__':

    # gives priority to local libs
    sys.path.insert(0, "./lib/python")

    main()
