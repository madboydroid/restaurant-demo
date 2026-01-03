from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_phone = Column(String)
    payment_type = Column(String)
    total = Column(Numeric)
    status = Column(String)
