from crewai import Task
from textwrap import dedent

class TradingOpportunityTasks:
    def scan_technical_signals(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING OPPORTUNITY]
                Scan for technical trading signals for {asset_class} instrument {instrument_name} in the {market} market
                by leveraging the outputs from the technical analysis (table: {market.lower()}_{asset_class.lower()}_technical_analysis).

                Signal categories include:
                1. Trend Signals:
                   - Moving average crossovers, trend breakouts, momentum confirmations.
                2. Pattern Signals:
                   - Chart pattern completions, candlestick, volume, and harmonic patterns.
                3. Indicator Signals:
                   - RSI divergences, MACD crossovers, Bollinger Band setups.

                Store signals in:
                Database Table: {market.lower()}_{asset_class.lower()}_technical_signals
                Fields: signal_type, timeframe, strength, confidence, entry_price, stop_loss, target

                These signals integrate with the outputs of the market analysis phase.
                """),
            agent=agent
        )

    def identify_fundamental_triggers(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING OPPORTUNITY]
                Identify fundamental triggers for {asset_class} instrument {instrument_name} in the {market} market.
                Utilize the fundamental analysis results (table: {market.lower()}_{asset_class.lower()}_fundamental_analysis) as a key input.

                For different asset classes, consider:
                - Stocks: earnings surprises, valuation disconnects, corporate events.
                - Crypto: protocol upgrades, token economics shifts.
                - Currency: economic data releases, policy shifts.
                - Commodities: supply/demand changes, inventory reports.

                Store findings in:
                Database Table: {market.lower()}_{asset_class.lower()}_fundamental_triggers
                Include trigger details as well as impact assessment.
                """),
            agent=agent
        )

    def detect_sentiment_opportunities(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING OPPORTUNITY]
                Identify sentiment-based trading opportunities for {asset_class} instrument {instrument_name} in the {market} market.
                Leverage the outputs from the sentiment analysis (table: {market.lower()}_{asset_class.lower()}_sentiment_analysis).

                Monitor sentiment trends from:
                1. News sources.
                2. Social media platforms.
                3. Broader market sentiment indicators.

                Store detected opportunities in:
                Database Table: {market.lower()}_{asset_class.lower()}_sentiment_opportunities
                with sentiment scores, source credibility, and signal strength.
                """),
            agent=agent
        )

    def analyze_market_regime_opportunities(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING OPPORTUNITY]
                Identify trading opportunities based on market regime analysis for {asset_class} instrument {instrument_name} in the {market} market.
                Utilize the regime detection results (table: {market.lower()}_{asset_class.lower()}_market_regimes).

                Evaluate:
                - Regime transition points.
                - Changes in volatility and correlation.
                - Seasonal and cyclical patterns.

                Store opportunities in:
                Database Table: {market.lower()}_{asset_class.lower()}_regime_opportunities
                including regime context and trading parameters.
                """),
            agent=agent
        )

    def identify_statistical_arbitrage(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING OPPORTUNITY]
                Detect statistical arbitrage opportunities for {asset_class} instrument {instrument_name} in the {market} market.
                Combine insights from the statistical (table: {market.lower()}_{asset_class.lower()}_statistical_analysis) and market analysis phases.

                Focal points:
                - Mean reversion setups, pairs trading.
                - Cross-market inefficiencies.
                - Derivative mispricing analyses.

                Store these opportunities in:
                Database Table: {market.lower()}_{asset_class.lower()}_statistical_arbitrage
                with complete opportunity parameters.
                """),
            agent=agent
        )

    def generate_trade_recommendations(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING OPPORTUNITY]
                Synthesize signals from technical, fundamental, sentiment, regime, and statistical analyses to generate actionable trade recommendations
                for {asset_class} instrument {instrument_name} in the {market} market.

                The recommendation should detail:
                - Entry, stop-loss, and target prices.
                - Position sizing and risk management rules.
                - Confluence of signals from the earlier tasks.

                Store the recommendations in:
                Database Table: {market.lower()}_{asset_class.lower()}_trade_recommendations

                This task integrates the outputs of the Identify Trading Signals phase.
                """),
            agent=agent
        )

    def prioritize_opportunities(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING OPPORTUNITY]
                Rank and prioritize all detected trading opportunities for {asset_class} instrument {instrument_name} in the {market} market.
                Consider criteria such as signal strength, risk/reward ratio, market context, and portfolio fit.

                Store the final prioritized list in:
                Database Table: {market.lower()}_{asset_class.lower()}_opportunity_rankings
                """),
            agent=agent
        )

    def generate_opportunity_report(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [TRADING OPPORTUNITY]
                Compile a comprehensive trading opportunity report for {asset_class} instrument {instrument_name} in the {market} market.
                The report should integrate:
                - All detected signals (technical, fundamental, sentiment, etc.).
                - Detailed analysis of each opportunity.
                - Prioritized recommendations and risk assessments.

                Store the full report as:
                Database Table: {market.lower()}_{asset_class.lower()}_opportunity_reports
                and generate a PDF:
                /reports/opportunities/{market.lower()}/{asset_class.lower()}/{instrument_name}_{TIMESTAMP}.pdf

                This report supports higher management decision making.
                """),
            agent=agent
        )