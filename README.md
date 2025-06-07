# Binomial Option Pricing Models (Python)

This project implements binomial tree models for pricing **European** and **American** options using the **Cox-Ross-Rubinstein (CRR)** framework. It includes support for both **call** and **put** options and allows for the inclusion of continuous dividend yields.

---

## Features

- European **Call** and **Put** pricing
- American **Call** and **Put** pricing (with early exercise)
- Handles continuous dividend yield
- Customizable parameters: interest rate, volatility, maturity, etc.
- Accurate numerical pricing using binomial trees

---

## Functions

| Function Name        | Option Type     | Early Exercise | Notes                                        |
|----------------------|------------------|----------------|----------------------------------------------|
| `Euro_Call()`     | European Call     |  No          | Standard European call using binomial tree   |
| `Euro_Put()`      | European Put      |  No          | Standard European put                        |
| `American_Call()` | American Call     | Yes         | Early exercise allowed; only matters if `D > 0` |
| `American_Put()`  | American Put      | Yes         | Early exercise optimally applied             |

---

##  Function Parameters

All pricing functions accept the following arguments:

- `r` : risk-free interest rate (annual, continuously compounded)
- `D` : dividend yield (annual, continuous)
- `volatility` : stock volatility (σ)
- `S0` : initial stock price
- `K` : strike price
- `T` : time to maturity (in years)
- `n` : number of binomial steps

---

##  Example

```python

Euro_Call(0.04, 0, 0.2, 100, 105, 0.5, 1000)
Euro_Put(0.04, 0, 0.2, 100, 105, 0.5, 1000)

American_Call(0.04, 0.03, 0.2, 100, 105, 0.5, 1000) 
American_Put(0.04, 0, 0.2, 100, 105, 0.5, 1000)
