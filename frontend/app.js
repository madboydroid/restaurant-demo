const API="http://localhost:8000";
const tbody=document.getElementById("orders");
const modal=document.getElementById("orderModal");
document.querySelector(".new-order").onclick=()=>modal.style.display="block";
async function loadOrders(){
const r=await fetch(API+"/orders");
const d=await r.json();
tbody.innerHTML="";
d.forEach(o=>{tbody.innerHTML+=`<tr><td>${o.id}</td><td>${o.customer_name}</td><td>${o.payment_type}</td><td>${o.total}</td><td>${o.status}</td></tr>`});
}
async function saveOrder(){
await fetch(API+"/orders",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({
customer_name:customerName.value,
customer_phone:customerPhone.value,
payment_type:paymentType.value,
total:totalAmount.value
})});
modal.style.display="none";
loadOrders();
}
loadOrders();
