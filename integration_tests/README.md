# Integration Tests for OpenEMS

This package provides an integration test framework and integration tests for OpenEMS.
It's in a very early stage and currently only target to edge specific integration tests.

# Requirements
This project requires [poetry](https://python-poetry.org) to run.

In the local development environment it also requires the openems project next to this project. So a directory structure
like the following:
- some_folder
  - openems (exactly this name)
  - openems_integration_tests (name doesn't matter)

The openems project must have a build jar file (with `./gradlew buildEdge` executed in the openems directory) so the
integration test can start and stop the ems service as desired.

## Usage
Integration tests take care about starting/stopping the EMS service. So don't run another instance of the EMS service
while executing the integration tests.

By default, this package assumes you're using a Voltfang OpenEMS environment. You can override this by setting the
`EMS_INTEGRATION_TEST_ENVIRONMENT` environment variable to a value defined in 
`openems_integration_tests.conftest.ExecutionEnvironment` which are:
- `DEVELOPER` - Vanilla OpenEMS environment

For the profile `DEVELOPER_VOLTFANG` tests expect OpenEMS configuration files in `~/development/data/edge/empty/config`.
You can overwrite this location for every profile with the environment variable `EMS_CONFIG_DIR`. Integration tests will
overwrite files in this directory! So be sure to have a backup of your configuration if you want to restore it.

You can execute tests with
`poetry run pytest openems_integration_tests`
