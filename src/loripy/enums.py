from enum import Enum


class TransactionType(Enum):
    """Types of transactions in the system."""

    PAYMENT = "PAYMENT"
    """Transactions related to transferring sonhos to other users."""

    DAILY_REWARD = "DAILY_REWARD"
    """Transactions related to Loritta's daily reward."""

    COINFLIP_BET = "COINFLIP_BET"
    """Transactions related to coinflip bets."""

    COINFLIP_BET_GLOBAL = "COINFLIP_BET_GLOBAL"
    """Transactions related to global coinflip bets."""

    EMOJI_FIGHT_BET = "EMOJI_FIGHT_BET"
    """Transactions related to emoji fight bets."""

    BLACKJACK = "BLACKJACK"
    """Transactions related to blackjack bets."""

    MINES = "MINES"
    """Transactions related to Mines bets."""

    DROP = "DROP"
    """Transactions related to sonhos drops."""

    RAFFLE = "RAFFLE"
    """Transactions related to Loritta raffles."""

    LOTTERY = "LOTTERY"
    """Transactions related to Loritta lotteries."""

    HOME_BROKER = "HOME_BROKER"
    """Transactions related to Loritta's stock market simulator."""

    SHIP_EFFECT = "SHIP_EFFECT"
    """Transactions related to bribing the love oracle."""

    SPARKLYPOWER_LSX = "SPARKLYPOWER_LSX"
    """Transactions related to SparklyPower, Loritta's Minecraft server."""

    SONHOS_BUNDLE_PURCHASE = "SONHOS_BUNDLE_PURCHASE"
    """Transactions related to purchasing sonhos bundles."""

    INACTIVE_DAILY_TAX = "INACTIVE_DAILY_TAX"
    """Transactions related to the inactivity tax on the daily reward."""

    DIVINE_INTERVENTION = "DIVINE_INTERVENTION"
    """Transactions performed by Loritta admins (constituent power)."""

    BOT_VOTE = "BOT_VOTE"
    """Transactions related to bot voting websites."""

    POWERSTREAM = "POWERSTREAM"
    """Transactions related to Loritta livestreams."""

    EVENTS = "EVENTS"
    """Transactions related to Loritta events."""

    LORI_COOL_CARDS = "LORI_COOL_CARDS"
    """Transactions related to Loritta Figurittas events."""

    LORITTA_ITEM_SHOP = "LORITTA_ITEM_SHOP"
    """Transactions related to Loritta items like profile backgrounds and designs."""

    BOM_DIA_E_CIA = "BOM_DIA_E_CIA"
    """Transactions related to Bom Dia & Cia."""

    GARTICOS = "GARTICOS"
    """Transactions related to GarticBot."""

    MARRIAGE = "MARRIAGE"
    """Transactions related to marriages in Loritta."""

    REPUTATIONS = "REPUTATIONS"
    """Transactions related to Loritta reputations."""

    VACATION_MODE = "VACATION_MODE"
    """Transactions related to the vacation mode system."""
