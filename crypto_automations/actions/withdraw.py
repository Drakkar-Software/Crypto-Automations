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
import decimal

import crypto_automations.internal as internals
import crypto_automations.models as models


class Withdraw(models.Action):
    def __init__(self,
                 source_exchange: internals.OctoBotExchange,
                 destination_exchange: internals.OctoBotExchange,
                 asset: str,
                 amount: decimal.Decimal):
        super().__init__()
        self.source_exchange = source_exchange
        self.destination_exchange = destination_exchange
        self.asset = asset
        self.amount = amount

    async def run(self):
        # get the deposit address
        # withdraw to destination
        pass
