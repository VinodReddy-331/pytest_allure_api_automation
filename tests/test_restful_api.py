import pytest
from src.APIClient import APIClient

@pytest.fixture(scope='module')
def setup_function(env):
    apiObj = APIClient("https://api.restful-api.dev")
    print(env)
    return apiObj, env

def test_getobject(setup_function):
    apiObj, env =setup_function
    response = apiObj.get("/objects")
    print(response.json())
    assert response.status_code == 200 , f"Status Code is not matching "