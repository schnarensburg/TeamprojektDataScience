import numpy as np
from stl import mesh

##<<<<<<< Updated upstream
##=======
filepath = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z19/PointClouds/cutZ19.stl'
outpath = '/Users/aarongrommes/Library/CloudStorage/OneDrive-Persönlich/Studies/Semester 6/Teamprojekt/TeamprojektDataScience/TeamprojektDataScience/01_DATA/Z19/PointClouds/cutCADZ19.xyz'
#>>>>>>> Stashed changes
#Load the STL file and create a mesh object
stl_file = mesh.Mesh.from_file(filepath)

#Extract vertices of the mesh as a numpy array
vertices = stl_file.vectors.reshape((-1, 3))

#Save the vertex coordinates as an XYZ file
np.savetxt(outpath, vertices, fmt='%f', delimiter=' ')
