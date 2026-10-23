# Notebook 10 setup

The supplied Kaggle run is complete. The canonical notebook preserves all seven executed cells and outputs. Epoch 8 was selected, and the fixed 25% DINOv2 TTA blend scored 0.9806, tying the displayed best. See `results/dinov2_base224/` for the history, class metrics, submitted CSV and score evidence. The instructions below describe reproducing the recorded experiment.

Import `notebooks/10-dinov2-base224-validation.ipynb` into Kaggle. Attach the private `10_dinov2_inputs.zip` (5.17 MiB) and the original Competition images. Enable a GPU and Internet. No secret is required for the public pretrained weights. This experiment does not use the binary specialist checkpoint or the resize-comparison input pack.

Run one cell at a time. Review the short Part 3 speed/memory check before starting Part 4. The training cell runs all eight epochs automatically: one classifier-only epoch followed by seven full fine-tuning epochs. Review Part 5's validation results before Part 6's test export. The notebook never uploads a Kaggle submission.

The current best remains 0.9806. The submitted candidate kept 75% of the earlier exact winning probability file and added 25% DINOv2 TTA. The separate split-trained validation proxy improved from 23 to 18 errors, with five fixes and no new errors; it is not an independent validation result for the full-data submitted blend.

Local preparation checks passed before the run. The returned Kaggle execution and both backup archives were checked after completion. No local GPU training or model-checkpoint resumption test was performed. See `docs/setup_and_reproduction.md` and `results/analysis_and_limits.md` for inputs, methods and limits.
