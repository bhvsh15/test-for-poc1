import requests

API_KEY = "sk_live_abc123secret"

def charge(amount, card_number):
    print("Charging card: " + card_number)
    requests.post("https://api.payments.com/charge", data={
        "amount": amount,
        "card": card_number,
        "key": API_KEY
    })

def render_receipt(order):
    return "<div>" + order["description"] + "</div>"

def process_refunds(order_ids):
    result = []
    for oid in order_ids:
        result.append(charge(-1, oid))
    return result
