# Experiment evidence

The best confirmed public score remains **0.9806**. The thirteen rows in `submission_history.csv` record the confirmed outcomes retained by this project review, rather than a complete Kaggle account export. No Notebook 10 score is included.

| Folder or file | Evidence |
|---|---|
| `original_models/` | Original histories and two-/three-model validation comparisons. |
| `split42/` | Controlled control/geometry runs, paired errors, class metrics and curves. |
| `confirmation_split1337/` | Saved separate-split confirmation and class metrics. |
| `original_plus_geometry/` | Intermediate 0.9793 recipe and its split-42 comparison. |
| `full_data_128/` | Full-data control/geometry pair and seven-epoch histories. |
| `convnextv2_split1337/` | Eight-class V2, clean/TTA/stress metrics and blend diagnostics. |
| `full_data_convnextv2/` | Later full-data V2; its tested replacement blend scored 0.9797. |
| `best_ensemble/` | Exact 0.9806 seven-model recipe, class order and selected CSV. |
| `efficientnetv2s_192/` | Completed Notebook 07 history, curves, class metrics and comparison; tested blend 0.9805. |
| `cat_mouth_nose_specialist/` | Completed Notebook 08 binary metrics, frozen policy and all-class paired results; public 0.9799. |
| `resize_comparison/` | Completed Notebook 09 comparison, baseline reproduction and subgroup results; no submission. |
| `validation_audit/` | Crop-shape and perceptual-similarity audit summaries and methods. |
| `dinov2_base224/` | Notebook 10 plan/status and CPU preparation checks only; no model results. |
| `submission_history.csv` | Thirteen confirmed public outcomes, including unsuccessful trials. |
| `public_followups.json` | Seven timestamped follow-up observations and evidence paths. |
| `evidence/` | Nine unchanged public-score screenshots and their SHA256 index. |
| `followup_recipes/` | Recipes, source digests and observed outcomes for tested follow-ups. |

Read [analysis_and_limits.md](analysis_and_limits.md) for what these experiments establish. The exact full-data winning blend has no independent holdout score. The earlier 17-error result belongs to the 0.9793 split-42 blend; the later 23-error reference is a split-trained diagnostic proxy. They are not validation scores of the final 0.9806 submission.

Completed code and saved outputs are in Notebooks 01–09. Notebook 10 is a prepared source copy with empty outputs because no executed copy has been received. GPU training was not rerun for this repository update. Large checkpoints, probability arrays, input ZIPs and non-winning submission CSVs stay in private Kaggle outputs/downloaded backups, indexed in `docs/private_artifact_inventory.json`.

Original run-export metadata was saved before manual Kaggle submissions, so a retained `complete_run.json` can have a null public-score field. Read `submission_history.csv`, `public_followups.json` and the later review/recipe records for the confirmed submission outcomes. The source export is preserved as historical evidence.
