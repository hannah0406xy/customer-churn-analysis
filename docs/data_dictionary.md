# Telecom Churn Dataset Dictionary

This document describes the variables in the telecom churn dataset.

| Variable Name | Description | Type |
|--------------|-------------|------|
| Notes |  |  |
| Customers were selected as follows: mature customers, customers who were with the company for at least six months, were sampled during July, September and November of 2001, and January of 2002.  For each customer, predictor variables were calculated based on the previous four months.  Churn was then calculated based on whether the customer left the company during the period 31-60 days after the customer was originally sampled.  The one-month treatment lag between sampling and observed churn was for the practical concern that in any application, a few weeks would be needed to score the customer and implement any proactive actions. |  |  |
| Several variables are in the form of means or ranges.  These were calculated per month over the previous four months of data. For example: month1revenue = 100, month2revenue = 125, month3revenue = 135, month4revenue=120; |  |  |
| the mean would be the average of the four, i.e. (100 + 125 + 135 + 120) / 4= 120. The range would be the difference between the highest and lowest values, i.e. 135 - 100 = 35. |  |  |
| Statistical values shown are of the calibration data set. |  |  |
| For some variables, additional explanations can be found by clicking the hyperlinked variable name. |  |  |
| Interval Variables | Explanation | % Missing |
| ADJMOU | Billing adjusted total minutes of use over the life of the customer | 0.0 |
| ADJQTY | Billing adjusted total number of calls over the life of the customer | 0.0 |
| ADJREV | Billing adjusted total revenue over the life of the customer | 0.0 |
| ATTEMPT_MEAN | Mean number of attempted calls | 0.0 |
| ATTEMPT_RANGE | Range of number of attempted calls | 0.0 |
| AVG3MOU | Average monthly minutes of use over the previous three months | 0.0 |
| AVG3QTY | Average monthly number of calls over the previous three months | 0.0 |
| AVG3REV | Average monthly revenue over the previous three months | 0.0 |
| AVG6MOU | Average monthly minutes of use over the previous six months | 0.02839 |
| AVG6QTY | Average monthly number of calls over the previous six months | 0.02839 |
| AVG6REV | Average monthly revenue over the previous six months | 0.02839 |
| AVGMOU | Average monthly minutes of use over the life of the customer | 0.0 |
| AVGQTY | Average monthly number of calls over the life of the customer | 0.0 |
| AVGREV | Average monthly revenue over the life of the customer | 0.0 |
| BLCK_DAT_MEAN | Mean number of blocked (failed) data calls | 0.0 |
| BLCK_DAT_RANGE | Range of number of blocked (failed) data calls | 0.0 |
| BLCK_VCE_MEAN | Mean number of blocked (failed) voice calls | 0.0 |
| BLCK_VCE_RANGE | Range of number of blocked (failed) voice calls | 0.0 |
| CALLFWDV_MEAN | Mean number of call forwarding calls | 0.0 |
| CALLFWDV_RANGE | Range of number of call forwarding calls | 0.0 |
| CALLWAIT_MEAN | Mean number of call waiting calls | 0.0 |
| CALLWAIT_RANGE | Range of number of call waiting calls | 0.0 |
| CC_MOU_MEAN | Mean unrounded minutes of use of customer care (see CUSTCARE_MEAN) calls | 0.0 |
| CC_MOU_RANGE | Range of unrounded minutes of use of customer care calls | 0.0 |
| CCRNDMOU_MEAN | Mean rounded minutes of use of customer care calls | 0.0 |
| CCRNDMOU_RANGE | Range of rounded minutes of use of customer care calls | 0.0 |
| CHANGE_MOU | Percentage change in monthly minutes of use vs previous three month average | 0.00891 |
| CHANGE_REV | Percentage change in monthly revenue vs previous three month average | 0.00891 |
| COMP_DAT_MEAN | Mean number of completed data calls | 0.0 |
| COMP_DAT_RANGE | Range of number of completed data calls | 0.0 |
| COMP_VCE_MEAN | Mean number of completed voice calls | 0.0 |
| COMP_VCE_RANGE | Range of number of completed voice calls | 0.0 |
| COMPLETE_MEAN | Mean number of completed calls | 0.0 |
| COMPLETE_RANGE | Range of number of completed calls | 0.0 |
| CUSTCARE_MEAN | Mean number of customer care calls | 0.0 |
| CUSTCARE_RANGE | Range of number of customer care calls | 0.0 |
| DA_MEAN | Mean number of directory assisted calls | 0.00357 |
| DA_RANGE | Range of number of directory assisted calls | 0.00357 |
| DATOVR_MEAN | Mean revenue of data overage | 0.00357 |
| DATOVR_RANGE | Range of revenue of data overage | 0.00357 |
| DROP_BLK_MEAN | Mean number of dropped or blocked calls | 0.0 |
| DROP_BLK_RANGE | Range of number of dropped or blocked calls | 0.0 |
| DROP_DAT_MEAN | Mean number of dropped (failed) data calls | 0.0 |
| DROP_DAT_RANGE | Range of number of dropped (failed) data calls | 0.0 |
| DROP_VCE_MEAN | Mean number of dropped (failed) voice calls | 0.0 |
| DROP_VCE_RANGE | Range of number of dropped (failed) voice calls | 0.0 |
| EQPDAYS | Number of days (age) of current equipment | 1e-05 |
| INONEMIN_MEAN | Mean number of inbound calls less than one minute | 0.0 |
| INONEMIN_RANGE | Range of number of inbound calls less than one minute | 0.0 |
| IWYLIS_VCE_MEAN | Mean number of inbound wireless to wireless voice calls | 0.0 |
| IWYLIS_VCE_RANGE | Range of number of inbound wireless to wireless voice calls | 0.0 |
| MONTHS | Total number of months in service | 0.0 |
| MOU_CDAT_MEAN | Mean unrounded minutes of use of completed data calls | 0.0 |
| MOU_CDAT_RANGE | Range of unrounded minutes of use of completed data calls | 0.0 |
| MOU_CVCE_MEAN | Mean unrounded minutes of use of completed voice calls | 0.0 |
| MOU_CVCE_RANGE | Range of unrounded minutes of use of completed voice calls | 0.0 |
| MOU_MEAN | Mean number of monthly minutes of use | 0.00357 |
| MOU_OPKD_MEAN | Mean unrounded minutes of use of off-peak data calls | 0.0 |
| MOU_OPKD_RANGE | Range of unrounded minutes of use of off-peak data calls | 0.0 |
| MOU_OPKV_MEAN | Mean unrounded minutes of use of off-peak voice calls | 0.0 |
| MOU_OPKV_RANGE | Range of unrounded minutes of use of off-peak voice calls | 0.0 |
| MOU_PEAD_MEAN | Mean unrounded minutes of use of peak data calls | 0.0 |
| MOU_PEAD_RANGE | Range of unrounded minutes of use of peak data calls | 0.0 |
| MOU_PEAV_MEAN | Mean unrounded minutes of use of peak voice calls | 0.0 |
| MOU_PEAV_RANGE | Range of unrounded minutes of use of peak voice calls | 0.0 |
| MOU_RANGE | Range of number of minutes of use | 0.00357 |
| MOU_RVCE_MEAN | Mean unrounded minutes of use of received voice calls | 0.0 |
| MOU_RVCE_RANGE | Range of unrounded minutes of use of received voice calls | 0.0 |
| MOUIWYLISV_MEAN | Mean unrounded minutes of use of inbound wireless to wireless voice calls | 0.0 |
| MOUIWYLISV_RANGE | Range of unrounded minutes of use of inbound wireless to wireless voice calls | 0.0 |
| MOUOWYLISV_MEAN | Mean unrounded minutes of use of outbound wireless to wireless voice calls | 0.0 |
| MOUOWYLISV_RANGE | Range of unrounded minutes of use of outbound wireless to wireless voice calls | 0.0 |
| OWYLIS_VCE_MEAN | Mean number of outbound wireless to wireless voice calls | 0.0 |
| OWYLIS_VCE_RANGE | Range of number of outbound wireless to wireless voice calls | 0.0 |
| OPK_DAT_MEAN | Mean number of off-peak data calls | 0.0 |
| OPK_DAT_RANGE | Range of number of off-peak data calls | 0.0 |
| OPK_VCE_MEAN | Mean number of off-peak voice calls | 0.0 |
| OPK_VCE_RANGE | Range of number of off-peak voice calls | 0.0 |
| OVRMOU_MEAN | Mean overage minutes of use | 0.00357 |
| OVRMOU_RANGE | Range of overage minutes of use | 0.00357 |
| OVRREV_MEAN | Mean overage revenue | 0.00357 |
| OVRREV_RANGE | Range of overage revenue | 0.00357 |
| PEAK_DAT_MEAN | Mean number of peak data calls | 0.0 |
| PEAK_DAT_RANGE | Range of number of peak data calls | 0.0 |
| PEAK_VCE_MEAN | Mean number of inbound and outbound peak voice calls | 0.0 |
| PEAK_VCE_RANGE | Range of number of inbound and outbound peak voice calls | 0.0 |
| PLCD_DAT_MEAN | Mean number of attempted data calls placed | 0.0 |
| PLCD_DAT_RANGE | Range of number of attempted data calls placed | 0.0 |
| PLCD_VCE_MEAN | Mean number of attempted voice calls placed | 0.0 |
| PLCD_VCE_RANGE | Range of number of attempted voice calls placed | 0.0 |
| RECV_SMS_MEAN | Mean number of received SMS calls | 0.0 |
| RECV_SMS_RANGE | Range of number of received SMS calls | 0.0 |
| RECV_VCE_MEAN | Mean number of received voice calls | 0.0 |
| RECV_VCE_RANGE | Range of number of received voice calls | 0.0 |
| RETDAYS | Number of days since last retention call | 0.96017 |
| REV_MEAN | Mean monthly revenue (charge amount) | 0.00357 |
| REV_RANGE | Range of revenue (charge amount) | 0.00357 |
| RMCALLS | Total number of roaming calls | 0.85777 |
| RMMOU | Total minutes of use of roaming calls | 0.85777 |
| RMREV | Total revenue of roaming calls | 0.85777 |
| ROAM_MEAN | Mean number of roaming calls | 0.00357 |
| ROAM_RANGE | Range of number of roaming calls | 0.00357 |
| THREEWAY_MEAN | Mean number of three way calls | 0.0 |
| THREEWAY_RANGE | Range of number of three way calls | 0.0 |
| TOTCALLS | Total number of calls over the life of the customer | 0.0 |
| TOTMOU | Total minutes of use over the life of the customer | 0.0 |
| TOTMRC_MEAN | Mean total monthly recurring charge | 0.00357 |
| TOTMRC_RANGE | Range of total monthly recurring charge | 0.00357 |
| TOTREV | Total revenue | 0.0 |
| UNAN_DAT_MEAN | Mean number of unanswered data calls | 0.0 |
| UNAN_DAT_RANGE | Range of number of unanswered data calls | 0.0 |
| UNAN_VCE_MEAN | Mean number of unanswered voice calls | 0.0 |
| UNAN_VCE_RANGE | Range of number of unanswered voice calls | 0.0 |
| VCEOVR_MEAN | Mean revenue of voice overage | 0.00357 |
| VCEOVR_RANGE | Range of revenue of voice overage | 0.00357 |
| Appendix |  |  |
| ADJMOU | Billings adjustments include any corrections to customer billing, including reimbursement for dropped calls, etc. |  |
| Return |  |  |
| ATTEMPT_MEAN | PLCD_DAT_MEAN + PLCD_VCE_MEAN |  |
| Return | Lines 108 + 110 |  |
| CCRNDMOU_MEAN | Rounded minutes refers to minutes rounded to the nearest whole minute, either rounding up (31 - 59 seconds) or rounding down (1 - 30 seconds). |  |
| Return | The minimum number of minutes of any single call is one minute. The value of 0 represents no calls were made. |  |
| COMPLETE_MEAN | COMP_DAT_MEAN + COMP_VCE_MEAN |  |
| Return | Lines 40 + 42 |  |
| CUSTCARE_MEAN | Customer care calls include any inbound calls to the company regarding complaints, disputes or questions (IVR Interactive Voice Response calls included). |  |
| Return |  |  |
| DATOVR_MEAN | Overage represents calls or minutes of use over the number of minutes allowed by that customer's calling plan. |  |
| Return |  |  |
| DROP_BLK_MEAN | BLCK_DAT_MEAN + BLCK_VCE_MEAN + DROP_DAT_MEAN + DROP_VCE_MEAN |  |
| Return | Lines 28 + 30 + 54 + 58 |  |
| IWYLIS_VCE_MEAN | Wireless to wireless calls represent calls from one wireless phone to another wireless phone. |  |
| Return |  |  |
| OVRREV_MEAN | DATOVR_MEAN + VCEOVR_MEAN |  |
| Return | Lines 50 + 135 |  |
| RECV_SMS_MEAN | SMS stands for Short Message Service, which is distinct from data and voice calls |  |
| Return |  |  |
| RETDAYS | Retention calls include any calls from the customer regarding loyalty or retention, e.g. contract renewal, relating competitor's offer, etc. |  |
| Return | Missing values for this variable can be assumed to mean there have been no retention calls made by the customer. |  |
| TOTMRC_MEAN | Monthly Recurring Charge is the base cost of the calling plan regardless of actual minutes used. |  |
| Return |  |  |
| MOU_OPKD_MEAN | Peak time calls refer to calls made from 7:00 am to 9:00 pm from Monday to Friday. |  |
| Return | Off-peak calls refer to calls made at all other times. |  |
