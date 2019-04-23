"""Setup jsonschema2template"""
import setuptools

setuptools.setup(
    name='jsonschema2template',
    py_modules=['jsonschema2template'],
    python_requires='>=3',
    install_requires=['argcomplete'],
    entry_points={
        'console_scripts': [
            'jsonschema2template = jsonschema2template:main'
        ]
    }
)
