from datetime import datetime, timedelta

import pytest
import requests

START_DATE = datetime(2021, 1, 1)


@pytest.fixture(scope="session")
def response():
    return requests.get("https://b40gp3.deta.dev/thedailystoic").json()


def test_all_days_present(response):
    actual_keys = [row["key"] for row in response]
    expected_keys = [(START_DATE + timedelta(i)).strftime("%B_%-d")
                     for i in range(365)]
    keys_not_there = set(expected_keys) - set(actual_keys)
    superfluent_keys = set(actual_keys) - set(expected_keys)
    assert len(keys_not_there) == 0, f"Missing keys: {keys_not_there}"
    assert len(superfluent_keys) == 0, f"Unexpected keys: {superfluent_keys}"
