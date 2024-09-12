### **Fitness Ring Market Research Project**

📲 This project aims to identify the most suitable European market for selling the Fitness Ring by analyzing various factors such as GDP, obesity rates, physical activity, sedentary hours, and demographics in different countries.

## Table of Contents

- [Introduction](#introduction)
- [Dataset and Cleaning Process](#dataset-and-cleaning-process)
- [Business Objective](#business-objective)
- [Key Insights](#key-insights)
- [Conclusions](#conclusions)

## Introduction

🚀  The Fitness Ring is a lightweight wearable that tracks heart rate, physical activity, and more. Our goal is to determine which European country is the most promising market for expanding the Fitness Ring business.

## Dataset and Cleaning Process

👉 For the analysis, two sources were used:

1. **Individual Health Data**: This dataset contains detailed information about individuals with heart disease, including their age, sex, obesity rates, sedentary hours per week, activity hours per week, and the country they reside in.
   
2. **Country GDP Data**: Instead of using a dataset from Kaggle as originally planned, GDP data was obtained via the World Bank API. This change aligns with the bootcamp's project guidelines to combine API and database sources.

The combination of these sources allows us to determine which country in Europe would be the most suitable market for the Fitness Ring. By considering health-related metrics and economic factors:
- **Individual Health Data** helps us understand the prevalence of heart disease, obesity, physical activity, and other related factors in different countries.
- **Country GDP Data** serves as a measure of economic prosperity, indicating potential willingness to pay for health-related products like the Fitness Ring.

  **Data Cleaning Process**
  
To prepare the data for analysis, the following steps were performed:

 - **Loading Data**: Data from the CSV files and the API were loaded into pandas DataFrames.
 - **Handling Missing Values**: No missing or null values were found.
 - **Data Type Conversion**: Ensured that columns had the correct data types, particularly converting numerical columns to floats.
 - **Removing Duplicates**: No duplicates were found.
 - **Filtering Data**: Filtered the dataset to include only relevant rows, specifically focusing on European countries.

The cleaned data was then used to identify key insights and make informed decisions about the most suitable European market for the Fitness Ring.

### 📊 Key Insights

1. **Germany as the Top Market**: Germany emerged as the best market due to:
   - **High Obesity Rates**: One of the highest in Europe, signaling a need for health solutions.
   - **Active Population**: Strong interest in physical fitness, despite obesity concerns.
   - **Low Sedentary Hours**: Germans spend fewer hours inactive, showing potential for health tech adoption.
   - **Strong GDP**: As Europe’s largest economy, Germany has high purchasing power for health-related products.
   -  ![image](https://github.com/user-attachments/assets/b203f9a1-dc5a-45ac-975a-2ed39e37269a)
   -  ![image](https://github.com/user-attachments/assets/48e6d9d5-fd58-4031-8894-2fabac9a6dc8)
   -  ![image](https://github.com/user-attachments/assets/a63dc14e-f105-4593-8e06-1db1fb34ad25)
   -  ![image](https://github.com/user-attachments/assets/4b8ebaa2-6dcf-47f9-bad3-e6226e2e2042)




2. **Growing Health Awareness**: Germany’s active yet health-conscious population is likely to adopt the Fitness Ring for tracking progress and improving well-being.

3. **Incentivizing Behavior Change**: The Fitness Ring can motivate healthier habits, aligning with Germany’s fitness trends and reducing sedentary lifestyles.

### Conclusion

💡 Based on the analysis of health data and economic factors, Germany presents the ideal market for launching the Fitness Ring in Europe. Germany offers the greatest potential for successful market entry. The Fitness Ring's ability to track and promote healthier habits can address health challenges while tapping into the growing interest in personal well-being.





