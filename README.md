# limmy_blender_video

This a `python script` / `.blend` that creates a version of a Limmy video using an image and a song.
Example: https://youtu.be/SiC2qVCB98s

![Example still](example_still.jpg?raw=true "Example still")

To run, first download [yt5s.com-Limmy's Show - Benny Harvey R.I.P. (4K Remaster)-(1080p).mp4`](https://yt5s.com/en87?q=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DRQzmTrlc4wA)
(md5=b3b172b7eb77db9f4592c8d79c47c257)

Then overwrite `limmy_tshirt.jpeg` and `limmy_song.m4a`
with a square-ish `jpeg` and an `m4a`
(`m4a` is the audio from an `mp4`;
it sometimes has the extension `.mp4` but it's the same so you can just rename it `.m4a`).

Then run this (tested with Blender 3.0.0):

```blender --factory-startup -b limmy.blend -P limmy.py -x 1 -o //limmy_ -a -- -v 0.5 -a1 10 -a2 10```

* `-x 1` = use extension
* `-o //limmy_` = output name
* `-a` = render all frames
* `--` = everything after this is an argument to `limmy.py`
* `-v 0.5` = volume 50%
* `-a1 10` = add 10 frames before fist pump, to time the video with the music
* `-a2 10` = add 10 frames after fist pump, to time the video with the music

See https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html for all Blender command line options.
