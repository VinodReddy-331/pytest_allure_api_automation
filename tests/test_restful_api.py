import json

import allure
import pytest
import os
from src.APIClient import APIClient
from src.ConfigManager import ConfigManager
from src.APIHelpers import APIHelpers

@pytest.fixture(scope='module')
def setup_function(env):
    workspace_dir = os.path.abspath(os.curdir)
    print("Workspace directory:", workspace_dir)
    confObj = ConfigManager(env,f"{workspace_dir}\conf\configuration_qa.json")
    apiObj = APIClient(f"{confObj.load_config()['base_url']}")
    helperObj = APIHelpers()
    print(env)
    return apiObj, env, helperObj, workspace_dir

@allure.epic("API Automation")
@allure.severity(severity_level="High")
@pytest.mark.smoke
def test_getobject(setup_function):
    apiObj, env, helperObj, workspace_dir = setup_function
    response = apiObj.get("/objects")
    # helperObj.save_pretty_json(response.json(),f"{workspace_dir}/benchmark_outputs/objects.json"
    output = helperObj.compare_jsons(response.json(),f"{workspace_dir}/benchmark_outputs/objects.json")
    assert response.status_code == 200 , f"Status Code is not matching, actual status_code {response.status_code}"
    assert output, f"Actual & Expected Responses are not matching"

