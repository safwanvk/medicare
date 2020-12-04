import React from 'react'
import ReactDOM from 'react-dom'
import Login from './pages/login'
import MainComponents from './components/MainComponents'

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
            <Route exact path="/home" component={MainComponents}></Route>
        </switch>
    </Router>
    ,document.getElementById('root'))