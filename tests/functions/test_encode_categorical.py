import pytest
from hypothesis import given

from janitor.errors import JanitorError
from janitor.testing_utils.strategies import (
    categoricaldf_strategy,
    df_strategy,
)


@pytest.mark.hyp
@given(df=categoricaldf_strategy())
def test_encode_categorical(df):
    df = df.encode_categorical("class_label")
    assert df["class_label"].dtypes == "category"


@pytest.mark.hyp
@given(df=df_strategy())
def test_encode_categorical_missing_column(df):
    with pytest.raises(AssertionError):
        df.encode_categorical("aloha")


@pytest.mark.hyp
@given(df=df_strategy())
def test_encode_categorical_missing_columns(df):
    with pytest.raises(AssertionError):
        df.encode_categorical(["animals@#$%^", "cities", "aloha"])


@pytest.mark.hyp
@given(df=df_strategy())
def test_encode_categorical_invalid_input(df):
    with pytest.raises(JanitorError):
        df.encode_categorical(1)
