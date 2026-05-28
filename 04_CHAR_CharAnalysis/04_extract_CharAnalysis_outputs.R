# ============================================================
# APPENDIX D SCRIPT 04
# Extract CharAnalysis outputs and fire-episode tables
# ============================================================

library(readxl)
library(dplyr)
library(writexl)
library(ggplot2)

base_dir <- "Supplementary_Data_D"
data_dir <- file.path(base_dir, "data_workbooks")
out_dir  <- file.path(base_dir, "outputs")
fig_dir  <- file.path(base_dir, "figures")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)

charanalysis_file <- file.path(data_dir, "D1_CharAnalysis_Modern1900_Outputs.xlsx")

time_series <- read_excel(charanalysis_file, sheet = "time_series")
significant_years <- read_excel(charanalysis_file, sheet = "significant_years")
fire_episodes <- read_excel(charanalysis_file, sheet = "fire_episodes")
site_summary <- read_excel(charanalysis_file, sheet = "site_summary")
fri_summary <- read_excel(charanalysis_file, sheet = "fri_summary")

write_xlsx(
  list(
    Time_series = time_series,
    Significant_years = significant_years,
    Fire_episodes = fire_episodes,
    Site_summary = site_summary,
    FRI_summary = fri_summary
  ),
  file.path(out_dir, "AppendixD_CharAnalysis_tables.xlsx")
)

# Appendix figure: interpolated charcoal, background and threshold.
p1 <- ggplot(time_series, aes(x = Year_CE)) +
  geom_line(aes(y = Cint), linewidth = 0.35) +
  geom_line(aes(y = Cback), linetype = "dashed", linewidth = 0.35) +
  geom_line(aes(y = Threshold), linetype = "dotted", linewidth = 0.35) +
  geom_point(
    data = subset(time_series, Significant_Fire_Year == TRUE),
    aes(y = Cint),
    size = 1.2
  ) +
  facet_wrap(~ Plot_Site, scales = "free_y") +
  labs(
    x = "Year CE",
    y = "Interpolated CHARa",
    title = "CharAnalysis screening outputs by site"
  ) +
  theme_bw(base_size = 10)

ggsave(file.path(fig_dir, "AppendixD_CharAnalysis_site_outputs.pdf"), p1, width = 10, height = 7)

# Appendix figure: possible fire-return intervals by site.
p2 <- ggplot(fire_episodes, aes(x = Plot_Site, y = Possible_FRI_yr)) +
  geom_point(size = 2, na.rm = TRUE) +
  coord_flip() +
  labs(x = "Site", y = "Possible fire-return interval (years)") +
  theme_bw(base_size = 10)

ggsave(file.path(fig_dir, "AppendixD_possible_FRI_by_site.pdf"), p2, width = 8, height = 5)
