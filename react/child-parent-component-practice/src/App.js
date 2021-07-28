import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
	constructor(props) {
		super(props);
		this.clicked = this.clicked.bind(this);
		this.state = {
			hit: true,
		}
	}

	clicked = () => {
		let t = true;
		if (this.state.hit) {
			t = false;
		}
		this.setState({
			hit: t,
		});
	}

  	render() {
    	return (
			<div>
    			<Child1 clicked={this.clicked}></Child1>
				{this.state.hit && <Child2/>}
			</div>
    	);
  }
}

class Child1 extends Component {
	constructor(props) {
		super(props);
	}
	render() {
		return (
			<button onClick={this.props.clicked}> Clicked here </button>
		)
	}
}

class Child2 extends Component {
	render() {
		return (
			<div style={{width: 100, height: 100, backgroundColor: "red"}}></div>
		)
	}
}

export default App;
