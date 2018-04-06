from distutils.core import setup, Extension

setup(
    ext_modules=[Extension("_AX5043", ["AX5043_SPI.c"])],
)


