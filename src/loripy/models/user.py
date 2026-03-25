from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class UserFeatures(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    third_party_sonhos_transfer_tax: float


class User(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: int
    xp: int
    sonhos: int
    about_me: str | None
    gender: str | None = None
    emoji_fight_emoji: str | None
    loritta_ban_state: str | None
    features: UserFeatures
