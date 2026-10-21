# Report references

Use these paths after this update is merged. They are references to saved evidence, not claims that every notebook should be rerun in one session.

| Report task | Main source | Supporting evidence |
|---|---|---|
| Task 1 Dataset exploration | `notebooks/01-eda-facial-features.ipynb` | `results/split42/shape_summary.csv` and the EDA figures retained in the notebook. |
| Task 2 Preprocessing | `notebooks/02a-convnext-128-training.ipynb` and `notebooks/04-controlled-improvement.ipynb` | Transform definitions, split settings, preview outputs and saved configurations. |
| Task 3 Model development | `notebooks/02a-convnext-128-training.ipynb`, `notebooks/02b-convnext-224-training.ipynb`, `notebooks/02c-efficientnetv2s-128-training.ipynb` | The ConvNeXt V2 section of Notebook 04 and `results/best_ensemble/recipe.json`. |
| Task 4 Training strategy | Training cells and curves in Notebooks 02a, 02b, 02c, 04 and 06 | `results/split42/`, `results/confirmation_split1337/`, `results/full_data_128/`, `results/convnextv2_split1337/` and `results/full_data_convnextv2/`. |
| Task 5 Evaluation | `notebooks/03-original-ensemble-tta.ipynb`, `notebooks/04-controlled-improvement.ipynb` and `notebooks/05-original-plus-geometry.ipynb` | `results/submission_history.csv`, classification reports, confusion matrices, validation result tables and the exact winning recipe. |
| Task 6 Analysis and improvements | Comparisons in Notebooks 03, 04, 05 and 08 | Paired error tables, two-split comparisons, synthetic stress results and the unsuccessful public follow-ups. |

For an academic report, cite notebook names and the relevant section or experiment, with repository paths where useful. The final Word report is being written separately, one subsection at a time.

The 0.9806 recipe uses the split-trained V2 checkpoint selected at epoch 7. Notebook 06's full-data V2 replacement scored 0.9797 at the tested 25% weight. Do not interchange these models or attach the earlier 99.822% split-42 validation accuracy to the final seven-model ensemble.
