from crewai import Task
from textwrap import dedent

class PortfolioManagementTasks:
    def monitor_portfolio_risk(self, agent, portfolio_id, market):
        return Task(
            description=dedent(f"""\
                [PORTFOLIO RISK MONITORING]
                Continuously monitor and track real-time risk metrics for portfolio "{portfolio_id}" in the {market} market.
                
                Key risk metrics to capture:
                - Value at Risk (VaR)
                - Total and per-asset exposure
                - Portfolio volatility and standard deviation
                - Inter-asset correlations
                - Stress test outcomes
                
                Integration:
                - Connect to real-time market data feeds.
                - Update risk metrics dynamically.
                
                Store results as follows:
                - Database Table: {market.lower()}_portfolio_risk
                - Log File: /reports/portfolio_risk/{portfolio_id}_{{TIMESTAMP}}.json
                
                These outputs support ongoing risk management and feed into downstream tasks.
                """),
            agent=agent
        )

    def set_stop_loss_take_profit(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [STOP-LOSS & TAKE-PROFIT]
                Determine the optimal stop-loss and take-profit levels for {asset_class} instrument "{instrument_name}" in the {market} market.
                
                Analysis guidelines:
                - Analyze historical price volatility and chart support/resistance levels.
                - Assess risk/reward ratios based on technical indicators.
                - Generate recommended levels with alternative scenarios as needed.
                
                Store recommendations in:
                - Database Table: {market.lower()}_{asset_class.lower()}_risk_management
                - Output Report: /reports/risk_management/{instrument_name}_{{TIMESTAMP}}.json
                
                This task’s output aids in automated trade management for risk mitigation.
                """),
            agent=agent
        )

    def adjust_position_sizes(self, agent, portfolio_id, market):
        return Task(
            description=dedent(f"""\
                [POSITION SIZING ADJUSTMENT]
                Dynamically adjust and optimize position sizes for portfolio "{portfolio_id}" in the {market} market.
                
                Considerations include:
                - Current portfolio risk exposure.
                - Market volatility and changing conditions.
                - Investor's risk tolerance and predefined risk limits.
                - Quantitative methods (e.g., Kelly Criterion, mean-variance optimization).
                
                Store the adjusted position data in:
                - Database Table: {market.lower()}_position_sizing
                - Recommendation Report: /reports/position_sizing/{portfolio_id}_{{TIMESTAMP}}.json
                
                This task updates trade sizes to maintain risk within acceptable levels.
                """),
            agent=agent
        )

    def construct_optimal_portfolio(self, agent, market, investment_horizon, risk_tolerance):
        return Task(
            description=dedent(f"""\
                [OPTIMAL PORTFOLIO CONSTRUCTION]
                Develop an optimized portfolio allocation strategy for the {market} market based on:
                - Investment Horizon: {investment_horizon}
                - Risk Tolerance: {risk_tolerance}
                
                Approach:
                - Utilize optimization techniques such as Modern Portfolio Theory (MPT) and mean-variance optimization.
                - Incorporate asset correlation and diversification principles.
                - Provide recommended allocation percentages for each asset class.
                
                Final outputs to store:
                - Database Table: {market.lower()}_optimal_portfolio
                - PDF Report: /reports/portfolio_construction/{market.lower()}_optimal_portfolio_{{TIMESTAMP}}.pdf
                
                The optimized portfolio allocation serves as actionable guidance for balancing risk versus return.
                """),
            agent=agent
        )