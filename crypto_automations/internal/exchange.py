#  This file is part of Crypto-Automations (https://github.com/Drakkar-Software/Crypto-Automations)
#  Copyright (c) 2024 Drakkar-Software, All rights reserved.
#
#  OctoBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  OctoBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with Crypto-Automations. If not, see <https://www.gnu.org/licenses/>.
import typing

import crypto_automations.internal as internals
import octobot_trading.api as trading_api
import octobot_trading.exchanges as exchanges
import octobot_commons.constants as commons_constants

# TODO remove
import logging

ccxt_logger = logging.getLogger('ccxt')
ccxt_logger.setLevel(logging.CRITICAL)


class OctoBotExchange:
    def __init__(self,
                 name: str,
                 internal_name: str,
                 api_key: str,
                 api_secret: str,
                 api_password: typing.Optional[str] = None):
        self.name = name
        self.internal_name = internal_name
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_password = api_password

        self.exchange_manager: typing.Optional[exchanges.ExchangeManager] = None

    async def initialize(self):
        mock_config = internals.get_config()
        # inject credentials
        mock_config['exchanges'] = {
            self.internal_name: {
                commons_constants.CONFIG_EXCHANGE_KEY: self.api_key,
                commons_constants.CONFIG_EXCHANGE_SECRET: self.api_secret,
                commons_constants.CONFIG_EXCHANGE_PASSWORD: self.api_password,
            }
        }

        self.exchange_manager = await trading_api.create_exchange_builder(mock_config, self.internal_name) \
            .is_real() \
            .is_rest_only() \
            .is_exchange_only() \
            .is_ignoring_config() \
            .disable_trading_mode() \
            .build()


EXCHANGE_INSTANCES: typing.List[OctoBotExchange] = []


def add_new_exchange(exchange: OctoBotExchange):
    EXCHANGE_INSTANCES.append(exchange)


def get_exchange(name: str) -> typing.Optional[OctoBotExchange]:
    return next((exchange for exchange in EXCHANGE_INSTANCES if exchange.name == name), None)
