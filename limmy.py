import bpy
import sys

def bprint(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

volume = 1
add_frames = {
    "pause_scene_1": 0,
    "pause_scene_2": 0,
}

for n in range(len(argv)):
    if argv[n] == "-v":
        volume = float(argv[n+1])
    elif argv[n] == "-a1":
        add_frames["pause_scene_1"] = int(argv[n+1])
    elif argv[n] == "-a2":
        add_frames["pause_scene_2"] = int(argv[n+1])
              
context = bpy.context
scene = context.scene
sed = scene.sequence_editor
sed.active_strip = None

sequences = sed.sequences_all

for strip in sequences:
    if strip.name == "limmy_song.001":
        strip.volume = volume

if add_frames["pause_scene_1"] != 0 or add_frames["pause_scene_2"] != 0:
    for active_scene in ["pause_scene_1", "pause_scene_2"]:
        for strip in sequences:
            if strip.name == active_scene:
                strip.select = True
                s_end = strip.frame_final_end
                delta = add_frames[active_scene]

        for strip in sorted(sequences, key=lambda x: -x.frame_final_end):
            if strip.name.startswith("speed"):
                # not allowed
                continue
            
            if strip.frame_final_end == s_end:
                strip.frame_final_end += add_frames[active_scene]

            if strip.frame_final_start >= s_end:
                strip.frame_start += add_frames[active_scene]
  
scene.frame_end = bpy.context.scene.frame_end + add_frames["pause_scene_1"] + add_frames["pause_scene_2"]
