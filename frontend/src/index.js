import React from 'react';
import ReactDOM from 'react-dom';
import Login from './pages/login';
import HomeComponent from './pages/HomeComponent'
import { PrivateRoute } from "./utils/PrivateRoute";
import { PrivateRouteNew } from "./utils/PrivateRouteNew";
import CompanyComponent from './pages/CompanyComponent';
import LogoutComponent from './pages/LogoutComponent';
import CompanyDetailsComponent from './pages/CompanyDetailsComponent';
import Config from './utils/Config'

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
            <Route exact path={Config.logoutPageUrl} component={LogoutComponent}></Route>
            <PrivateRouteNew exact path="/home"  activepage="0" page={HomeComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/company"   activepage="1" page={CompanyComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/companydetails/:id" activepage="1" page={CompanyDetailsComponent}></PrivateRouteNew>
        </switch>
    </Router>
    ,document.getElementById('root')) 