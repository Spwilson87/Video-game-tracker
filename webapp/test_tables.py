from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #check for html response 200
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/owned_table")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

            

if __name__ == "__main__":
    unittest.main()