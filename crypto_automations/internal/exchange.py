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


EXCHANGE_INSTANCES: typing.List[OctoBotExchange] = []


def add_new_exchange(exchange: OctoBotExchange):
    EXCHANGE_INSTANCES.append(exchange)


def get_exchange(name: str) -> typing.Optional[OctoBotExchange]:
    return next((exchange for exchange in EXCHANGE_INSTANCES if exchange.name == name), None)
