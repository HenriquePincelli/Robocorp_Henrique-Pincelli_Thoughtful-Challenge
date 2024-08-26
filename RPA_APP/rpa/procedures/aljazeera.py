from RPA_APP.rpa.screens.aljazeera_screens import AljazeeraScreensService
from RPA_APP.rpa.screens.screens import Screens
import json
import sys


# >>>>>>>>>INITIALIZE SERVICES>>>>>>>>>
service_screen = AljazeeraScreensService()
service = Screens()
#  <<<<<<<<<INITIALIZE SERVICES<<<<<<<<<

# >>>>>>>>>Destiny directory for news images>>>>>>>>>
directory = "output/"
excel_filename = "aljazeera_news.xlsx"
# <<<<<<<<<Destiny directory for news images<<<<<<<<<


class RPAAljazeera:

    def newest_news(email, search_phrase, show_more):
        try:
            # >>>>>>>>>RPA Payload>>>>>>>>>
            payload = {
                "email": email,
                "search_phrase": search_phrase,
                "show_more": show_more
            }
            # <<<<<<<<<RPA Payload<<<<<<<<<

            # >>>>>>>>>Start RPA process>>>>>>>>>
            print("Starting RPA process.........")
            return_rpa = service_screen.rpa_aljazeera(payload)
            if not return_rpa["status"]:
                return {"status": False, "msg": return_rpa["msg"]}
            # <<<<<<<<<Start RPA process<<<<<<<<<

            # >>>>>>>>>Save Aljazeera data in 'output/aljazeera_news.xlsx'>>>>>>>>>
            print("Saving Aljazeera data in 'output/aljazeera_news.xlsx'.........")
            return_excel = service.make_excel_file(payload, return_rpa["data"], directory, excel_filename)
            if not return_excel["status"]:
                return {"status": False, "msg": return_excel["msg"]}
            # <<<<<<<<<Save Aljazeera data in 'output/aljazeera_news.xlsx'<<<<<<<<<

            # >>>>>>>>>Send excel file by email>>>>>>>>>
            if payload["email"] is not None:
                print("Sending excel file by email.........")
                return_email = service.send_excel_email(payload["email"], "Aljazeera Excel", directory, excel_filename)
                if not return_email["status"]:
                    return {"status": False, "msg": return_email["msg"]}
                return {"status": True, "msg": f"News Storaged and Sent to Email: {payload['email']}"}
            # <<<<<<<<<Send excel file by email<<<<<<<<<

            return {"status": True, "msg": f"News Storaged."}
        except Exception as e:
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            print("=-==-==-=ERROR=-==-==-=")
            print(traceback_details)
            print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            return {"status": False, "msg": json.dumps(traceback_details)}
