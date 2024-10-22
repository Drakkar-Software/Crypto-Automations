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
import typing

import crypto_automations.internal as internals
import crypto_automations.models as models
import octobot_trading.personal_data as personal_data


class Portfolio(models.Action):
    DEFAULT_REFRESH_DELAY = 30

    def __init__(self,
                 exchange: internals.OctoBotExchange,
                 refresh_delay=DEFAULT_REFRESH_DELAY,
                 on_refresh_async_callback: typing.Optional[
                     typing.Callable[
                         [personal_data.Portfolio], typing.Awaitable[None]
                     ]
                 ] = None):
        super().__init__()
        self.exchange = exchange
        self.refresh_delay = refresh_delay
        self.on_refresh_async_callback = on_refresh_async_callback

        self.portfolio: typing.Optional[personal_data.Portfolio] = None

    async def run(self):
        try:
            # refresh portfolio based on refresh_delay
            self.portfolio = await self.exchange.exchange_manager.exchange.get_balance()
            print(self.portfolio)

            await asyncio.sleep(self.refresh_delay)

            if self.on_refresh_async_callback is not None:
                await self.on_refresh_async_callback(self.portfolio)
        except Exception as e:
            print(f"Failed to update balance: {e}")  # TODO logger
            await asyncio.sleep(self.refresh_delay)
