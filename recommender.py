import pandas as pd


performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)


def recommend_funds(risk):

    result = (
        performance[
            performance["risk_grade"] == risk
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return result[
        [
            "scheme_name",
            "fund_house",
            "sharpe_ratio",
            "risk_grade"
        ]
    ]


if __name__ == "__main__":

    risk = input(
        "Enter risk (Low/Moderate/High): "
    )

    print(
        recommend_funds(risk)
    )