FROM python:3.10-slim AS wheels
COPY requirements.txt requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

FROM python:3.10-slim AS runtime-packeges
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev


FROM runtime-packeges

COPY --from=wheels /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY telegram/ /app/telegram/
COPY main.py /app/main.py
COPY answers.txt /app/answers.txt

CMD python3 /app/main.py

