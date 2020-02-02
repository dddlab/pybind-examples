

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

double square(double x) {
    return x * x;
}

PYBIND11_MODULE(code, m) {
    m.def("square", py::vectorize(square));
}
