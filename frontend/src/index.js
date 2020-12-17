import React from 'react';
import ReactDOM from 'react-dom';
import Login from './pages/login';
import HomeComponent from './pages/HomeComponent'
import { PrivateRoute } from "./utils/PrivateRoute";
import { PrivateRouteNew } from "./utils/PrivateRouteNew";
import CompanyComponent from './pages/CompanyComponent';
import LogoutComponent from './pages/LogoutComponent';
import CompanyDetailsComponent from './pages/CompanyDetailsComponent';
import CompanyAddBankComponent from './pages/CompanyAddBankComponent';
import CompanyEditBankComponent from './pages/CompanyEditBankComponent';
import MedicineAddComponent from './pages/MedicineAddComponent';
import MedicineManageComponent from './pages/MedicineManageComponent';
import CompanyAccountComponent from './pages/CompanyAccountComponent';
import EmployeeComponent from './pages/EmployeeComponent';
import EmployeeDetailsComponent from './pages/EmployeeDetailsComponent';
import BillGenerateComponent from './pages/BillGenarateComponent';
import Config from './utils/Config';

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
            <PrivateRouteNew exact path="/addCompanyBank/:id" activepage="1" page={CompanyAddBankComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/editcompanybank/:company_id/:id" activepage="1" page={CompanyEditBankComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/addMedicine" activepage="2" page={MedicineAddComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/manageMedicine" activepage="3" page={MedicineManageComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/manageCompanyAccount" activepage="4" page={CompanyAccountComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/employeeManage" activepage="5" page={EmployeeComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/employeedetails/:id" activepage="5" page={EmployeeDetailsComponent}></PrivateRouteNew>
            <PrivateRouteNew exact path="/generateBill" activepage="6" page={BillGenerateComponent}></PrivateRouteNew>
        </switch>
    </Router>
    ,document.getElementById('root')) 