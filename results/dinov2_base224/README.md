# Completed DINOv2 Base 224 experiment

The fixed submitted blend uses 75% of the exact earlier seven-model 0.9806 ensemble and 25% DINOv2 Base 224px horizontal-flip averaged probabilities. It scored **0.9806**, confirmed on 24 October 2026 at 03:28 Pacific/Auckland. This ties the displayed best. The 134 changed test labels are disagreements with the earlier submission, not known corrections. No private-leaderboard result or unrounded ordering is established.

Eight epochs completed on a Tesla T4: one head-only epoch followed by seven full fine-tuning epochs. Epoch 8 was selected by clean validation accuracy, with ordinary NLL as the tie-breaker. Saved training-plus-validation history totals 8,585.8 seconds (143.1 minutes), excluding most backup overhead and test inference. The short synthetic speed check excludes those costs and must not be reported as total training time.

| Comparison on split 1337 | Validation errors out of 9,547 |
|---|---:|
| Split-trained reference proxy | 23 |
| DINOv2 alone with clean inference | 24 |
| DINOv2 alone with flip TTA | 29 |
| 75% proxy plus 25% DINOv2 clean | 18 |
| 75% proxy plus 25% DINOv2 TTA | 18 |

The fixed TTA blend corrected five validation errors and created none. Both blends have the same validation class predictions. These are reused development results from a **split-trained proxy**, not an independent holdout score for the submitted ensemble, which contains full-data models. The public tie shows that the proxy gain did not establish a higher displayed public score.

The folder retains the original history, curve, configurations, per-class metrics, confusion matrices, comparisons and prediction fingerprints. `candidate_recipe.json`, `validation_review.json` and `complete_run.json` are unchanged pre-submission exports and therefore retain null public scores or `submitted: false`. Read `public_result.json` for the later confirmed outcome. The candidate CSV is retained here alongside the earlier selected file under `results/best_ensemble/`.

The supplied executed notebook is byte-preserved at `notebooks/10-dinov2-base224-validation.ipynb`. The prepared source is preserved at `archive/10-dinov2-base224-prepared.ipynb`. `completed_run_review.json` records independent CPU reconstruction of the submission and validation metrics, matching IDs/classes/configuration fingerprints, notebook consistency and backup integrity. Checkpoint tensors were not deserialised locally and GPU resumption was not tested.

Large checkpoints, all six probability arrays and both backup ZIPs remain private. Their filenames and fingerprints are in `docs/private_artifact_inventory.json` and `archive_fingerprints.json`. The recovery backup retains optimizer/scheduler/scaler/random states for completed epochs; the smaller review backup retains the selected model without the full optimizer-state checkpoint.

`preparation_checks.json` is historical CPU preparation evidence. Its arbitrary fixtures are not trained DINOv2 results. No new training or Kaggle submission was performed during this repository update.
