FROM mambaorg/micromamba:latest

# Set a custom, writable root and temporary directory
ENV MAMBA_ROOT_PREFIX=/micromamba
ENV PATH=/micromamba/envs/base/bin:$PATH
ENV TMPDIR=/micromamba/tmp

# Create the directories with open permissions
RUN mkdir -p $MAMBA_ROOT_PREFIX && chmod -R a+w $MAMBA_ROOT_PREFIX \
 && mkdir -p $TMPDIR && chmod -R a+w $TMPDIR

WORKDIR /app

# Copy the conda environment file
COPY FinBot/env.yml /tmp/env.yml

# Update the base environment using the custom root prefix
RUN micromamba env update --root-prefix $MAMBA_ROOT_PREFIX -n base -f /tmp/env.yml && micromamba clean -a -y

# Copy the pip requirements and install pip packages
COPY FinBot/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# (Optional) Copy all project files into the container for development/testing
COPY . /app

# Open an interactive bash shell for development
CMD ["/bin/bash"] 