from libcpp.memory cimport shared_ptr

cdef extern from "impl/solvers/ScipBackend.h":
    cdef cppclass SolverBackend:
        pass

    cdef cppclass ScipBackend(SolverBackend):
        pass

cdef shared_ptr[SolverBackend] create_scip_backend()
