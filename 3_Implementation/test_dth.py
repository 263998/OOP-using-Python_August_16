"""Module dth imported here"""

import dth


def test_dth2_vaidate_base_pack():
    """testing validate base pack method"""
    test = dth.BasePackage("prakhar", "Gold", 4)
    assert test.validate_base_pack_name() is True
    test = dth.BasePackage("prakhar", "gold", 4)
    assert test.validate_base_pack_name() is False
    test = dth.BasePackage("prakhar", "Goldi", 4)
    assert test.validate_base_pack_name() is False
    test = dth.BasePackage("prakhar", "hgsjjsj", 4)
    assert test.validate_base_pack_name() is False


def test_calculate_monthly_rent():
    """testing calculate monthly rent method"""
    test = dth.BasePackage("prakhar", "Gold", 4)
    assert test.calculate_monthly_rent() == 440
    test = dth.BasePackage("prakhar", "Silver", 6)
    assert test.calculate_monthly_rent() == 350
    test = dth.BasePackage("prakhar", "Platinum", 4)
    assert test.calculate_monthly_rent() == 560
    test = dth.BasePackage("prakhar", "xyz", 6)
    assert test.calculate_monthly_rent() == -1


def test_get_base_pack_name():
    """testing get base pack name method"""
    test = dth.BasePackage("prakhar", "Gold", 4)
    assert test.get_base_pack_name() == "Gold"
    test = dth.BasePackage("prakhar", "Silver", 4)
    assert test.get_base_pack_name() == "Silver"
    test = dth.BasePackage("prakhar", "Platinum", 4)
    assert test.get_base_pack_name() == "Platinum"
    test = dth.BasePackage("prakhar", "xyz", 4)
    assert test.get_base_pack_name() == "xyz"


def test_get_subscription_period():
    """testing get subscription period method"""
    test = dth.BasePackage("prakhar", "Gold", 4)
    assert test.get_subscription_period() == 4
    test = dth.BasePackage("prakhar", "Gold", 0)
    assert test.get_subscription_period() == 0
    test = dth.BasePackage("prakhar", "Gold", 24)
    assert test.get_subscription_period() == 24
    test = dth.BasePackage("prakhar", "Gold", 12)
    assert test.get_subscription_period() == 12


def test_get_consumer_name():
    """testing get consumer name method"""
    test = dth.BasePackage("prakhar", "GOld", 4)
    assert test.get_consumer_name() == "prakhar"
    test = dth.BasePackage("xyz", "GOld", 4)
    assert test.get_consumer_name() == "xyz"
    test = dth.BasePackage("abcd", "GOld", 4)
    assert test.get_consumer_name() == "abcd"
    test = dth.BasePackage("rohan", "GOld", 4)
    assert test.get_consumer_name() == "rohan"
