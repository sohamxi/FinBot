from crewai import Task
from textwrap import dedent

class TradingStrategyTasks:
    def develop_trading_strategy(self, agent, asset_class, instrument_name, market, signals, insights):
        return Task(
            description=dedent(f"""\
                [TRADING STRATEGY]
                Develop a complete Python trading strategy for {asset_class} instrument "{instrument_name}" in the {market} market.
                This strategy should leverage the recommended signals and insights generated in the trading opportunity phase:
                  - Signals from table: {market.lower()}_{asset_class.lower()}_trade_recommendations
                  - Insights from table: {market.lower()}_{asset_class.lower()}_insights

                The strategy must include:
                1. Entry and exit criteria based on the detected signals.
                2. Integrated risk management (stop-loss, take-profit, and position sizing).
                3. Modular and well-documented Python code (clear inline comments and a main function to initiate backtests/live trading).
                4. Logging and error handling to facilitate monitoring and further collaboration.

                The output should be a complete Python module ready for integration with backtesting or live trading frameworks.
                Recommended Signals:
                {signals}

                Analysis & Insights:
                {insights}
                """),
            agent=agent
        )