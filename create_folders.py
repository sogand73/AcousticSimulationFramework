import os

# Main folder
root = "Acoustic-Simulator-full"

# List of subfolders you want inside it
subfolders = [
    "anchor_combos",
    "correlation_functions",
    "correlation_functions_with_AGC",
    "dist_th",
    "estimation_data",
    "logfiles",
    "LPF_curve",
    "LPF_curves_per_simulation",
    "LPF_dataset_downsampled",
    "models",
    "old",
    "pyroomacoustics_main",
    "result_figs",
    "RIRs",
    "RX_audio",
    "RX_audio_with_AWGN",
    "RX_audio_with_SIR_and_AWGN",
    "Sim_data",
    "Sim_output_data",
    "venv_location"
]

# Create main folder
os.makedirs(root, exist_ok=True)

# Create all subfolders inside the main one
for sf in subfolders:
    os.makedirs(os.path.join(root, sf), exist_ok=True)

print(f"Created {root} with {len(subfolders)} subfolders.")
