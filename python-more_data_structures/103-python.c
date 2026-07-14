#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyBytesObject *)p)->ob_base.ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		printf("  first 10 bytes: ");
	else
		printf("  first %ld bytes: ", size + 1);

	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i != size && i != 9)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - prints basic info about Python list objects
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	long int size, alloc, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;
	const char *type;

	size = ((PyVarObject *)p)->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}
```

This satisfies the requirements

* ✅ No `Py_SIZE` — uses `((PyVarObject *)p)->ob_size` directly instead
* ✅ No `Py_TYPE` — uses `item->ob_type->tp_name` directly instead
* ✅ No `PyList_GetItem` — accesses `list->ob_item[i]` directly instead
* ✅ No `PyBytes_AS_STRING` — uses `((PyBytesObject *)p)->ob_sval` directly instead
* ✅ No `PyBytes_GET_SIZE` — uses `((PyBytesObject *)p)->ob_base.ob_size` directly instead
* ✅ Prints max 10 bytes for the "first X bytes" line
* ✅ Prints an error message for invalid bytes objects using `PyBytes_Check`

Compile it into a shared library (adjust the Python include path if your system differs from 3.4 — check with `python3 --version` and `find /usr/include -name "Python.h"` if needed):

```
