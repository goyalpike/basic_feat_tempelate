from pathlib import Path

import jupytext
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


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


def convert_py_to_notebooks(py_dir, notebooks_dir_output):
    """Convert all Python scripts in the specified directory to Jupyter notebooks.

    Args:
    - py_dir (str): The directory containing the Python scripts.
    - notebooks_dir_output (str): The directory where the converted Jupyter notebooks will be saved.
    """
    py_dir = Path(py_dir).resolve()  # Convert to absolute Path object
    notebooks_dir_output = Path(notebooks_dir_output).resolve()  # Convert to absolute Path object

    # Iterate over all files in the specified directory
    for py_file in py_dir.glob("*.py"):  # Search for all .py files
        try:
            # Load the Python script using jupytext
            # jupytext.read() will detect the cell markers and convert accordingly
            notebook = jupytext.read(py_file, fmt="py:percent")

            # Determine the output path for the Jupyter notebook
            notebook_filename = py_file.stem + ".ipynb"  # Replace .py with .ipynb
            notebook_path = notebooks_dir_output / notebook_filename

            # Write the Jupyter notebook using jupytext
            jupytext.write(notebook, notebook_path, fmt="ipynb")

            print(f"Converted {py_file.name} to {notebook_filename}.")

            # Load the newly created notebook
            with open(notebook_path, encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)

            # Create an ExecutePreprocessor object to execute the notebook
            ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

            # Execute the notebook
            ep.preprocess(nb, {"metadata": {"path": str(notebooks_dir_output)}})

            # Save the executed notebook
            with open(notebook_path, "w", encoding="utf-8") as f:
                nbformat.write(nb, f)

            print(f"Executed and saved {notebook_filename}.")
        except Exception as e:
            print(f"Error converting {py_file.name}: {e}")
