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
import asyncio

import crypto_automations.internal as internals
import crypto_automations.models as models


class Portfolio(models.Action):
    def __init__(self, exchange: internals.OctoBotExchange, refresh_delay=30, on_refresh_async_callback=None):
        super().__init__()
        self.exchange = exchange
        self.refresh_delay = refresh_delay
        self.on_refresh_async_callback = on_refresh_async_callback

        self.portfolio = None

    async def run(self):
        # refresh portfolio based on refresh_delay

        # TODO fetch pf on exchange

        await asyncio.sleep(self.refresh_delay)

        if self.on_refresh_async_callback is not None:
            await self.on_refresh_async_callback(self.portfolio)
