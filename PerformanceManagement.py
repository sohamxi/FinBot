from crewai import Task
from textwrap import dedent

class PerformanceReportTasks:
    def generate_performance_report(self, agent, account_id, market):
        return Task(
            description=dedent(f"""\
                [PERFORMANCE REPORT]
                Generate a detailed report summarizing trading performance, risk metrics, and other key indicators for account "{account_id}" in the {market} market.
                
                The report should include:
                1. Trade Performance:
                   - Profit/Loss, win rate, and detailed trade statistics.
                   - Equity curve visualizations and cumulative returns.
                2. Risk Metrics:
                   - Value at Risk (VaR), maximum drawdown, and exposure analysis.
                   - Risk-adjusted returns (e.g., Sharpe ratio).
                3. Operational Metrics:
                   - Order execution efficiency, fill rates, and latency metrics.
                   - Portfolio turnover and diversification details.
                4. Summary & Insights:
                   - Commentary on performance trends.
                   - Recommendations for strategy adjustments.
                
                Data Sources:
                   - Backtesting results (from trading strategy backtest tasks).
                   - Live trade execution logs and monitoring data.
                   - Risk management and portfolio metrics.
                
                Store outputs as follows:
                   - PDF Report: /reports/performance/{market.lower()}/{account_id}_performance_report_{{TIMESTAMP}}.pdf
                   - Database Table: {market.lower()}_performance_reports
                    
                The final report should be clear and actionable, enabling higher management to make informed decisions.
                """),
            agent=agent
        )