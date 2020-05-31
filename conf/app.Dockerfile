#
# Copyright (c) 2020 Nox Technologies Ltd <info at noxt eu>
# All rights reserved.
#
# Use is subject to license terms, as specified in the LICENSE file.
#

# Debian 10.x image
FROM debian:buster
RUN apt-get update

#
# Install the build tools and/or dependencies.
#
RUN apt-get install -y procps net-tools vim less
RUN apt-get install -y python3 python3-pip

RUN pip3 install pipenv

#
# Setup unprivileged user.
#
RUN useradd -m svc
RUN mkdir /data
RUN chown svc /data
USER svc
WORKDIR app

#
# Setup the Python application.
#
WORKDIR /app
COPY ./src /app

RUN pipenv sync --three --keep-outdated --dev --clear

#
# Run the service.
#
EXPOSE 8000 5000
ENTRYPOINT ["pipenv", "run"]
CMD ["cdocstore"]
