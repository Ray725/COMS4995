from formatting.format_helper import format_message
from formatting.format_helper import format_message_helper

class TestFormatting:
    def test_format_message_error_handling(self):
        assert format_message('test', 'test', []) == None

    def test_format_message(self):
        expected_output = '<b>a</b>\n<i>b</i>\n1: c\n'
        assert format_message('a', 'b', ['c']) == expected_output

    def test_format_message_helper_error_handling(self):
        assert format_message_helper([]) == None

    def test_format_message_helper(self):
        expected_output = '<b>a</b>\n<i>b</i>\n1: c\n'
        assert format_message_helper(['a', 'b', 'c']) == expected_output
