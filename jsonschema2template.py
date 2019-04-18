"""Convert JSON schema to minimal JSON template"""
import argparse
import importlib
import json


def create_template(schema, minimal=False):
    """Reads JSON schema and creates template JSON that contains all required
    objects with sample values.

    :param dict schema: Schema for JSON object
    :param bool minimal: If ``True``, add only required objects to template
    :returns dict: JSON object
    """
    if schema["type"] == 'object':
        json_object = dict()

        try:
            required_objects = schema['required']
        except KeyError:
            required_objects = list()
        try:
            defined_objects = list(schema['properties'].keys())
        except KeyError:
            defined_objects = list()

        if minimal:
            objects = required_objects
        else:
            objects = list(set(required_objects+defined_objects))

        for name in objects:
            try:
                json_object[name] = create_template(schema['properties'][name])
            except KeyError:
                json_object[name] = '<undefined_type>'
    else:
        json_object = f"<{schema['type']}>"

    return json_object


def main():
    """Parse arguments and read JSON schema from a variable in python module
    given as argument. Prints a minimal JSON template generated from schema.

    :returns: ``None``
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('module',
                        help='The python module from which schema is found')
    parser.add_argument('variable',
                        help='The varible that contains the schema')
    parser.add_argument('--print-schema',
                        help='Also print the schema (for debugging)',
                        default=False,
                        action='store_true')
    parser.add_argument('--minimal',
                        help='Print minimal template that contains only '
                             'required objects',
                        default=False,
                        action='store_true')
    args = parser.parse_args()

    # Import module
    module = importlib.import_module(args.module)

    # Print schema
    if args.print_schema:
        print('Schema:')
        print(json.dumps(module.__dict__[args.variable],
                         indent=4,
                         sort_keys=True))
        print('\nTemplate:')

    # Print template
    print(json.dumps(create_template(module.__dict__[args.variable]),
                     indent=4,
                     sort_keys=True))


if __name__ == "__main__":
    main()
