from pydantic import BaseModel, Field


class CurrencyModel(BaseModel):
	asset_id: str
	icon_id: str = Field(alias="id_icon")
	name: str
	price_usd: float | None = None


class CurrencyAdditional(CurrencyModel):
	volume_1hrs_usd: str
	volume_1day_usd: str
	volume_1mth_usd: str
