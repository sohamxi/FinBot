from crewai import Task
from textwrap import dedent

class TradeExecutionTasks:
    def execute_trades(self, agent, account_id, orders, market):
        return Task(
            description=dedent(f"""\
                [TRADE EXECUTION - ORDER PLACEMENT]
                Execute live buy and sell orders for account "{account_id}" in the {market} market.

                Instructions:
                1. Integrate with the appropriate broker API (e.g., Alpaca API, Interactive Brokers API) to send orders.
                2. Validate each order from the provided 'orders' list. Each order should detail:
                   - Order type (market, limit, stop, etc.)
                   - Asset class, instrument name, quantity, and price limits.
                   - Time-in-force and any specific instructions.
                3. Implement robust error handling, order confirmation, and logging mechanisms.
                4. Record each executed trade and confirmation details in a common repository.
                
                Store outputs:
                - Database Table: {market.lower()}_trade_executions
                - Log file: /reports/trade_executions/{account_id}_{{TIMESTAMP}}.json

                The outputs from this task will feed into real-time monitoring and performance evaluation processes.
                """),
            agent=agent
        )

    def monitor_trade_execution(self, agent, account_id, market):
        return Task(
            description=dedent(f"""\
                [TRADE EXECUTION - MONITORING]
                Continuously monitor live trade execution for account "{account_id}" in the {market} market.

                Instructions:
                1. Connect with the broker API to track the status of orders, capturing:
                   - Order fill rates and statuses (e.g., partially filled, fully filled, canceled).
                   - Execution timings and any errors encountered.
                2. Update and log the real-time performance and order details.
                3. Generate periodic performance reports and alerts, if necessary.
                
                Store monitoring data:
                - Database Table: {market.lower()}_order_execution_monitoring
                - Alert logs: /reports/trade_monitoring/{account_id}_{{TIMESTAMP}}.json

                This task provides continuous feedback on live trading, supporting risk management and adaptive strategy adjustments.
                """),
            agent=agent
        )