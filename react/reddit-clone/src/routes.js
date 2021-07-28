import React from 'react';
import { Router, Route } from 'react-router';

import App from './containers/App';

const Routes = (props) => (
  <Router {...props}>
    <Route path="/" component={ <div>Hello World!</div }>
    </Route>
  </Router>
);

export default Routes;
