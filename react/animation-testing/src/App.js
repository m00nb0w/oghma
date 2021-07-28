import React, { Component } from 'react';
import { CSSTransitionGroup } from 'react-transition-group'
import AnimateOnChange from 'react-animate-on-change'
import logo from './logo.svg';
import './App.css';

class App extends Component {
	// constructor(props) {
	// 	super(props);
	// 	this.state = {items: ['hello', 'world', 'click', 'me']};
	// 	this.handleAdd = this.handleAdd.bind(this);
	// }
    //
	// handleAdd() {
	// 	const newItems = this.state.items.concat([
	// 		prompt('Enter some text')
	// 	]);
	// 	this.setState({items: newItems});
	// }
    //
	// handleRemove(i) {
	// 	let newItems = this.state.items.slice();
	// 	newItems.splice(i, 1);
	// 	this.setState({items: newItems});
	// }
    //
	// render() {
	// 	const items = this.state.items.map((item, i) => (
	// 		<div key={item} onClick={() => this.handleRemove(i)}>
	// 			{item}
	// 		</div>
	// 	));
    //
	// 	return (
	// 		<div>
	// 			<button onClick={this.handleAdd}>Add Item</button>
	// 			<CSSTransitionGroup
	// 				transitionName="example"
	// 				transitionEnterTimeout={500}
	// 				transitionLeaveTimeout={300}>
    //
	// 				{items}
	// 			</CSSTransitionGroup>
	// 		</div>
	// 	);
	// }
	constructor(props) {
		super(props);
		this.state = {
			combo: 0,
			diff: 0,
		}
	}

	add = () => {
		this.setState({
			combo: this.state.combo + 1,
			diff: 1,
		});
	}

	render () {
		let comboElement =
			<AnimateOnChange
				baseClassName="score"
				animationClassName="Score--bounce"
				animate={this.state.diff != 0}>
				Combo {this.state.combo}
			</AnimateOnChange>
		return (
			<div id="container">
				<button id="addButton" onClick={this.add}>Add Combo</button>
				{comboElement}
			</div>
		)
	}
}

export default App;
