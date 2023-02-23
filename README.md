# Simple encryption with password and salt
## Sources
### Create python package
https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

## Build and use
Build the package
```python
python setup.py bdist_wheel
```

Close the virtual environment, then install the package locally to the user to make it available everywhere

```python
pip install --user dist/encrypt-1.0.0-py3-none-any.whl --force-reinstall

```

Encrypt

```bash
python -m encrypt file_name -e
```

Decrypt

```bash
python -m encrypt file_name -d
```
