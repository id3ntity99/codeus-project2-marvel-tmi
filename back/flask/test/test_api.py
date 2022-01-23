from dotenv import load_dotenv
import os
import sys
import unittest

testdir = os.path.dirname(__file__)
srcdir = ".."
fullpath = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, fullpath)

from main import create_app

load_dotenv(verbose=True)


class TestApi(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.tester = app.test_client()
        self.API_KEY = os.getenv("API_KEY")

    ### Status code testing ###
    def test_status_code_search_all(self):
        response = self.tester.get(
            "/api/avengers/all", headers={"X-API-key": self.API_KEY}
        )

        self.assertEqual(200, response.status_code)

    def test_status_code_search_by_name(self):
        keywords = ["jess", "tony", " ", "=", ".env"]
        for keyword in keywords:
            response = self.tester.get(
                "/api/avengers?search={}".format(keyword),
                headers={"X-API-key": self.API_KEY},
            )
            self.assertEqual(200, response.status_code)

    def test_error_search_all(self):
        # Request without api key
        response = self.tester.get("/api/avengers/all")
        self.assertEqual(400, response.status_code)

        # Request with wrong api key
        response = self.tester.get(
            "/api/avengers/all", headers={"X-API-key": "wrong_key"}
        )
        self.assertEqual(400, response.status_code)

        # Request with wrong header name
        response = self.tester.get(
            "/api/avengers/all", headers={"x-api-ky": self.API_KEY}
        )


if __name__ == "__main__":
    unittest.main()
