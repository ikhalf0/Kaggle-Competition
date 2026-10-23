# Report references

These are stable paths for this branch and for `main` after this update is merged. They point to saved evidence; running all training notebooks again is not required to inspect the report figures. Completed Notebooks 01–10 preserve their executed outputs. Notebook 10's submitted 25% DINOv2 TTA blend ties the displayed best at 0.9806.

| Report task | Main sources | Supporting evidence |
|---|---|---|
| Task 1 Dataset exploration | Notebook 01 | EDA figures, `results/split42/shape_summary.csv`, `results/validation_audit/` for the later crop-shape/similarity checks. |
| Task 2 Preprocessing | Notebooks 02a, 04 and the input sections of 07–09 | Saved transform definitions/configurations; Notebook 09's resize comparison. Explain that letterbox was tested only at inference for a square-trained model. |
| Task 3 Model development | Notebooks 02a, 02b, 02c, 04, 07, 08 and 10 | `results/best_ensemble/recipe.json`, EfficientNet192 configuration, specialist configuration and frozen routing policy. Notebook 10 adds a completed transformer comparison; its configuration, history, metrics and public outcome are in `results/dinov2_base224/`. |
| Task 4 Training strategy | Notebooks 02a–02c, 04, 06–08 and 10 | Histories and curves in the matching results folders. Keep ordinary validation NLL separate from augmented, label-smoothed training loss. |
| Task 5 Evaluation | Notebooks 03–05 and 07–10 | `results/submission_history.csv`, `results/evidence/`, class metrics, paired errors and `results/resize_comparison/`. The final 0.9806 blend has no independent holdout score. |
| Task 6 Analysis and improvements | Notebooks 04–10, plus the audit summaries | `results/analysis_and_limits.md`, unsuccessful public follow-ups, crop-shape differences and the limits of reused validation/synthetic checks. Notebook 10 improved the proxy from 23 to 18 errors but tied the displayed public score; separate these findings. |

Canonical notebooks are linked from the root README. The selected CSV remains `results/best_ensemble/submission_best75_convnextv2_tta25.csv`. The unchanged screenshots and digest index are under `results/evidence/`. Use filenames plus relevant notebook sections or table names when referencing evidence in the Word report, which is prepared separately.

The 0.9806 recipe uses the split-trained V2 checkpoint selected at epoch 7. Notebook 06's later full-data V2 replacement scored 0.9797. The earlier 99.822% split-42 validation accuracy belongs to the 0.9793 intermediate blend. The 23-to-22-error EfficientNet and specialist comparisons use a separate split-trained proxy. None is an independent validation score of the exact final seven-model winner.

The full-data notebook numbered 06 was originally executed with an 08 filename. Canonical Notebook 08 now refers to the later cat-pair specialist. Notebook 09's supplied filename had the spelling `09-resize-comparsion.ipynb`; its repository filename is corrected without changing any notebook bytes. Provenance and digests are in `docs/notebook_provenance.json`.

The later DINOv2 candidate is retained at `results/dinov2_base224/submission_best75_dinov2b224tta25.csv`. It adds an eighth model through a 75/25 blend with the earlier seven-model ensemble. Both scored 0.9806 at displayed precision and neither exact full-data blend has an independent holdout score.
