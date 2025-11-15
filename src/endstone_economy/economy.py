from endstone.plugin import Plugin  
from colorama import Fore
from endstone import ColorFormat

class EconomyPlugin(Plugin):

    api_version = "0.10"
    prefix = f"{Fore.GREEN}EconomyPlugin{Fore.RESET}"
    commands = []

    def on_load(self):
        self.logger.info('§ePlugin loaded !')

    