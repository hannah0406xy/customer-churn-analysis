import numpy as np
import pandas as pd
from scipy.optimize import minimize
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

def load_customer_data():
    """Load the processed customer data with CLV and targeting segments."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'data', 'processed', 'modeling_data_with_targeting.csv')
    df = pd.read_csv(data_path)
    print("\nData loaded successfully.")
    print(f"Number of customers: {len(df):,}")
    print("\nRevenue statistics:")
    print(df['rev_Mean'].describe())
    return df

def two_part_tariff_profit(params, customer_data, segment=None):
    """Calculate profit for a two-part tariff pricing model."""
    fixed_fee, variable_rate = params
    
    # Filter by segment if specified
    if segment:
        mask = customer_data['targeting_segment'] == segment
        data = customer_data[mask]
    else:
        data = customer_data
    
    # Calculate revenue components
    fixed_revenue = fixed_fee * len(data)
    
    # Convert standardized revenue to actual revenue
    actual_revenue = 100 + data['rev_Mean'] * 50  # $50-$150 range
    variable_revenue = variable_rate * actual_revenue.sum()
    total_revenue = fixed_revenue + variable_revenue
    
    # Calculate costs
    variable_costs = 0.6 * variable_revenue
    fixed_costs = 5 * len(data)  # $5 fixed cost per customer
    total_costs = variable_costs + fixed_costs
    
    # Calculate profit
    profit = total_revenue - total_costs
    
    return -profit

def optimize_pricing(customer_data, segment=None):
    """Optimize two-part tariff pricing for maximum profit."""
    # Initial guess and bounds
    initial_params = (25, 0.1)  # ($25 fixed fee, 10% variable rate)
    bounds = [(0, 100), (0, 0.3)]  # Fixed fee: $0-$100, Variable rate: 0-30%
    
    # Optimize
    result = minimize(
        two_part_tariff_profit,
        initial_params,
        args=(customer_data, segment),
        bounds=bounds,
        method='L-BFGS-B'
    )
    
    # Calculate profit at optimal parameters
    optimal_profit = -result.fun
    
    return {
        'fixed_fee': result.x[0],
        'variable_rate': result.x[1],
        'profit': optimal_profit,
        'success': result.success,
        'message': result.message
    }

def simulate_retention_scenarios(customer_data, base_pricing, discount_rates=[0.05, 0.10, 0.15]):
    """
    Simulate the impact of retention discounts on profit.
    
    Parameters:
    -----------
    customer_data : pd.DataFrame
        Customer data with usage and CLV information
    base_pricing : dict
        Base pricing parameters
    discount_rates : list
        List of discount rates to simulate
    
    Returns:
    --------
    pd.DataFrame
        Results of retention discount scenarios
    """
    results = []
    
    for rate in discount_rates:
        # Apply discount to variable rate
        discounted_rate = base_pricing['variable_rate'] * (1 - rate)
        
        # Calculate profit with discount
        profit = -two_part_tariff_profit(
            (base_pricing['fixed_fee'], discounted_rate),
            customer_data
        )
        
        results.append({
            'discount_rate': rate,
            'new_variable_rate': discounted_rate,
            'profit': profit,
            'profit_change': profit - base_pricing['profit']
        })
    
    return pd.DataFrame(results)

def main():
    # Load data
    customer_data = load_customer_data()
    
    # Calculate actual revenue statistics
    actual_revenue = 100 + customer_data['rev_Mean'] * 50
    print("\nActual revenue statistics ($50-$150 range):")
    print(actual_revenue.describe())
    
    # Optimize pricing for overall customer base
    print("\nOptimizing pricing for overall customer base...")
    base_optimization = optimize_pricing(customer_data)
    print("\nBase Pricing Optimization Results:")
    print(f"Optimal fixed fee: ${base_optimization['fixed_fee']:.2f}")
    print(f"Optimal variable rate: {base_optimization['variable_rate']*100:.1f}%")
    print(f"Expected profit: ${base_optimization['profit']:,.2f}")
    
    # Calculate per-customer metrics
    n_customers = len(customer_data)
    avg_profit_per_customer = base_optimization['profit'] / n_customers
    print(f"\nPer-customer metrics:")
    print(f"Average profit per customer: ${avg_profit_per_customer:.2f}")
    
    # Optimize pricing for each targeting segment
    print("\nOptimizing pricing for each segment...")
    segment_results = {}
    for segment in customer_data['targeting_segment'].unique():
        print(f"\nSegment: {segment}")
        segment_optimization = optimize_pricing(customer_data, segment)
        segment_results[segment] = segment_optimization
        print(f"Optimal fixed fee: ${segment_optimization['fixed_fee']:.2f}")
        print(f"Optimal variable rate: {segment_optimization['variable_rate']*100:.1f}%")
        print(f"Expected profit: ${segment_optimization['profit']:,.2f}")
        
        # Calculate segment size and per-customer metrics
        segment_size = len(customer_data[customer_data['targeting_segment'] == segment])
        avg_profit_per_customer = segment_optimization['profit'] / segment_size
        print(f"Segment size: {segment_size:,} customers")
        print(f"Average profit per customer: ${avg_profit_per_customer:.2f}")
    
    # Save results
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    # Save base optimization results
    with open(os.path.join(base_dir, 'models', 'pricing_optimization.json'), 'w') as f:
        json.dump({
            'base_optimization': base_optimization,
            'segment_optimization': segment_results
        }, f, indent=2)
    
    # Simulate retention discount scenarios
    retention_scenarios = simulate_retention_scenarios(
        customer_data,
        base_optimization
    )
    
    # Save retention scenarios
    retention_scenarios.to_csv(
        os.path.join(base_dir, 'models', 'retention_scenarios.csv'),
        index=False
    )
    
    # Create visualizations
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=retention_scenarios,
        x='discount_rate',
        y='profit_change',
        palette='viridis'
    )
    plt.title('Profit Impact of Retention Discounts')
    plt.xlabel('Discount Rate')
    plt.ylabel('Change in Profit ($)')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'models', 'retention_discount_impact.png'))
    plt.close()
    
    # Create segment pricing comparison
    segment_pricing = pd.DataFrame([
        {
            'segment': segment,
            'fixed_fee': results['fixed_fee'],
            'variable_rate': results['variable_rate'],
            'profit': results['profit']
        }
        for segment, results in segment_results.items()
    ])
    
    plt.figure(figsize=(14, 6))
    sns.barplot(
        data=segment_pricing,
        x='segment',
        y='profit',
        palette='viridis'
    )
    plt.title('Optimal Profit by Customer Segment')
    plt.xlabel('Customer Segment')
    plt.ylabel('Profit ($)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'models', 'segment_pricing_comparison.png'))
    plt.close()
    
    print("\nPricing analysis complete. Results saved in models/ directory.")

if __name__ == '__main__':
    main() 