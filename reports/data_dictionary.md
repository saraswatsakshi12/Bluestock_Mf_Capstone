\# Data Dictionary



\## dim\_fund



| Column | Type | Description |

|---|---|---|

| amfi\_code | TEXT | Unique AMFI scheme identifier |

| scheme\_name | TEXT | Mutual fund scheme name |

| fund\_house | TEXT | Asset management company |

| category | TEXT | Fund category |

| risk\_grade | TEXT | Risk classification |





\## fact\_nav



| Column | Type | Description |

|---|---|---|

| amfi\_code | TEXT | Scheme identifier |

| date | DATE | NAV date |

| nav | REAL | Net Asset Value |





\## fact\_transactions



| Column | Type | Description |

|---|---|---|

| transaction\_type | TEXT | SIP/Lumpsum/Redemption |

| amount | REAL | Investment amount |

| transaction\_date | DATE | Transaction date |





\## fact\_performance



| Column | Type | Description |

|---|---|---|

| return\_1yr\_pct | REAL | 1 year return |

| return\_3yr\_pct | REAL | 3 year return |

| return\_5yr\_pct | REAL | 5 year return |

| expense\_ratio\_pct | REAL | Fund expense ratio |





Source:

Bluestock Mutual Fund Capstone Dataset

