from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Order
from schemas import OrderCreate, OrderOut

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/orders", response_model=OrderOut)
def create_order(order: OrderCreate):
    db: Session = SessionLocal()
    new_order = Order(**order.dict(), status="Yeni")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@app.get("/orders", response_model=list[OrderOut])
def get_orders():
    db: Session = SessionLocal()
    return db.query(Order).order_by(Order.id.desc()).all()
