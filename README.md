# Coronavirus Twitter MapReduce Analysis

## Project Overview
This project analyzes ~1.1 billion geotagged tweets from 2020 to study how discussion of COVID-19 spread across languages, countries, and time.

Because the dataset is too large for traditional analysis, I implemented a parallel MapReduce pipeline in Python + Bash on a multi-processor server.

- **Mapper:** scans each day of tweets and counts hashtag usage by **language** and **country**
- **Reducer:** aggregates all daily outputs into global totals
- **Visualization:** generates plots for the top 10 languages/countries and a time-series over 2020

## Results

## Coronavirus Language Analysis
![Coronavirus Language Analysis](plots/coronavirus_lang.png)

## Coronavirus Country Analysis
![Coronavirus Country Analysis](plots/coronavirus_country.png)

## Korean Hashtag Language Analysis
![Korean Language Analysis](plots/korean_lang.png)

## Korean Hashtag Country Analysis
![Korean Country Analysis](plots/korean_country.png)
