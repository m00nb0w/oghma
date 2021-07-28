/**
 * @Author: tnlong1997
 * @Date:   2019-12-03T09:22:36-05:00
 * @Email:  tnlong1997@gmail.com
 * @Last modified by:   tnlong1997
 * @Last modified time: 2019-12-15T17:22:54-05:00
 */

 import React from "react";
 import List from "./List";
 import Form from "./Form";
 import Post from "./Posts";

 const App = () => (
   <>
     <div>
       <h2>Articles</h2>
       <List />
     </div>
     <div>
       <h2>Add a new article</h2>
       <Form />
     </div>
     <div>
       <h2>API posts</h2>
       <Post />
     </div>
   </>
 );

 export default App;
