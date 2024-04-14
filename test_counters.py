import pytest
from playwright.sync_api import Page

BASE_URL = "https://www.avito.ru/avito-care/eco-impact"
ALL_COUNTERS = "//*[contains(@class, 'desktop-impact-items')]"
CO2_COUNTER = "//*[contains(@class, 'desktop-label') and text()='не попало в атмосферу']/../.."
WATER_COUNTER = "//*[contains(@class, 'desktop-label') and text()='было сохранено']/../.."
ENERGY_COUNTER = "//*[contains(@class, 'desktop-label') and text()='было сэкономлено']/../.."

@pytest.fixture(autouse=True)
def set_up(page: Page):
    page.goto(BASE_URL)

def test_all_counters(page: Page):
    page.locator(ALL_COUNTERS).screenshot(path="output/1.png")


def test_co2_counter(page: Page):
    page.locator(CO2_COUNTER).screenshot(path="output/2.png")


def test_water_counter(page: Page):
    page.locator(WATER_COUNTER).screenshot(path="output/3.png")


def test_energy_counter(page: Page):
    page.locator(ENERGY_COUNTER).screenshot(path="output/4.png")