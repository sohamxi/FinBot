from crewai import Task
from textwrap import dedent

class MarketAnalysisTasks:
    def perform_technical_analysis(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [MARKET ANALYSIS]
                Using the analysis-ready dataset from preprocessing (table: {market.lower()}_{asset_class.lower()}_analysis_ready), perform a comprehensive technical analysis for {asset_class} instrument {instrument_name} in the {market} market.

                Analysis includes:
                - Trend and momentum analysis
                - Chart and candlestick pattern recognition
                - Analysis of key technical indicators (MA, RSI, MACD)

                Store outcomes in:
                Database Table: {market.lower()}_{asset_class.lower()}_technical_analysis

                These results feed directly into the trading signals and recommendations.
                """),
            agent=agent
        )

    def perform_fundamental_analysis(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [MARKET ANALYSIS]
                Analyze fundamental data for {asset_class} instrument {instrument_name} using economic indicators and corporate events
                (integrated in the normalized data table: {market.lower()}_{asset_class.lower()}_normalized).

                Components:
                - Core ratios, financial metrics, and industry comparisons (for stocks).
                - Network and token economics for crypto.
                - Economic and political factors for currencies/commodities.

                Store results:
                Database Table: {market.lower()}_{asset_class.lower()}_fundamental_analysis

                Outcomes from this analysis are crucial for identifying longer-term trading opportunities.
                """),
            agent=agent
        )

    def analyze_market_sentiment(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [MARKET ANALYSIS]
                Analyze market sentiment related to {asset_class} instrument {instrument_name} in the {market} market.

                Steps:
                - Process sentiment data from news and social media (sourced from preprocessing).
                - Aggregate sentiment indicators (including Fear & Greed, volume analysis, etc.).

                Store compiled sentiment analysis:
                Database Table: {market.lower()}_{asset_class.lower()}_sentiment_analysis

                The sentiment analysis output will be used to complement technical and fundamental signals.
                """),
            agent=agent
        )

    def detect_market_regimes(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [MARKET ANALYSIS]
                Identify market regimes for {asset_class} instrument {instrument_name} in the {market} market
                using the integrated analysis-ready dataset.

                Analysis comprises:
                - Regime classification (trending, neutral, volatile).
                - Transition and duration analysis.
                - Correlation studies with related instruments.

                Store the regime analysis:
                Database Table: {market.lower()}_{asset_class.lower()}_market_regimes

                This information helps explain signal behaviors and refine trading recommendations.
                """),
            agent=agent
        )

    def perform_statistical_analysis(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [MARKET ANALYSIS]
                Execute a statistical analysis on the analysis-ready dataset for {asset_class} instrument {instrument_name} in the {market} market.

                Analysis includes:
                - Descriptive and time-series statistics.
                - Hypothesis testing and regression models.

                Store the statistical analysis results:
                Database Table: {market.lower()}_{asset_class.lower()}_statistical_analysis

                These metrics provide additional context for signal validation.
                """),
            agent=agent
        )

    def detect_anomalies(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [MARKET ANALYSIS]
                Detect anomalies in the market behavior for {asset_class} instrument {instrument_name} in the {market} market.

                Methods:
                - Price, volume, and behavioral anomaly detection.
                - Statistical outlier and pattern deviation analysis.

                Store anomaly detection results:
                Database Table: {market.lower()}_{asset_class.lower()}_anomalies

                Anomaly detection supports risk management and the refinement of trading signals.
                """),
            agent=agent
        )

    def generate_scenario_analysis(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [MARKET ANALYSIS]
                Develop scenario analyses for {asset_class} instrument {instrument_name} in the {market} market.

                Components:
                - Define multiple market scenarios (bullish, bearish, stress).
                - Conduct risk analysis including VaR and stress testing.
                - Project potential impacts on price and market correlations.

                Store the scenario analysis:
                Database Table: {market.lower()}_{asset_class.lower()}_scenarios

                These scenarios are key inputs to identifying actionable trading opportunities.
                """),
            agent=agent
        )

    def generate_insights_report(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [MARKET ANALYSIS]
                Synthesize all analysis results (technical, fundamental, sentiment, statistical, regimes, anomalies, and scenarios) for {asset_class} instrument {instrument_name} in the {market} market to generate comprehensive insights.

                Report components:
                - Executive summary and key findings.
                - Detailed breakdown of analytical components.
                - Actionable recommendations for management.

                Store insights and recommendations:
                Database Table: {market.lower()}_{asset_class.lower()}_insights
                PDF Report: /reports/{market.lower()}/{asset_class.lower()}/{instrument_name}_analysis_{TIMESTAMP}.pdf

                This report will be used by the trading opportunity identification tasks.
                """),
            agent=agent
        )