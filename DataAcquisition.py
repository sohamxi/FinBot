from crewai import Task
from textwrap import dedent

class DataAcquisitionTasks:
    def fetch_multi_frequency_ohlc(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA ACQUISITION]
                Collect OHLC data for {asset_class} instrument {instrument_name} in the {market} market across multiple frequencies (e.g., 5m, 15m, 1h, daily).

                Guidelines:
                - Use asset-class and market appropriate data sources (e.g., AlphaVantage for stocks, Binance for crypto).
                - Respect API rate limits and include robust error handling.
                - Store all raw data in a shared repository for downstream processing:
                  Path: /data/raw/{market.lower()}/{asset_class.lower()}/{instrument_name}/ohlc_{{FREQUENCY}}_{{YYYY-MM}}.parquet

                The output of this task will be used as the input for the data preprocessing pipeline.
                """),
            agent=agent,
            expected_output="Parquet files containing raw OHLC data at multiple frequencies for the specified instrument stored in the designated repository."
        )

    def stream_real_time_ticks(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA ACQUISITION]
                Capture real-time tick data for {asset_class} instrument {instrument_name} in the {market} market.

                Guidelines:
                - Use streaming APIs appropriate to the asset class (e.g., Polygon.io WebSocket for stocks, exchange feeds for crypto).
                - Respect rate limits and include reconnection logic.
                - Store output in JSON format in a common repository:
                  Path: s3://{market.lower()}_market/{asset_class.lower()}/tick_data/{instrument_name}_{{TIMESTAMP}}.json

                This task's output is essential for real-time analysis and will be merged later with historical data.
                """),
            agent=agent,
            expected_output="JSON files containing real-time tick data stored in the appropriate S3 bucket."
        )

    def collect_orderbook_option_data(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA ACQUISITION]
                Fetch order book depth and derivatives data for {asset_class} instrument {instrument_name} in the {market} market.

                Guidelines:
                - Use the appropriate data source based on asset class (e.g., Finnhub for stocks, exchange APIs for crypto).
                - Respect rate limits and include error handling.
                - Store the results in the shared repository:
                  Order Book Path: /data/raw/{market.lower()}/{asset_class.lower()}/orderbook/{instrument_name}_{{SOURCE}}_{{TIMESTAMP}}.json
                  Derivatives Path: /data/raw/{market.lower()}/{asset_class.lower()}/derivatives/{instrument_name}_{{EXPIRY_DATE}}_{{TYPE}}.csv

                These outputs will be ingested by subsequent preprocessing tasks.
                """),
            agent=agent,
            expected_output="JSON file for order book data and CSV file for derivatives data stored in the respective directories."
        )

    def scrape_news_sentiment(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA ACQUISITION]
                Scrape and extract news and social media sentiment for {asset_class} instrument {instrument_name} in the {market} market.

                Guidelines:
                - Use multiple sources (e.g., Moneycontrol/Benzinga for stocks, CoinDesk for crypto, Twitter & Reddit for social sentiment).
                - Process data with a sentiment model (e.g., HuggingFace).
                - Store output in shared directories:
                  News: /data/raw/{market.lower()}/{asset_class.lower()}/news/{instrument_name}_{{DATE}}.json
                  Social: /data/raw/{market.lower()}/{asset_class.lower()}/social/{instrument_name}_{{PLATFORM}}_{{DATE}}.csv

                The resulting sentiment data will be used for both preprocessing and market analysis.
                """),
            agent=agent,
            expected_output="JSON file for news sentiment and CSV file for social media sentiment stored in the respective directories."
        )

    def ingest_corporate_actions(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA ACQUISITION]
                Aggregate corporate events or relevant market events for {asset_class} instrument {instrument_name} in the {market} market.

                Guidelines:
                - For stocks, pull data from SEC EDGAR/BSE feeds; for crypto, gather token event data; for currencies and commodities, pull relevant event indicators.
                - Store data within a common storage:
                  Database Table: {market.lower()}_{asset_class.lower()}_events
                  Fields: instrument_name, event_type, date, value, currency, details

                This output will later be combined with other data sets during preprocessing.
                """),
            agent=agent,
            expected_output="Confirmation of corporate actions data ingestion into the specified database table, along with relevant details."
        )

    def fetch_economic_alt_data(self, agent, asset_class, market):
        return Task(
            description=dedent(f"""\
                [DATA ACQUISITION]
                Collect economic indicators and alternative data pertinent to {asset_class} in the {market} market.

                Guidelines:
                - For traditional assets, use FRED or MOSPI; for crypto, collect network and mining data; for currencies/commodities, include respective economic indicators.
                - Store output:
                  Economic Data: /data/raw/{market.lower()}/{asset_class.lower()}/economics/{{INDICATOR}}_{{PERIOD}}.csv
                  Alternative Data: /data/raw/{market.lower()}/{asset_class.lower()}/alt_data/{{TYPE}}_{{DATE}}.{{FORMAT}}

                These data sets will be used by preprocessing and analysis tasks.
                """),
            agent=agent,
            expected_output="CSV files containing economic and alternative data stored in the appropriate directories."
        )

    def validate_and_log_compliance(self, agent, asset_class, market):
        return Task(
            description=dedent(f"""\
                [DATA ACQUISITION]
                Perform compliance checks during data collection for {asset_class} in the {market} market.

                Guidelines:
                - Validate compliance with SEBI/SEC, AML/KYC, and other regulatory frameworks.
                - Generate logs and audit files:
                  Log Path: /data/compliance/{market.lower()}/{asset_class.lower()}/regulatory_{{DATE}}.log
                  Audit File: /data/compliance/{market.lower()}/{asset_class.lower()}/audit.csv

                Ensure that all acquired data meets regulatory standards. This metadata is crucial for downstream processing and analysis.
                """),
            agent=agent,
            expected_output="Compliance log and audit file generated and stored in the designated directory."
        )