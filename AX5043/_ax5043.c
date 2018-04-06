
#include <Python.h>
#include <numpy/arrayobject.h>
#include "AX5043_SPI.h"
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

static char module_docstring[] =
    "This module provides an interface for AX5043 Antenna.";

static char ax5043_writeReg_docstring[] =
    "Write packets to a register.";

static PyObject *ax5043_writeReg(PyObject *self, PyObject *args);

static PyObject *ax5043_writeReg(PyObject *self, PyObject *args){
    uint16_t addr;
    unsigned char value;
     if (!PyArg_ParseTuple(args, "IB", &addr, &value))
        return NULL;
    ax5043_writeReg(addr,value);



    PyObject *ret = Py_BuildValue("B", value);
    return ret;
}



static PyMethodDef module_methods[] = {
    {"writeReg", ax5043_writeReg, METH_VARARGS, ax5043_writeReg_docstring},
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

    /* Load `numpy` functionality. */
    import_array();

    return module;
}

