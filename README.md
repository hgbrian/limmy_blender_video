# limmy_blender_video

To run first overwrite `limmy_tshirt.jpeg` and `limmy_song.m4a`

```blender --factory-startup -b limmy.blend -P limmy.py -x 1 -o //limmy_ -a -- -v 0.5 -a1 10 -a2 10```

* `-x 1` = use extension
* `-o //limmy_` = output name
* `--` = everything after this is an argument to limmy.py
* `-v 0.5` = volume 50%
* `-a1 10` = add 10 frames before fist pump, to time the video with the music
* `-a2 10` = add 10 frames after fist pump, to time the video with the music

See https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html for all Blender command line options.
