# Telecom_user_analytics

**Table of content**

- [Telecom User Analytics](#Telecom_user_analytics)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Install](#install)
  - [Data](#data)
  - [Features](#features)
    - [Data Exploration](#data-exploration)
    - [Scripts](#scripts)
    - [Test](#test)
    - [Travis CI](#travis-ci)

## Overview

This repository analyzes the data of TelleCo, a company in Greece. The outcome of the analytics will be usefull to determine for a wealthy investor whether the company is worth selling or buying.

## Requirements
  Python 3.5 and above, Pip and MYSQL
  The visualization are made using plotly

## Install
```
git clone https://github.com/Micky373/Telecom_user_analytics.git
cd Telecom_user_analytics
pip install -r requirements.txt
```

## Data
  - The data used in the project is generated automatically by TellCo systems.
  - The data is [here](https://docs.google.com/spreadsheets/d/1UXgtCVtB75-tkEfwGEV4pEw_uBcvXX3J/edit?usp=sharing&ouid=105193269694034938380&rtpof=true&sd=true) - extracted from a month of aggregated data on xDR. 
  - The features described can be found [here](https://docs.google.com/spreadsheets/d/1EDo8PyBRGMu5n3DoP5NfhxxSq_9yA5ro/edit?usp=sharing&ouid=105193269694034938380&rtpof=true&sd=true).

## Features

### Data Exploration
  - Data exploration is done in the notebooks folder the notebooks are named as:
        - user_overview_analysis.ipynb
        - user_engagement_analysis.ipynb
        - user_satisfaction_analysis.ipynb
        - user_experience_analysis.ipynb

### Scripts
 - All the scripts used by the notebooks are inside the scripts folder.

### Test
 - Tests for the scripts are inside the tests folder.

### Travis CI
  - The file .travis.yml contains the configuration for Travis.
