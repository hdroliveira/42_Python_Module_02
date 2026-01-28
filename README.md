# Python Module 02 - 👤 Author: hdroliveira

![42 Porto](https://img.shields.io/badge/42-Porto-blue)
![Language](https://img.shields.io/badge/Language-Python%203.10+-yellow)
![Style](https://img.shields.io/badge/Style-Flake8-green)

**Garden Guardian** (Python Module 02) focuses on **Data Engineering** and **Resilience**. In real-world agricultural systems, sensors fail and data gets corrupted. This module teaches how to build "bulletproof" pipelines using Python's Exception Handling (`try`, `except`, `raise`, `finally`) to ensure the system never crashes.

## 📂 Project Structure

The goal is to move from basic error catching to building a full fault-tolerant management system.

| Exercise | Name | Description | Key Concept |
| :--- | :--- | :--- | :--- |
| **ex00** | `ft_first_exception` | Validate temperature inputs and handle non-numeric data. | Basic `try` / `except` |
| **ex01** | `ft_different_errors` | Handle specific errors (`ValueError`, `KeyError`, `ZeroDivisionError`). | Multiple `except` blocks |
| **ex02** | `ft_custom_errors` | Create domain-specific errors (`PlantError`, `WaterError`). | **Custom Exceptions** |
| **ex03** | `ft_finally_block` | Ensure resources are closed (cleanup) regardless of errors. | The `finally` block |
| **ex04** | `ft_raise_errors` | Validate logic (e.g., water levels) and signal issues manually. | The `raise` keyword |
| **ex05** | `ft_garden_management` | A complete system integrating all previous error handling techniques. | **Full System Integration** |

## 💡 Key Concepts

### 1. Robustness (No Crashes)
[cite_start]The golden rule of this module is: **Your program must never crash**[cite: 705]. Even if a user inputs "abc" for a temperature, the program must catch the error, print a helpful message, and continue execution.

### 2. Custom Exception Hierarchy (ex02)
Standard Python errors aren't always descriptive enough. We create a hierarchy of errors specific to our domain:
```python
class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass
    
# Usage
try:
    ...
except GardenError as e:
    print(f"Caught a garden issue: {e}") # Catches PlantError too!

	3. Resource Cleanup (ex03)
When dealing with external resources (like a watering system or file), we must ensure they are closed even if the code fails. This is done using finally:

try:
    print("Opening watering system...")
    water_plants() # Might crash!
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Closing watering system...") # Always runs

	🛠️ Usage
Requirements
Python 3.10+

Flake8 standards.


Type Hints are mandatory.

Running the System (ex05)
The final exercise combines Classes (Module 01) with Error Handling (Module 02).

python3 ex05/ft_garden_management.py

Expected Output Example:

=== Garden Management System ===
Added tomato successfully
Error adding plant: Plant name cannot be empty! [Handled]
Watering tomato... success
Closing watering system (cleanup)

⚠️ Notes

Defensive Programming: Use raise  to enforce logical constraints (e.g., "Water level cannot be > 10") before they cause weird bugs later.

Specificity: Always prefer catching specific errors (e.g., ValueError) over a naked except: block.