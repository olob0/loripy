from datetime import datetime
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, WrapValidator
from pydantic.alias_generators import to_camel

from loripy.enums import TransactionType


class BaseTransaction(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    type: str
    id: int
    transaction_type: TransactionType
    timestamp: datetime
    user: str


class BaseSonhosTransaction(BaseTransaction):
    sonhos: int


class DailyRewardTransaction(BaseSonhosTransaction):
    type: Literal["DailyRewardSonhosTransaction"]


class BlackjackTransaction(BaseSonhosTransaction):
    type: Literal[
        "BlackjackJoinedTransaction",
        "BlackjackSplitTransaction",
        "BlackjackPayoutTransaction",
        "BlackjackTiedTransaction",
        "BlackjackInsurancePayoutTransaction",
        "BlackjackInsuranceTransaction",
        "BlackjackDoubleDownTransaction",
        "BlackjackRefundTransaction",
    ]
    match_id: int


class MinesTransaction(BaseSonhosTransaction):
    type: Literal["MinesJoinedTransaction", "MinesPayoutTransaction", "MinesRefundTransaction"]
    match_id: int


class CoinFlipBetTransaction(BaseTransaction):
    type: Literal["CoinFlipBetSonhosTransaction"]
    winner: str
    loser: str
    quantity: int
    quantity_after_tax: int
    tax: int | None
    tax_percentage: float | None


class CoinFlipBetGlobalTransaction(BaseTransaction):
    type: Literal["CoinFlipBetGlobalSonhosTransaction"]
    winner: str
    loser: str
    quantity: int
    quantity_after_tax: int
    tax: int | None
    tax_percentage: float | None
    time_on_queue: int


class EmojiFightBetTransaction(BaseTransaction):
    type: Literal["EmojiFightBetSonhosTransaction"]
    winner: str
    users_in_match: int
    emoji: str
    entry_price: int
    entry_price_after_tax: int
    tax: int | None
    tax_percentage: float | None


class DropTransaction(BaseSonhosTransaction):
    type: Literal["DropChatTransaction", "DropCallTransaction", "DropChatChoiceTransaction"]
    drop_id: int
    charged: bool
    given_by_id: int | None
    received_by_id: int
    guild_id: int


class RaffleTicketsTransaction(BaseSonhosTransaction):
    type: Literal["RaffleTicketsSonhosTransaction"]
    ticket_quantity: int


class RaffleRewardTransaction(BaseTransaction):
    type: Literal["RaffleRewardSonhosTransaction"]
    quantity: int
    quantity_after_tax: int
    tax: int | None
    tax_percentage: float | None


class LotteryTicketsTransaction(BaseSonhosTransaction):
    type: Literal["LotteryTicketsTransaction"]
    lottery_id: int
    ticket_id: int


class LotteryRewardTransaction(BaseSonhosTransaction):
    type: Literal["LotteryRewardTransaction"]
    lottery_id: int
    taxed: bool
    payout_without_tax: int


class BrokerTransaction(BaseSonhosTransaction):
    type: Literal["BrokerSonhosTransaction"]
    action: str
    ticker: str
    stock_price: int
    stock_quantity: int


class SonhosBundlePurchaseTransaction(BaseSonhosTransaction):
    type: Literal["SonhosBundlePurchaseSonhosTransaction"]


class ChargebackedSonhosBundleTransaction(BaseSonhosTransaction):
    type: Literal["ChargebackedSonhosBundleTransaction"]
    triggered_by_user_id: int


class SparklyPowerLSXTransaction(BaseSonhosTransaction):
    type: Literal["SparklyPowerLSXSonhosTransaction"]
    action: str
    sparkly_power_sonhos: int
    player_name: str
    player_unique_id: str
    exchange_rate: float


class InactiveDailyTaxTransaction(BaseSonhosTransaction):
    type: Literal["DailyTaxSonhosTransaction"]
    max_day_threshold: int
    minimum_sonhos_for_trigger: int


class DivineInterventionTransaction(BaseSonhosTransaction):
    type: Literal["DivineInterventionSonhosTransaction"]
    action: str
    reason: str | None


class BotVoteTransaction(BaseSonhosTransaction):
    type: Literal["BotVoteSonhosTransaction"]
    website_source: str


class PowerStreamTransaction(BaseSonhosTransaction):
    type: Literal[
        "PowerStreamClaimedLimitedTimeSonhosRewardSonhosTransaction",
        "PowerStreamClaimedFirstSonhosRewardSonhosTransaction",
    ]
    live_id: str
    stream_id: int


class PaymentSonhosTransaction(BaseSonhosTransaction):
    type: Literal["PaymentSonhosTransaction"]
    given_by: str
    received_by: str


class APIInitiatedPaymentSonhosTransaction(BaseSonhosTransaction):
    type: Literal["APIInitiatedPaymentSonhosTransaction"]
    given_by: str
    received_by: str
    reason: str


class ThirdPartyPaymentSonhosTransaction(BaseSonhosTransaction):
    type: Literal["ThirdPartyPaymentSonhosTransaction"]
    given_by: str
    received_by: str
    tax: int
    tax_percentage: float
    reason: str


class Christmas2022Transaction(BaseSonhosTransaction):
    type: Literal["Christmas2022SonhosTransaction"]
    gifts: int


class Easter2023Transaction(BaseSonhosTransaction):
    type: Literal["Easter2023SonhosTransaction"]
    baskets: int


class ReactionEventTransaction(BaseSonhosTransaction):
    type: Literal["ReactionEventSonhosTransaction"]
    event_internal_id: str
    crafted_count: int


class ShipEffectTransaction(BaseSonhosTransaction):
    type: Literal["ShipEffectSonhosTransaction"]


class LoriCoolCardsEventTransaction(BaseSonhosTransaction):
    type: Literal[
        "LoriCoolCardsBoughtBoosterPackSonhosTransaction",
        "LoriCoolCardsFinishedAlbumSonhosTransaction",
    ]
    event_id: int


class LoriCoolCardsTradeTransaction(BaseSonhosTransaction):
    type: Literal["LoriCoolCardsPaymentSonhosTradeTransaction"]
    given_by: str
    received_by: str


class LorittaItemShopBackgroundTransaction(BaseSonhosTransaction):
    type: Literal[
        "LorittaItemShopBoughtBackgroundTransaction",
        "LorittaItemShopComissionBackgroundTransaction",
    ]
    internal_background_id: str


class LorittaItemShopProfileDesignTransaction(BaseSonhosTransaction):
    type: Literal[
        "LorittaItemShopBoughtProfileDesignTransaction",
        "LorittaItemShopComissionProfileDesignTransaction",
    ]
    internal_profile_design_id: str


class BomDiaECiaTransaction(BaseSonhosTransaction):
    type: Literal[
        "BomDiaECiaCallCalledTransaction",
        "BomDiaECiaCallWonTransaction",
    ]


class GarticosTransferTransaction(BaseSonhosTransaction):
    type: Literal["GarticosTransferTransaction"]
    garticos: int
    transfer_rate: float


class MarriageMarryTransaction(BaseSonhosTransaction):
    type: Literal["MarriageMarryTransaction"]
    married_with_user_id: int


class MarriageActionTransaction(BaseSonhosTransaction):
    type: Literal[
        "MarriageRestoreTransaction",
        "MarriageRestoreAutomaticTransaction",
        "MarriageLoveLetterTransaction",
    ]


class ReputationDeletedLeaveTransaction(BaseSonhosTransaction):
    type: Literal["ReputationDeletedLeaveTransaction"]


class VacationModeLeaveTransaction(BaseSonhosTransaction):
    type: Literal["VacationModeLeaveTransaction"]


class UnknownTransaction(BaseTransaction):
    type: Literal["UnknownSonhosTransaction"]


PaymentTransaction = (
    PaymentSonhosTransaction | APIInitiatedPaymentSonhosTransaction | ThirdPartyPaymentSonhosTransaction
)

EventsTransaction = Christmas2022Transaction | Easter2023Transaction | ReactionEventTransaction | ShipEffectTransaction

Transaction = (
    MinesTransaction
    | DivineInterventionTransaction
    | BotVoteTransaction
    | PowerStreamTransaction
    | EventsTransaction
    | SonhosBundlePurchaseTransaction
    | ChargebackedSonhosBundleTransaction
    | SparklyPowerLSXTransaction
    | InactiveDailyTaxTransaction
    | BrokerTransaction
    | LotteryTicketsTransaction
    | LotteryRewardTransaction
    | RaffleTicketsTransaction
    | RaffleRewardTransaction
    | DropTransaction
    | EmojiFightBetTransaction
    | BlackjackTransaction
    | PaymentTransaction
    | CoinFlipBetTransaction
    | CoinFlipBetGlobalTransaction
    | LoriCoolCardsEventTransaction
    | LoriCoolCardsTradeTransaction
    | LorittaItemShopBackgroundTransaction
    | LorittaItemShopProfileDesignTransaction
    | BomDiaECiaTransaction
    | GarticosTransferTransaction
    | MarriageMarryTransaction
    | MarriageActionTransaction
    | ReputationDeletedLeaveTransaction
    | VacationModeLeaveTransaction
    | DailyRewardTransaction
    | UnknownTransaction
)


class GenericTransaction(BaseTransaction):
    model_config = ConfigDict(extra="allow", alias_generator=to_camel, populate_by_name=True)

    transaction_type: str


def _parse_transaction_fallback(v: Any, handler: Any) -> Any:
    try:
        return handler(v)
    except ValidationError:
        if isinstance(v, dict):
            return GenericTransaction(**v)
        raise


DiscriminatedTransaction = Annotated[Transaction, Field(discriminator="type")]
SafeTransaction = Annotated[DiscriminatedTransaction, WrapValidator(_parse_transaction_fallback)]


class Paging(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    total: int
    limit: int
    offset: int


class TransactionsResponse(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    transactions: list[SafeTransaction]
    paging: Paging
