import React from "react";
import { BrowserRouter as Router, Redirect, Route, Switch } from "react-router-dom";

import './Assets/css/index.min.css'

import Main from './Routes/Main'

function Routers () {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={Main}/>
                <Redirect from="*" to="/" />
            </Switch>
        </Router>
    )
}

export default Routers