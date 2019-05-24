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
 * print_python_string - prints python string
 * @p: PyObject
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	char *s = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	length = PyUnicode_GET_LENGTH(p);
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		s = "compact ascii";
	}
	else
	{
		s = "compact unicode object";
	}
	printf("  type: %s\n", s);
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}
