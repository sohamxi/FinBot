from crewai import Task
from textwrap import dedent

class DataPreprocessingTasks:
    def validate_raw_data(self, agent, asset_class, instrument_name, market, data_type):
        return Task(
            description=dedent(f"""\
                [DATA PREPROCESSING]
                Validate raw {data_type} data for {asset_class} instrument {instrument_name} sourced from /data/raw/{market.lower()}/{asset_class.lower()}.

                Checks to perform:
                - Completeness and error detection (missing values, gaps, and outliers).
                - Timestamp consistency and correct data types.
                - Compare with baseline metrics if available.

                Generate a validation report:
                Path: /data/validation_reports/{market.lower()}/{asset_class.lower()}/{instrument_name}_{data_type}_{TIMESTAMP}.json

                This report will be used to decide if re-acquisition is needed or to proceed with cleaning.
                """),
            agent=agent
        )

    def clean_time_series_data(self, agent, asset_class, instrument_name, market, data_type):
        return Task(
            description=dedent(f"""\
                [DATA PREPROCESSING]
                Clean and standardize {data_type} time series data for {asset_class} instrument {instrument_name} in the {market} market.
                
                Cleaning steps include:
                - Handling missing values (forward fill, interpolation).
                - Outlier detection and correction.
                - Timezone normalization to UTC.
                - Adjust for corporate actions (if applicable).

                Store cleaned data in:
                Path: /data/cleaned/{market.lower()}/{asset_class.lower()}/{instrument_name}_{data_type}_{TIMESTAMP}.parquet

                The output from this task will be merged into a common schema for analysis.
                """),
            agent=agent
        )

    def transform_to_common_schema(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA PREPROCESSING]
                Transform the cleaned data for {asset_class} instrument {instrument_name} in the {market} market into a common schema.

                Requirements:
                - Standardize column names, data types, and timestamp formats.
                - Normalize currency and volume units.
                - Merge various data sources (historical, real-time, corporate actions) into a unified data model.

                Store the transformed data in a central analysis database:
                Database Table: {market.lower()}_{asset_class.lower()}_normalized

                This common schema will be the primary input for market analysis and signal processing.
                """),
            agent=agent
        )

    def calculate_technical_indicators(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA PREPROCESSING]
                Calculate technical indicators from the normalized data for {asset_class} instrument {instrument_name} in the {market} market.
                
                Indicators to compute:
                - Moving averages (SMA, EMA)
                - Momentum indicators (RSI, MACD)
                - Volatility measures (Bollinger Bands, ATR)
                - Volume-based indicators (OBV)

                Store calculated indicators with metadata:
                Database Table: {market.lower()}_{asset_class.lower()}_indicators
                """),
            agent=agent
        )

    def generate_derived_features(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA PREPROCESSING]
                Generate derived features for {asset_class} instrument {instrument_name} in the {market} market.

                Feature categories:
                - Price-derived metrics (returns, volatility)
                - Volume-derived metrics (VWAP)
                - Time-based features (seasonality, periodicity)
                - Custom features based on cross-asset correlations

                Store derived features:
                Database Table: {market.lower()}_{asset_class.lower()}_features
                Include metadata and transformation logic.
                """),
            agent=agent
        )

    def quality_assurance_check(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA PREPROCESSING]
                Perform a final quality assurance check on the preprocessed data for {asset_class} instrument {instrument_name} in the {market} market.

                Verification steps:
                - Completeness and consistency across merged sources.
                - Statistical validation and business logic tests.
                - Cross-referencing against raw data snapshots.

                Generate a QA report:
                Path: /data/qa_reports/{market.lower()}/{asset_class.lower()}/{instrument_name}_{TIMESTAMP}.json

                This report confirms that the data is ready for downstream market analysis.
                """),
            agent=agent
        )

    def prepare_analysis_ready_dataset(self, agent, asset_class, instrument_name, market):
        return Task(
            description=dedent(f"""\
                [DATA PREPROCESSING]
                Create the final analysis-ready dataset for {asset_class} instrument {instrument_name} in the {market} market.

                Steps:
                - Merge cleaned data, technical indicators, and derived features.
                - Include market context data.
                - Perform indexing and versioning.

                Store the final dataset:
                Database Table: {market.lower()}_{asset_class.lower()}_analysis_ready
                Along with a comprehensive data dictionary and metadata.

                This dataset will underpin all subsequent market analysis tasks.
                """),
            agent=agent
        )