import dataclasses
from time import sleep
from typing import Optional

import pytest

from openems_integration_tests.ems.ems import EmsClient


@pytest.mark.ems_config.with_args("peak_and_emergency")
def test_channel_peak_shaving(ems_cli: EmsClient):


    # Test Peak Shaving

    # Configured ESS has initial SoC of 50%
    # Configured ESS has Charge Limit 100.000
    # Configured ESS has Discharge Limit 100.000

    # Configured PeakShave should shave above 10.000
    # Configured PeakShave should recharge under 5.000

    # Production 0, Consumption 9000  - p_ess = 0
    ems_cli.set_production_power(0)
    ems_cli.set_consumption_power(9000)

    # Wait for energy to be high enough
    sleep(10)

    assert ems_cli.get_active_power() == 0

    # Production 0, Consumption 12000 - p_ess = 2000
    ems_cli.set_production_power(0)
    ems_cli.set_consumption_power(12000)

    # Wait for energy to be high enough
    sleep(10)

    assert ems_cli.get_active_power() == 2000

    # Production 0, Consumption 4000  - p_ess = -1000
    ems_cli.set_production_power(0)
    ems_cli.set_consumption_power(4000)

    # Wait for energy to be high enough
    sleep(10)

    assert ems_cli.get_active_power() == -1000