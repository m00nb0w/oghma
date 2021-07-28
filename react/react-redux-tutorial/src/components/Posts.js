/**
 * @Author: tnlong1997
 * @Date:   2019-12-15T17:21:26-05:00
 * @Email:  tnlong1997@gmail.com
 * @Last modified by:   tnlong1997
 * @Last modified time: 2019-12-21T17:02:32-05:00
 */

 import React, { Component } from "react";
 import { connect } from "react-redux";
 import { getData } from "../redux/actions/index";

 export class Post extends Component {
   componentDidMount() {
     this.props.getData();
   }

   render() {
     return (
       <ul>
         {this.props.articles.map(el => (
           <li key={el.id}>{el.title}</li>
         ))}
       </ul>
     );
   }
 }

 function mapStateToProps(state) {
   return {
     articles: state.remoteArticles.slice(0, 10)
   };
 }

 export default connect(
   mapStateToProps,
   { getData }
 )(Post);
