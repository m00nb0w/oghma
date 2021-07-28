/**
 * @Author: tnlong1997
 * @Date:   2019-12-03T09:41:02-05:00
 * @Email:  tnlong1997@gmail.com
 * @Last modified by:   tnlong1997
 * @Last modified time: 2019-12-15T15:03:17-05:00
 */

import React from "react";
import { connect } from "react-redux";

const mapStateToProps = state => {
	return { articles: state.articles };
}

const ConnectedList = ({articles}) => (
	<ul>
		{articles.map(el => (
			<li key={el.id}> {el.title} </li>
		))}
	</ul>
);

const List = connect(mapStateToProps) (ConnectedList);

export default List;
