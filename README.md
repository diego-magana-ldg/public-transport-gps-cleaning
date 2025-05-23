# Public Transport GPS Cleaning

In this repository, you will find a Python script developed to clean, filter, and extract useful subsets of raw GPS data collected from concessioned public transport vehicles in Mexico City. It was originally created as part of a data analysis effort at SEMOVI (Secretaría de Movilidad de la Ciudad de México).

## Purpose

The data obtained from concessioned vehicles was often unstructured and messy. This tool allows for quick identification of specific units, filtering, and preparation of datasets for further spatial or operational analysis.

## What it does

- Loads a raw `.csv` file with GPS logs
- Lists available columns and unique vehicle IDs (`Placa`)
- Filters records by a selected list of units
- Exports:
  - `filtered_records.csv`: only the units of interest
  - `unique_plates.csv`: a list of all detected plates

## Input

- A `.csv` file with columns including `Placa` (vehicle ID), GPS positions, and timestamps.

## Use Case Example

This script was used to extract operational records for specific ramales (branches) on Mexico City's Ruta 3 line. The filtered dataset was loaded into ArcGIS using XY coordinates. Based on the visible travel patterns, a route shape was manually delineated and exported as a .kml file. This allowed for the visualization and mapping of actual public transport trajectories, supporting operational analysis and planning.

## Technologies

- Python
- pandas

## Disclaimer

This repository contains only a sample script. No sensitive or operational data is included.
