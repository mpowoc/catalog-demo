Catalog Demo
============

If all the prerequisites are satisfied, start a venv and install dependencies:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Start dev dependencies. This will start a postgres instance, localstack, and apply specified terraform needs locally
```
cd dev/
./setup-dev-environment.sh
```

Create a user in the database and run migrations
```
python manage.py migrate 
python manage.py createsuperuser --username admin --email admin@example.com
```

TODO: requirements.txt has a mix of dev dependencies. Clean up.

## Environment Prerequisites

### Python Environment 

Install Pyenv: https://github.com/pyenv/pyenv
```
curl -fsSL https://pyenv.run | bash 
```

Set up Pyenv in environment (zsh example)
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

The project's version is stored in `.python-version`, recognized by pyenv

### Local Development: Service Dependencies

- Docker
- minikube: `brew install minikube`
- k9s: `brew install k9s`
- terraform: `brew tap hashicorp/tap && brew install hashicorp/tap/terraform`
- tflocal: `pip install terraform-local`
- awscli-local: `pip install awscli-local`


