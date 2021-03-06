# This file is a part of ArgoScuolaNext Python API
#
# Copyright (c) 2019 The ArgoScuolaNext Python API Authors (see AUTHORS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from argoscuolanext.session import Session
import pytest

pytest.session = None


@pytest.fixture
def credentials(pytestconfig):
    return (pytestconfig.getoption("school_code"),
            pytestconfig.getoption("username"),
            pytestconfig.getoption("password"))


def test_login(credentials):
    pytest.session = Session(*credentials)

    assert pytest.session.logged_in


def test_login_using_token(credentials):
    pytest.session = Session.from_token(credentials[0], pytest.session.token)

    assert pytest.session.logged_in
