# Simple encryption with password and salt
## Sources
### Create python package
https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

## Build and use
Install openssl
```bash
brew install openssl
```

Follow insttructions from install process
```txt
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /opt/homebrew/etc/openssl@3/certs

and run
  /opt/homebrew/opt/openssl@3/bin/c_rehash

openssl@3 is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS provides LibreSSL.

If you need to have openssl@3 first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/openssl@3/bin:$PATH"' >> ~/.zshrc

For compilers to find openssl@3 you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/openssl@3/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/openssl@3/include"
```

Virtual env and install packages
```bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Build the package
```bash
python setup.py bdist_wheel
```

Close the virtual environment, then install the package locally to the user to make it available everywhere

```bash
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

