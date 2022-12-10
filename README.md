# Description

`dash_select` is a simple wrapper over `<select>` component that can be used in Dash.
Under the hood handles `onChange` event and returns a selected value (or list of them if used in `multiple` mode)


# Installation

This module can only be installed from pip

`pip install dash-select`

# API

```

Select(
    id: str
    options: List[str]
    value: str | List[str]
    class_name: str
    size: int
    disabled: bool
    multiple: bool
    style: dict
)

```

# Usage

See `usage.py` for a code example