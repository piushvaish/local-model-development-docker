################ BUILD IMAGE ################
FROM python:3.7.0
# virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# add and install requirements
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# Path

ENV PATH="/opt/venv/bin:$PATH"

RUN pip3 install --upgrade jupyterthemes
RUN pip3 install jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user
RUN jupyter nbextensions_configurator enable --user
RUN jupyter nbextension enable jupyter-js-widgets/extension
RUN jupyter nbextension enable jupyter-notebook-gist/notebook-extension
RUN jupyter nbextension enable contrib_nbextensions_help_item/main
RUN jupyter nbextension enable autosavetime/main
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable code_font_size/code_font_size
RUN jupyter nbextension enable code_prettify/code_prettify
RUN jupyter nbextension enable collapsible_headings/main
RUN jupyter nbextension enable comment-uncomment/main
RUN jupyter nbextension enable equation-numbering/main
RUN jupyter nbextension enable execute_time/ExecuteTime
RUN jupyter nbextension enable gist_it/main
RUN jupyter nbextension enable hide_input/main
RUN jupyter nbextension enable spellchecker/main
RUN jupyter nbextension enable toc2/main
RUN jupyter nbextension enable toggle_all_line_numbers/main


RUN ["mkdir", "notebooks"]
WORKDIR /notebooks
COPY conf/.jupyter /root/.jupyter
ADD run_jupyter.sh /
RUN chmod +x /run_jupyter.sh

# Jupyter 
EXPOSE 8888 
# Store notebooks in this mounted directoryVOLUME /notebooks
CMD ["/run_jupyter.sh"]
