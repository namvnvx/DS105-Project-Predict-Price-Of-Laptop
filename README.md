# 💻 Laptop Price Analysis and Prediction on TGDD Retail Website  

## 📊 Data Collection  
- The dataset was collected from the **Thegioididong** website ([TGDD](https://www.thegioididong.com/laptop)) on **October 24, 2024**.  
- It includes **laptop prices** from various brands currently available on the market.  
- The dataset consists of **284 different laptops** and **35 variables**, including:  
  - **2 continuous variables**: ‘Latest Price’ and ‘Core Count’.  
  - **33 categorical variables**: ‘Product Name’, ‘RAM’, ‘CPU Technology’, etc.  

### ⚠️ Data Preprocessing Issues  
Two main issues were identified in the dataset:  
1. **Apple MacBook Data**:  
   - MacBooks belong to a different segment compared to most other laptops, introducing noise into the dataset.  
   - **Solution**: All MacBook data was removed.  
2. **Missing Data**:  
   - Some laptops had missing values due to the manufacturer not disclosing specific specifications.  
   - **Solution**: Missing values were categorized as `NaN` and handled accordingly.  

## 📈 II. Analysis and Model Selection  

After evaluating **R² (coefficient of determination)** and **MSE (Mean Squared Error)**, we initially selected a **third-degree polynomial regression model** for training. However, after training, the results were:  

| Metric  | Value |  
|---------|----------------|  
| **R²**  | 0.9936  |  
| **MSE** | 3.77 × 10²⁰ |  

### ⚠️ Issue with Polynomial Model  
- Despite the high **R² score**, the **MSE was extremely large**, indicating poor generalization.  
- To address this, we applied **feature selection** by considering:  
  - **Correlation coefficients** for continuous variables.  
  - **ANOVA (Analysis of Variance)** for categorical variables.  
- Additionally, we tested a model using **all available features**.  

### 🏆 Final Model Selection  
| Feature Selection Method | R² Score | MSE |  
|--------------------------|------------|-------------------|  
| **Selected Features (High Coefficients)** | 0.8313 | 1.04 × 10¹⁴ |  
| **All Features** | 0.8493 | 9.40 × 10¹³ |  

🔹 Although the **R² scores** of these models were lower than the **polynomial regression**, the **MSE was significantly lower**, indicating better performance.  

✅ **Final Decision:** We selected the **model using all features** as the primary model for laptop price prediction.  
