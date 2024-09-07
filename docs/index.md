# Simple Math Functions

It demonstrates simple math functions in python :-) However, main purpose of this repository to show how different components are connections; these includes:

- Automatic building of documentation 
- Deployment of webpage using mkdocs
- Automatic running notebooks that are used to build documentation
- Installation of required packages using poetry in CI 
- Option: Installation with conda; it is required when dependencies becomes complicated

## Examples
It contains as of now two examples. Please [have a look at simple examples](./examples/01_demo.ipynb).

## Code

**Python** is awesome

```python
def say_hello(name:str = None):
    if name:
        print(f'Hello {name}!')
    else:
        print('Hello there!')
```
## TODO
We are in the stage of making more fancy. 