import os

import pandas as pd
import pytest


@pytest.mark.functions
def test_convert_excel_date():
    df = (
        pd.read_excel(os.path.join(pytest.EXAMPLES_DIR, "dirty_data.xlsx"))
        .clean_names()
        .convert_excel_date("hire_date")
    )

    assert df["hire_date"].dtype == "M8[ns]"
