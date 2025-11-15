from endstone.plugin import Plugin  
from colorama import Fore
from endstone import ColorFormat
from endstone_economy.src.database import Database

class EconomyPlugin(Plugin):

    api_version = "0.10"
    prefix = f"{Fore.GREEN}EconomyPlugin{Fore.RESET}"
    
    def on_load(self):
        self.logger.info('§ePlugin loaded !')

        db = Database()
        self.logger.info(f'§aDreWen15 a {db.getMoneyByUser('DreWen15')}$§r')
        db.close()

