# DINOv2 Base 224px — in progress

The user reports this Kaggle run is underway. This folder contains the plan and local preparation checks only. No executed Notebook 10, GPU timings, trained checkpoint, validation result or public score has been received. The confirmed best remains 0.9806.

`preparation_checks.json` records CPU checks of input identity, split separation, source compilation, cache guards and temporary comparison/export fixtures. Those fixtures used earlier model predictions and are **not DINOv2 results**. The notebook's actual GPU loading, training, checkpoint resume and speed remain unverified here.

Run `notebooks/10-dinov2-base224-validation.ipynb` one cell at a time with the private `10_dinov2_inputs.zip` and Competition. Review the short speed check before training and review Part 5 before test inference. No new weight grid, routing search or automatic Kaggle submission is included. See `docs/setup_and_reproduction.md` for inputs and limits.
