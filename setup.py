from setuptools import setup, find_packages

setup(
    name = 'Running_DeepSlice_2024',
    version = '0.1',
    packages = find_packages(),
    install_requires=[
      #add dependencies  
    ],
    entry_points = {
      "console_scripts":[
        "Automatic-Registration = Running_DeepSlice_2024.Application:main",
      ],
    },
)