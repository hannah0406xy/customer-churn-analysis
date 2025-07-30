# Data Preprocessing Report

## Missing Values Analysis
| Column | Missing Values | Percentage | Imputation Strategy |
|--------|---------------|------------|-------------------|
| mailflag | 98,523.0 | 98.52% | Removed |
| solflag | 98,039.0 | 98.04% | Removed |
| crtcount | 96,500.0 | 96.50% | Removed |
| retdays | 96,017.0 | 96.02% | Removed |
| tot_acpt | 96,017.0 | 96.02% | Removed |
| tot_ret | 96,017.0 | 96.02% | Removed |
| REF_QTY | 95,545.0 | 95.55% | Removed |
| wrkwoman | 87,491.0 | 87.49% | Removed |
| educ1 | 86,478.0 | 86.48% | Removed |
| rmcalls | 85,777.0 | 85.78% | Removed |
| rmrev | 85,777.0 | 85.78% | Removed |
| rmmou | 85,777.0 | 85.78% | Removed |
| pcowner | 81,534.0 | 81.53% | Removed |
| div_type | 81,459.0 | 81.46% | Removed |
| occu1 | 73,353.0 | 73.35% | Unknown category |
| proptype | 71,788.0 | 71.79% | Unknown category |
| cartype | 68,412.0 | 68.41% | Unknown category |
| children | 65,928.0 | 65.93% | Unknown category |
| mailordr | 64,363.0 | 64.36% | Unknown category |
| mailresp | 62,889.0 | 62.89% | Unknown category |
| pre_hnd_price | 57,515.0 | 57.52% | Mean |
| last_swap | 57,278.0 | 57.28% | Unknown category |
| numbcars | 49,366.0 | 49.37% | Mean |
| dwllsize | 38,308.0 | 38.31% | Unknown category |
| HHstatin | 37,923.0 | 37.92% | Unknown category |
| ownrent | 33,706.0 | 33.71% | Unknown category |
| dwlltype | 31,909.0 | 31.91% | Unknown category |
| lor | 30,190.0 | 30.19% | Mean |
| income | 25,436.0 | 25.44% | Mean |
| adults | 23,019.0 | 23.02% | Mean |
| infobase | 22,079.0 | 22.08% | Unknown category |
| hnd_webcap | 10,189.0 | 10.19% | Mode |
| prizm_social_one | 7,388.0 | 7.39% | Mode |
| avg6rev | 2,839.0 | 2.84% | Median |
| avg6qty | 2,839.0 | 2.84% | Median |
| avg6mou | 2,839.0 | 2.84% | Median |
| marital | 1,732.0 | 1.73% | Mode |
| mtrcycle | 1,732.0 | 1.73% | Median |
| ethnic | 1,732.0 | 1.73% | Mode |
| age1 | 1,732.0 | 1.73% | Median |
| age2 | 1,732.0 | 1.73% | Median |
| forgntvl | 1,732.0 | 1.73% | Median |
| rv | 1,732.0 | 1.73% | Median |
| kid16_17 | 1,732.0 | 1.73% | Mode |
| truck | 1,732.0 | 1.73% | Median |
| kid6_10 | 1,732.0 | 1.73% | Mode |
| kid11_15 | 1,732.0 | 1.73% | Mode |
| kid0_2 | 1,732.0 | 1.73% | Mode |
| car_buy | 1,732.0 | 1.73% | Mode |
| creditcd | 1,732.0 | 1.73% | Mode |
| kid3_5 | 1,732.0 | 1.73% | Mode |
| change_rev | 891.0 | 0.89% | Median |
| change_mou | 891.0 | 0.89% | Median |
| hnd_price | 847.0 | 0.85% | Median |
| rev_Mean | 357.0 | 0.36% | Median |
| da_Range | 357.0 | 0.36% | Median |
| ovrrev_Range | 357.0 | 0.36% | Median |
| datovr_Mean | 357.0 | 0.36% | Median |
| roam_Mean | 357.0 | 0.36% | Median |
| rev_Range | 357.0 | 0.36% | Median |
| mou_Range | 357.0 | 0.36% | Median |
| totmrc_Range | 357.0 | 0.36% | Median |
| mou_Mean | 357.0 | 0.36% | Median |
| ovrmou_Range | 357.0 | 0.36% | Median |
| vceovr_Range | 357.0 | 0.36% | Median |
| ovrrev_Mean | 357.0 | 0.36% | Median |
| datovr_Range | 357.0 | 0.36% | Median |
| roam_Range | 357.0 | 0.36% | Median |
| ovrmou_Mean | 357.0 | 0.36% | Median |
| da_Mean | 357.0 | 0.36% | Median |
| totmrc_Mean | 357.0 | 0.36% | Median |
| vceovr_Mean | 357.0 | 0.36% | Median |
| csa | 40.0 | 0.04% | Mode |
| area | 40.0 | 0.04% | Mode |
| models | 1.0 | 0.00% | Median |
| dualband | 1.0 | 0.00% | Mode |
| refurb_new | 1.0 | 0.00% | Mode |
| phones | 1.0 | 0.00% | Median |
| eqpdays | 1.0 | 0.00% | Median |

## Categorical Variables
| Column | Unique Values | Encoded |
|--------|--------------|----------|
| new_cell | 3 | Yes |
| crclscod | 54 | Yes |
| asl_flag | 2 | Yes |
| prizm_social_one | 5 | Yes |
| csa | 798 | Yes |
| area | 19 | Yes |
| dualband | 4 | Yes |
| refurb_new | 2 | Yes |
| last_swap | 1284 | Yes |
| hnd_webcap | 3 | Yes |
| occu1 | 22 | Yes |
| ownrent | 2 | Yes |
| dwlltype | 2 | Yes |
| marital | 5 | Yes |
| mailordr | 1 | Yes |
| mailresp | 1 | Yes |
| children | 2 | Yes |
| infobase | 2 | Yes |
| cartype | 7 | Yes |
| HHstatin | 6 | Yes |
| dwllsize | 15 | Yes |
| proptype | 6 | Yes |
| ethnic | 17 | Yes |
| kid0_2 | 2 | Yes |
| kid3_5 | 2 | Yes |
| kid6_10 | 2 | Yes |
| kid11_15 | 2 | Yes |
| kid16_17 | 2 | Yes |
| creditcd | 2 | Yes |
| car_buy | 2 | Yes |

## Numerical Variables
| Column | Mean | Std | Min | Max |
|--------|------|-----|-----|-----|
| rev_Mean | 58.72 | 46.29 | -6.17 | 3843.26 |
| mou_Mean | 513.56 | 525.17 | 0.00 | 12206.75 |
| totmrc_Mean | 46.18 | 23.62 | -26.91 | 409.99 |
| da_Mean | 0.89 | 2.18 | 0.00 | 159.39 |
| ovrmou_Mean | 41.07 | 97.30 | 0.00 | 4320.75 |
| ovrrev_Mean | 13.56 | 30.50 | 0.00 | 1102.40 |
| vceovr_Mean | 13.30 | 30.06 | 0.00 | 896.09 |
| datovr_Mean | 0.26 | 3.13 | 0.00 | 423.54 |
| roam_Mean | 1.29 | 14.71 | 0.00 | 3685.20 |
| rev_Range | 44.62 | 88.14 | 0.00 | 13740.54 |
| mou_Range | 378.25 | 453.63 | 0.00 | 43050.00 |
| totmrc_Range | 8.48 | 25.79 | 0.00 | 599.98 |
| da_Range | 1.63 | 2.98 | 0.00 | 77.22 |
| ovrmou_Range | 93.94 | 188.64 | 0.00 | 4292.00 |
| ovrrev_Range | 31.35 | 62.51 | 0.00 | 2410.14 |
| vceovr_Range | 30.84 | 61.76 | 0.00 | 2409.75 |
| datovr_Range | 0.74 | 7.99 | 0.00 | 838.89 |
| roam_Range | 3.51 | 51.56 | 0.00 | 13622.97 |
| change_mou | -13.93 | 276.09 | -3875.00 | 31219.25 |
| change_rev | -1.02 | 50.36 | -1107.74 | 9963.66 |
| drop_vce_Mean | 5.96 | 8.95 | 0.00 | 232.67 |
| drop_dat_Mean | 0.04 | 0.88 | 0.00 | 207.33 |
| blck_vce_Mean | 4.02 | 10.67 | 0.00 | 385.33 |
| blck_dat_Mean | 0.03 | 1.49 | 0.00 | 413.33 |
| unan_vce_Mean | 27.78 | 38.36 | 0.00 | 848.67 |
| unan_dat_Mean | 0.03 | 0.50 | 0.00 | 81.67 |
| plcd_vce_Mean | 144.88 | 158.27 | 0.00 | 2289.00 |
| plcd_dat_Mean | 0.87 | 9.05 | 0.00 | 733.67 |
| recv_vce_Mean | 55.09 | 86.84 | 0.00 | 3369.33 |
| recv_sms_Mean | 0.05 | 2.13 | 0.00 | 517.33 |
| comp_vce_Mean | 108.89 | 118.58 | 0.00 | 1894.33 |
| comp_dat_Mean | 0.77 | 8.13 | 0.00 | 559.33 |
| custcare_Mean | 1.79 | 5.32 | 0.00 | 675.33 |
| ccrndmou_Mean | 4.67 | 12.76 | 0.00 | 861.33 |
| cc_mou_Mean | 3.68 | 10.54 | 0.00 | 602.95 |
| inonemin_Mean | 29.77 | 55.83 | 0.00 | 3086.67 |
| threeway_Mean | 0.28 | 1.09 | 0.00 | 66.00 |
| mou_cvce_Mean | 227.76 | 264.40 | 0.00 | 4514.45 |
| mou_cdat_Mean | 1.84 | 23.73 | 0.00 | 3032.05 |
| mou_rvce_Mean | 111.65 | 162.69 | 0.00 | 3287.25 |
| owylis_vce_Mean | 24.75 | 34.41 | 0.00 | 644.33 |
| mouowylisv_Mean | 28.47 | 48.96 | 0.00 | 1802.71 |
| iwylis_vce_Mean | 7.89 | 16.15 | 0.00 | 519.33 |
| mouiwylisv_Mean | 18.19 | 41.42 | 0.00 | 1703.54 |
| peak_vce_Mean | 88.48 | 103.07 | 0.00 | 2090.67 |
| peak_dat_Mean | 0.36 | 4.07 | 0.00 | 281.00 |
| mou_peav_Mean | 174.08 | 207.67 | 0.00 | 4015.35 |
| mou_pead_Mean | 0.71 | 8.41 | 0.00 | 1036.05 |
| opk_vce_Mean | 66.00 | 91.46 | 0.00 | 1643.33 |
| opk_dat_Mean | 0.42 | 4.65 | 0.00 | 309.67 |
| mou_opkv_Mean | 165.28 | 237.33 | 0.00 | 4337.89 |
| mou_opkd_Mean | 1.14 | 17.77 | 0.00 | 2922.04 |
| drop_blk_Mean | 10.04 | 15.42 | 0.00 | 489.67 |
| attempt_Mean | 145.75 | 159.35 | 0.00 | 2289.00 |
| complete_Mean | 109.67 | 119.59 | 0.00 | 1894.33 |
| callfwdv_Mean | 0.01 | 0.55 | 0.00 | 81.33 |
| callwait_Mean | 1.78 | 5.35 | 0.00 | 212.67 |
| drop_vce_Range | 5.45 | 8.55 | 0.00 | 313.00 |
| drop_dat_Range | 0.07 | 1.04 | 0.00 | 143.00 |
| blck_vce_Range | 4.75 | 12.98 | 0.00 | 739.00 |
| blck_dat_Range | 0.05 | 2.61 | 0.00 | 680.00 |
| unan_vce_Range | 20.86 | 34.64 | 0.00 | 1395.00 |
| unan_dat_Range | 0.06 | 1.05 | 0.00 | 223.00 |
| plcd_vce_Range | 74.66 | 103.94 | 0.00 | 2656.00 |
| plcd_dat_Range | 1.13 | 11.21 | 0.00 | 1352.00 |
| recv_vce_Range | 30.80 | 54.57 | 0.00 | 2109.00 |
| recv_sms_Range | 0.06 | 1.82 | 0.00 | 244.00 |
| comp_vce_Range | 54.69 | 75.13 | 0.00 | 1748.00 |
| comp_dat_Range | 1.00 | 10.14 | 0.00 | 1274.00 |
| custcare_Range | 2.12 | 5.41 | 0.00 | 690.00 |
| ccrndmou_Range | 7.09 | 18.69 | 0.00 | 1590.00 |
| cc_mou_Range | 5.99 | 16.71 | 0.00 | 1201.78 |
| inonemin_Range | 17.98 | 36.25 | 0.00 | 1879.00 |
| threeway_Range | 0.50 | 1.59 | 0.00 | 95.00 |
| mou_cvce_Range | 136.30 | 184.91 | 0.00 | 5439.61 |
| mou_cdat_Range | 2.55 | 31.54 | 0.00 | 3748.02 |
| mou_rvce_Range | 77.27 | 123.99 | 0.00 | 7146.73 |
| owylis_vce_Range | 15.64 | 23.49 | 0.00 | 699.00 |
| mouowylisv_Range | 22.61 | 41.67 | 0.00 | 1897.20 |
| iwylis_vce_Range | 6.39 | 12.34 | 0.00 | 441.00 |
| mouiwylisv_Range | 17.96 | 40.00 | 0.00 | 2011.32 |
| peak_vce_Range | 47.44 | 63.61 | 0.00 | 1291.00 |
| peak_dat_Range | 0.50 | 5.00 | 0.00 | 350.00 |
| mou_peav_Range | 107.35 | 139.44 | 0.00 | 4112.96 |
| mou_pead_Range | 1.09 | 12.73 | 0.00 | 1851.83 |
| opk_vce_Range | 38.09 | 60.94 | 0.00 | 1679.00 |
| opk_dat_Range | 0.57 | 6.21 | 0.00 | 929.00 |
| mou_opkv_Range | 113.89 | 177.86 | 0.00 | 4783.67 |
| mou_opkd_Range | 1.65 | 22.62 | 0.00 | 2881.59 |
| drop_blk_Range | 9.07 | 16.35 | 0.00 | 724.00 |
| attempt_Range | 75.17 | 104.99 | 0.00 | 2669.00 |
| complete_Range | 55.16 | 76.20 | 0.00 | 2028.00 |
| callfwdv_Range | 0.02 | 0.68 | 0.00 | 102.00 |
| callwait_Range | 1.85 | 4.59 | 0.00 | 227.00 |
| months | 18.83 | 9.66 | 6.00 | 61.00 |
| uniqsubs | 1.55 | 1.08 | 1.00 | 196.00 |
| actvsubs | 1.36 | 0.66 | 0.00 | 53.00 |
| totcalls | 2877.14 | 3790.86 | 0.00 | 98874.00 |
| totmou | 7648.36 | 8666.56 | 0.00 | 233419.10 |
| totrev | 1031.92 | 852.91 | 3.65 | 27321.50 |
| adjrev | 960.11 | 840.17 | 2.40 | 27071.30 |
| adjmou | 7546.31 | 8594.89 | 0.00 | 232855.10 |
| adjqty | 2836.37 | 3756.51 | 0.00 | 98705.00 |
| avgrev | 57.91 | 36.16 | 0.48 | 924.27 |
| avgmou | 483.73 | 438.49 | 0.00 | 7040.13 |
| avgqty | 173.55 | 167.82 | 0.00 | 3017.11 |
| avg3mou | 519.64 | 533.63 | 0.00 | 7716.00 |
| avg3qty | 180.34 | 192.73 | 0.00 | 3909.00 |
| avg3rev | 59.19 | 46.70 | 1.00 | 1593.00 |
| avg6mou | 509.63 | 496.66 | 0.00 | 7217.00 |
| avg6qty | 178.37 | 182.72 | 0.00 | 3256.00 |
| avg6rev | 58.68 | 40.76 | -2.00 | 866.00 |
| hnd_price | 101.88 | 61.01 | 9.99 | 499.99 |
| pre_hnd_price | 82.71 | 60.25 | 9.99 | 499.99 |
| phones | 1.79 | 1.31 | 1.00 | 28.00 |
| models | 1.55 | 0.90 | 1.00 | 16.00 |
| truck | 0.19 | 0.39 | 0.00 | 1.00 |
| mtrcycle | 0.01 | 0.12 | 0.00 | 1.00 |
| rv | 0.08 | 0.28 | 0.00 | 1.00 |
| lor | 6.18 | 4.74 | 0.00 | 15.00 |
| age1 | 30.95 | 22.04 | 0.00 | 99.00 |
| age2 | 20.78 | 23.76 | 0.00 | 99.00 |
| adults | 2.53 | 1.45 | 1.00 | 6.00 |
| income | 5.78 | 2.18 | 1.00 | 9.00 |
| numbcars | 1.57 | 0.63 | 1.00 | 3.00 |
| forgntvl | 0.06 | 0.23 | 0.00 | 1.00 |
| eqpdays | 391.93 | 256.48 | -5.00 | 1823.00 |

## New Engineered Features
| Feature | Description |
|---------|-------------|
| revenue_per_minute | Average revenue per minute of usage |
| care_per_month | Average customer care calls per month |
| avg_monthly_revenue | Average monthly revenue |
| avg_monthly_minutes | Average monthly minutes of usage |
| avg_monthly_calls | Average monthly number of calls |
| drop_rate | Ratio of dropped calls to placed calls |
| block_rate | Ratio of blocked calls to placed calls |
| service_quality_score | Overall service quality score |
| peak_usage_ratio | Ratio of peak time usage to total usage |
| off_peak_usage_ratio | Ratio of off-peak time usage to total usage |
| weekend_usage_ratio | Ratio of weekend usage to total usage |
| care_intensity | Customer care calls per month |
| care_quality | Ratio of completed calls to attempted calls |
| price_per_minute | Average price per minute of usage |
| device_age_months | Age of device in months |
| price_change_ratio | Ratio of current to previous handset price |
| mou_trend | Change in minutes of usage |
| rev_trend | Change in revenue |
| usage_volatility | Variability in usage patterns |
| household_size | Total number of adults and children |
| income_per_adult | Average income per adult |
| cars_per_adult | Average number of cars per adult |

## Interaction Features
| Feature | Description |
|---------|-------------|
| revenue_usage_efficiency | Interaction between revenue and usage |
| revenue_care_ratio | Interaction between revenue and customer care |
| usage_care_ratio | Interaction between usage and customer care |
| quality_revenue_impact | Impact of service quality on revenue |
| quality_usage_impact | Impact of service quality on usage |
| drop_block_interaction | Interaction between drop and block rates |
| peak_off_peak_ratio | Ratio of peak to off-peak usage |
| weekday_weekend_ratio | Ratio of weekday to weekend usage |
| usage_pattern_score | Combined usage pattern score |
| care_quality_intensity | Interaction between care quality and intensity |
| service_care_impact | Impact of service quality on customer care |
| care_trend_impact | Impact of customer care on usage trends |
| price_quality_ratio | Interaction between price and service quality |
| device_price_impact | Impact of device age on price changes |
| plan_usage_efficiency | Efficiency of plan usage |
| trend_volatility | Interaction between trends and volatility |
| revenue_usage_trend | Combined revenue and usage trends |
| quality_trend_impact | Impact of service quality on trends |
| household_income_ratio | Interaction between household size and income |
| lifestyle_score | Combined lifestyle indicators |
| demographic_usage_impact | Impact of demographics on usage |

## Composite Features
| Feature | Description |
|---------|-------------|
| customer_value_score | Overall customer value metric |
| churn_risk_score | Overall churn risk metric |
| loyalty_score | Overall customer loyalty metric |

## Feature Importance Analysis
| Feature | Importance Score |
|---------|-----------------|
| eqpdays | 0.0169 |
| device_age_months | 0.0155 |
| mou_trend | 0.0125 |
| months | 0.0110 |
| revenue_usage_trend | 0.0106 |
| rev_trend | 0.0097 |
| device_price_impact | 0.0097 |
| trend_volatility | 0.0097 |
| quality_trend_impact | 0.0095 |
| care_trend_impact | 0.0095 |
| loyalty_score | 0.0091 |
| csa | 0.0090 |
| change_mou | 0.0089 |
| mou_Range | 0.0087 |
| price_per_minute | 0.0087 |
| usage_volatility | 0.0085 |
| avgrev | 0.0085 |
| avgqty | 0.0085 |
| adjrev | 0.0084 |
| care_quality_intensity | 0.0084 |
