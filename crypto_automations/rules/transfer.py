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
import decimal
import typing

import crypto_automations.actions as actions
import crypto_automations.internal as internals
import crypto_automations.models as models

import octobot_commons.constants as common_constants
import octobot_trading.constants as trading_constants


class Transfer(models.Rule):
    def __init__(self,
                 source_exchanges: typing.Optional[typing.List[str]] = None,
                 source_wallets: typing.Optional[typing.List[str]] = None,
                 destination_exchanges: typing.Optional[typing.List[str]] = None,
                 destination_wallets: typing.Optional[typing.List[str]] = None,
                 assets_whitelist: typing.Optional[typing.List[str]] = None,
                 minimum_amount_per_assets: typing.Optional[typing.Dict] = None,
                 destination_wallet_generation_count: typing.Optional[int] = None):
        super().__init__()
        self.source_exchanges = source_exchanges
        self.source_wallets = source_wallets
        self.destination_exchanges = destination_exchanges
        self.destination_wallets = destination_wallets
        self.destination_wallet_generation_count = destination_wallet_generation_count
        self.assets_whitelist = assets_whitelist
        self.minimum_amount_per_assets = minimum_amount_per_assets

        self.source_exchange_instances: typing.List[internals.OctoBotExchange] = [
            internals.get_exchange(exchange)
            for exchange in self.source_exchanges
        ] if self.source_exchanges is not None else []
        self.destination_exchange_instances: typing.List[internals.OctoBotExchange] = [
            internals.get_exchange(exchange)
            for exchange in self.destination_exchanges
        ] if self.destination_exchanges is not None else []

        self.portfolio_per_exchange: typing.Dict[str, actions.Portfolio] = {}

        self.pending_transfers: typing.List[actions.Withdraw] = []

    async def portfolio_callback(self, exchange: internals.OctoBotExchange, portfolio: typing.Dict[str, typing.Dict]):
        for asset, minimum_account in self.minimum_amount_per_assets.items():
            asset_portfolio = portfolio.get(asset, None)
            if asset_portfolio is not None:
                asset_amount = asset_portfolio.get(common_constants.PORTFOLIO_AVAILABLE,
                                                   asset_portfolio.get(trading_constants.CONFIG_PORTFOLIO_FREE))
                if asset_amount > minimum_account:
                    print(f"{exchange.name} has {asset_amount} {asset}")
                    await self.perform_transfer(exchange, asset, minimum_account)
                else:
                    print(f"{exchange.name} has not enough {asset}")

    async def perform_transfer(self, exchange, asset: str, amount: decimal.Decimal):
        # TODO support multiple destinations (multiple destinations exchange or wallet)
        # TODO support destination wallet generation
        await actions.Withdraw(exchange, self.destination_exchange_instances[0], asset, amount).run()

    async def run(self):
        # create portfolio per exchange
        self.portfolio_per_exchange = {
            exchange.name: actions.Portfolio(exchange,
                                             on_refresh_async_callback=lambda pf: self.portfolio_callback(exchange, pf))
            for exchange in self.source_exchange_instances
        }

        # start portfolios
        await asyncio.gather(*[
            portfolio.run()
            for portfolio in self.portfolio_per_exchange.values()
        ])

    async def stop(self):
        if len(self.pending_transfers) > 0:
            print(f"Error: trying to stop while {len(self.pending_transfers)} transfers are pending")  # TODO use logger
        else:
            await super().stop()
