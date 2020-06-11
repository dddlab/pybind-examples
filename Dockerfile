FROM jupyter/scipy-notebook:dc57157d6316

RUN wget https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.zip && \
    unzip eigen-3.3.7.zip && \
    rm eigen-3.3.7.zip && \
    pip install pybind11
    
RUN pip install cppimport
 
