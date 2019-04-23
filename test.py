"""Tests for jsonshcema2template module"""
import jsonschema2template

SAMPLE_SCHEMA = {
    "type": "object",
    "required": ["foo1", "foo2", "foo3", "foo4", "foo5", "foo8"],
    "properties": {
        # string object
        "foo1": {
            "type": "string"
        },

        # object that contains other objects
        "foo2": {
            "type": "object",
            "required": ["bar1", "bar2"]
        },

        # empty object
        "foo3": {
            "type": "object"
        },

        # array object
        "foo4": {
            "type": "array",
            "items": {
                "type": 'string'
            }
        },

        # foo5 is required but not defined at all

        # optional object
        "foo6": {
            "type": "boolean"
        },

        # optional array
        "foo7": {
            "type": "array",
        },

        # object that contains optional sub-objects
        "foo8": {
            "type": "object",
            "required": ["bar1"],
            "properties": {
                # the optional sub-object
                "bar2": {
                    "type": "string"
                }
            }
        }
    }
}

FULL_TEMPLATE = {
    "foo1": "<string>",
    "foo2": {
        "bar1": "<undefined_type>",
        "bar2": "<undefined_type>"
    },
    "foo3": {},
    "foo4": ["<string>"],
    "foo5": "<undefined_type>",
    "foo6": "<boolean>",
    "foo7": [],
    "foo8": {
        "bar1": "<undefined_type>",
        "bar2": "<string>"
    }
}

MINIMAL_TEMPLATE = {
    "foo1": "<string>",
    "foo2": {
        "bar1": "<undefined_type>",
        "bar2": "<undefined_type>"
    },
    "foo3": {},
    "foo4": ["<string>"],
    "foo5": "<undefined_type>",
    "foo8": {
        "bar1": "<undefined_type>",
    }
}


def test_create_template():
    """Test that create_template produces correct JSON template from sample
    schema.
    """
    assert jsonschema2template.create_template(SAMPLE_SCHEMA) \
        == FULL_TEMPLATE


def test_create_minimal_template():
    """Test that create_template produces correct minimal JSON template from
    sample schema.
    """
    assert jsonschema2template.create_template(SAMPLE_SCHEMA, minimal=True) \
        == MINIMAL_TEMPLATE
