import subprocess

# Define the range of values for k and m
k_values = [0, 1, 2, 3]
m_values = [0, 1, 2, 3]

# Print table header
print("|   k   |   m   |   Accuracy   |")

# Iterate over all combinations of k and m
for k in k_values:
    for m in m_values:
        # Construct the command to run main.py
        command = f"python3 main.py --file ../../Data/soybean.csv --k {k} --m {m}"

        # Execute the command and capture the output
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Extract accuracy from the output
        accuracy_line = [line for line in result.stdout.split('\n') if 'Accuracy' in line]
        accuracy = float(accuracy_line[0].split()[-1]) if accuracy_line else None

        # Print the table row with a placeholder for None values
        accuracy_str = f"{accuracy:.2f}%" if accuracy is not None else "N/A"
        print(f"|   {k}   |   {m}   |   {accuracy_str}   |")
