from crewai import Task
from textwrap import dedent

class TradingBacktestTasks:
    def backtest_trading_strategy(self, agent, asset_class, instrument_name, market, strategy_code):
        return Task(
            description=dedent(f"""\
                [TRADING BACKTEST]
                Evaluate the performance of the trading strategy for {asset_class} instrument "{instrument_name}" in the {market} market using historical data.

                Requirements:
                1. Utilize historical data from the analysis-ready dataset:
                   - Data Source: Database Table: {market.lower()}_{asset_class.lower()}_analysis_ready
                2. Integrate the provided strategy code (from the Trading Strategy phase):
                   - Strategy Code: {strategy_code}
                3. Include performance metrics such as:
                   - Profit/Loss, Sharpe Ratio, Maximum Drawdown, Win Rate, and Equity Curve.
                4. Simulate realistic trade executions, factoring in commission, slippage, and risk management parameters.
                5. Generate a comprehensive backtest report that includes:
                   - Detailed trade logs, performance metrics, and visualizations (e.g., equity curve plots).
                6. Store the results as follows:
                   - Database Table: {market.lower()}_{asset_class.lower()}_backtest_results
                   - PDF Report: /reports/backtest/{market.lower()}/{asset_class.lower()}/{instrument_name}_backtest_{{TIMESTAMP}}.pdf

                Instructions:
                - Validate all configuration parameters before the backtest.
                - Document any assumptions or limitations of the backtesting process.
                - Ensure the strategy code is modular and can be executed within the chosen backtesting framework (e.g., Backtrader, Zipline, or Freqtrade).

                The output must provide a robust backtesting evaluation to inform further strategy optimization or live deployment.
                """),
            agent=agent
        )