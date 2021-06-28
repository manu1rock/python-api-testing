import pytest
from assertpy import assert_that
from helper.demo_app_client import DemoAppClient

client = DemoAppClient()


@pytest.fixture
def get_auth_token():
    return client.get_auth_token()


def test_if_registered_users_can_be_retrieved(get_auth_token):
    response = client.get_registered_users(get_auth_token).as_dict
    assert_that(response['status']).is_equal_to("SUCCESS")
    assert_that(response['payload']).contains("Mike")


def test_if_single_user_can_be_retrieved(get_auth_token):
    response = client.get_single_user(get_auth_token, "Mike").as_dict
    assert_that(response['status']).is_equal_to("SUCCESS")


def test_if_single_user_can_be_updated(get_auth_token):
    response = client.update_user(get_auth_token, "Mike").as_dict
    assert_that(response['status']).is_equal_to("SUCCESS")
