from crewai import Task
from textwrap import dedent

class BuildTradingStrategiesTasks:
    def develop_trading_strategy(self, agent, asset_class, instrument_name, market, signals, insights):
        return Task(
            description=dedent(f"""\
                [TRADING STRATEGY - DEVELOPMENT]
                Develop a complete Python trading strategy for {asset_class} instrument "{instrument_name}" in the {market} market.
                The strategy should leverage the recommended trading signals and insights generated from the analysis phase.
                
                Requirements:
                1. Define clear entry and exit conditions based on the provided signals.
                2. Incorporate integrated risk management (stop-loss, take-profit, and dynamic position sizing).
                3. Use a modular and well-documented Python code structure with clear inline comments.
                4. Include a main function or equivalent entry point for both backtesting and live trading.
                
                Recommended Signals:
                {signals}
                
                Analysis & Insights:
                {insights}
                
                The output should be a robust Python module, ready for integration with a backtesting framework.
                """),
            agent=agent
        )

    def backtest_trading_strategy(self, agent, asset_class, instrument_name, market, strategy_code):
        return Task(
            description=dedent(f"""\
                [TRADING STRATEGY - BACKTEST]
                Evaluate the performance of the developed trading strategy for {asset_class} instrument "{instrument_name}" in the {market} market using historical data.
                
                Requirements:
                1. Integrate the provided strategy code into a backtesting framework (e.g., Backtrader, Zipline, or Freqtrade).
                2. Simulate historical trading using realistic parameters (commissions, slippage, etc.).
                3. Compute key performance metrics such as Profit/Loss, Sharpe Ratio, Maximum Drawdown, Win Rate, and generate an equity curve.
                4. Produce a comprehensive backtest report including detailed trade logs and visualizations.
                
                Data Source: Use the analysis-ready dataset from preprocessing (e.g., table: {market.lower()}_{asset_class.lower()}_analysis_ready).
                Store Results:
                   - Database: {market.lower()}_{asset_class.lower()}_backtest_results
                   - PDF Report: /reports/backtest/{market.lower()}/{asset_class.lower()}/{instrument_name}_backtest_{{TIMESTAMP}}.pdf
                """),
            agent=agent
        )

    def optimize_strategy_parameters(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING STRATEGY - OPTIMIZATION]
                Fine-tune the parameters of the trading strategy developed for {asset_class} instrument "{instrument_name}" in the {market} market.
                
                Requirements:
                1. Apply optimization techniques (e.g., grid search, Bayesian optimization) to the backtested strategy.
                2. Optimize for key performance metrics while minimizing risk factors.
                3. Generate a detailed report outlining optimized parameters and performance improvements.
                
                Store Optimized Results:
                   - Database: {market.lower()}_{asset_class.lower()}_optimized_strategies
                   - PDF Report: /reports/optimization/{market.lower()}/{asset_class.lower()}/{instrument_name}_optimization_{{TIMESTAMP}}.pdf
                """),
            agent=agent
        )

    def select_best_trading_strategy(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING STRATEGY - SELECTION]
                Evaluate all developed and optimized trading strategies for {asset_class} instrument "{instrument_name}" in the {market} market.
                
                Requirements:
                1. Compare strategies based on backtest performance, risk-adjusted returns, and stability under varying market conditions.
                2. Establish ranking criteria including signal confluence, risk/reward ratio, and execution feasibility.
                3. Select the best-performing strategy and document the selection rationale.
                
                Store the Selected Strategy:
                   - Database: {market.lower()}_{asset_class.lower()}_selected_strategy
                   - PDF Report: /reports/selection/{market.lower()}/{asset_class.lower()}/{instrument_name}_selected_strategy_{{TIMESTAMP}}.pdf
                """),
            agent=agent
        )