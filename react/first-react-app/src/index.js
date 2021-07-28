import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Dividend from './dividend';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Dividend />, document.getElementById('root'));
registerServiceWorker();
