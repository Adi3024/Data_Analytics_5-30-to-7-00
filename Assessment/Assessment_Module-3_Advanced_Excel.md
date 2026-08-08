Theme: Business Problem Framing & KPI Identification

  Dataset: https://www.kaggle.com/datasets/carrie1/ecommerce-data

***Section A : Concept Application***

**Q-1** 
What is the first step an analyst should take before opening a dataset to investigate flat revenue despite increased traffic ?

**ANSWER**
1. The first step an analyst should take is to understand the business problem and business context before opening the dataset. This includes understanding the business model, industry/sector, process flow, objectives, and key performance indicators (KPIs). 

2. After defining the problem (e.g., why revenue is flat despite increased traffic), the analyst can frame the right business 
   questions and then analyze the relevant data. 


**Q-2**
What specific characteristics distinguish a "Key Performance Indicator" (KPI) from a standard business metric?

**ANSWER**
- A Key Performance Indicator (KPI) is a measurable value that shows how effectively a business is achieving its strategic goals. A 
  standard business metric measures business activity, while a KPI is directly linked to business objectives and helps evaluate performance.

**Characteristics**
a. Time-Bound
b. Measurable
c. Actionable
d. Relevant
e. Goal-oriented

**Difference Between KPI and Business Metric**

i. KPI should be 
- Measures progress toward a business goal
- Strategic
- Helps in decision-making

ii. Business Metric should be 
- Measures general business activity
- Operational
- Used for monitoring
stomer Repeat Rate as either
Descriptive or Diagnostic KPIs and state 


**Q-3**
Classify Average Order Value (AOV) and Customer Repeat Rate as either Descriptive or Diagnostic KPIs and State the questions they answer.

**ANSWER**
Average Order Value (AOV) : is a Descriptive KPI because it summarizes past performance by showing the average value of each order. It answers "What happened?"

Customer Repeat Rate : is a Diagnostic KPI because it helps explain why sales or revenue may be increasing or decreasing by measuring customer loyalty and repeat purchasing behavior. It answers "Why did it happen?"

|          KPI         |     Type    |                          Answer                              |
| -------------------- | ------------| ------------------------------------------------------------ |
|Average Order Value |Descriptive KPI|What is the average amount spent by a customer per order?     |
|Customer Repeat Rate|Diagnostic KPI |Are customers returning to make repeat purchases?             |


**Q-4**
Provide one justified reason to choose Excel and one reason to choose Power BI for analyzing Monthly Revenue.

**ANSWER**
EXCEL : It is ideal for data analysis using formulas, Pivot Tables, and charts, making it quick and easy to calculate and summarize 
        monthly revenue for small to medium-sized datasets.

POWER BI : It is better for handling large datasets, providing advanced data modeling, and creating interactive dashboards and reports for monthly revenue analysis.


**Q-5**
Is "Number of Customers" a valid Diagnostic KPI for revenue trends? Justify by comparing Descriptive vs Diagnostic logic.

**ANSWER**
Is "Number of Customers" a valid Diagnostic KPI for revenue trends? - NO
It is a Descriptive KPI because it only tells how many customers the business has during a given period. It describes what happened but does not explain why revenue increased or decreased.

| Descriptive KPI              | Diagnostic KPI                     |
| ---------------------------- | ---------------------------------- |
| Tells **what happened**      | Explains **why it happened**       |
| Example: Number of Customers | Example: Customer Repeat Rate, AOV |
| Summarizes performance       | Identifies causes of performance   |


**Q-6**
Why is treating raw data columns (like UnitPrice) as KPIs incorrect, and what
transformation steps are required to create a meaningful KPI?

**ANSWER**
|Raw Data Column|          Why It's Not a KPI         |     After Transformation  |       Meaningful KPI         |
|---------------|-------------------------------------|---------------------------|------------------------------|
|   UnitPrice   | Shows only price of one product     | Revenue = Qty × UnitPrice | Monthly Revenue              |
|   Quantity    | Shows items sold in one transaction | Total Quantity Sold       | Total Sales Volume           |
|   InvoiceDate | Shows only the transaction date     | Group by Month            | Monthly Sales Trend          |
|   CustomerID  | Identifies a customer               | Count Unique Customers    | Customer Count / Repeat Rate |

and for the transformation werequired :
+------+-----------------------------------------------+------------------------------------------+
| Step | Action                                        | Example                                  |
+------+-----------------------------------------------+------------------------------------------+
| 1    | Clean the data                                | Remove duplicates & missing values       |
| 2    | Create calculated fields                      | Revenue = Quantity × UnitPrice           |
| 3    | Aggregate the data                            | Sum Revenue by Month                     |
| 4    | Calculate KPIs                                | Monthly Revenue, AOV, Repeat Rate        |
+------+-----------------------------------------------+------------------------------------------+



***Section B: Practical Task***

**Q-1**
Use Power Query to perform data profiling on the Online Retail dataset, identifying missing values in "CustomerID" and "Description" to quantify data quality impact on KPI accuracy.

**ANSWER**

To solve this in Excel/Power Query using the Kaggle Online Retail dataset, follow these steps:

1. Load the dataset into Excel:
   - Open Excel
   - Data -> Get Data -> From Text/CSV
   - Select the ecommerce dataset file (CSV/Excel)
   - Load it to the Power Query Editor

2. Apply column type conversion:
   - InvoiceNo -> Text
   - StockCode -> Text
   - Description -> Text
   - Quantity -> Whole Number
   - InvoiceDate -> Date/Time
   - UnitPrice -> Decimal Number
   - CustomerID -> Whole Number
   - Country -> Text

3. Use Power Query Profile options:
   - In Power Query Editor, go to View -> Data Profiling
   - Enable Column Quality, Column Distribution, and Column Profile
   - Review missing value percentages for each field

4. Identify the two critical quality issues demanded in the question:
   - CustomerID missing values
   - Description missing values

Power Query profiling on the Online Retail dataset shows the following data quality issue:

| Column | Total Rows | Missing Values | Missing % | KPI Impact |
| ------ | ---------- | -------------- | --------- | ---------- |
| CustomerID | 541,909 | 135,080 | 24.9% | Customer-level KPIs are incomplete; customer count, repeat rate, and retention metrics become unreliable |
| Description | 541,909 | 1,454 | 0.27% | Product-level analysis is affected, but the impact is small compared with CustomerID |

5. Quantification of KPI accuracy impact:
   - CustomerID null rate = 135,080 / 541,909 * 100 = 24.9%
   - Description null rate = 1,454 / 541,909 * 100 = 0.27%

6. Business interpretation:
   - CustomerID missing values are a major problem because the dataset cannot reliably compute unique customer counts, repeat customer rate, customer retention, and customer segmentation.
   - Since 24.9% of rows are missing CustomerID, customer-based KPIs will be built on a partial customer base. This directly reduces the accuracy of repeat-rate, active customer, and customer KPI analysis.
   - Description missing values are less severe (0.27%) but still affect product/product-category reporting. If the Description is blank, product-level analysis cannot classify the transaction product correctly.

7. Recommended Power Query cleaning steps:
   - Remove or flag rows with null CustomerID before customer-level KPI calculations
   - Replace blank Description with a standard text such as "Missing Description"
   - Or create a product lookup/fallback using StockCode if Description is blank
   - Keep revenue/amount rows for gross revenue and order-level calculations, because orders can still contribute to sales totals even if CustomerID is missing

8. KPI-level conclusion:
   - Total revenue and order-level KPIs can still be computed from the dataset
   - Customer KPI accuracy is significantly impacted because the missing CustomerID rate is high
   - Product KPI accuracy is mildly impacted because Description missing is low

So, after profiling in Power Query:

- CustomerID missing values should be treated as a data quality issue affecting customer dimension accuracy
- Description missing values should be treated as a product metadata quality issue affecting product reporting and classification
- The final KPI dashboard should use filtered or validated customer records for customer-based KPIs, and clearly document the data quality limitation for customer repeat-rate calculations
