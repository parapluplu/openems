# Integration Tests for OpenEMS

This package provides an integration test framework and integration tests for OpenEMS.
It's in a very early stage and currently only target to edge specific integration tests.

# Requirements
This project requires [poetry](https://python-poetry.org) to run.

The openems project must have a build jar file (with `./gradlew buildEdge` executed in the openems directory) so the
integration test can start and stop the ems service as desired.

Each time you update the project `pyproject.toml` file or when you setup the project initially execute:
```
poetry install
```

## Usage
Integration tests take care about starting/stopping the EMS service. So don't run another instance of the EMS service
while executing the integration tests.

By default, this package assumes you're using a Voltfang OpenEMS environment. You can override this by setting the
`EMS_INTEGRATION_TEST_ENVIRONMENT` environment variable to a value defined in 
`openems_integration_tests.conftest.ExecutionEnvironment` which are:
- `DEVELOPER` - Vanilla OpenEMS environment

You can execute tests with
`poetry run pytest openems_integration_tests`
