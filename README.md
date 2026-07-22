# Blue Mountains Fire History PhD Supplementary Repository

**Version:** 1.0.0  
**Release date:** 22 July 2026  
**Author:** Maame Adwoa Maisie  
**Institution:** University of Wollongong  
**GitHub:** https://github.com/Maame084/Blue-Mountains-Fire-History-PhD-Supplementary-Repository  
**Zenodo DOI:**https://doi.org/10.5281/zenodo.21481862


## Repository overview

This repository accompanies the PhD thesis:

**Fire Regime Shifts in the Twentieth Century in the Upper Blue Mountains of Eastern Australia: Insights from Charcoal Records of Temperate Highland Peat Swamps on Sandstone**

It is a supplementary research archive containing machine-readable datasets, selected analytical scripts and code fragments, statistical outputs, supplementary figures and documentation used in the thesis. Complete methodological descriptions, interpretation and conclusions remain in the thesis.

The repository is intended to support transparent inspection of the evidence used in the thesis.  
## Repository structure

| Folder | Contents | Thesis linkage |
|---|---|---|
| `01_Chronology/` | OxCal scripts and full age–depth outputs | Chapters 4–6; Appendix B; Supplementary Data S1–S2 |
| `02_ITRAX_MagSus/` | ITRAX XRF, magnetic susceptibility, LOI-aligned data and PCA outputs | Chapters 4–6; Appendix C; Supplementary Data S3–S4 |
| `03_ImageJ_Charcoal_Analysis/` | ImageJ-derived charcoal counts, areas and raw quantification | Chapters 4–6; Supplementary Data S5 and D3 |
| `04_CHAR_CharAnalysis/` | CharAnalysis time series, significant years, fire episodes, summaries and extraction script | Chapters 4–6; Supplementary Data D1 |
| `05_Raman_Spectroscopy/` | Calibration data, peak fits, spectral data, modelling material and selected Python/MATLAB files | Chapters 4–6; Supplementary Data S6 |
| `06_Climate_Attribution/` | Hydroclimate, fire-weather, climate-mode, population and integrated attribution datasets | Chapters 4–7; Supplementary Data S7 |

See `THESIS_REPOSITORY_CROSSWALK.md` for the detailed connection between the thesis, appendices and repository resources.

## Quick start

1. Read `REPOSITORY_MANIFEST.csv` to identify the archived files, checksums and thesis linkage.
2. Read the README inside the relevant analytical folder.
3. Use the thesis methods chapter as the authoritative description of the analytical workflow.
4. Verify downloaded files against `SHA256SUMS.txt`.

## Software represented in the archive

The archived workflows and files use or reference:

- OxCal 4.4;
- R 4.4.x;
- Python;
- MATLAB;
- ImageJ; and
- Microsoft Excel.

Some scripts depend on functions, classes, software or source files from the original analysis environment and are retained as methodological documentation rather than standalone executable packages. Folder-level READMEs identify these cases.


## Citation

Before the Zenodo record is published, cite the GitHub release as:

> Maisie, M. A. (2026). Blue Mountains Fire History PhD Supplementary Repository (Version 1.0.0) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.21481862


## Licence

Original materials created by the author are released under the Creative Commons Attribution 4.0 International licence, subject to the qualifications in `LICENSE`. Third-party source data and reproduced materials remain subject to their original terms and licences.

## Integrity and versioning

- `REPOSITORY_MANIFEST.csv` records file paths, sizes, checksums and status.
- `SHA256SUMS.txt` provides SHA-256 checksums for this release.
- `CHANGELOG.md` records repository changes.
- `CITATION.cff` supplies citation metadata for GitHub and other services.

## Contact

Maame Adwoa Maisie  
University of Wollongong
