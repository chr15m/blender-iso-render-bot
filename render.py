import os
import sys
import math

import bpy
from mathutils import Vector, Euler, Matrix, Quaternion
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--scale", help="Scale tiles by some percentage.", default=100, type=int)
parser.add_argument("--dest", help="Folder to output renders into.", default=os.path.dirname(bpy.data.filepath))

args = parser.parse_args(sys.argv[5:])

for scene in bpy.data.scenes:
    scene.render.resolution_percentage = args.scale
    #scene.render.resolution_x = 128
    #scene.render.resolution_y = 256
    #scene.render.use_border = False

bpy.ops.object.select_all(action='DESELECT')

cam = bpy.data.objects["Camera"]

bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
cursor_loc = bpy.context.scene.cursor_location

print("Destination folder:", args.dest)

for x in range(4):
    bpy.data.scenes["Scene"].render.filepath = os.path.join(args.dest, bpy.path.basename(bpy.data.filepath).replace(".blend", "-%d.png") % x)
    bpy.ops.render.render(write_still=True)
    
    mat = (Matrix.Translation(cursor_loc) * Matrix.Rotation(math.pi / 2.0, 4, 'Z') * Matrix.Translation(-cursor_loc))
    cam.matrix_world = mat * cam.matrix_world

sys.exit()
