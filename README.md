# Tubular

Tubular is made to help you download music and video from Youtube.

## How to use
The file `tubular.sh` is double-clickable and will launch this interface.  

![](https://www.dropbox.com/s/wwly8xbo4fydrhx/tubular.png?dl=0&raw=1)

Then you chose if you want to download a single track, of a entire playlist. In both case, an ID is necessary: 

> The track at https://www.youtube.com/watch?v=**crZEforiKp0** has the ID **crZEforiKp0**

> The playlist at 
> https://www.youtube.com/watch?v=1E2OZTRmNxk&list=**PLK6CFF5XENOmeKZ4LtrU9CuUyHqsMc9Dl** has the ID **PLK6CFF5XENOmeKZ4LtrU9CuUyHqsMc9Dl**

Finally, you can tick the **Audio** checkbox if you want to download the audio track only. I noticed that the m4a files downloaded are not compatible with all audio player, but work fine with VLC (which was not really made to be an audio player but is compatible with a lot of formats).

*Note :*  the console output might be not really reactive as long as the download is in progress.

This project is based on [Pafy](https://github.com/np1/pafy) for everything related to Youtube and on  [BLANK_GOOEY](https://github.com/jonathanlurie/BLANK_GOOEY) for the GUI.  

## Licence

MIT, see LICENCE.txt for more info