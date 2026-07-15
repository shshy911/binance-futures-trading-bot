import logging
logger = logging.getLogger(name=__name__)

def place_market_order(client,market_order):
    logger.info(
    f"Placing MARKET order: "
    f"{market_order.side} "
    f"{market_order.quantity} "
    f"{market_order.symbol}"
)
    try:
        response = client.futures_create_order(
        symbol = market_order.symbol,
        side = market_order.side,
        quantity = market_order.quantity,
        type = "MARKET"
    )
    except Exception as e:
        logger.error(f"Market Order Exception:{e}") 
        raise 
    order_summary = format_response(response=response)
    logger.info(f"Order summary:{order_summary}")
    return order_summary




def place_limit_order(client,limit_order):
    logger.info(
    f"Placing Limit order: "
    f"{limit_order.side} "
    f"{limit_order.quantity} "
    f"{limit_order.symbol}"
)
    try:
        response = client.futures_create_order(
        symbol = limit_order.symbol,
        side = limit_order.side,
        quantity = limit_order.quantity,
        type = "LIMIT",
        price = limit_order.price,
        timeInForce="GTC"
    )
    except Exception as e:
        logger.error(f"Limit Order Exception:{e}") 
        raise 
    order_summary = format_response(response=response)
    logger.info(f"Order summary:{order_summary}")
    return order_summary
def format_response(response):
    return {
        "Order ID": response.get("orderId"),
        "Symbol": response.get("symbol"),
        "Side": response.get("side"),
        "Order Type": response.get("type"),
        "Status": response.get("status"),
        "Executed Quantity": response.get("executedQty"),
        "Average Price": response.get("avgPrice"),
    }