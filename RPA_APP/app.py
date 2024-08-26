import os
from RPA_APP.rpa.procedures import RPAAljazeera
from RPA_APP.rpa.services.aljazeera_service import AljazeeraService
from RPA_APP.config import EMAIL_ALJAZEERA, SERCH_PHRASE_ALJAZEERA, SHOW_MORE_ALJAZEERA


def rpa_procedures():
    """Function to init RPA's"""

    # >>>>>>>>>Aljazeera's RPA>>>>>>>>>
    # >>>>>>>>>Parameters from robocorp storage>>>>>>>>>
    email = EMAIL_ALJAZEERA
    search_phrase = SERCH_PHRASE_ALJAZEERA
    show_more = SHOW_MORE_ALJAZEERA
    # <<<<<<<<<Parameters from robocorp storage<<<<<<<<<

    # >>>>>>>>>RPA's Procedure>>>>>>>>>
    print("=-=" * 24)
    print("Initiating Aljazeera's RPA")
    result_aljazeera = RPAAljazeera.newest_news(email=email, search_phrase=search_phrase, show_more=show_more)
    print(">" * 45)
    print(result_aljazeera)
    print("<" * 45)
    print("=-=" * 24)
    # <<<<<<<<<RPA's Procedure<<<<<<<<<
    # <<<<<<<<<Aljazeera's RPA<<<<<<<<<

def rpa_challenge():
    """Main function to run the application"""

    # >>>>>>>>>Ensure that RPA procedures run within the application context>>>>>>>>>
    rpa_procedures()
    # <<<<<<<<<Ensure that RPA procedures run within the application context<<<<<<<<<
