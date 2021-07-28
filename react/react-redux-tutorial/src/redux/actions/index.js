/**
 * @Author: tnlong1997
 * @Date:   2019-12-01T18:51:09-05:00
 * @Email:  tnlong1997@gmail.com
 * @Last modified by:   tnlong1997
 * @Last modified time: 2019-12-21T17:02:02-05:00
 */

import { ADD_ARTICLE, DATA_LOADED } from "../constants/action-types";

export function addArticle(payload) {
	return {
		type: ADD_ARTICLE,
		payload: payload,
	};
};

export function getData() {
	return {
		type: "DATA_REQUESTED"
	};
}
