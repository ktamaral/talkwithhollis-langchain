FROM python:3.9

ENV APP_ID_NUMBER=55008
ENV APP_ID_NAME=twhadm
ENV GROUP_ID_NUMBER=1636
ENV GROUP_ID_NAME=appcommon

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

RUN useradd --create-home ${APP_ID_NAME}:${GROUP_ID_NAME} && \
  mkdir -p /home/${APP_ID_NAME}/data

COPY --chown=${APP_ID_NAME}:${GROUP_ID_NAME} . /home/${APP_ID_NAME}

WORKDIR /home/${APP_ID_NAME}

USER ${APP_ID_NAME}

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
