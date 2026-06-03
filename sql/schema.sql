CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_grade TEXT
);


CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    year INTEGER,
    month INTEGER
);


CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    date DATE,
    nav REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);


CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    transaction_type TEXT,
    amount REAL,
    transaction_date DATE,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);


CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);


CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    aum_crore REAL,
    date DATE,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);