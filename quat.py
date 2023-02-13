import bpy
from math import *
from mathutils import *
# Variable for currently active object
myobj = bpy.context.object

# Clear all previous animation data amd set rotation mode
myobj.animation_data_clear()
myobj.rotation_mode = 'QUATERNION'

# set first and last frame index
total_time = 25
fps = 24
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 600 # total_time*fps=total_frames
I = Matrix(((0.5,0,0),(0,2,0),(0,0,4)))
omega=Vector((0.01, 1, 0))
q=Quaternion((1, 0, 0, 0))
h=0.01
# loop of frames and insert keyframes at every frame
nlast = bpy.context.scene.frame_end
for n in range(nlast):
    t = total_time*n/nlast

    # Set frame like this
    bpy.context.scene.frame_set(n)

    # Get quaternion, take ten steps with this loop
    for step in range(10):
        eulers=I.inverted()@(omega.cross(I@omega))
        omega=omega-h*eulers
        qexp=Quaternion(h*omega)
        q=q@qexp

    # Set quaternion for rotation
    myobj.rotation_quaternion=q

    # Insert new keyframe for rotation
    myobj.keyframe_insert(data_path="rotation_quaternion")