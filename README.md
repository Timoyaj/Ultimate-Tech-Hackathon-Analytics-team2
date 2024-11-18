# SME Market Entry Navigator - ETL Pipeline Project

## Overview
This project aims to build an ETL (Extract, Transform, Load) pipeline for the SME Market Entry Navigator to help small and medium-sized enterprises (SMEs) assess market opportunities in West Africa. The project integrates multiple datasets related to macroeconomic indicators, trade flows, and logistics to provide insights that support strategic market entry decisions.

## Project Structure
```
Ultimate-Tech-Hackathon-Analytics-team2/
├── data/                           # Raw data files
├── notebooks/                      # Jupyter notebooks for exploration
├── scripts/                        # Python scripts for the ETL process
├── output/                         # Processed data and database files
├── config/                         # Configuration files
├── logs/                           # Log files for debugging and monitoring
├── tests/                          # Unit tests for ETL components
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── .gitignore                      # Git ignore file
```

## Getting Started

### Prerequisites
- Python 3.7+
- `pip` package manager
- Install dependencies from `requirements.txt` using the command:
  ```
  pip install -r requirements.txt
  ```

### Folder Setup
1. Create a folder named `data` in the root directory and place all raw data files in it. Make sure the following files are available:
   - `indicators.csv`
   - `International_LPI_from_2007_to_2023_0.xlsx`
   - `Goods UN Comtrade data_11_15_2024_11_6_8.csv`
   - `servicesun comtrade_data11_15_2024_11_14_7.csv`
   - `NTM-Indicators-Measure-Sector.csv`

2. Create other folders as per the project structure for storing outputs, logs, and tests.

### Running the ETL Pipeline
To execute the ETL pipeline, run the `data_processing_pipeline.py` script located in the `scripts/` folder:
```
python scripts/data_processing_pipeline.py
```
This script will:
1. Extract data from various sources.
2. Transform data by cleaning, integrating, and standardizing it.
3. Load the transformed data into an SQLite database and export a CSV backup.

## Project Components
### 1. Data Extraction
- **Macroeconomic Indicators**: Extracted from the `indicators.csv` file.
- **FDI Data**: Extracted via the World Bank API.
- **Logistics Performance Index**: Extracted from `International_LPI_from_2007_to_2023_0.xlsx`.
- **Trade Data (Goods and Services)**: Extracted from UN Comtrade datasets.
- **NTM Data**: Extracted from `NTM-Indicators-Measure-Sector.csv`.

### 2. Data Transformation
- Clean the extracted data, remove unnecessary columns, rename columns, and handle missing values.
- Integrate all datasets into a single dataset for analysis.

### 3. Data Loading
- Store the final dataset in an SQLite database (`sme_market_entry_navigator.db`).
- Export a CSV backup (`integrated_market_data.csv`) to the `output/` folder.

## Configuration
- API keys, file paths, and other configuration options can be stored in the `config/config.yaml` file.

## Logs
- Logs for tracking ETL operations are stored in the `logs/` folder to facilitate debugging and monitoring.

## Testing
- Unit tests are available in the `tests/` folder to validate the ETL components.
- To run the tests, use:
  ```
  python -m unittest discover tests
  ```

## Test Coverage Report
To generate a test coverage report for the project, use the following commands:

1. **Install `coverage` Package**:
   ```sh
   pip install coverage
   ```

2. **Run Tests with Coverage**:
   ```sh
   coverage run -m unittest discover tests
   ```

3. **Generate Coverage Report**:
   ```sh
   coverage report
   ```
   This command will provide a summary of the coverage for each file in your project.

4. **Generate an HTML Report** (Optional):
   ```sh
   coverage html
   ```
   The HTML report will be generated in a folder named `htmlcov/`. Open the `index.html` file to view detailed coverage information.

**User Stories for Each Component**

**Team Member A: Data Extraction, Loading, and Preprocessing**

* **User Story 1: Data Extraction and Loading**
  * Title: As a user, I want the system to load market data seamlessly.
  * Description: I want the system to load data from the database without any manual intervention so that I can access the latest data for analysis and insights.
  * Acceptance Criteria:
    * Data should be extracted from the SQLite database (sme_market_entry_navigator.db) into a pandas DataFrame.
    * Data should be in a clean and accessible format for downstream analysis.
    * The loading function should handle connection open/close smoothly, with error handling.
* **User Story 2: Data Preprocessing**
  * Title: As a data analyst, I want the data to be preprocessed and ready for analysis.
  * Description: I need the data to be cleaned, missing values handled, and formatted consistently so that I can run analyses and machine learning models without issues.
  * Acceptance Criteria:
    * The data should have no missing values or null values that affect model performance.
    * Columns should be renamed and standardized for consistency.
    * The cleaned data should be saved as a DataFrame that is ready for analysis.

**Team Member B: Visual Analytics Implementation**

* **User Story 3: Visualize FDI Trends**
  * Title: As an SME looking to expand, I want to see FDI trends over time for a specific country.
  * Description: I want a line chart that shows the Foreign Direct Investment trends so that I can understand historical investment levels in the country.
  * Acceptance Criteria:
    * Users can select a country, and the system displays an FDI trend chart.
    * The chart should clearly label the year on the x-axis and FDI value (in USD) on the y-axis.
* **User Story 4: Visualize GDP Growth Rate**
  * Title: As an economist, I want to see GDP growth rate trends for selected countries.
  * Description: I want to see the annual GDP growth rate in a bar chart to understand economic performance over time.
  * Acceptance Criteria:
    * Users can select a country and view a bar chart of GDP growth rate.
    * The chart should display the year and corresponding growth rate (%) clearly.
* **User Story 5: Visualize Logistics Performance Index (LPI) Trends**
  * Title: As a logistics company, I want to see the LPI trends for a country to understand infrastructure and logistics performance.
  * Description: I need an LPI trend chart that shows how well the country has performed over the years in logistics.
  * Acceptance Criteria:
    * Users can select a country and view an LPI trend chart.
    * The x-axis should represent years, while the y-axis should represent LPI score.
* **User Story 6: Market Attractiveness Score**
  * Title: As an investor, I want to see a market attractiveness score for different countries.
  * Description: I need to see a summary score that evaluates multiple indicators to determine the attractiveness of a market.
  * Acceptance Criteria:
    * The system should calculate the market attractiveness score based on selected indicators.
    * The score should be displayed clearly as a single metric on the dashboard.

**Team Member C: Predictive Analytics and Machine Learning**

* **User Story 7: Predict FDI Trends Using Linear Regression**
  * Title: As an investor, I want to see predicted FDI trends for the next few years.
  * Description: I need a prediction of FDI values so that I can make informed decisions on potential investments in the country.
  * Acceptance Criteria:
    * Users can view a prediction of FDI trends for the next 5 years.
    * The system should display both historical and predicted data on the same chart for easy comparison.
* **User Story 8: Predict FDI with Machine Learning (Random Forest)**
  * Title: As a market analyst, I want to understand the drivers of FDI with deeper insights.
  * Description: I need insights into what economic indicators contribute to FDI levels so that I can better understand the market.
  * Acceptance Criteria:
    * The system should provide a Random Forest model that predicts FDI values based on indicators.
    * Users should see model performance metrics (Mean Squared Error, R² Score).
    * Feature importance should be visualized, highlighting which indicators contribute the most to FDI.

**Team Member D: Recommendation Engine and Integration**

* **User Story 9: Get Recommendations for Market Entry**
  * Title: As an SME owner, I want personalized recommendations for market entry.
  * Description: I need recommendations on which countries might be the best fit for my business based on economic and logistical factors.
  * Acceptance Criteria:
    * Users can use sliders to input criteria like GDP Growth Rate, Ease of Doing Business Score, and LPI Score.
    * The system should filter countries based on user criteria and show the list of recommended countries.
* **User Story 10: Machine Learning-Enhanced Recommendations**
  * Title: As a market strategist, I want recommendations that are enhanced by machine learning.
  * Description: I need recommendations that not only filter data but also use machine learning predictions to estimate FDI potential for a given set of criteria.
  * Acceptance Criteria:
    * The recommendation engine should predict potential FDI values using a trained Random Forest model.
    * Users should see recommended countries along with a prediction of potential FDI for each.
* **User Story 11: Integrate All Features into a User-Friendly Dashboard**
  * Title: As an end-user, I want all insights and visualizations to be available in a single, intuitive dashboard.
  * Description: I want a user-friendly interface that brings together visualizations, analytics, and recommendations for a holistic view of market opportunities.
  * Acceptance Criteria:
    * The dashboard should allow users to select a country and view all visualizations related to that country (FDI trend, GDP growth, LPI, correlation heatmap).
    * Users should be able to access predictive analytics and recommendations easily.
    * All components should be integrated seamlessly without any issues or inconsistencies.

**Summary of User Stories**

**Team Member A:**
* Data extraction and loading.
* Data preprocessing to prepare for further analysis.

**Team Member B:**
* Create visual analytics (FDI trends, GDP growth, LPI trends).
* Calculate and display the market attractiveness score.

**Team Member C:**
* Predict future FDI values using linear regression.
* Train a Random Forest model to provide insights into FDI drivers and predict FDI levels.

**Team Member D:**
* Develop an interactive recommendation engine for market entry.
* Integrate machine learning predictions for deeper insights in recommendations.
* Integrate all features into a user-friendly dashboard for seamless user experience.

*Each user story can serve as a mini-project, helping team members understand their roles from an end-user perspective and implement features that address specific user needs. Let me know if you need more details or adjustments to fit your project goals!*
## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please contact the project maintainers at [tertimothy@gmail.com].
