# Coronavirus Twitter MapReduce Analysis

## Project Overview

This project analyzes about 1.1 billion geotagged tweets collected throughout 2020 to examine how COVID-19 discussions spread across countries, languages, and time. Using Python, Bash, and the MapReduce programming, I built a processing pipeline capable of handling large-scale social media data on a multi-processor server.

The project tracks hashtag usage related to the coronavirus and transforms raw tweet data into visual insights through country-level, language-level, and temporal analysis. The workflow consists of a mapper that processes daily tweet files, reducers that aggregate results into global totals, and visualization scripts that generate comparative bar charts and yearly trend plots.

---

## Takeaways

Through this project, I gained experience working with extremely large scale datasets, building a scalable data processing pipeline, and figuring out how to work with multilingual social media text and geographic metadata to analyze hashtag trends across countries and languages. Additionally, I used JSON to organize structured output data and created visualizations with Matplotlib to better communicate temporal and geographic patterns within the dataset.

---

## Pipeline Components

### 1. Mapper (`map.py`)
Processes daily tweet files and counts hashtag usage by both language and country, generating intermediate `.lang` and `.country` files for each day of 2020.

### 2. Reducer (`reduce.py`)
Combines all intermediate language and country files into aggregated global totals.

### 3. Visualization (`visualize.py`)
Creates bar charts displaying the top 10 countries or languages associated with a selected hashtag.

### 4. Trend Analysis (`alternative_reduce.py`)
Produces a time-series visualization showing how hashtag usage changed throughout 2020.

## Results

## Coronavirus Top Languages With English #coronavirus
![Coronavirus Language Analysis](plots/coronavirus_lang.png)

## Coronavirus Top Countries With English #coronavirus 
![Coronavirus Country Analysis](plots/coronavirus_country.png)

## Korean Hashtag Top Language 
![Korean Language Analysis](plots/korean_lang.png)

## Korean Hashtag Top Country
![Korean Country Analysis](plots/korean_country.png)


## Hashtag Usage Over Time (2020)

- The blue line represents the English hashtag (#coronavirus), while the orange line represents the Korean hashtag (#코로나바이러스).

![Hashtag Timeline](plots/hashtag_timeseries.png)
