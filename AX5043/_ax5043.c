
#include <Python.h>
#include "AX5043_SPI.h"
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

static char module_docstring[] =
    "This module provides an interface for AX5043 Antenna.";

static char ax5043_write_docstring[] = 
    "Write packets to AX_REG_FIFODATA register.";

static PyObject *ax5043_ax5043_write(PyObject *self, PyObject *args);


static PyMethodDef module_methods[] = {
    {"write_reg", ax5043_ax5043_write, METH_VARARGS, ax5043_write_docstring},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC PyInit__ax5043(void)
{
    PyObject *module;
    static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "_ax5043",
        module_docstring,
        -1,
        module_methods,
        NULL,
        NULL,
        NULL,
        NULL
    };
    module = PyModule_Create(&moduledef);
    if (!module) return NULL;

    return module;
}

static PyObject *ax5043_ax5043_write(PyObject *self, PyObject *args){
    unsigned char value;
     if (!PyArg_ParseTuple(args, "B", &value))
        return NULL;
    ax5043_write(value);

    PyObject *ret = Py_BuildValue("B", value);
    return ret;
}

