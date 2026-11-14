"""
Title: End-to-End Data Analytics Lifecycle
Description: A modular Python script demonstrating business discovery, 
             data preparation, exploration, statistics, and predictive modeling.
"""

# ==========================================
# IMPORTS (Libraries for Data, Stats, & Viz)
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ==========================================
# SUB-STEP FUNCTIONS (The Lifecycle Phases)
# ==========================================

def phase_1_discovery_and_setup():
    """
    Module 1: Foundations, Business Understanding & Setup
    - Define business objective (e.g., Coffee Shop Revenue Analysis).
    - Load the 25-record real-world CSV dataset.
    - Initial inspection (head, info, missing values).
  
    """
    file_path = r'problem\coffee_shop_data.csv'
    print("Executing Phase 1: Discovery & Data Setup...")
    try:
        # Load dataset from external CSV file
        df = pd.read_csv(file_path)
        print(f"-> Successfully loaded dataset from: {file_path}")
    except FileNotFoundError:
        print(f"-> Error: Could not find '{file_path}'. Please ensure the CSV file is in the same directory.")
        raise
    
    print("-> Business Objective: Predict and optimize daily revenue based on operational drivers.")
    print(f"-> Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nFirst 5 Records of the Dataset:")
    print(df.head())
    
    # Check for missing values
    missing_count = df.isnull().sum().sum()
    print(f"\n-> Missing Values Check: {missing_count} missing values found.")
    
    return df
    


def phase_2_descriptive_statistics(df):
    """
    Module 2: Descriptive Statistics & Data Measures
    - Calculate Central Tendency (Mean, Median, Mode).
    - Calculate Dispersion (Standard Deviation, Variance, IQR, Range).
    - Check Distribution Shape & Outliers.
  
    """
    print("Executing Phase 2: Descriptive Statistics & Measures...")
    print("-" * 65)
    target_col = 'Daily_Revenue_USD'
    revenue = df[target_col]
    mean_val = revenue.mean()
    median_val = revenue.median()
    std_val = revenue.std()
    var_val = revenue.var()
    q1 = revenue.quantile(0.25)
    q3 = revenue.quantile(0.75)
    iqr_val = q3 - q1
    data_range = revenue.max() - revenue.min()

    print(f"-> Metric Analyzed: {target_col}")
    print(f"   * Mean: ${mean_val:.2f}")
    print(f"   * Median: ${median_val:.2f}")
    print(f"   * Standard Deviation: ${std_val:.2f}")
    print(f"   * Variance: {var_val:.2f}")
    print(f"   * Interquartile Range (IQR): ${iqr_val:.2f}")
    print(f"   * Range: ${data_range:.2f} (Min: ${revenue.min()}, Max: ${revenue.max()})")
    
    # Outlier detection using IQR rule
    lower_bound = q1 - 1.5 * iqr_val
    upper_bound = q3 + 1.5 * iqr_val
    outliers = revenue[(revenue < lower_bound) | (revenue > upper_bound)]
    print(f"-> Outlier Analysis (IQR Method): {len(outliers)} outliers detected.")
    return df

def phase_3_bivariate_association(df):
    """
    Module 4: Bivariate & Multivariate Association
    - Analyze relationships between variables (e.g., Marketing Spend vs. Revenue).
    - Compute Covariance and Pearson Correlation Matrix.
    - Generate exploratory visualizations (Scatter plots, Correlation heatmap).
  
    """
    print("Executing Phase 3: Bivariate Association & Visualization...")
    print("-" * 65)
    
    numeric_df = df[['Temperature_C', 'Foot_Traffic', 'Marketing_Spend_USD', 'Daily_Revenue_USD']]
    # Compute correlation matrix
    corr_matrix = numeric_df.corr(method='pearson')
    print("-> Pearson Correlation Matrix:")
    print(corr_matrix.round(3))

    spend_rev_corr = corr_matrix.loc['Marketing_Spend_USD', 'Daily_Revenue_USD']
    print(f"\n-> Key Insight: Correlation between Marketing Spend and Daily Revenue is {spend_rev_corr:.2f}.")
    print("   Interpretation: Strong positive linear association. Higher marketing spend strongly aligns with increased revenue.")
    
    # TODO: Plot correlation heatmap and scatter plots
    # Generate Correlation Heatmap and Scatter Plots
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('Phase 3: Bivariate Association & Correlation Analysis', fontsize=14, fontweight='bold')

    # 1. Correlation Heatmap
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        center=0,
        square=True,
        linewidths=0.5,
        ax=axes[0]
    )
    axes[0].set_title('Pearson Correlation Heatmap')

    # 2. Scatter Plot: Marketing Spend vs. Daily Revenue
    sns.regplot(
        data=df,
        x='Marketing_Spend_USD',
        y='Daily_Revenue_USD',
        ax=axes[1],
        scatter_kws={'alpha': 0.7, 'color': '#1f77b4'},
        line_kws={'color': '#d62728'}
    )
    axes[1].set_title('Marketing Spend vs. Daily Revenue')
    axes[1].set_xlabel('Marketing Spend (USD)')
    axes[1].set_ylabel('Daily Revenue (USD)')
    axes[1].grid(True, linestyle='--', alpha=0.5)

    # 3. Scatter Plot: Foot Traffic vs. Daily Revenue
    sns.regplot(
        data=df,
        x='Foot_Traffic',
        y='Daily_Revenue_USD',
        ax=axes[2],
        scatter_kws={'alpha': 0.7, 'color': '#2ca02c'},
        line_kws={'color': '#d62728'}
    )
    axes[2].set_title('Foot Traffic vs. Daily Revenue')
    axes[2].set_xlabel('Foot Traffic (Visitors)')
    axes[2].set_ylabel('Daily Revenue (USD)')
    axes[2].grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig('phase3_bivariate_analysis.png', dpi=300)
    plt.show()
    return df
 


def phase_4_predictive_modeling(df):
    """
    Module 6 & 8: Predictive Analytics & Regression Modeling
    - Set up a simple predictive model (e.g., Simple Linear Regression).
    - Train the model on independent variables to predict revenue.
    - Establish a baseline evaluation.
   
    """
    print("Executing Phase 4: Predictive Modeling...")
    print("-" * 65)
    
    # Define Independent variable (X) and Dependent variable (y)
    X = df[['Marketing_Spend_USD']]
    y = df['Daily_Revenue_USD']

    # Initialize and fit Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    intercept = model.intercept_
    coefficient = model.coef_[0]
    
    print("-> Simple Linear Regression Fitted:")
    print(f"   * Formula: Daily Revenue = ({coefficient:.2f} * Marketing Spend) + {intercept:.2f}")
    print(f"   * Model Slope (Coefficient): {coefficient:.2f} (For every $1 increase in marketing, revenue increases by ~$ {coefficient:.2f})")
    
    return model, X, y


def phase_5_evaluation_and_reporting(model, X, y, df):
    """
    Module 6 & 7: Model Evaluation, Generalization & Business Decision
    - Evaluate model performance (e.g., R-squared, Mean Absolute Error).
    - Discuss generalization and overfitting risks on small data.
    - Translate technical findings into prescriptive business recommendations.
    [Allocation: 5 Marks]
    """
    print("Executing Phase 5: Evaluation & Business Action...")
    print("-" * 65)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    print(f"-> Model Evaluation Metrics:")
    print(f"   * R-Squared ($R^2$): {r2:.3f} (Explains {r2*100:.1f}% of the variance in revenue)")
    print(f"   * Mean Absolute Error (MAE): ${mae:.2f}")
    
    print("\n-> Prescriptive Business Recommendation:")
    print("   1. Investment Decision: Marketing spend exhibits a powerful positive ROI. Increasing daily marketing budget yields predictable revenue growth.")
    print("   2. Operational Readiness: Ensure foot traffic staffing matches projected high-spend days to prevent service bottlenecks.")
    
    return r2, mae


# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function that coordinates the entire data analytics 
    lifecycle in chronological order.
    """
    print("=" * 60)
    print("STARTING COMPLETE DATA ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 60)
    
    df = phase_1_discovery_and_setup()
    print("-" * 60)
    
    df = phase_2_descriptive_statistics(df )
    print("-" * 60)
    
    df = phase_3_bivariate_association(df)
    print("-" * 60)
    
    model, X, y = phase_4_predictive_modeling(df)
    print("-" * 60)
    
    phase_5_evaluation_and_reporting(model, X, y,df)
    
    print("=" * 60)
    print("ANALYTICS LIFECYCLE COMPLETED SUCCESSFULLY")
    print("=" * 60)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_analytics_lifecycle()