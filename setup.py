import os
from ctypes import util

from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension

# enable test coverage tracing if CYTHON_TRACE is set to a non-zero value
CYTHON_TRACE = int(os.getenv("CYTHON_TRACE") in ("1", "True"))
DO_SCIP = True
DO_GUROBI = True

include_dirs = ["ilpy/impl"]
library_dirs = []
compile_args = ["-O3"]
modules = []
define_macros=[("CYTHON_TRACE", CYTHON_TRACE)]
if os.name == "nt":
    compile_args.append("/std:c++17")
else:
    compile_args.append("-std=c++17")

# include conda environment windows include/lib if it exists
# this will be done automatically by conda build, but is useful if someone
# tries to build this directly with pip install in a conda environment
if os.name == "nt" and "CONDA_PREFIX" in os.environ:
    include_dirs.append(os.path.join(os.environ["CONDA_PREFIX"], "Library", "include"))
    library_dirs.append(os.path.join(os.environ["CONDA_PREFIX"], "Library", "lib"))

if DO_SCIP:
    scip_wrapper = Extension(
        "ilpy.scip_wrap",
        sources=["ilpy/scip_wrap.pyx"],
        libraries=["libscip"] if os.name == "nt" else ["scip"],
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        language="c++",
        extra_compile_args=[*compile_args, "-DHAVE_SCIP"],
        define_macros=define_macros
    )
    modules.append(scip_wrapper)

# look for various gurobi versions, which are annoyingly
# suffixed with the version number, and wildcards don't work
if DO_GUROBI:
    for v in range(80, 200):
        gurobi_lib = f"libgurobi{v}" if os.name == "nt" else f"gurobi{v}"
        if (gurolib := util.find_library(gurobi_lib)) is not None:
            print("FOUND GUROBI library: ", gurolib)
            gurobi_wrapper = Extension(
                "ilpy.gurobi_wrap",
                sources=["ilpy/gurobi_wrap.pyx"],
                libraries=[gurobi_lib],
                include_dirs=include_dirs,
                library_dirs=library_dirs,
                language="c++",
                extra_compile_args=[*compile_args, "-DHAVE_GUROBI"],
                define_macros=define_macros
            )
            modules.append(gurobi_wrapper)
            break

    else:
        print("WARNING: GUROBI library not found")


ilpy_wrapper = Extension(
    "ilpy.wrapper",
    sources=["ilpy/wrapper.pyx"],
    extra_compile_args=compile_args,
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    language="c++",
    define_macros=define_macros,
)

modules.append(ilpy_wrapper)

setup(
    ext_modules=cythonize(
        modules,
        compiler_directives={
            "linetrace": CYTHON_TRACE,
            "language_level": "3",
        },
    )
)
