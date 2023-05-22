from stl import mesh
import numpy as np
import os

##<<<<<<< Updated upstream
##=======
script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, "../01_DATA/Z13/PointClouds/cutZ13.stl")

script_dir = os.path.dirname(os.path.abspath(__file__))
outpath = os.path.join(script_dir, "../01_DATA/Z13/PointClouds/cutCAD_Z13.xyz")

#>>>>>>> Stashed changes
#Load the STL file and create a mesh object
stl_file = mesh.Mesh.from_file(filepath)

#Extract vertices of the mesh as a numpy array
vertices = stl_file.vectors.reshape((-1, 3))

#Save the vertex coordinates as an XYZ file
np.savetxt(outpath, vertices, fmt='%f', delimiter=' ')
