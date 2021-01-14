class Config {
    static loginUrl = "https://zabmsms.herokuapp.com/api/gettoken/";
    static homeUrl = "/home";
    static logoutPageUrl = "/logout";
    static refreshApiUrl = "https://zabmsms.herokuapp.com/api/resfresh_token/";
    static companyApiUrl = "https://zabmsms.herokuapp.com/api/company/";
    static companyBankApiUrl = "https://zabmsms.herokuapp.com/api/company_bank/";
    static companyOnly = "https://zabmsms.herokuapp.com/api/company_only/";
    static medicineApiUrl = "https://zabmsms.herokuapp.com/api/medicine/";
    static companyAccountApiUrl = "https://zabmsms.herokuapp.com/api/company_account/";
    static medicineNameApiUrl = "https://zabmsms.herokuapp.com/api/medicine_by_name/";
    static employeeApiURL = "https://zabmsms.herokuapp.com/api/employee/";
    static employeeSalaryByIdApiUrl = "https://zabmsms.herokuapp.com/api/employee_salary_by_id/";
    static employeeBankApiUrlBYID = "https://zabmsms.herokuapp.com/api/employee_bank_by_id/";
    static employeeSalaryApiUrl = "https://zabmsms.herokuapp.com/api/employee_all_salary/";
    static employeeBankApiUrl = "https://zabmsms.herokuapp.com/api/employee_all_bank/";
    static generateBillApiUrl = "https://zabmsms.herokuapp.com/api/generate_bill_api/";
    static customerRequestApiUrl = "https://zabmsms.herokuapp.com/api/customer_request/";
    static homeApiUrl = "https://zabmsms.herokuapp.com/api/home_api/";

    static sidebarItem = [
        { index: "0", title: "Home", url: "/home", icons: "home"},
        { index: "1", title: "Company", url: "/company", icons: "assessment"},
        { index: "2", title: "Add Medicine", url: "/addMedicine", icons: "assessment"},
        { index: "3", title: "Manage Medicine", url: "/manageMedicine", icons: "assessment"},
        { index: "4", title: "Manage Company Account", url: "/manageCompanyAccount", icons: "assessment"},
        { index: "5", title: "Manage Employee", url: "/employeeManage", icons: "assessment"},
        { index: "6", title: "Generate Bill", url: "/generateBill", icons: "assessment"},
        { index: "7", title: "Customer Request", url: "/customerRequest", icons: "assessment"},
    ]
}


export default Config;