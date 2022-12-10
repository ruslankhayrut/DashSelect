# AUTO GENERATED FILE - DO NOT EDIT

export select

"""
    select(;kwargs...)

A Select component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `class_name` (String; optional)
- `disabled` (Bool; optional)
- `multiple` (Bool; optional)
- `options` (Array of String | Reals; optional)
- `size` (Real; optional)
- `style` (Dict; optional)
- `value` (Array | String | Real; optional)
"""
function select(; kwargs...)
        available_props = Symbol[:id, :class_name, :disabled, :multiple, :options, :size, :style, :value]
        wild_props = Symbol[]
        return Component("select", "Select", "dash_select", available_props, wild_props; kwargs...)
end

