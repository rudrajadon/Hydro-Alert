# Streamflow Prediction for Mahi Basin Catchments using LSTM

## Objective  
To develop a data-driven LSTM model that predicts daily streamflow discharge for seven catchments in the Mahi basin using rainfall and meteorological data from the CAMELS-IND dataset.

## Methods  
- **Data:** CAMELS-IND (precipitation and meteorological features)  
- **Model:** LSTM neural network  
- **Task:** Regression (predict discharge, not classification)  
- **Evaluation:** RMSE, R², plots  

## Results  

### Summary Table  
| Catchment | RMSE   | R²    |
|-----------|--------|-------|
| 10004     | 234.75 | -7.37 |
| 10005     | 42.52  | -0.14 |
| 10008     | 509.31 | -0.09 |
| 10010     | 212.43 | 0.08  |
| 10011     | 242.95 | 0.08  |
| 10013     | 44.79  | -0.63 |
| 10014     | 66.83  | 0.09  |

### Interpretation  
- Catchments **10010**, **10011**, and **10014** show slight predictive skill (**R² > 0**).  
- Most catchments still require improvement (negative R² indicates performance worse than mean prediction).  
- Possible reasons include catchment heterogeneity, missing data, or the need for better feature engineering and tuning.

---

## Future Work: Flood Thresholds  

Once discharge prediction is reliable, we will classify flood/danger stages using hydrological thresholds:

1. **Return Period Exceeding Bankfull Stage**  
   - Use statistical analysis to determine discharge values that exceed the river’s bankfull level (e.g., 10-year return flood).

2. **Actual Danger Water Level and Corresponding Discharge**  
   - Use observed danger-level data and its equivalent discharge to set actionable thresholds.

These thresholds will allow transformation of discharge predictions into **flood alerts**.

---

## Next Steps  
- Improve model performance through:  
  - Data cleaning  
  - Feature selection  
  - Hyperparameter optimization  
- After better performance is achieved, integrate flood classification based on hydrological thresholds.
