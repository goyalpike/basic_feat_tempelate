from pathlib import Path

import jupytext


def convert_notebooks_to_py(notebooks_dir, notebooks_dir_output):
    """Convert .ipynb to .py."""
    notebooks_dir = Path(notebooks_dir).resolve()  # Convert to absolute Path object
    notebooks_dir_output = Path(notebooks_dir_output).resolve()  # Convert to absolute Path object

    for notebook_file in notebooks_dir.glob("*.ipynb"):  # Search for all .ipynb files
        if "_demo" not in str(notebook_file):
            continue
        try:
            # Load the notebook using jupytext
            notebook = jupytext.read(notebook_file)

            # Determine the output path for the Python script
            script_filename = notebook_file.stem + ".py"  # Replace .ipynb with .py

            script_path = notebooks_dir_output / script_filename

            # Write the Python script using jupytext
            jupytext.write(notebook, script_path, fmt="py:percent")
            print(f"Succesfully converted {notebook_file}!")
        except Exception as e:
            print(f"Error converting {notebook_file.name}: {e}")
