# MIT License
#
# Copyright (c) 2020 Jonathan Zernik
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
import pytest
from bitcoin.core import CoreMainParams
from squeak.core.signing import CSigningKey
from squeak.core.signing import CSqueakAddress

from squeaknode.bitcoin.block_info import BlockInfo
from squeaknode.core.squeaks import make_squeak_with_block


@pytest.fixture
def signing_key():
    yield CSigningKey.generate()


@pytest.fixture
def address(signing_key):
    verifying_key = signing_key.get_verifying_key()
    yield str(CSqueakAddress.from_verifying_key(verifying_key))


@pytest.fixture
def genesis_block_info():
    yield BlockInfo(
        block_height=0,
        block_hash=CoreMainParams.GENESIS_BLOCK.GetHash(),
        block_header=CoreMainParams.GENESIS_BLOCK.get_header().serialize(),
    )


@pytest.fixture
def squeak_content():
    yield "hello!"


@pytest.fixture
def squeak_and_secret_key(signing_key, squeak_content, genesis_block_info):
    yield make_squeak_with_block(
        signing_key,
        squeak_content,
        genesis_block_info.block_height,
        genesis_block_info.block_hash,
    )


@pytest.fixture
def squeak(squeak_and_secret_key):
    squeak, _ = squeak_and_secret_key
    yield squeak


@pytest.fixture
def secret_key(squeak_and_secret_key):
    _, secret_key = squeak_and_secret_key
    yield secret_key
