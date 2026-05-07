# Coronavirus Twitter MapReduce Analysis

## Project Overview
This project analyzes ~1.1 billion geotagged tweets from 2020 to study how discussion of COVID-19 spread across languages, countries, and time.

Because the dataset is too large for traditional analysis, I implemented a parallel MapReduce pipeline in Python + Bash on a multi-processor server.

- **Mapper:** scans each day of tweets and counts hashtag usage by **language** and **country**
- **Reducer:** aggregates all daily outputs into global totals
- **Visualization:** generates plots for the top 10 languages/countries and a time-series over 2020

## Results

### English hashtag (#coronavirus)

**Top languages**
![Top languages](plots/lang_coronavirus.png)

**Top countries**
![Top countries](plots/country_coronavirus.png)

### Korean hashtag (#코로나바이러스)

**Top languages**
![Top languages](plots/lang_korean_hashtag.png)

**Top countries**
![Top countries](plots/country_korean_hashtag.png)

### Hashtag usage over time (2020)
- The blue line indicates the english hashtag (#coronavirus) and the orange line indicates the Korean hashtag (#코로나바이러스).
![Time series](plots/hashtag_timeseries.png)

## Key Findings
- The English hashtag appears broadly across countries/languages.
- The Korean hashtag is concentrated in South Korea and mostly in Korean-language tweets.
- One of the reasons for low use of (#코로나바이러스) can be due to the tweet being written in Korean, but with english hashtag attached to them. 
- Both show a large spike in early 2020 followed by decline through the year.

