FROM continuumio/anaconda3
MAINTAINER "Liwei Sun"

# set path
ENV PATH /opt/conda/bin:$PATH

# install packages
RUN conda install jupyter -y && \
    conda install numpy pandas matplotlib seaborn -y && \
    conda install scikit-learn=0.21.2 && \
    conda install -c conda-forge imbalanced-learn=0.5.0

RUN ["mkdir", "/home/insight"]
RUN ["mkdir", "/home/insight/notebooks"]
RUN ["mkdir", "/home/insight/scripts"]
RUN ["mkdir", "/home/insight/data"]
RUN ["mkdir", "/home/insight/data/nba_reg18"]

# copy data and scripts
COPY /data/nba_reg18/nba_comments_reg18_* /home/insight/data/nba_reg18/
COPY /data/nba_reg18/nba_submissions_reg18_* /home/insight/data/nba_reg18/
COPY /data/teams /home/insight/data/
COPY /notebooks/Wk3_Final_Model.ipynb /home/insight/notebooks/
COPY /notebooks/entity* /home/insight/notebooks/
COPY /notebooks/bot* /home/insight/notebooks/
COPY /notebooks/kwords2.txt /home/insight/notebooks/
COPY /scripts/cal_auc.py /home/insight/scripts/
COPY /scripts/teamname_stdize.py /home/insight/scripts/
COPY /scripts/preprocess.py /home/insight/scripts/

# configure jupyter notebook
RUN mkdir /root/.jupyter
COPY /docker/jupyter_notebook_config.py /root/.jupyter/

# Jupyter ports
EXPOSE 8888

# run jupyter notebook
CMD ["jupyter", "notebook"]