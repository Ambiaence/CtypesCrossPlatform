import ctypes
testlib = ctypes.CDLL('/home/programmer/Projects/ctypesTesting/testlib.so')
testlib.myprint()
