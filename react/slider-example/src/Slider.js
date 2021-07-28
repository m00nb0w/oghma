import React, { Component } from 'react';

import SlideOne from './SlideOne';
import SlideTwo from './SlideTwo';
import SlideThree from './SlideThree';

export default class Slider extends Component {
	constructor(props) {
		super(props);

		this.state = {
			slideCount: 1
		}
	}

	render() {
		return (
			<div className="slider">
				{ this.state.slideCount === 1 ? <SlideOne /> : null }
        		{ this.state.slideCount === 2 ? <SlideTwo /> : null }
        		{ this.state.slideCount === 3 ? <SlideThree /> : null }
			</div>
		);
	}
}
