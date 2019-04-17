"""Tests for jsonshcema2template module"""
import jsonschema2template

SAMPLE_SCHEMA = {
    "type": "object",
    "required": ["foo1", "foo2", "foo3", "foo4"],
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
        }
        # foo4 is required but not defined at all
    }
}

EXPECTED_OUTPUT = {
    "foo1": "<string>",
    "foo2": {
        "bar1": "<undefined_type>",
        "bar2": "<undefined_type>"
    },
    "foo3": {},
    "foo4": "<undefined_type>"

}


def test_create_template():
    """Test that create_template produces correct JSON template from sample
    schema.
    """
    assert jsonschema2template.create_template(SAMPLE_SCHEMA) \
        == EXPECTED_OUTPUT
