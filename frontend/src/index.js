import React from 'react';
import ReactDOM from 'react-dom';
import Login from './pages/login';
import HomeComponent from './pages/HomeComponent'
import { PrivateRoute } from "./utils/PrivateRoute";
import { PrivateRouteNew } from "./utils/PrivateRouteNew";
import CompanyComponent from './pages/CompanyComponent';

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
            <PrivateRouteNew exact path="/home" page={<HomeComponent />}></PrivateRouteNew>
            <PrivateRouteNew exact path="/company" page={<CompanyComponent />}></PrivateRouteNew>
        </switch>
    </Router>
    ,document.getElementById('root')) 