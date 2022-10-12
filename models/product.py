from dataclasses import dataclass, field


@dataclass
class Product():
    id: int
    description: str
    gtin: str
    stock_quantity: float
    unit_price: float
    stock_price: float = field(init=False)

    def __post_init__(self):
        self.unit_price = float(self.unit_price) if self.unit_price else 0.0
        self.stock_quantity = float(self.stock_quantity) if self.stock_quantity else 0.0

        self.stock_price = self.unit_price * self.stock_quantity