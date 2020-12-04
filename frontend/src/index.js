import React from 'react';
import ReactDOM from 'react-dom';
import Login from './pages/login';
import MainComponents from './components/MainComponents';
import { PrivateRoute } from "./utils/PrivateRoute";

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";


ReactDOM.render(
    <Router>
        <switch>
            <Route exact path="/" component={Login}></Route>
            <PrivateRoute exact path="/home" component={MainComponents}></PrivateRoute>
        </switch>
    </Router>
    ,document.getElementById('root'))