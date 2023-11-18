import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_initial_state(tv):
    assert not tv._Television__status
    assert not tv._Television__muted
    assert tv._Television__volume == Television.MIN_VOLUME
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_power(tv):
    tv.power()
    assert tv._Television__status
    tv.power()
    assert not tv._Television__status

def test_mute(tv):
    tv.mute()
    assert tv._Television__muted and tv._Television__volume == Television.MIN_VOLUME
    tv.power()
    tv.mute()
    assert not tv._Television__muted and tv._Television__volume == tv._Television__temp

def test_channel_up(tv):
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL + 1
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL + 1
    for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL + 1):
        tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_channel_down(tv):
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL - 1
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL - 1
    for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL + 1):
        tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL

def test_volume_up(tv):
    tv.volume_up()
    assert tv._Television__volume == Television.MIN_VOLUME + 1
    tv.power()
    tv.volume_up()
    assert tv._Television__volume == Television.MIN_VOLUME + 1
    for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME + 1):
        tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME

def test_volume_down(tv):
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME - 1
    tv.power()
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME - 1
    for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME + 1):
        tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME
