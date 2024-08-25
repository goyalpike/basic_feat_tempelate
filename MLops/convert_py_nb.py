from math_ops.utils import convert_notebooks_to_md_with_outputs

notebooks_dir = "./src/example_scripts/"
notebooks_dir_docs = "./docs/examples/"

# convert_py_to_notebooks(notebooks_dir, notebooks_dir_docs)
convert_notebooks_to_md_with_outputs(notebooks_dir_docs)
