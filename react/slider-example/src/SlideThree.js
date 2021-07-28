import React, { Component } from 'react';

const SlideThree= (props) => {

	let background = {
		backgroundImage: '../public/img/aurora.jpg',
		backgroundSize: 'cover',
		backgroundPosition: 'center'
	}

	return <div style={background} className="slide"></div>
}

export default SlideThree;
