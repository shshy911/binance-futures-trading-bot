import typer
import logging

from bot.client import get_client
from bot.logging_config import setup_logging
from bot.validators import MarketOrder, LimitOrder
from bot.orders import place_market_order, place_limit_order

app = typer.Typer()

logger = logging.getLogger(__name__)

@app.command()
def place_order(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    setup_logging()

    client = get_client()
    try:
        if order_type.upper() == "MARKET":
            market_order = MarketOrder(
                symbol=symbol,
                side=side,
                quantity=quantity
            )
            logger.info("Input Validated")
            response = place_market_order(client=client,market_order=market_order)
            for key, value in response.items():
                typer.echo(f"{key}: {value}")
        elif order_type.upper() == "LIMIT":
            limit_order = LimitOrder(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )
            logger.info("Input Validated")
            response = place_limit_order(client=client,limit_order=limit_order)
            for key, value in response.items():
                typer.echo(f"{key}: {value}")
        else:
            raise ValueError("Order type must be MARKET or LIMIT.")
    except Exception as e:
        logger.error(f"CLI Error: {e}")
        typer.echo(f"Error: {e}")
if __name__ == "__main__":
    app()