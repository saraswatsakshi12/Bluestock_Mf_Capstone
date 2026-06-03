import requests
import pandas as pd
from pathlib import Path


OUTPUT = Path("data/raw")


schemes = {
    "HDFC_Top100_NAV": "125497",
    "SBI_Bluechip_NAV": "119551",
    "ICICI_Bluechip_NAV": "120503",
    "Nippon_LargeCap_NAV": "118632",
    "Axis_Bluechip_NAV": "119092",
    "Kotak_Bluechip_NAV": "120841"
}


def fetch_nav():

    for name, code in schemes.items():

        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(data["data"])

            file = OUTPUT / f"{name}.csv"

            df.to_csv(file, index=False)

            print(f"Saved {name}")

        else:
            print(f"Failed {name}")


if __name__ == "__main__":
    fetch_nav()