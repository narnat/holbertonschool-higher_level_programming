#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <pymacro.h>
#include <floatobject.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <assert.h>
#include <stdlib.h>
#include <bytesobject.h>
#include <float.h>

/**
 * print_python_float - prints basic info about float object
 * @p: PyObject
 * Return: Nothing
 */
void print_python_float(PyObject *p)
{
	double d = ((PyFloatObject *)(p))->ob_fval;
	char *s1;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	s1 = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s1);
	fflush(stdout);
}


/**
 * print_python_bytes - Print python list info
 * @p: PyObject
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	/* PyBytesObject *obj = (PyBytesObject *)p; */
	char *str = NULL;
	int size = 0, i = 0, max;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	str = ((PyBytesObject *)p)->ob_sval;
	size = PyBytes_Size(p);
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	max  = size + 1;
	if (max > 10)
		max = 10;
	printf("  first %i bytes: ", max);
	for (i = 0; i < max; i++)
	{
		if (i != max - 1)
			printf("%02hhx ", str[i]);
		else
			printf("%02hhx\n", str[i]);
	}
	fflush(stdout);
}

/**
 * print_python_list - Print python list info
 * @p: PyObject
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	ssize_t a = 0;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}
	printf("[*] Size of the Python List = %ld\n", PyList_GET_SIZE(p));
	printf("[*] Allocated = %ld\n", obj->allocated);
	for (; a < PyList_GET_SIZE(p); a++)
	{
		printf("Element %ld: %s\n", a, (obj->ob_item[a])->ob_type->tp_name);
		if (strcmp((obj->ob_item[a])->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(obj->ob_item[a]);
		if (strcmp((obj->ob_item[a])->ob_type->tp_name, "float") == 0)
			print_python_float(obj->ob_item[a]);
	}
	fflush(stdout);
}
