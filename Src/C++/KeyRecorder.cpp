#include <Python.h>

/* Execute func(x, y) in the Python interpreter. The
arguments and return result of the function must
be Python floats */


int main() {};
double call_func(PyObject* func, double x, double y)
{
	PyObject* args;
	PyObject* kwargs;
	PyObject* result = 0;
	double retval;

	// Make sure we own the GIL
	PyGILState_STATE state = PyGILState_Ensure();


	// Verify that func is a proper callable
	if (!PyCallable_Check(func))
	{
		fprintf(stderr, "call_func: expected a callable\n");
		goto fail;
	}

	// Step3
	args = Py_BuildValue("(dd)", x, y);
	kwargs = NULL;

	// Step 4
	result = PyObject_Call(func, args, kwargs);
	Py_DECREF(args);
	Py_XDECREF(kwargs);

	// Step 5
	if (PyErr_Occurred())
	{
		PyErr_Print();
		goto fail;
	}

	// Verify the result is a float object
	if (!PyFloat_Check(result))
	{
		fprintf(stderr, "call_func: callable didn't return a float\n");
		goto fail;
	}

	// Step 6
	retval = PyFloat_AsDouble(result);
	Py_DECREF(result);

	// Step 7
	PyGILState_Release(state);
	return retval;
fail:
	Py_XDECREF(result);
	PyGILState_Release(state);
	abort();
}

static PyMethodDef superfastcode_methods[] = {
    // The first property is the name exposed to Python, fast_tanh, the second is the C++
    // function name that contains the implementation.
    { "fast_tanh", (PyCFunction)calloc, METH_VARARGS, nullptr },

    // Terminate the array with an object containing nulls.
    { nullptr, nullptr, 0, nullptr }
};

static PyModuleDef superfastcode_module = {
	PyModuleDef_HEAD_INIT,
	"superfastcode",                        // Module name to use with Python import statements
	"Provides some functions, but faster",  // Module description
	0,
	superfastcode_methods                   // Structure that defines the methods of the module
};

PyMODINIT_FUNC PyInit_superfastcode() {
	return PyModule_Create(&superfastcode_module);
}

