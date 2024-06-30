# Configuration file for Jupyter Notebook

# Set a password for Jupyter Notebook (replace with your own password)
c.NotebookApp.password = 'y_secret_password'

# Set the default kernel for new notebooks
c.NotebookApp.default_kernel = 'python3'

# Set the theme for Jupyter Notebook (options: 'light', 'dark', 'lab')
c.NotebookApp.theme = 'light'

# Allow Jupyter Notebook to be accessed from a specific IP address
c.NotebookApp.ip = 'localhost'

# Set the port number for Jupyter Notebook (default is 8888)
c.NotebookApp.port = 8888

# Set the notebook directory (where notebooks will be saved)
c.NotebookApp.notebook_dir = '~/notebooks'

# Set the browser to use when opening Jupyter Notebook
c.NotebookApp.browser = 'chrome'

# Disable the startup banner
c.NotebookApp.show_banner = False

# Set the timeout for idle kernels (in seconds)
c.NotebookApp.kernel_timeout = 300

# Set the maximum number of open notebooks
c.NotebookApp.max_open_notebooks = 10