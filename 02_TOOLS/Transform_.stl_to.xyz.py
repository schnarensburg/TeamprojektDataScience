import numpy as np
import stl
from stl import mesh
import os

##<<<<<<< Updated upstream
##=======
script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, "../01_DATA/Z19/PointClouds/cutZ19.stl")

script_dir = os.path.dirname(os.path.abspath(__file__))
outpath = os.path.join(script_dir, "../01_DATA/Z19/PointClouds/cutCAD_Z19.xyz")

#>>>>>>> Stashed changes
#Load the STL file and create a mesh object
stl_file = stl.mesh.Mesh.from_file(filepath)

#Extract vertices of the mesh as a numpy array
vertices = stl_file.vectors.reshape((-1, 3))

#Save the vertex coordinates as an XYZ file
np.savetxt(outpath, vertices, fmt='%f', delimiter=' ')
