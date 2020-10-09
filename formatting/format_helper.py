def format_message(data):
    '''Formats data as message for sending.

    Args:
        data: an array of the format
                [author, source (link or book name), text]

    Returns:
        A string to be sent over Telegram or another messaging service.
    '''
    if len(data) != 3:
        print('Error! Expected data format is ' + \
              '[author, source (link or book name), text]')
        return

    author = data[0]
    source = data[1]
    text = data[2]
    formatted = f'<b>{author}</b>\n'
    formatted += f'<i>{source}</i>\n'
    formatted += text

    return formatted
