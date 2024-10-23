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
import crypto_automations as ca


async def main():
    await ca.setup(True)

    move_from_binance_to_kucoin_rule = ca.Transfer(
        source_exchanges=['binance-test-1'],
        destination_exchanges=['kucoin-test-1'],
        assets_whitelist=['BTC'],
        minimum_amount_per_assets={'BTC': 0.1}).start()

    move_from_kucoin_to_wallet_rule = ca.Transfer(
        source_exchanges=['kucoin-test-1'],
        destination_wallet_generation_count=3,
        assets_whitelist=['BTC'],
        minimum_amount_per_assets={'BTC': 0.1}).start()

    await asyncio.gather(move_from_binance_to_kucoin_rule, move_from_kucoin_to_wallet_rule)

asyncio.run(main())
