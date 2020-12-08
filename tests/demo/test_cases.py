"""Test sample"""
import pytest


@pytest.mark.sanity
def test_one():
    print('Test One - Sanity')


@pytest.mark.sanity
def test_two():
    print('Test Two - Sanity')


@pytest.mark.regression
def test_three():
    print('Test Three - Regression')
