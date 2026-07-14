import ctypes

lib = ctypes.CDLL('./libPyList.so')

lib.print_python_list_info.argtypes = [ctypes.py_object]

l = ['hello', 'World']
lib.print_python_list_info(l)

del l[1]
lib.print_python_list_info(l)

l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
