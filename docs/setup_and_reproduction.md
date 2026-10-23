# Setup and reproduction

## Recorded environment

The later Kaggle runs record Python 3.13.15, PyTorch 2.11.0+cu128, torchvision 0.26.0+cu128 and timm 1.0.29. See `results/environment.json` and the run configurations. NumPy, pandas, Pillow, scikit-learn, matplotlib and tqdm are also imported. The completed Notebooks 07–10 also record NumPy 2.1.3, pandas 2.3.3 and Pillow 13.0.0. Exact versions of scikit-learn, matplotlib and tqdm were not recorded; do not treat this list as a fully locked environment. Use a compatible Kaggle GPU environment for training. The existing notebooks do not establish bit-for-bit reproducibility across hardware and package versions.

## Inputs

Attach the original competition dataset containing `train_labels.csv`, `sample_submission.csv`, and the train/test JPEG folders. Images use five-digit names such as `00001.jpg`. Notebook 01 produces `train_metadata_clean.csv`. The original training notebooks require that metadata as a Kaggle input. Their historical `BASE` path may need adjustment for the current dataset attachment.

The original ensemble requires `best_convnext_t_128.pth`, `best_convnext_t_224.pth` and `best_effnetv2_s_128.pth`. Later notebooks also require the matching private outputs described in their opening cells. Notebook 05 specifically needs the split-42 controlled output, rather than using models trained on a different split to evaluate that holdout.

Notebook 06 can reuse the cleaned metadata from the supplied training-metadata cache or supported earlier backup outputs. Its first user-added cell reads the optional Kaggle Secret `kaggle-assignment3` into `HF_TOKEN`; skip that cell if the secret is not configured. The public pretrained model does not require this token. The notebook itself contains no token value.

## Viewing results and reproducing experiments

Completed canonical Notebooks 01–10 retain their saved outputs. Notebook 10's returned execution, history, predictions and public tie were checked; its original prepared source is archived separately. View them directly when checking figures and results. Running training cells starts the recorded experiments again. Notebook 04 retains confirmation, full-data-pair and V2 sections in their executed order; the appended sections use definitions created by earlier cells. It is not a standalone final seven-checkpoint inference command.

To reproduce the original models, run Notebook 01 followed by the relevant 02 training notebook with its recorded seed, transforms, model and settings. Notebook 03 loads those checkpoints and averages original/flip probabilities. The winning original weights are 40% ConvNeXt 128, 40% ConvNeXt 224 and 20% EfficientNetV2-S 128. Its later shape-adjustment experiments are separate recipes.

Use the controlled code in Notebook 04 and the saved configurations to reproduce the split-42 control/geometry experiment or the split-1337 confirmation. Select the intended split and output directory before starting a new training run. The full-data pair uses all 63,645 cleaned images, seven epochs and training seed 42. The split-trained V2 uses split 1337, size 192, batch 64 and eight scheduled epochs, selecting epoch 7. Notebook 06 instead trains V2 on all images with a seven-epoch schedule.

## Winning prediction recipe

The exact effective weights are recorded in `results/best_ensemble/recipe.json`: original ConvNeXt 128 TTA 11.25%, original ConvNeXt 224 TTA 11.25%, original EfficientNetV2-S 128 TTA 5.625%, split-42 geometry 128 clean 28.125%, full-data control 128 TTA 9.375%, full-data geometry 128 clean 9.375%, and split-1337 ConvNeXt V2 192 TTA 25%.

Average class probabilities with those weights before choosing the highest-probability class. TTA means the mean of original-image and horizontal-flip probabilities. Preserve the eight-class order and the sample-submission image-ID order; do not blend class-label CSVs as though they were probabilities. Validate finite probabilities and row sums and export exactly 29,443 unique image IDs with columns `image_id,class`.

The selected final CSV is committed at `results/best_ensemble/submission_best75_convnextv2_tta25.csv`. Its SHA256 is `8d255cfb971b031801ac95e8600fdada6eb0d51190b993e472b305d148639d23`. The locations of all seven private winning checkpoint and probability files are recorded in `docs/private_artifact_inventory.json`. A consolidated command that loads all seven checkpoints and exports this CSV remains a separate reproducibility task; this repository reorganisation preserves the experiment sources and exact recipe without claiming that command already exists.

## Interpreting metrics

Each holdout result belongs to its recorded split and inference view. Exact duplicate hashes are disjoint within each split, but related source-photo crops may cross splits. Synthetic wide/tall stress views probe the augmentation family and are not unbiased estimates of general robustness.

The original EfficientNet notebook uses label-smoothed cross-entropy for both training and validation loss. The controlled notebook uses smoothed training loss and ordinary validation NLL. Their loss values are not directly comparable. EfficientNet's patience-three early-stopping condition did not trigger; it completed eight epochs. The later full-data models deliberately have no independent holdout score, and that applies to the exact final ensemble too.


## Later notebooks and private inputs

| Notebook | Inputs besides Competition | Execution and evidence |
|---|---|---|
| 07 EfficientNet192 | `07_effnet192_inputs.zip`: cleaned metadata, exact split and reference predictions. | Eight completed epochs, selected epoch 7. Clean/TTA results and the 0.9805 public trial are separate records. The saved output includes nonfatal worker-cleanup messages; training and export completed. |
| 08 Cat-pair specialist | `08_cat_pair_inputs.zip`: exact pair/full splits, frozen references and routing manifest. | Eight completed binary epochs, selected epoch 8. The executed copy retains the corrected float64 routing and later recovery/backup cells. Public candidate 0.9799. |
| 09 Resize comparison | `09_resize_comparison_inputs.zip`: **eight-class** split-trained V2 checkpoint and reference data. | Inference only. It does not use the binary specialist checkpoint, train a model or export a submission. |
| 10 DINOv2 Base224 | `10_dinov2_inputs.zip`: metadata, split, prior validation predictions and exact winning test probabilities/CSV. | Completed eight epochs, selected epoch 8. The tested 75/25 winner/DINOv2 TTA blend scored 0.9806. No token was required for the public pretrained download. For a new run, retain the recorded speed and validation review steps. |

Keep input datasets private. The input ZIPs and probability arrays are omitted from Git; their filenames and hashes are in the private artifact inventory. An authorised reviewer needs those matching private artifacts. Their manifest fingerprints are checked by each notebook. Automatic path discovery accepts unpacked input directories or the supported ZIP filename; if multiple matching inputs are attached, set the explicit path at the top of the notebook.

Notebook 10 explicitly sets `img_size=224`, overriding the model card's default 518px. It verifies model normalisation and eight output classes. The official timm loader resizes pretrained position embeddings to that grid. The classifier-only warm-up is followed by a new two-rate AdamW optimizer for full fine-tuning. Accumulation uses micro-batches of 32 and an effective batch of 64. The final partial update uses its actual number of images. Full fine-tuning has a short warm-up and cosine decay; the scheduler advances only on successful AMP updates.

The speed check makes no optimizer update and excludes image loading, optimizer overhead, validation, backups and test inference. It is not a total-runtime measurement. Notebook 10 has an eight-hour guard between saved epochs, but does not measure account-wide GPU quota or time lost to interrupted epochs. The supplied Kaggle run completed on a Tesla T4. Its saved history totals 143.1 training-plus-validation minutes, excluding most backup overhead and test inference. GPU training and resumption were not rerun locally.

Completed epochs save optimizer, scheduler, scaler and random states in `last.pth` and create a recovery ZIP. Download it or save a Kaggle version with outputs before ending a session. The smaller review ZIP omits `last.pth`; it supports review/inference from `best.pth`, while full optimizer-state resumption requires the recovery artifacts. Matching run configuration and environment fingerprints are enforced. An interrupted epoch repeats from the last completed epoch. No notebook can recover an unsaved file after Kaggle has discarded the old session.
