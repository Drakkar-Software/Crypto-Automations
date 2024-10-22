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
#  This file is part of OctoBot-Script (https://github.com/Drakkar-Software/OctoBot-Script)
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
#  License along with OctoBot-Script. If not, see <https://www.gnu.org/licenses/>.
import aiohttp
import crypto_automations.constants as constants
import crypto_automations.internal as internals
import octobot_tentacles_manager.api as api
import octobot_commons.configuration.config_file_manager as config_file_manager


async def setup(quite_mode: bool) -> bool:
    # load config
    config = config_file_manager.load(constants.EXCHANGE_CONFIG_PATH)

    # download tentacles (TODO: check if necessary)
    await install_all_tentacles(quite_mode)

    # create exchange instances
    for exchange in config.get('exchanges', []):
        internals.add_new_exchange(internals.OctoBotExchange(
            name=exchange.get('name'),
            internal_name=exchange.get('internal_name'),
            api_key=exchange.get('api_key'),
            api_secret=exchange.get('api_secret'),
            api_password=exchange.get('api_password'),
        ))


async def install_all_tentacles(quite_mode: bool) -> bool:
    internals.enable_base_logger()
    error_count = 0
    install_path = internals.get_module_appdir_path()
    tentacles_path = internals.get_tentacles_path()
    tentacles_urls = internals.get_public_tentacles_urls()
    async with aiohttp.ClientSession() as aiohttp_session:
        for tentacles_url in tentacles_urls:
            error_count += await api.install_all_tentacles(tentacles_url,
                                                           aiohttp_session=aiohttp_session,
                                                           quite_mode=quite_mode)
    return error_count == 0
