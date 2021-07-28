/**
 * @Author: tnlong1997
 * @Date:   2019-12-15T16:00:27-05:00
 * @Email:  tnlong1997@gmail.com
 * @Last modified by:   tnlong1997
 * @Last modified time: 2019-12-15T16:00:43-05:00
 */

 import {
 	ADD_ARTICLE
 } from "../constants/action-types";

 const forbiddenWords = ["spam", "money"];

 export function forbiddenWordsMiddleware({
 	dispatch
 }) {
 	return function(next) {
 		return function(action) {
 			// do your stuff
 			if (action.type === ADD_ARTICLE) {
 				const foundWord = forbiddenWords.filter(word =>
 					action.payload.title.includes(word)
 				);
 				if (foundWord.length) {
 					return dispatch({
 						type: "FOUND_BAD_WORD"
 					});
 				}
 			}
 			return next(action);
 		};
 	};
 }
