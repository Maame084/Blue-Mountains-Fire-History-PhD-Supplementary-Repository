# Raman spectroscopy data

This folder contains the Raman spectroscopy files supplied with the supplementary repository.

| File | Description |
|---|---|
| `00_Supplementary_Data_S6_Raman_Spectroscopy_Index.xlsx` | Index of the Raman files and suggested thesis cross-references. |
| `S6_File_Manifest.csv` | CSV manifest matching the files present in this folder. |
| `S6_02_Calibration_Raman_Parameters_All_Species.xlsx` | Calibration Raman parameter workbook for the analysed species and heat-flux treatments. |
| `S6_04_ANOVA_Calibration_Experiment_Source.docx` | ANOVA and Tukey supporting material for the calibration experiment. |
| `S6_05_Baseline_Correction_Original.py` | Original baseline-correction code fragment preserved as supplied. It is not a standalone executable script. |
| `S6_07_All_Raman_Data.xlsx` | Raman data workbook used in the calibration and sedimentary workflow. External workbook links and private source paths were removed for public archiving; cell values were preserved. |
| `S6_07_Formula_Map.csv` | Records the 15 internal formulas flattened to cached values when `S6_07_All_Raman_Data.xlsx` was sanitised. |
| `S6_08_Peak_Fits_Calibration.xlsx` | Calibration peak-fit workbook. Retained cell note: Brynn Hibbert: Removed lines with R^2&lt;0.97 142 reduced to 134 |
| `S6_09_Swamp_Peak_Fits.xlsx` | Sedimentary charcoal peak-fit workbook. |
| `S6_10_Reconstruct_MATLAB_Live_Script.mlx` | MATLAB live script associated with spectral reconstruction or chemometric modelling. |
| `S6_11_Gaussian_Peak_Fitting_Original.py` | Original Gaussian peak-fitting support code. |
| `S6_12_Baseline_Correction_Cleaned_For_Appendix.py` | Cleaned and commented baseline-correction helper derived from the original fragment. |

## Reproducibility notes

- `S6_12_Baseline_Correction_Cleaned_For_Appendix.py` is syntactically valid Python but depends on the local `spectrum` class used in the original analysis environment.
- `S6_05_Baseline_Correction_Original.py` is retained as a historical code fragment and is not expected to run independently.
- The values in `S6_07_All_Raman_Data.xlsx` were verified as unchanged after external-link sanitisation. The removed formula locations and expressions are documented in `S6_07_Formula_Map.csv`.
