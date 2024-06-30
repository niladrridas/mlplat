FROM jupyter/scipy-notebook:latest

# Install required packages
RUN pip install -r requirements.txt

# Copy configuration files
COPY config.json /etc/jupyter/
COPY jupyter_notebook_config.py /etc/jupyter/

# Expose port
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--port", "8888", "--allow-root"]