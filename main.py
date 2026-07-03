# =========================
# 1. PROCESS PAYMENT FUNCTION
# =========================

def process_payment(wallet_balance, item_price):
    if wallet_balance >= item_price:
        wallet_balance = wallet_balance - item_price
        print("Payment Successful")
        return wallet_balance
    else:
        print("Error: Not enough wallet balance")
        return wallet_balance


# =========================
# 2. DISPLAY ACTIVE QUEUES FUNCTION
# =========================

def display_active_queues(queues):
    print("\n--- Active Pending Queues ---")
    
    for queue in queues:
        if queue["status"] == "Pending":
            print(f"Queue ID: {queue['queue_id']}")
            print(f"Menu: {queue['menu']}")
            print(f"Price: {queue['total_price']}")
            print(f"Status: {queue['status']}")
            print("------------------------")


# =========================
# TEST DATA (จำลองระบบ)
# =========================

queues = [
    {"queue_id": 101, "menu": "Pad Thai", "total_price": 50, "status": "Pending"},
    {"queue_id": 102, "menu": "Fried Rice", "total_price": 60, "status": "Ready"},
    {"queue_id": 103, "menu": "Noodle Soup", "total_price": 45, "status": "Pending"}
]

# =========================
# TEST FUNCTION
# =========================

wallet = 200

wallet = process_payment(wallet, 50)
wallet = process_payment(wallet, 300)  # test error case

display_active_queues(queues)

print("\nRemaining Wallet:", wallet)