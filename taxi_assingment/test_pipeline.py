import pandas as pd
from utils import load_data, get_missing_values, print_5


def test_load_data():
    df = load_data(r"D:\coding\assignment-mini-project-\taxi_assingment\data_files\yellow_tripdata_2026-01.parquet")

    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_get_missing_values():
    df = pd.DataFrame({
        "A": [1, None, 3],
        "B": [None, None, 3]
    })

    result = get_missing_values(df)

    assert result["A"] == 1
    assert result["B"] == 2


def test_print_5(capsys):
    df = pd.DataFrame({"A": [1, 2, 3, 4, 5, 6]})

    print_5(df)
    captured = capsys.readouterr()

    assert "A" in captured.out