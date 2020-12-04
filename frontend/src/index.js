import React from 'react'
import ReactDOM from 'react-dom'
import Login from './pages/login'
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
        </switch>
    </Router>
    ,document.getElementById('root'))