# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Select(Component):
    """A Select component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- class_name (string; optional)

- disabled (boolean; default False)

- multiple (boolean; default False)

- options (list of string | numbers; optional)

- size (number; default 1)

- style (dict; optional)

- value (list | string | number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_select'
    _type = 'Select'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, options=Component.UNDEFINED, value=Component.UNDEFINED, style=Component.UNDEFINED, class_name=Component.UNDEFINED, multiple=Component.UNDEFINED, size=Component.UNDEFINED, disabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'class_name', 'disabled', 'multiple', 'options', 'size', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'class_name', 'disabled', 'multiple', 'options', 'size', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Select, self).__init__(**args)
