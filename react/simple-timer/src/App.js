import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

	constructor(props) {
		super(props);

		this.state = {
			time: 0,
		}

		this.startTimer = this.startTimer.bind(this);
		this.stopTimer = this.stopTimer.bind(this);
		this.resetTimer = this.resetTimer.bind(this);
	}

	startTimer() {
		console.log("start");
		this.timer = setInterval(() => this.setState({
			time: this.state.time + 1,
		}), 1000)
	}

	stopTimer() {
		console.log("stop");
		clearInterval(this.timer);
	}

	resetTimer() {
		console.log("reset");
		this.setState({
			time: 0,
		})
	}

	render() {
		console.log(this.state.time);
		return (
			<div>
				<h3> Timer: {this.state.time} </h3>
				<button onClick={this.startTimer}> Start </button>
				<button onClick={this.stopTimer}> Stop </button>
				<button onClick={this.resetTimer}> Reset </button>
			</div>
		);
	}
}

export default App;
