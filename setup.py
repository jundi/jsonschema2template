"""Setup jsonschema2template"""
import setuptools

setuptools.setup(
    name='jsonschema2template',
    py_modules=['jsonschema2template'],
    entry_points={
        'console_scripts': [
            'jsonschema2template = jsonschema2template:main'
        ]
    }
)
