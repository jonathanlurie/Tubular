"""
The MIT License (MIT)

Copyright (c) 2015 Jonathan Lurie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import os

import pafy



class PafyWrapper:

    _currentTrackTitle = None
    _currentTrackDuration = None
    _currentTrackID = None

    # used when audio part only is fetched
    _forceToMp3 = False

    # TODO : convert to mp3 not available yet
    def __init__(self, forceMp3=False):
        self._forceToMp3 = forceMp3


    # Download a video in its best quality.
    # arg audio = True : download only the best quality audio
    def _download(self, video, audio=False, path=""):

        if(audio):
            stream = video.getbestaudio(preftype="mp3", ftypestrict=False)
        else:
            stream = video.getbest(preftype="mp4")

        #stream.quality
        #stream.extension
        #stream.get_filesize()
        self.printCurrentTrackInfo()
        stream.download(quiet=True, filepath=path, callback=self._progressCallback)
        print("DONE\n")

    def printCurrentTrackInfo(self):
        print("[" + self._currentTrackDuration.encode('utf-8').strip() + "] [ID: " + self._currentTrackID.encode('utf-8').strip() + "] " + self._currentTrackTitle.encode('utf-8').strip())
        #print("[" + self._currentTrackDuration + "] [ID: " + self._currentTrackID + "] " + self._currentTrackTitle)


    # callback used for stream.download
    def _progressCallback(self, bytesTotal, bytesReceived, percentProgress, kBRate, remainingSeconds):
        None
        #print(bytesTotal)
        #print(bytesReceived)
        #print(percentProgress)
        #print(kBRate)
        #print(remainingSeconds)
        #print("")


    # download a single Youtube track
    # arg audio=True : download only the audio
    # arg path : folder to download. Default is on current dir
    def downloadTrack(self, trackID, audio=False, path=""):

        track = pafy.new(trackID)

        # get some info about the current track
        self._currentTrackTitle = track.title
        self._currentTrackDuration = track.duration
        self._currentTrackID = track.videoid

        #print vid.keywords
        self._download(track, audio=audio, path=path)



    # download all track from a Youtube playlist
    # arg audio=True : download only the audio
    # arg path : folder to download. Default is on current dir
    def downloadPlaylist(self, playlistID, audio=False, path=""):

        playlist = pafy.get_playlist(playlistID)


        for item in playlist['items']:
            meta = item['playlist_meta']

            # get some info about the current track
            self._currentTrackTitle = meta["title"]
            self._currentTrackDuration = meta["duration"]
            self._currentTrackID = meta["encrypted_id"]

            self._download(item['pafy'], audio=audio, path=path)





if __name__ == '__main__':

    pw = PafyWrapper()
    pw.downloadTrack("x2AOjb9HW2E", path="tracks/", audio=True)
    pw.downloadPlaylist("https://www.youtube.com/watch?v=crZEforiKp0&list=RDcrZEforiKp0#t=1" , path="tracks/", audio=True)
