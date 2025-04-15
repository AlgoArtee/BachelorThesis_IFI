import json
import matplotlib.pyplot as plt
import pandas as pd

# Function to parse the duration value (e.g., "2980s" -> 2980.0)
def parse_duration(duration):
    if isinstance(duration, str):
        duration = duration.strip()
        if duration.endswith("s"):
            try:
                return float(duration[:-1])
            except:
                return None
        else:
            try:
                return float(duration)
            except:
                return None
    elif isinstance(duration, (int, float)):
        return float(duration)
    return None

# List the files and their associated tool names.
file_info = [
    ("Playwright", "../data/playwright_test_run_2025_03_31_19_26_23.json"),
    ("Playwright", "..data/playwright_test_run_2025_04_13_06_03_56_AT-75.json"),
    ("TestZeus Hercules", "../data/testzeus_hercules_test_run_2025_04_02_12_42_54.json"),
    ("TestZeus Hercules", "../data/testzeus_hercules_test_run_2025_04_14_23_44_54_AT-75.json"),
    ("xLAM", "../data/xlam_test_run_2025_04_08_00_28_37.json")
]

# Create a list to store aggregated data.
data_rows = []
for tool, file_path in file_info:
    with open(file_path, 'r') as f:
        json_data = json.load(f)
        # Loop over each test record in the file's "table"
        for test in json_data.get("table", []):
            # Extract test result (e.g., "Success", "Failed", "Unknown")
            result = test.get("test_result")
            # Parse and convert duration into a float
            duration = parse_duration(test.get("duration"))
            data_rows.append({
                "Tool": tool,
                "TestName": test.get("test_name"),
                "Result": result,
                "Duration": duration
            })

# Create a DataFrame
df = pd.DataFrame(data_rows)

# --- Visualization 1: Stacked Bar Chart for Test Results ---
# Count test results by tool
result_counts = df.groupby(["Tool", "Result"]).size().unstack(fill_value=0)
ax1 = result_counts.plot(kind='bar', stacked=True, figsize=(8, 6))
ax1.set_title("Test Result Distribution per Tool")
ax1.set_xlabel("Tool")
ax1.set_ylabel("Number of Tests")
plt.tight_layout()
plt.show()

# --- Visualization 2: Boxplot for Test Duration Distribution ---
plt.figure(figsize=(8, 6))
df.boxplot(column="Duration", by="Tool", grid=False)
plt.title("Test Duration Distribution per Tool")
plt.suptitle('')  # Remove the automatic overall title
plt.xlabel("Tool")
plt.ylabel("Duration (s)")
plt.tight_layout()
plt.show()

# --- Visualization 3: Average Test Duration per Tool ---
avg_duration = df.groupby("Tool")["Duration"].mean()
plt.figure(figsize=(6, 4))
avg_duration.plot(kind='bar')
plt.title("Average Test Duration per Tool")
plt.xlabel("Tool")
plt.ylabel("Average Duration (s)")
plt.tight_layout()
plt.show()

# --- Visualization 4: Success Rate Comparison ---
# Define success as the tests with result "Success"
success_counts = df[df["Result"] == "Success"].groupby("Tool").size()
total_counts = df.groupby("Tool").size()
# Calculate success rate as a percentage
success_rate = (success_counts / total_counts * 100).fillna(0)
plt.figure(figsize=(6, 4))
success_rate.plot(kind='bar')
plt.title("Success Rate per Tool (%)")
plt.xlabel("Tool")
plt.ylabel("Success Rate (%)")
plt.tight_layout()
plt.show()
