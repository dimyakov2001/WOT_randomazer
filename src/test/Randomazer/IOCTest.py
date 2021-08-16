import unittest

from src.main.Randomazer.IOCContainer import IOCContainer, IOCContainerException


class IOCContainerTest(unittest.TestCase):

    def test_normal_register_resolve_int(self):
        ioc = IOCContainer()
        ioc.register_dependency("int", 1)
        self.assertEqual(ioc.resolve_dependency("int"), 1)

    def test_normal_register_resolve_string(self):
        ioc = IOCContainer()
        ioc.register_dependency("str", "abc")
        self.assertEqual(ioc.resolve_dependency("str"), "abc")

    def test_normal_register_resolve_object(self):
        class TestClass:
            field = 0

        test_object = TestClass()
        test_object.field = 10

        ioc = IOCContainer()
        ioc.register_dependency("object", test_object)

        self.assertEqual(ioc.resolve_dependency("object"), test_object)

    def test_resolve_exception(self):
        ioc = IOCContainer()
        ioc.register_dependency("int", 1)

        with self.assertRaisesRegex(IOCContainerException, "Can't find dependence 'str' to resolve."):
            ioc.resolve_dependency("str")

    def test_delete_exception(self):
        ioc = IOCContainer()
        ioc.register_dependency("int", 1)

        with self.assertRaisesRegex(IOCContainerException, "Can't find dependence 'a' to delete."):
            ioc.delete_dependency("a")
