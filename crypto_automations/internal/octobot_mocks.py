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

import os
import json
import appdirs

import crypto_automations
import crypto_automations.constants as constants
import octobot_commons.constants as commons_constants
import octobot_commons.enums as commons_enums
import octobot_tentacles_manager.api as octobot_tentacles_manager_api
import octobot_tentacles_manager.constants as octobot_tentacles_manager_constants
import octobot.configuration_manager as octobot_configuration_manager


def get_tentacles_config():
    # use tentacles config from user appdirs as it is kept up to date at each tentacle packages install
    ref_tentacles_config_path = os.path.join(
        get_module_appdir_path(),
        octobot_tentacles_manager_constants.USER_REFERENCE_TENTACLE_CONFIG_PATH,
        commons_constants.CONFIG_TENTACLES_FILE
    )
    tentacles_setup_config = octobot_tentacles_manager_api.get_tentacles_setup_config(ref_tentacles_config_path)
    return tentacles_setup_config


def get_config():
    with open(get_module_config_path("config_mock.json")) as f:
        config = json.load(f)
        config[commons_constants.CONFIG_TIME_FRAME] = []
        config[commons_constants.CONFIG_CRYPTO_CURRENCIES] = []
        return config


def get_module_install_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_module_config_path(file_name):
    return os.path.join(get_module_install_path(), constants.CONFIG_PATH, file_name)


def get_module_appdir_path():
    dirs = appdirs.AppDirs(crypto_automations.PROJECT_NAME, crypto_automations.AUTHOR, crypto_automations.VERSION)
    return dirs.user_data_dir


def get_internal_import_path():
    return os.path.join(get_module_appdir_path(), constants.ADDITIONAL_IMPORT_PATH)


def get_tentacles_path():
    return os.path.join(get_internal_import_path(), octobot_tentacles_manager_constants.TENTACLES_PATH)


def get_imported_tentacles_path():
    import tentacles
    return os.path.dirname(os.path.abspath(tentacles.__file__))


def get_public_tentacles_urls():
    return [
        octobot_configuration_manager.get_default_tentacles_url()
    ]