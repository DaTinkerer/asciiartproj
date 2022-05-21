import pytest
from app import create_app
# from werkzeug.test import Client
# from werkzeug.testapp import test_app
# import unittest
# from app import index
def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200

# if __name__ == "__main__":
#     unittest.main()
