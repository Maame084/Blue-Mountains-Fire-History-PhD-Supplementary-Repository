#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Appendix E / Supplementary Data S6
Raman linear baseline-correction helper.

Purpose
-------
This cleaned code records the baseline-correction workflow used for Raman spectra:
1. load an xy text spectrum;
2. reverse the spectrum if required by the local spectrum object;
3. subset to 900-2000 cm-1;
4. smooth with a 9-point window;
5. fit a linear baseline; and
6. subtract the baseline before parameter extraction or peak fitting.

Important
---------
This helper assumes access to the local `spectrum` class used in the original
analysis environment. It is therefore provided as reproducibility documentation,
not as a standalone package.
"""

def apply_linear_baseline(folder, filename, spectrum_class, lower=900.0, upper=2000.0, smooth_window=9):
    """
    Apply the Raman baseline-correction sequence used in the thesis workflow.

    Parameters
    ----------
    folder : str
        Folder containing the spectrum file.
    filename : str
        Name of the xy text spectrum file.
    spectrum_class : class
        Local spectrum class with load_xy_txt, reverse, subset, smooth,
        baseline_linear and subtract methods.
    lower, upper : float
        Wavenumber bounds for the retained Raman spectral region.
    smooth_window : int
        Smoothing window applied before fitting the linear baseline.

    Returns
    -------
    corrected : object
        Baseline-corrected spectrum object.
    filepath_stem : str
        Spectrum filepath without the extension.
    """
    spectrum_path = folder + filename
    filepath_stem = folder + filename[0:len(filename) - 4]

    s = spectrum_class()
    s.load_xy_txt(spectrum_path)

    s_reversed = s.reverse()
    s_subset = s_reversed.subset(lower, upper)
    s_smoothed = s_subset.smooth(smooth_window)
    baseline = s_smoothed.baseline_linear()
    corrected = s_subset.subtract(baseline)

    return corrected, filepath_stem
