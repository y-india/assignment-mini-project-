# OpsPulse Mini Project (Assignment Requirements)

## 1. Get Data (Input Stage)

You must:
- Choose a dataset or public API
- Example options:
  - NYC Taxi dataset (your case)
  - Weather API
  - Finance API

### Your case:
- Dataset: `yellow_tripdata.parquet`

### Task:
- Load the dataset into Python

---

## 2. Save Raw Data

You must:
- Store the original dataset locally without changes

### Output file:
- `raw.csv` or raw copy of parquet data

### Purpose:
- Preserve original data before processing (real-world practice)

---

## 3. Transform Data (Using Pandas)

This is the main part of the assignment.

You must:
- Clean the dataset
- Select important columns
- Create new features

### Examples:
- Convert datetime columns
- Compute trip duration
- Remove invalid or null values
- Handle outliers (optional)

### Output:
- `cleaned_taxi.csv`

### Purpose:
- Shows ability to process and structure raw data

---

## 4. Pytest Tests (2–3 Tests)

You must write automated tests using pytest.

### Required tests:
- Test if data loads correctly
- Test if transformation works
- Test data validity (example: no negative trip duration)

### Purpose:
- Ensures code correctness and reliability

---

## 5. Project Structure

Your project should be organized like this:
