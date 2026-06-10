# Berlin Emergency Response Data Analysis

This repository contains a Streamlit dashboard and a Jupyter notebook for exploring Berlin emergency response patterns using Berlin mission datasets from 2020–2025.

## Files

- `app.py`: Streamlit application for interactive district-level emergency incident trend analysis.
- `Berlin Emergency Response Patterns.ipynb`: Jupyter notebook with exploratory analysis, visualizations, and modeling experiments.
- `Berlin Emergency Response Patterns.executed.ipynb`: Executed notebook output created during validation.
- `Berlin_Missions_2020_2025.csv`: Berlin mission dataset used by both the app and notebook.
- `Berlin_Regional_2020_2025.csv`: Regional Berlin dataset for additional analysis.

## Requirements

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Streamlit App

From the project root:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Running the Notebook

Open `Berlin Emergency Response Patterns.ipynb` in Jupyter Lab, Jupyter Notebook, or VS Code and run all cells.

## Notes

- The project expects the dataset files to be present at:
  - `Berlin_Missions_2020_2025.csv`
  - `Berlin_Regional_2020_2025.csv`
- The notebook and app both use absolute paths inside the notebook and app code, so updating those paths may be necessary if the data is moved.

