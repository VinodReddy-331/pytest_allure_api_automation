import  pytest
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against (e.g. dev, qa, prod)"
    )

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")