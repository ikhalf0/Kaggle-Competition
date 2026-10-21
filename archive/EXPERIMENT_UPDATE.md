# Experiment update: full-data ensemble, 21 October 2026

Public Kaggle best: **0.9801**, rank **4** when observed. Previous public bests were 0.9785 and 0.9793. Public rank and score are observations, not private-leaderboard results.

## Second-split confirmation

Both configurations were retrained from scratch using split seed 1337 and training seed 42. On 9,547 validation images, the control made 26 clean errors and the geometry model made 33. Flip TTA left control errors at 26 and reduced geometry errors to 29. Geometry reduced errors on synthetic wide/tall views from 122/1,084 to 82/68. Its clean-accuracy benefit was inconsistent across the two random splits, while these synthetic robustness gains repeated. Related source-photo crops may still cross a random split; exact-duplicate removal does not establish source independence.

## Full-data training

A control ConvNeXt Tiny and a geometry ConvNeXt Tiny were trained from pretrained weights at 128 pixels on all 63,645 cleaned labelled images, for seven epochs each. Seven epochs were selected using the best epochs from earlier validation runs (epochs 6 and 7 for each configuration). These full-data models have no independent holdout validation score.

Both used AdamW, learning rate 0.0003, weight decay 0.05, label smoothing 0.1, one-epoch warm-up and cosine decay. Exact settings and package versions are in the saved configs; actual_epochs records the seven-epoch full-data budget. The inherited epochs field is 8 from the comparison configuration and was overridden by FULL_EPOCHS=7, as recorded in actual_epochs and training_plan.json.

## Submitted recipe

- 75% previous 0.9793 ensemble probabilities
- 12.5% full-data control probabilities with horizontal-flip TTA
- 12.5% full-data geometry probabilities without TTA

This recipe was a conservative trial, with no independent validation score for its full-data components. It changed 86 predictions relative to the previous benchmark and scored **0.9801** on the public leaderboard. Submission: submission_benchmark75_fullpair25.csv. The recipe file records the submission SHA-256 digest.

## Files to commit

This pack includes the saved, completed Notebook 4 at notebooks/04_controlled_improvement.ipynb, including the second-split and appended full-data training code and outputs. Replace your existing Notebook 4 with this version (keep your repository’s established location/name) and commit the small result files. Retain Notebook 5 in the repository if not already committed. Add the new public leaderboard screenshot as evidence, and update the repository README to link to these notes.

Preserve model checkpoints, probability arrays, competition images and submission prediction files in private Kaggle/local storage. This pack contains no tokens, prediction files or model weights. Keep the original final submission CSV for the assessment deliverables.

Reference and acknowledge pretrained models, libraries and assistance according to course rules; be able to explain every submitted code component.
