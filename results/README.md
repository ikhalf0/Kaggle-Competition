# Experiment evidence

Configurations, histories and curves describe saved runs; no new training was performed for this reorganisation.

| Folder or file | Evidence |
|---|---|
| `original_models/` | Original saved histories and three-model validation comparison. |
| `split42/` | Controlled control/geometry experiment, paired errors and aggregate dimensions. |
| `confirmation_split1337/` | Separate split confirmation, configurations, class metrics and curves. |
| `original_plus_geometry/` | Intermediate blend comparison and 0.9793 recipe. |
| `full_data_128/` | Full-data control and geometry pair, seven-epoch histories and recorded plan. |
| `convnextv2_split1337/` | Split-trained V2, clean/TTA/stress metrics and same-split blend comparisons. |
| `full_data_convnextv2/` | Later full-data V2 configuration and seven-epoch training history. |
| `best_ensemble/` | Exact 0.9806 seven-model weights, class order and winning CSV digest. |
| `submission_history.csv` | Nine confirmed public submission outcomes retained in the supplied evidence. |
| `public_followups.json` | Timestamped records of the three later public trials. |
| `best_ensemble/submission_best75_convnextv2_tta25.csv` | Verified final 0.9806 prediction CSV with all 29,443 test IDs. |
| `evidence/` | Unchanged public-score screenshots and capture index. |
| `followup_recipes/` | Exact component weights and CSV digests for the three later public trials. |

The final blend's validation accuracy is unavailable because it includes full-data models. The 17-error/99.822% result belongs to the earlier 0.9793 blend on split 42. Public-score observations are not estimates of private-leaderboard accuracy.

The split-42 blend comparison, original two-model comparison and full-data-pair 50% recipe are also retained beside their corresponding experiments. `original_models/historical_public_scores.csv` separately records two earlier scores reported in historical source, with their weaker evidence status explicit. The nine-row main log is not a complete lifetime Kaggle submission export.

Large private artifacts remain in Kaggle outputs and downloaded backups; `docs/private_artifact_inventory.json` accounts for all seven winning checkpoints and probability files. The selected final CSV is included here. The archive folders preserve historical versions; the canonical notebooks are under `notebooks/`.
