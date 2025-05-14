import json

import allure
import pytest
import os
from src.APIClient import APIClient
from src.ConfigManager import ConfigManager
from src.APIHelpers import APIHelpers


@allure.epic("API Automation")
@pytest.fixture(scope='module')
def setup_function(env):
    workspace_dir = os.path.abspath(os.curdir)
    confObj = ConfigManager(env,f"{workspace_dir}\conf\configuration_qa.json")
    apiObj = APIClient(f"{confObj.load_config()['base_url']}")
    helperObj = APIHelpers()
    return apiObj, env, helperObj, workspace_dir, confObj

@allure.severity(severity_level="High")
@pytest.mark.smoke
def test_getobject(setup_function):
    apiObj, env, helperObj, workspace_dir, confObj = setup_function
    response = apiObj.get("/objects")
    # helperObj.save_pretty_json(response.json(),f"{workspace_dir}/benchmark_outputs/objects.json"
    output = helperObj.compare_jsons(response.json(),f"{workspace_dir}/benchmark_outputs/objects.json")
    assert response.status_code == 200 , f"Status Code is not matching, actual status_code {response.status_code}"
    assert output, f"Actual & Expected Responses are not matching"

@allure.severity(severity_level="High")
@pytest.mark.smoke
def test_getobject_id3(setup_function):
    apiObj, env, helperObj, workspace_dir, confObj = setup_function
    response = apiObj.get("/objects?id=3")
    # helperObj.save_pretty_json(response.json(),f"{workspace_dir}/benchmark_outputs/objects_id3.json")
    output = helperObj.compare_jsons(response.json(),f"{workspace_dir}/benchmark_outputs/objects.json")
    assert response.status_code == 200 , f"Status Code is not matching, actual status_code {response.status_code}"
    assert output, f"Actual & Expected Responses are not matching"