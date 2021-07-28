import React, { Component } from 'react';
import Img from 'react-image';

const SlideOne= (props) => {

	var imageUrl = require('./img/aurora.jpg')

	// let background = {
  	// 	backgroundImage: `url(${imageUrl})`,
  	// 	backgroundSize: 'cover',
  	// 	backgroundPosition: 'center'
	// }
    //
  	// return <div style={background} className="slide"></div>
	return <Img src={"https://caothu360.com/wp-content/uploads/2018/07/photo-0-15191861295451421349567-1530599105363180563578-1.jpg"} />
	// return <h1> Ling </h1>
}

export default SlideOne;
