import pandas as pd
import pytest

from janitor.testing_utils.fixtures import (
    multiindex_with_missing_3level_dataframe,
    multiindex_with_missing_dataframe,
)


def test_collapse_levels_sanity(multiindex_with_missing_dataframe):
    with pytest.raises(TypeError):
        multiindex_with_missing_dataframe.collapse_levels(sep=3)


def test_collapse_levels_non_multilevel(multiindex_with_missing_dataframe):
    # an already single-level DataFrame is not distorted
    pd.testing.assert_frame_equal(
        multiindex_with_missing_dataframe.copy().collapse_levels(),
        multiindex_with_missing_dataframe.collapse_levels().collapse_levels(),
    )


def test_collapse_levels_functionality_2level(
    multiindex_with_missing_dataframe
):

    assert all(
        multiindex_with_missing_dataframe.copy()
        .collapse_levels()
        .columns.values
        == ["a", "Normal  Distribution", "decorated-elephant_r.i.p-rhino :'("]
    )
    assert all(
        multiindex_with_missing_dataframe.copy()
        .collapse_levels(sep="AsDf")
        .columns.values
        == [
            "a",
            "Normal  Distribution",
            "decorated-elephantAsDfr.i.p-rhino :'(",
        ]
    )


def test_collapse_levels_functionality_3level(
    multiindex_with_missing_3level_dataframe
):
    assert all(
        multiindex_with_missing_3level_dataframe.copy()
        .collapse_levels()
        .columns.values
        == [
            "a",
            "Normal  Distribution_Hypercuboid (???)",
            "decorated-elephant_r.i.p-rhino :'(_deadly__flamingo",
        ]
    )
    assert all(
        multiindex_with_missing_3level_dataframe.copy()
        .collapse_levels(sep="AsDf")
        .columns.values
        == [
            "a",
            "Normal  DistributionAsDfHypercuboid (???)",
            "decorated-elephantAsDfr.i.p-rhino :'(AsDfdeadly__flamingo",
        ]
    )
