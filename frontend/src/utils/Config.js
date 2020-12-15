class Config {
    static loginUrl = "http://127.0.0.1:8000/api/gettoken/";
    static homeUrl = "/home";
    static logoutPageUrl = "/logout";
    static refreshApiUrl = "http://127.0.0.1:8000/api/resfresh_token/";
    static companyApiUrl = "http://127.0.0.1:8000/api/company/";
    static companyBankApiUrl = "http://127.0.0.1:8000/api/company_bank/";
    static companyOnly = "http://127.0.0.1:8000/api/company_only/";
    static medicineApiUrl = "http://127.0.0.1:8000/api/medicine/";

    static sidebarItem = [
        { index: "0", title: "Home", url: "/home", icons: "home" },
        { index: "1", title: "Company", url: "/company", icons: "assessment" },
        { index: "2", title: "Add Medicine", url: "/addMedicine", icons: "assessment"},
    ]
}


export default Config;