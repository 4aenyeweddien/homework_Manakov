from src.processing import filter_by_state, sort_by_date
import pytest


@pytest.fixture
def list_dict():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_filter_by_state(list_dict):
    assert filter_by_state(list_dict) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def list_dict_no_state():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_filter_by_no_state(list_dict_no_state):
    assert filter_by_state(list_dict_no_state) == []


def test_sort_by_date_reverse(list_dict):
    assert sort_by_date(list_dict) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date(list_dict):
    assert sort_by_date(list_dict) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


# @pytest.mark.parametrize("state_id, expected",
#                     ("EXECUTED",
#                     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))
#                                               # ("Счет 64686473678894779589", "Счет **9589"),
#                                               # ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
#                                               # ("Счет 35383033474447895560", "Счет **5560"),
#                                               # ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
#                                               # ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
#                                               # ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
#                                               # ("Счет 73654108430135874305", "Счет **4305"),])