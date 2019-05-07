#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - Print python list info
 * @p: PyObject
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	Py_ssize_t j = 0;
	ssize_t a = 0;
	PyListObject *obj = (PyListObject *)p;
	i = PyList_Size(p);
	j = obj->allocated;
	printf("[*] Size of the Python List = %ld\n", i);
	printf("[*] Allocated = %ld\n", j);
	for (; a < i; a++)
	{
		printf("Element %ld: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
	}
}
