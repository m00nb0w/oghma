/**
 * @Author: tnlong1997
 * @Date:   2019-12-15T15:32:49-05:00
 * @Email:  tnlong1997@gmail.com
 * @Last modified by:   tnlong1997
 * @Last modified time: 2019-12-15T15:47:44-05:00
 */

import React, {
	Component
} from "react";

import {
	connect
} from "react-redux";

import {
	addArticle
} from "../redux/actions/index";

function mapDispatchToProps(dispatch) {
	return {
		addArticle: article => dispatch(addArticle(article))
	};
}

class ConnectedForm extends Component {
	constructor(props) {
		super(props);
		this.state = {
			title: ""
		};
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	handleChange(event) {
		this.setState({
			[event.target.id]: event.target.value
		});
	}

	handleSubmit(event) {
		event.preventDefault();
		const {
			title
		} = this.state;
		this.props.addArticle({
			title
		});
		this.setState({
			title: ""
		});
	}

	render() {
		const {
			title
		} = this.state;
		return ( <
			form onSubmit = {
				this.handleSubmit
			} >
			<
			div >
			<
			label htmlFor = "title" > Title < /label> <
			input type = "text"
			id = "title"
			value = {
				title
			}
			onChange = {
				this.handleChange
			}
			/> <
			/div> <
			button type = "submit" > SAVE < /button> <
			/form>
		);
	}
}

const Form = connect(
	null,
	mapDispatchToProps
)(ConnectedForm);

export default Form;
