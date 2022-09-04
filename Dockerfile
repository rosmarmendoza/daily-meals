FROM python:3.8-alpine AS Builder

# Copy sources files
WORKDIR /code
COPY . .

# Installation dependencies
RUN pip install -r requirements.txt

# Default port
ARG ARG_DEFAULT_PORT=8000
EXPOSE $ARG_DEFAULT_PORT
ENV DEFAULT_PORT=${ARG_DEFAULT_PORT}

# Install migrations
RUN python manage.py migrate

# Run server
ENTRYPOINT python manage.py runserver 0.0.0.0:${DEFAULT_PORT}
