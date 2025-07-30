# INSY697 Telecom Churn Project – Atomic Task List (tasks.md)

Purpose  
A queue of ultra‑granular, test‑ready tasks for an engineering LLM. Execute sequentially; each task has exactly one concern, an explicit start trigger, a measurable end state, and (where relevant) a deadline.

## Phase 0 – Setup & Compliance
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T01 | Create Git repository `telecom-churn-survival` under team GitHub org | Team member logged into GitHub | Repo URL posted in team chat; another member can clone |
| T02 | Add `/data/raw` directory and copy `Cell1.csv` + `data_documentation_class.xls` | Local clone exists | Files appear in repo with correct sizes |
| T03 | Add `.gitignore` with typical Python ignores | Repo cloned | `git status` shows clean after build artifacts generated |
| T04 | Create `README.md` referencing project goals, dataset, and link to tasks.md | `.github` folder exists | CI passes markdown lint; README visible online |
| T05 | Create conda environment `telechurn` (Python 3.11) and save `environment.yml` | `environment.yml` pushed | `conda env create -f environment.yml` succeeds locally |

## Phase 1 – Data Understanding
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T06 | Load raw dataset into pandas and print shape | env active | Shape logged in `notebooks/01_data_overview.ipynb` |
| T07 | Generate data dictionary from `.xls` and commit as `docs/data_dictionary.md` | `.xls` present | File committed with >10 variables described |
| T08 | Verify churn label distribution | Notebook open | Bar chart saved as `outputs/churn_dist.png` |

## Phase 2 – Data Cleaning & Enhancement
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T09 | Identify missing values per column | Notebook 02 started | Table `na_summary.csv` saved in `/outputs` |
| T10 | Impute numeric NA with median and categorical with mode; save cleaned file `telecom_clean.parquet` | `na_summary.csv` exists | File saved; row count unchanged |
| T11 | Engineer `tenure_months` from relevant date fields | `telecom_clean.parquet` loaded | Column appears with non‑null numeric values |
| T12 | Integrate external census income data by customer zipcode | access to `census_income.csv` | Joined dataset `telecom_enriched.parquet` contains `median_income` |
| T13 | One‑hot encode categorical vars; save `telecom_ml_ready.parquet` | enriched file exists | File saved; one‑hot column count logged |

## Phase 3 – Baseline Survival Models
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T14 | Define event time (`tenure_months`) and indicator (`churn`) | ml_ready dataset ready | Variables `duration`,`event` added |
| T15 | Fit Kaplan‑Meier estimator overall | `duration`,`event` ready | Survival curve plot saved `km_overall.png` |
| T16 | Stratify KM curves by contract type; perform log‑rank test | KM notebook open | p‑value < 0.05 saved in `outputs/logrank_contract.txt` |

## Phase 4 – Advanced Survival & ML Models
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T17 | Fit Cox Proportional Hazards model; check Schoenfeld residuals | `duration`,`event` ready | Harrell c‑index printed |
| T18 | Fit Random Survival Forest with 5‑fold CV | scikit‑survival installed | Mean c‑index logged to `models/rsf_metrics.json` |
| T19 | Fit DeepSurv neural network | pytorch installed | Best val‑loss < 0.35 in training log |
| T20 | Compare survival models on hold‑out set | models trained | `survival_model_compare.csv` saved |

## Phase 5 – Classification & CLV Modeling (Beyond Survival)
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T21 | Train baseline Logistic Regression on churn | ml_ready dataset ready | ROC‑AUC logged |
| T22 | Train XGBoost classifier; perform Bayesian hyper‑opt | logistic complete | ROC‑AUC improvement ≥3 pp |
| T23 | Compute individual predicted CLV combining survival P(t) and ARPU | best survival model chosen | Column `expected_clv` added to dataset |
| T24 | Segment customers into CLV quintiles | `expected_clv` present | Segmentation summary plot saved |

## Phase 6 – Pricing & Strategy Analytics
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T25 | Implement two‑part tariff profit function in `analysis/pricing.py` | CLV quintiles ready | Unit test `pytest` passes |
| T26 | Optimize profit under current vs. tiered pricing via `scipy.optimize` | pricing.py implemented | Results JSON `pricing_counterfactuals.json` saved |
| T27 | Simulate retention‑discount scenarios and recompute profit | pricing baseline done | Profit delta table saved |

## Phase 7 – Paper Drafting
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T28 | Write Introduction (Page 1) in `paper/draft.docx` | repo set up | Intro word count 250‑300 |
| T29 | Compose Empirical Section (Page 2) summarizing data & models | KM and Cox done | Section committed |
| T30 | Compose Analytical Section (Page 3) covering pricing strategy | pricing scenarios done | Section committed |
| T31 | Compose Strategy Evaluation (Page 4) with counterfactuals & conclusion | counterfactuals simulated | Section committed |
| T32 | Place numbered tables & figures in `/paper/figures` | sections written | All refs resolved |

## Phase 8 – Presentation Prep
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T33 | Create PowerPoint `slides/telecom_churn.pptx` | repo present | File saved with cover slide |
| T34 | Export key visuals (KM, RSF lift, pricing) to 1920×1080 PNG | figures exist | Files appear in `/slides/assets` |
| T35 | Draft 15‑min narrative script in `slides/script.md` | pptx template exists | Read‑through ≤12 min |
| T36 | Conduct rehearsal; record timing | script complete | `rehearsal_1.txt` shows <15 min |

## Phase 9 – QA & Submission
| ID | Task | Start | End / Test |
|----|------|-------|------------|
| T37 | Run `pytest` for pipelines and utilities | all code committed | All tests pass |
| T38 | Lint codebase with `flake8`; fix errors | code present | `flake8` returns 0 |
| T39 | Spell‑check paper & slides with `codespell` | docs complete | 0 issues found |
| T40 | Submit paper PDF & slide deck via LMS | artifacts built | Submission receipt committed |

---

**Legend**  
Start – Condition to begin task  
End / Test – Observable artifact verifying completion  
Each task is atomic and non‑overlapping.
