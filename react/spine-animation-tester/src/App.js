import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
	render() {
		return (
			<div id="spine-animation" class="spine-widget"
				data-json="./assets/spineboy.json"
				data-atlas="./assets/spineboy.atlas"
				data-animation="hit"
			>
			</div>
		)
	}
}

export default App;
