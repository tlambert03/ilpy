from .scip_decl cimport ScipBackend, SolverBackend
from libcpp.memory cimport shared_ptr, make_shared
from libcpp.cast cimport static_pointer_cast

cdef shared_ptr[SolverBackend] create_scip_backend():
    return make_shared[ScipBackend]()

cdef shared_ptr[SolverBackend] create_scip_backend():
    cdef shared_ptr[ScipBackend] scip_backend = make_shared[ScipBackend]()
    return static_pointer_cast[SolverBackend](scip_backend)