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
import mock
import pytest

from squeaknode.config.config import SqueaknodeConfig
from squeaknode.core.lightning_address import LightningAddressHostPort
from squeaknode.core.peer_address import PeerAddress
from squeaknode.core.squeak_core import SqueakCore
from squeaknode.core.squeak_peer import SqueakPeer
from squeaknode.db.squeak_db import SqueakDb
from squeaknode.network.network_manager import NetworkManager
from squeaknode.node.payment_processor import PaymentProcessor
from squeaknode.node.squeak_controller import SqueakController


@pytest.fixture
def config():
    squeaknode_config = SqueaknodeConfig()
    squeaknode_config.read()
    return squeaknode_config


@pytest.fixture
def regtest_config():
    squeaknode_config = SqueaknodeConfig(
        dict_config={'node': {'network': 'regtest'}}
    )
    squeaknode_config.read()
    return squeaknode_config


@pytest.fixture
def squeak_db():
    # return SqueakDb(None, None, None)
    return mock.Mock(spec=SqueakDb)


@pytest.fixture
def network_manager():
    return mock.Mock(spec=NetworkManager)


@pytest.fixture
def squeak_core():
    return mock.Mock(spec=SqueakCore)


@pytest.fixture
def lightning_host_port():
    return LightningAddressHostPort(host="my_lightning_host", port=8765)


@pytest.fixture
def peer_address():
    return PeerAddress(host="fake_host", port=5678, use_tor=False)


@pytest.fixture
def peer_address_with_zero():
    return PeerAddress(host="fake_host", port=0, use_tor=False)


@pytest.fixture
def price_msat():
    return 777


@pytest.fixture
def payment_processor():
    return mock.Mock(spec=PaymentProcessor)


@pytest.fixture
def squeak_controller(
    squeak_db,
    squeak_core,
    payment_processor,
    network_manager,
    config,
):
    return SqueakController(
        squeak_db,
        squeak_core,
        payment_processor,
        network_manager,
        config,
    )


@pytest.fixture
def regtest_squeak_controller(
    squeak_db,
    squeak_core,
    payment_processor,
    network_manager,
    regtest_config,
):
    return SqueakController(
        squeak_db,
        squeak_core,
        payment_processor,
        network_manager,
        regtest_config,
    )


def test_nothing():
    assert True


def test_get_buy_offer(squeak_controller):
    assert squeak_controller.get_offer is not None


def test_get_network_default(squeak_controller):
    assert squeak_controller.get_network() == "testnet"


def test_get_network_regtest(regtest_squeak_controller):
    assert regtest_squeak_controller.get_network() == "regtest"


# def test_get_network_regtest(config, squeak_controller):
#     # with mock.patch.object(Config, 'squeaknode_network', new_callable=mock.PropertyMock) as mock_config:
#     # mock_config.return_value = 'regtest'
#     config.squeaknode_network = "regtest"
#     print(config.squeaknode_network)

#     assert squeak_controller.get_network() == "regtest"


def test_create_peer(squeak_db, squeak_controller, peer_address):
    squeak_controller.create_peer(
        "fake_peer_name",
        peer_address,
    )

    squeak_db.insert_peer.assert_called_with(
        SqueakPeer(
            peer_id=None,
            peer_name="fake_peer_name",
            address=peer_address,
            autoconnect=False,
        )
    )
