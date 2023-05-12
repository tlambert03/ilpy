# Installation

```bash
conda create -n ilpy -c conda-forge -c gurobi -c funkelab ilpy
```

This will install ``ilpy`` with all required dependencies, including binaries
for two discrete optimizers:

1. The `Gurobi Optimizer <https://www.gurobi.com/>`_. This is a comercial
   solver, which requires a valid license. Academic licenses are provided for
   free, see `here
   <https://www.gurobi.com/academia/academic-program-and-licenses/>`_ for how
   to obtain one.

2. The `SCIP Optimizer <https://www.scipopt.org/>`_, a free and open source
   solver. If ``ilpy`` does not find a valid Gurobi license, it will fall
   back to using SCIP.

## Do I have to use ``conda``?

Kinda, mostly because ``Gurobi`` and ``Scip`` are easily installed via
``conda``.

It is possible to not use ``conda``: If you have SCIP or Gurobi installed
otherwise, you can compile ``ilpy`` yourself from the PyPI repository (``pip
install ilpy``).  But wheels for ``ilpy`` are not currently provided on PyPI.
