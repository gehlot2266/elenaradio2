"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "5225174608 5265276618")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 10250331))
    CHAT = int(os.environ.get("CHAT", "723610758"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "723610758")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("API_HASH", "b31cf3be535317b24360651d066fb84b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5377682360:AAHcmCZqHlmBxQVrrh4-UCO8Lv7dGFpi9f4") 
    SESSION = os.environ.get("SESSION_STRING", "BQCwSUFmbGuCrIlQFBR2IHVQw7rRlcnxu5N3VTG22kEoO5olMFBz7pIuIcLlIYCmjUvqzxOn5w4VI4hdKcYXCBCPi0bNcRxydeem1XdhYHeeqT-7XX-zafSy2FR1TwU5FhBKZnfKI494isSad1QrtkSg8t9_ItPIgRfXQCGuxdVJmr4FixMLSUQm4vxBFgnlAIPIwl653beSz87iFvomZO72ShnU950_Uf8KWn_cjab6wkMO4TRPILo3HCJmeIDvBHrWjD1Syr8fDRjAinZ_vTg-P1EslyhCYPzCtZk5pM2TKtTc1zj7z2nsaKnGd-eN89j5LYwBGWbKR0dSlWK7v-a0ck9UpgA")

