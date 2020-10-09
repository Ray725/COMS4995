from formatting.format_helper import format_message

class TestFormatting:
    def test_format_message_error_handling(self):
        assert format_message([]) == None

    def test_format_message(self):
        expected_output = '<b>a</b>\n<i>b</i>\nc'
        assert format_message(['a', 'b', 'c']) == expected_output
