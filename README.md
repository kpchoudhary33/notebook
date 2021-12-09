# Jupyter Notebook App allows us to edit and run notebooks via a web browser.
# Its two main components are the kernels and a dashboard.


# Run Jupyter Notebook in your local:

- Step 1. Clone the repo and create env in python3+, install requirements.

- Step 2. Then run jupyter notebook in a other terminal(activate the enviroment) by this command:

    `python manage.py shell_plus --notebook`

    Then you see jupitar dashboard with notebook all project directories,
    files, headers and many more features of this tool.

Step 3. Access datahub code by jupitar follow this:
    - Go to New --> Django Shell-plus
    - Here any command you run in django shell can by triggered from here.

# Testing:

    from django.contrib.auth.models import User
    users = User.objects.all()

# Note_->
    settings can be update as per requirement in jupyter_notebook_config.py file.

    `c.allow_password_change=True`
    `c.NotebookApp.open_browser = False`
    `c.NotebookApp.base_url = '/ipython/'`

# To make port for notebook server we can set [by default port is 8888] ).
`c.NotebookApp.port = 9999`
..more settings can be found here https://jupyter-notebook.readthedocs.io/en/stable/config.html#options

# To generate password for jupyter

1. By using token in UI

    - pass the token(can access from notebook server running at backend) and new password.
    - restart the notebook server and then it will only ask for password.

2. By django_plus shell:

    `from notebook.auth import passwd;`
    `passwd()`

    Enter password: ········
    Verify password: ········
    returns <encrypted_password>

    Then this password needs to save into jupyter config file(optional in case of config.json file present it takes precedence over .py file.):

    c.NotebookApp.password = <encrypted_password>
    restart the notebook server

# Remove unwanted kernels:
jupyter kernelspec uninstall unwanted-kernel
