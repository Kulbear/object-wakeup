try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension
import numpy


# Get the numpy include directory.
numpy_include_dir = numpy.get_include()

# Extensions
# pykdtree (kd tree)
pykdtree = Extension(
    'main.utils.libkdtree.pykdtree.kdtree',
    sources=[
        'main/utils/libkdtree/pykdtree/kdtree.c',
        'main/utils/libkdtree/pykdtree/_kdtree_core.c'
    ],
    language='c',
    extra_compile_args=['-std=c99', '-O3', '-fopenmp'],
    extra_link_args=['-lgomp'],
)

# mcubes (marching cubes algorithm)
mcubes_module = Extension(
    'main.utils.libmcubes.mcubes',
    sources=[
        'main/utils/libmcubes/mcubes.pyx',
        'main/utils/libmcubes/pywrapper.cpp',
        'main/utils/libmcubes/marchingcubes.cpp'
    ],
    language='c++',
    extra_compile_args=['-std=c++11'],
    include_dirs=[numpy_include_dir]
)

# triangle hash (efficient mesh intersection)
triangle_hash_module = Extension(
    'main.utils.libmesh.triangle_hash',
    sources=[
        'main/utils/libmesh/triangle_hash.pyx'
    ],
    libraries=['m']  # Unix-like specific
)

# mise (efficient mesh extraction)
mise_module = Extension(
    'main.utils.libmise.mise',
    sources=[
        'main/utils/libmise/mise.pyx'
    ],
)

# simplify (efficient mesh simplification)
simplify_mesh_module = Extension(
    'main.utils.libsimplify.simplify_mesh',
    sources=[
        'main/utils/libsimplify/simplify_mesh.pyx'
    ]
)

# voxelization (efficient mesh voxelization)
voxelize_module = Extension(
    'main.utils.libvoxelize.voxelize',
    sources=[
        'main/utils/libvoxelize/voxelize.pyx'
    ],
    libraries=['m']  # Unix-like specific
)

# DMC extensions
dmc_pred2mesh_module = CppExtension(
    'main.dmc.ops.cpp_modules.pred2mesh',
    sources=[
        'main/dmc/ops/cpp_modules/pred_to_mesh_.cpp',
    ]   
)

dmc_cuda_module = CUDAExtension(
    'main.dmc.ops._cuda_ext',
    sources=[
        'main/dmc/ops/src/extension.cpp',
        'main/dmc/ops/src/curvature_constraint_kernel.cu',
        'main/dmc/ops/src/grid_pooling_kernel.cu',
        'main/dmc/ops/src/occupancy_to_topology_kernel.cu',
        'main/dmc/ops/src/occupancy_connectivity_kernel.cu',
        'main/dmc/ops/src/point_triangle_distance_kernel.cu',
    ]
)

# Gather all extension modules
ext_modules = [
    pykdtree,
    mcubes_module,
    triangle_hash_module,
    mise_module,
    simplify_mesh_module,
    voxelize_module,
    dmc_pred2mesh_module,
    dmc_cuda_module,
]

setup(
    ext_modules=cythonize(ext_modules),
    cmdclass={
        'build_ext': BuildExtension
    }
)
