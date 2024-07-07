from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


@dataclass
class BinanceAsset(DataClassJsonMixin):
    id: str
    assetCode: str
    assetName: str
    unit: str | None
    commissionRate: float
    isLegalMoney: bool
    logoUrl: str
    fullLogoUrl: str | None
    tags: list[str]
    delisted: bool
    preDelist: bool