# Known limitations

This file records limitations that users should understand before interpreting or reusing the archive.

## 1. Scope of reproducibility

The repository is a supplementary research archive rather than a fully automated end-to-end reproducibility package. It contains processed datasets, selected scripts, code fragments, workbooks and outputs. Complete methodological descriptions and the authoritative interpretation are in the thesis.

## 2. Climate-index series analysed under the label DMI

The original provider metadata for the climate-index series used under the label DMI could not be independently verified during final archiving. The archived files preserve the exact values used in the thesis; no recalculation, replacement or scientific reinterpretation was performed during repository preparation. The neutral `DMI_Labelled` naming is used to avoid asserting an independently verified official index identity.

## 3. Climate-attribution scripts

No complete climate-attribution processing or plotting scripts were present in the supplied archive. The repository preserves the inputs, aligned datasets, metadata and compiled figure output. Reproduction of the reported coefficients, lag screening and figures therefore requires the original analytical workflow or independent reimplementation from the thesis methods.

## 4. Raman code dependencies

`S6_05_Baseline_Correction_Original.py` is an incomplete historical code fragment. `S6_12_Baseline_Correction_Cleaned_For_Appendix.py` has valid Python syntax but depends on the original local `spectrum` class. The MATLAB live script may require the original MATLAB toolboxes and local analysis environment.

## 5. Sanitised Raman workbook

Private file paths and external workbook links were removed from `S6_07_All_Raman_Data.xlsx` before public archiving. Cached cell values were retained. The affected formula locations are documented in `S6_07_Formula_Map.csv`.

## 6. Third-party data

Some climate, government, mapping and other source datasets may remain subject to their original provider terms. The repository licence applies to original materials created by the author and does not override third-party rights.
