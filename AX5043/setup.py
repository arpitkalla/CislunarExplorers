from distutils.core import setup, Extension

setup(
    ext_modules=[Extension("_AX5043", ["_ax5043.c","AX5043_SPI.c"])]
)


