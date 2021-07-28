/**
 * @Author: tnlong1997
 * @Date:   2019-12-15T13:00:34-05:00
 * @Email:  tnlong1997@gmail.com
 * @Last modified by:   tnlong1997
 * @Last modified time: 2019-12-15T14:43:57-05:00
 */

 import store from "../redux/store/index";
 import { addArticle } from "../redux/actions/index";

 window.store = store;
 window.addArticle = addArticle;
