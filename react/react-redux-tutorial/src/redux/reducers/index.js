/**
* @Author: tnlong1997
* @Date:   2019-12-01T18:45:02-05:00
* @Email:  tnlong1997@gmail.com
 * @Last modified by:   tnlong1997
 * @Last modified time: 2019-12-21T17:19:46-05:00
*/

import {ADD_ARTICLE, DATA_LOADED} from "../constants/action-types";

const initialState = {
	articles: [],
	remoteArticles: [],
};

function rootReducer(state = initialState, action) {
	if (action.type === ADD_ARTICLE) {
		return Object.assign({}, state, {
			articles: state.articles.concat(action.payload)
		});
	}

	if (action.type === DATA_LOADED) {
		return Object.assign({}, state, {
			remoteArticles: state.remoteArticles.concat(action.payload)
		});
	}

	return state;
};

export default rootReducer;
