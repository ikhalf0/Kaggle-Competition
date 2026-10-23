# Notebook 10 setup

The user reports a Kaggle run underway. The repository contains the prepared source only; no executed copy or model result has been returned.

Import `notebooks/10-dinov2-base224-validation.ipynb` into Kaggle. Attach the private `10_dinov2_inputs.zip` (5.17 MiB) and the original Competition images. Enable a GPU and Internet. No secret is required for the public pretrained weights. This experiment does not use the binary specialist checkpoint or the resize-comparison input pack.

Run one cell at a time. Review the short Part 3 speed/memory check before starting Part 4. The training cell runs all eight epochs automatically: one classifier-only epoch followed by seven full fine-tuning epochs. Review Part 5's validation results before Part 6's test export. The notebook never uploads a Kaggle submission.

The current best remains 0.9806. The planned candidate keeps 75% of that exact winning probability file and adds 25% DINOv2 TTA. Its validation proxy is separate from the full-data winner. No score is claimed until a real submission result is supplied.

Local preparation checks passed. GPU model loading, timing, training and checkpoint resume remain to be checked on Kaggle. See `docs/setup_and_reproduction.md` and `results/analysis_and_limits.md` for inputs, methods and limits.
