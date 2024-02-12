from testify import TestCase, assert_equal, run
import requests

class OpenApiTestCase(TestCase):
    def test_addAPI(self):
        response=requests.get('https://api.mathjs.org/v4/?expr=2%2B3')
        result = int(response.content.decode('utf-8'))

        # Check if the response status code is 200 (OK)
        assert_equal(response.status_code, 200)
        #checking final result
        assert_equal(result,5)

    def test_subAPI(self):
        response=requests.get('https://api.mathjs.org/v4/?expr=100-80')
        result = int(response.content.decode('utf-8'))
        
        # Check if the response status code is 200 (OK)
        assert_equal(response.status_code, 200)
        #checking final result
        assert_equal(result,20)
    
    def test_mulAPI(self):
        response=requests.get('https://api.mathjs.org/v4/?expr=100*80')
        result = int(response.content.decode('utf-8'))
        
        # Check if the response status code is 200 (OK)
        assert_equal(response.status_code, 200)
        #checking final result
        assert_equal(result,8000)

    def test_divAPI(self):
        response=requests.get('http://api.mathjs.org/v4/?expr=100%2F80')
        result = float(response.content.decode('utf-8'))
        # Check if the response status code is 200 (OK)
        assert_equal(response.status_code, 200)
        #checking final result
        assert_equal(result,1.25)

if __name__ == '__main__':
    run()
        