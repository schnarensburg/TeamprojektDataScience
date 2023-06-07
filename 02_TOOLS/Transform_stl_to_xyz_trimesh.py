import trimesh
import os
import numpy as np


def stl_to_xyz(stl_file):
    # Load the STL file
    mesh = trimesh.load_mesh(stl_file)

    # Extract vertices from the mesh
    vertices = mesh.vertices

    # Output XYZ file path
    xyz_file = os.path.join(os.path.dirname(stl_file), os.path.splitext(os.path.basename(stl_file))[0] + '.xyz')

    # Save vertices to XYZ file
    np.savetxt(xyz_file, vertices, delimiter=' ', fmt='%.6f')
    print(f"XYZ file saved: {xyz_file}")

# Usage example
stl_file_path = '/Users/aaronneumann/Documents/GitHub/TeamprojektDataScience/01_DATA/Z13/PointClouds/cutCAD_Z13.xyz'
stl_to_xyz(stl_file_path)
