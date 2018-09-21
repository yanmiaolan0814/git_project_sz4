import pytest


class TestLogin(object):
    @pytest.mark.run(order=1)
    def test_login1(self):
        print("111")
        assert True

    @pytest.mark.run(order=2)
    def test_login2(self):
        print("222")
        assert True

    @pytest.mark.run(order=0)
    def test_login3(self):
        print("000")
        assert True

    @pytest.mark.run(order=-1)
    def test_login4(self):
        print("-1-1-1")
        assert True

    @pytest.mark.run(order=-2)
    def test_login5(self):
        print("-2-2-2")
        assert True

    @pytest.mark.run()
    def test_login6(self):
        print("空")
        assert True