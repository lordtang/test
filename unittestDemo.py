import unittest
import HTMLTestRunner

class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertTrue("foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(),["hello","world"])
        with self.assertRaises(TypeError):
            s.split(2)

def suite():
    '''
    功能：将测试用例添加到分组
    返回值：suite对象，供HTMLTestRunner实例调用
    参数：无
    '''
    # 创建suite对象
    suite = unittest.TestSuite()
    # 添加需要测试的方法或者用例
    suite.addTest(TestStringMethod("test_split"))
    return suite

if __name__ == "__main__":
    # with open('report.txt','a') as f:
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite())
    with open("HTTPreport.html",'wb+') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                                description="来自测试部门",
                                                title="使用HTML生成",
                                                verbosity=2
                                                )
                                                
        s = suite()
        runner.run(s)
    

    