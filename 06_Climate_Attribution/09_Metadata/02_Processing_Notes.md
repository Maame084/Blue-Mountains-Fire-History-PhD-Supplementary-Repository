# Processing Notes

- CSV headers were standardised to lower-case snake_case.
- Missing values coded as -99.99 in the Niño 3.4 and SOI files were converted to blank/NA.
- Monthly climate-mode records were aggregated to calendar-year means for annual attribution comparisons.
- VPD annual summaries were calculated from the daily Katoomba-area VPD file.
- Integrated annual datasets were merged by `year`.
- The original climate-index workbook labelled DMI was parsed from a fixed-width-style monthly table contained in a single Excel column. The provider metadata could not be independently verified during final archiving; the values are preserved exactly as analysed and no recalculation was performed.
