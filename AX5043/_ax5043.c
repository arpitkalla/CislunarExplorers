
#include <Python.h>
#include <numpy/arrayobject.h>
#include "AX5043_SPI.h"

static char module_docstring[] =
    "This module provides an interface for AX5043 Antenna.";

static char ax5043_writeReg_docstring[] =
    "Write packets to a register.";

static PyObject *ax5043_ax5043_writeReg(PyObject *self, PyObject *args);



static PyMethodDef module_methods[] = {
    {"writeReg", ax_5043_ax5043_writeReg, METH_VARARGS, ax5043_writeReg_docstring},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC init_ax5043(void)
{
    PyObject *m = Py_InitModule3("_ax5043", module_methods, module_docstring);
    if (m == NULL)
        return;
}

static PyObject *ax5043_ax5043_writeReg(PyObject *self, PyObject *args){
    uint16_t addr;
    unsigned char value;
     if (!PyArg_ParseTuple(args, "IB", &addr, &value))
        return NULL;
    ax5043_writeReg(addr,value);



    PyObject *ret = Py_BuildValue("B", value);
    return ret;
}
