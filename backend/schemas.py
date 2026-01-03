from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name: str
    customer_phone: str
    payment_type: str
    total: float

class OrderOut(OrderCreate):
    id: int
    status: str

    class Config:
        from_attributes = True
