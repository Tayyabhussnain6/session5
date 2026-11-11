from __future__ import annotations

from contextlib import contextmanager
from threading import Thread

import pytest
from werkzeug.serving import make_server

from app import InMemoryOrderStore, create_app


@contextmanager
def running_app():
    server = make_server(
        "127.0.0.1", 0, create_app(InMemoryOrderStore()), threaded=True
    )
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join(timeout=5)


@pytest.fixture
def app_url():
    with running_app() as url:
        yield url
