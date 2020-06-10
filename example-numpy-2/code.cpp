<%
cfg['compiler_args'] = ['-std=c++11']
setup_pybind11(cfg)
%>

// return data type 
//
// struct buffer_info {
//     void *ptr;
//     size_t itemsize;
//     std::string format;
//     int ndim;
//     std::vector<size_t> shape;
//     std::vector<size_t> strides;
// };


#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

// Passing in an array of doubles
void twice(py::array_t<double> xs) {
    py::buffer_info info = xs.request();
    auto ptr = static_cast<double *>(info.ptr);

    int n = 1;
    for (auto r: info.shape) {
      n *= r;
    }

    for (int i = 0; i <n; i++) {
        *ptr++ *= 2;
    }
}

// Passing in a generic array
double sum(py::array xs) {
    py::buffer_info info = xs.request();
    auto ptr = static_cast<double *>(info.ptr);

    int n = 1;
    for (auto r: info.shape) {
      n *= r;
    }

    double s = 0.0;
    for (int i = 0; i <n; i++) {
        s += *ptr++;
    }

    return s;
}

PYBIND11_MODULE(code, m) {
    m.def("sum", &sum);
    m.def("twice", &twice);
}

