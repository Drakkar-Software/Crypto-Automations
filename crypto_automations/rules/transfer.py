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

from crypto_automations.models.rule import Rule


class Transfer(Rule):
    def __init__(self,
                 source_exchanges: typing.List[str],
                 destination_exchanges: typing.List[str],
                 assets_whitelist: typing.Optional[typing.List[str]] = None,
                 minimum_amount_per_assets: typing.Optional[typing.Dict] = None):
        super().__init__()
        self.source_exchange = source_exchanges
        self.destination_exchange = destination_exchanges
        self.assets_whitelist = assets_whitelist
        self.minimum_amount_per_assets = minimum_amount_per_assets

    async def run(self):
        # initialize
        # setup portfolio callbacks => trigger event awaited in run()

        # wait for minimum amount per assets on each exchanges
        # if an exchange reach the minimum => start a withdraw action
        pass
