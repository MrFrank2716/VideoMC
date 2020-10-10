# rottenplayer

This is a Bukkit plugin for playing videos on sheep.  It's a little janky since it's basically just an MVP, but it works surprisingly well.  There's just no way to stop a video once you've started it and you kinda still have to know what you're doing.

Here's a video of it working, with *Bad Apple!!* of course: https://youtu.be/tO6sfku_1b8

## Building

It's set up with Maven so just run `mvn package` and it'll drop the jar file in `target/`.

## Usage

Basically just read `mkbadapple.sh` and it'll explain everything you really need to know.

You have to take the video and split it into a series of frames as single images, then the `rotten.py` script uses PIL to sample a grid of pixels from every frame and dump it all into another file that you can put in the `plugins/RottenPlayer/` directory on your server.

## TODO

**In all honesty, someone else should probably do these.  I'll accept PRs, I'm just too lazy to write it myself.**

* Make it so you can stop videos.

* More output back to the player

* Play from URLs

  * If you're really feeling it then you could bundle the Python script with the jar and convert the video on the fly if ffmpeg and Python and PIL are present on the server.  Would need some limits to keep it from overloading the server.
  
* Maybe add support for playing note block sounds somehow?

* Better handling of the region that sheep spawn in

* Make it able to spawn sheep if there's not enough

  * Or instead do some event handler nonsense to encourage sheep to distribute evenly.  But don't make it too obvious.

