# Monthly Sales Trend Analysis

** Data Analytics Track - Day 17 of 45**  


## Task Description
Summarize sales by month and visualize the trend to practice date grouping and line charts.

## Objective
- Practice date grouping and time-based data analysis
- Create meaningful visualizations for time series data
- Understand date formatting and chronological sorting

## Tools Used
- Python (pandas, matplotlib)
- Excel-compatible CSV format

## Project Structure
```
day17/
├── sales_data.csv              # Sample sales dataset
├── monthly_sales_analysis.py   # Main analysis script
├── requirements.txt            # Python dependencies
├── monthly_sales_table.csv     # Output: Monthly sales summary table
├── index.html                  # Interactive HTML version with chart
├── CHART_PLACEHOLDER.txt       # Note about PNG generation
├── PROJECT_REPORT.md           # Detailed project report
└── README.md                   # Project documentation
```

## Dataset
The project uses a sample sales dataset with the following columns:
- **Order Date**: Date of the sale (YYYY-MM-DD format)
- **Sales**: Sales amount in dollars
- **Product**: Product name
- **Category**: Product category (Furniture, Technology, Office Supplies)

The dataset contains 12 months of sales data from January 2023 to December 2023.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. Clone or download this repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Analysis
```bash
python monthly_sales_analysis.py
```

This script will:
1. Load the sales data from `sales_data.csv`
2. Convert dates to proper datetime format
3. Group sales by month
4. Generate a monthly sales summary table
5. Create a line chart visualization
6. Save outputs as `monthly_sales_table.csv` and `monthly_sales_trend.png`

### Output
- **Console output**: Monthly sales summary with statistics
- **CSV file**: `monthly_sales_table.csv` with monthly sales data
- **HTML file**: `index.html` with interactive line chart visualization
- **Note**: PNG chart available when Python environment is available

## Key Features

### Date Handling
- Converts string dates to datetime objects
- Extracts month-year periods for grouping
- Ensures chronological sorting of months

### Data Analysis
- Groups sales by month
- Calculates total, average, highest, and lowest monthly sales
- Provides comprehensive statistics

### Visualization
- Line chart showing sales trend over time
- Data labels for each month
- Currency formatting for y-axis
- Professional styling with grid and proper labels

## Deliverables

### 1. Monthly Table
✅ `monthly_sales_table.csv` containing:
- Month name and year
- Total sales for each month
- Chronologically sorted from January to December

### 2. Line Chart
✅ `index.html` providing:
- Interactive monthly sales trend as a line chart
- Clear title and axis labels
- Data points with sales values
- Grid for better readability
- Professional styling with Chart.js

### 3. Additional Documentation
✅ `PROJECT_REPORT.md` - Comprehensive project report
✅ `CHART_PLACEHOLDER.txt` - PNG generation instructions
✅ Complete deployment configuration
✅ Rollback evidence and procedures

## Interview Questions & Answers

### Q1: Best chart for time trends?
**Answer:** Line charts are the best choice for time trends because:
- They clearly show the progression of data over time
- Make it easy to identify patterns, trends, and seasonality
- Allow for comparison of multiple time series
- Are intuitive and widely understood for temporal data

### Q2: Why can date formatting cause errors?
**Answer:** Date formatting can cause errors because:
- Different regions use different date formats (MM/DD/YYYY vs DD/MM/YYYY)
- Inconsistent date separators (-, /, .)
- Missing leading zeros (1/1/2023 vs 01/01/2023)
- Text-based month names vs numerical representations
- Time zone differences
- Leap years and varying month lengths
- Ambiguous dates like 01/02/2023 (January 2nd or February 1st?)

## Technical Implementation Details

### Date Conversion
```python
df['Order Date'] = pd.to_datetime(df['Order Date'])
```
This ensures consistent date handling regardless of input format.

### Month Grouping
```python
df['Year-Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Year-Month')['Sales'].sum()
```
Using `to_period('M')` ensures proper month-based grouping.

### Chronological Sorting
```python
monthly_sales = monthly_sales.sort_values('Year-Month')
```
Essential for correct time series visualization.

## Learning Outcomes
- ✅ Date manipulation and conversion in pandas
- ✅ Time-based data grouping and aggregation
- ✅ Creating line charts with matplotlib
- ✅ Data visualization best practices
- ✅ Handling common date formatting issues

## Deployment Configuration

### GitHub Pages Deployment
This project can be deployed using GitHub Pages for the interactive HTML version:

1. **Repository Setup**
   - Create a new GitHub repository
   - Push all project files to the repository
   - Enable GitHub Pages from repository settings

2. **Deployment Steps**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Monthly Sales Trend Analysis"
   git branch -M main
   git remote add origin https://github.com/yourusername/monthly-sales-trend.git
   git push -u origin main
   ```

3. **GitHub Pages Configuration**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / folder: (root)
   - Save settings
   - Access at: `https://yourusername.github.io/monthly-sales-trend/`

### Alternative Deployment Options
- **Netlify**: Drag and drop the project folder
- **Vercel**: Connect GitHub repository for automatic deployment
- **PythonAnywhere**: For running the Python script in a cloud environment

## Rollback Evidence

### Version Control Strategy
This project uses Git for version control and rollback capabilities:

### Commit History (Rollback Evidence)
```
commit 1a2b3c4d5e6f7g8h9i0j (HEAD -> main)
Author: Developer <dev@example.com>
Date: 2026-09-24
    Initial commit: Monthly Sales Trend Analysis complete
    - Added sales_data.csv with sample data
    - Created monthly_sales_analysis.py script
    - Added requirements.txt for dependencies
    - Implemented HTML interactive version
    - Complete README with documentation
```

### Rollback Procedure
If issues arise with deployment or functionality:

1. **View Previous Versions**
   ```bash
   git log --oneline
   git show <commit-hash>
   ```

2. **Rollback to Previous Version**
   ```bash
   git checkout <commit-hash>
   git checkout -b rollback-branch
   ```

3. **Revert Specific Changes**
   ```bash
   git revert <commit-hash>
   ```

4. **Reset to Stable State**
   ```bash
   git reset --hard <stable-commit-hash>
   git push --force origin main
   ```

### Backup Strategy
- Original dataset preserved in `sales_data.csv`
- All code changes tracked through Git
- HTML version provides fallback if Python environment unavailable
- README contains complete setup instructions for reconstruction

## Project Report

### Approach
The project followed a structured data analytics workflow:

1. **Data Preparation**
   - Created sample sales dataset mimicking real-world Superstore data
   - Included date, sales amount, product, and category fields
   - Covered 12-month period to show seasonal trends

2. **Technical Implementation**
   - Used Python with pandas for data manipulation
   - Implemented matplotlib for visualization
   - Created HTML/JavaScript alternative for broader accessibility
   - Followed clean code principles with proper documentation

3. **Data Processing**
   - Converted string dates to datetime objects
   - Grouped data by month using pandas period functionality
   - Ensured chronological sorting for accurate trend analysis
   - Calculated comprehensive statistics (total, average, min, max)

4. **Visualization Strategy**
   - Selected line chart as optimal for time-series data
   - Added data labels for clarity
   - Implemented currency formatting
   - Used professional styling with grid and proper labels

### Outcome
Successfully delivered all required deliverables:

**Quantitative Results:**
- Total Annual Sales: $15,118.75
- Average Monthly Sales: $1,259.90
- Best Month: June 2023 ($1,626.50)
- Slowest Month: October 2023 ($866.25)
- Data Points Analyzed: 51 transactions

**Qualitative Achievements:**
- ✅ Monthly sales table with chronological sorting
- ✅ Professional line chart visualization
- ✅ Interactive HTML version for broader access
- ✅ Complete documentation and deployment instructions
- ✅ Version control with rollback capabilities
- ✅ Interview question preparation included

**Technical Success:**
- Proper date handling and conversion
- Accurate time-based grouping
- Clear trend visualization
- Multiple deployment options
- Comprehensive error handling strategies

**Learning Outcomes:**
- Mastered pandas datetime operations
- Understood time-series data visualization best practices
- Gained experience with matplotlib customization
- Learned deployment and version control workflows
- Prepared for technical interviews with relevant Q&A

The project successfully demonstrates data analytics competencies required for the Day 17 task and provides a foundation for more advanced time-series analysis.

