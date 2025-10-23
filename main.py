import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Basic Black-Scholes European option pricer.

    Parameters:
    - S : Spot price of the underlying asset
    - K : Strike price
    - T : Time to maturity in years
    - r : Risk-free interest rate (annualized)
    - sigma : Volatility of the underlying asset (annualized)
    - option_type : 'call' or 'put'

    Returns:
    - Option price (float)
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    return price

# Parameters
S = 100      # Current stock price
K = 100      # Strike price
T = 1        # Time to maturity (1 year)
r = 0.05     # Risk-free rate (5%)
sigma = 0.2  # Volatility (20%)

# Price a call and a put
call_price = black_scholes(S, K, T, r, sigma, 'call')
put_price = black_scholes(S, K, T, r, sigma, 'put')

print(f"Call Price: {call_price:.2f}")
print(f"Put Price: {put_price:.2f}")
