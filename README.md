# Cat and dog facial feature classification

ENGE707 Assignment 3. This private repository records the data exploration, training experiments and saved results for an eight-class Kaggle image classification task.

The best confirmed public score is **0.9806**, from `submission_best75_convnextv2_tta25.csv`, observed on 21 October 2026. Its exact seven-model recipe is in [results/best_ensemble/recipe.json](results/best_ensemble/recipe.json). Follow-up submissions and their unchanged score evidence are recorded in [results/submission_history.csv](results/submission_history.csv). Notebook 10 is complete: its 75% previous ensemble / 25% DINOv2 TTA blend also scored **0.9806**, observed on 24 October 2026. This is a displayed public tie; private performance and unrounded public ordering are unknown. [The DINOv2 evidence](results/dinov2_base224/README.md) is retained separately. None of the confirmed outcomes exceeds 0.9806. The newer full-data ConvNeXt V2 model is an unsuccessful follow-up and is not a component of the 0.9806 winner.

## Repository contents

| Notebook | Purpose |
|---|---|
| [01 Dataset exploration](notebooks/01-eda-facial-features.ipynb) | Class balance, examples, dimensions, quality checks and duplicate removal. |
| [02a ConvNeXt 128 training](notebooks/02a-convnext-128-training.ipynb) | Original 128px model and training pipeline. |
| [02b ConvNeXt 224 training](notebooks/02b-convnext-224-training.ipynb) | Original resolution experiment. |
| [02c EfficientNetV2 S training](notebooks/02c-efficientnetv2s-128-training.ipynb) | Original EfficientNetV2-S model, configuration and executed results. |
| [03 Original ensemble and TTA](notebooks/03-original-ensemble-tta.ipynb) | Original three-model ensemble and separate shape-prior experiments. |
| [04 Controlled improvement](notebooks/04-controlled-improvement.ipynb) | Executed split-1337 confirmation, full-data 128px pair and split-trained ConvNeXt V2 experiment. |
| [05 Original plus geometry](notebooks/05-original-plus-geometry.ipynb) | Split-42 geometry blending and the intermediate 0.9793 submission. |
| [06 Full-data ConvNeXt V2](notebooks/06-full-data-convnextv2.ipynb) | Later seven-epoch full-data V2 training and test predictions. |
| [07 EfficientNetV2-S 192](notebooks/07-efficientnetv2s-192-validation.ipynb) | Completed eight-class training and saved validation/test outputs; its tested blend scored 0.9805. |
| [08 Cat mouth/nose specialist](notebooks/08-cat-mouth-nose-specialist.ipynb) | Completed binary specialist and frozen routing; submitted TTA candidate scored 0.9799. |
| [09 Resize comparison](notebooks/09-resize-comparison.ipynb) | Completed inference-only stretch/letterbox comparison; no test prediction or submission. |
| [10 DINOv2 Base 224](notebooks/10-dinov2-base224-validation.ipynb) | Completed eight-class training, epoch 8 selected, validation/test exports and confirmed 0.9806 public tie at 25% TTA weight. |

The full-data ConvNeXt V2 notebook is numbered 06 for the repository reading order; it was originally executed as Notebook 08. Its saved backup names and code comments retain that historical label. The full-data pair and split-trained V2 experiments remain inside the executed Notebook 04. Notebook 05 is an intermediate experiment, rather than a cell dependency of the later appended sections. Historical Notebook 04 versions and the earlier two-model ensemble are preserved under [archive](archive/README.md). Completed notebooks retain their original code cells and saved outputs, including the returned Notebook 10. Its original prepared source is preserved in the archive. This reorganisation changes their repository paths, not their experiment results.

Small configurations, histories, confusion matrices, learning curves and comparisons are under [results](results/README.md). [The report file map](docs/report_file_map.md) identifies stable paths for Tasks 1 to 6. [The setup guide](docs/setup_and_reproduction.md) describes inputs, recorded versions and reproduction limits.

## Dataset and evaluation

The official dataset contains 63,660 labelled training images and 29,443 unlabelled test images. Removing 15 redundant exact duplicates leaves 63,645 training images. Both 85/15 stratified splits contain 54,098 training and 9,547 validation images. Seeds 42 and 1337 identify different splits. Deduplication does not establish independence between related crops from the same source photograph.

Use [results/submission_history.csv](results/submission_history.csv) for the confirmed public outcomes. The original three-model ensemble scored 0.9785. The 0.9793 blend had 17 validation errors on split 42. The final 0.9806 blend includes full-data components, so it has **no independent holdout validation score**. Neither a public score nor a historical rank establishes private-leaderboard performance.

## Private artifacts

The earlier selected [winning submission CSV](results/best_ensemble/submission_best75_convnextv2_tta25.csv) and [public-score screenshots](results/evidence/README.md) are retained in this private repository for assessment. Competition images, checkpoint weights, probability arrays and other lower-scoring candidate CSVs remain in private Kaggle inputs/outputs and downloaded backups. The [private artifact inventory](docs/private_artifact_inventory.json) accounts for all seven winning checkpoint and probability files. The recorded SHA256 verifies the selected CSV. An authorised reviewer needs the official dataset and the matching private artifacts to reproduce inference. Keep the existing authentic commit history when applying the reorganisation.
