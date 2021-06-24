from IPython.lib import passwd
# setting up password
password = passwd("secret")
c = get_config()  # get the config object
c.IPKernelApp.pylab = 'inline'  # in-line figure when using Matplotlib
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False  # do not open a browser window by default when using notebooks
c.NotebookApp.token = ''  # No token. Always use jupyter over ssh tunnel
c.NotebookApp.password_required= True
c.NotebookApp.password = password
c.NotebookApp.notebook_dir = '/notebooks'
c.NotebookApp.allow_root = True  # Allow to run Jupyter from root user inside Docker container
c.NotebookApp.allow_origin = '*'
# Fixed port for server access
c.NotebookApp.port = 8888
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}
