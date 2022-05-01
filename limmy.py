import bpy
import sys
from math import floor

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print("arg")
print(argv)

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

#def print(data):
#    for window in bpy.context.window_manager.windows:
#        screen = window.screen
#        for area in screen.areas:
#            if area.type == 'CONSOLE':
#                override = {'window': window, 'screen': screen, 'area': area}
#                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")       
              
context = bpy.context
scene = context.scene
sed = scene.sequence_editor
sed.active_strip = None

# pause_scene_1 = 187
# pause_scene_2 = 146 
# end of scene = 1808

# scene.002 1, 46, 954, 1864 (-> 1141, 1677)
# scene.004 1, 46, 1146, 1672

sequences = sed.sequences_all

for strip in sequences:
    if strip.name == "limmy_song.001":
        strip.volume = volume

if add_frames["pause_scene_1"] != 0 or add_frames["pause_scene_2"] != 0:
    for active_scene in ["pause_scene_1", "pause_scene_2"]:
        for strip in sequences:
            if strip.name == active_scene:
                strip.select = True
                #print(strip)
                #print(strip.name)
                #print(dir(strip))
                #print(strip.frame_final_start)
                #print(strip.frame_final_end)
                s_end = strip.frame_final_end
                delta = add_frames[active_scene] #floor((strip.frame_final_end - strip.frame_final_start)*(multiple))

        for strip in sorted(sequences, key=lambda x: -x.frame_final_end):
            if strip.name.startswith("speed"):
                # not allowed
                continue
            
            if strip.frame_final_end == s_end:
                print("ex")
                strip.frame_final_end += add_frames[active_scene]

            if strip.frame_final_start >= s_end:
                print("move")
                print(strip.name)
                print(strip.frame_start)
                #print(dir(strip))
                strip.frame_start += add_frames[active_scene]
                #strip.frame_final_end += delta
  
scene.frame_end = bpy.context.scene.frame_end + add_frames["pause_scene_1"] + add_frames["pause_scene_2"]
