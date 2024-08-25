import os
from pathlib import Path

import jupytext
import nbformat
from nbconvert import HTMLExporter
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


def convert_notebooks_to_md_with_outputs(notebooks_dir):
    """Convert all Jupyter notebooks in a directory to Markdown files, including outputs.

    Parameters
    ----------
    notebooks_dir (str): Path to the directory containing the notebooks.
    """
    # Ensure the notebooks_dir path is absolute
    notebooks_dir = os.path.abspath(notebooks_dir)

    # Loop through all files in the directory
    for filename in os.listdir(notebooks_dir):
        if filename.endswith(".ipynb"):
            notebook_path = os.path.join(notebooks_dir, filename)
            md_filename = filename.replace(".ipynb", ".md")
            md_path = os.path.join(notebooks_dir, md_filename)

            # Load the notebook
            with open(notebook_path, encoding="utf-8") as f:
                notebook = nbformat.read(f, as_version=4)

            # Convert notebook to Markdown with outputs
            # Create a Jupytext writer that includes outputs
            jupytext.write(notebook, md_path, fmt="md")

            print(f"Converted {filename} to Markdown with outputs at {md_path}")


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


def convert_notebooks_to_html(notebooks_dir, output_dir):
    """Convert all Jupyter notebooks to HTML in the specified directory.

    Args:
    - notebooks_dir (str): The directory containing the Jupyter notebooks.
    - output_dir (str): The directory where the HTML files will be saved.
    """
    notebooks_dir = Path(notebooks_dir).resolve()  # Convert to absolute Path object
    output_dir = Path(output_dir).resolve()  # Convert to absolute Path object
    output_dir.mkdir(parents=True, exist_ok=True)  # Create output directory if it doesn't exist

    # Iterate over all notebook files in the specified directory
    for notebook_file in notebooks_dir.glob("*.ipynb"):  # Search for all .ipynb files
        try:
            # Load the notebook
            with open(notebook_file, encoding="utf-8") as f:
                nb = nbformat.read(f, as_version=4)

            # Create an ExecutePreprocessor object to execute the notebook
            ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

            # Execute the notebook
            ep.preprocess(nb, {"metadata": {"path": str(notebooks_dir)}})

            # Convert the executed notebook to HTML
            html_exporter = HTMLExporter()
            body, resources = html_exporter.from_notebook_node(nb)

            # Write the HTML output
            html_file = output_dir / (notebook_file.stem + ".html")  # Replace .ipynb with .html
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(body)

            print(f"Converted and executed {notebook_file.name} to HTML.")
        except Exception as e:
            print(f"Error processing {notebook_file.name}: {e}")
