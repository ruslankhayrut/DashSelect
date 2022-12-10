import React, {Component} from 'react';
import PropTypes from 'prop-types';

export default class Select extends Component {
	render() {
		const { id, class_name, disabled, multiple, options, setProps, size, style, value} = this.props;

		const optionsList = options.map(el => (<option key={el} value={el}>{el}</option>))

		const finalStyle = {
			width: "100%",
			display: "block",
			...style,
		}

		var opts = {
			size: size,
			value: value,
			onChange: (e) => {
				setProps({value: multiple ? Array.from(e.target.selectedOptions, item => item.value) : e.target.value})
			}
		}

		if (disabled) {
			opts["disabled"] = "disabled"
		}

		if (multiple) {
			opts["multiple"] = "multiple"
		}

		return (
			<select className={class_name} style={finalStyle} {...opts}>
				{optionsList}
			</select>
		)

	}

};

Select.defaultProps = {
    options: [],
    value: [],
    multiple: false,
    size: 1,
    disabled: false,
    style: {},
};

Select.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

	// List of possible options
    options: PropTypes.arrayOf(PropTypes.oneOfType([PropTypes.string, PropTypes.number])),

	// Selected value / List of values if multiple
    value: PropTypes.oneOfType([PropTypes.array, PropTypes.string, PropTypes.number]),

	// Custom styles dict
    style: PropTypes.object,


	// Custom class name
    class_name: PropTypes.string,

	// Indicates whether the select can have multiple values selected
    multiple: PropTypes.bool,

	// Number of rows to be displayed
    size: PropTypes.number,

	// Indicates whether the select is disabled
    disabled: PropTypes.bool,

	/**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
