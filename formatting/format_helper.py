'''Contains functions to help with formatting data.
'''

def format_message(source_name, source_url, quotes):
    '''Formats data as message for sending.

    Args:
        quotes: an array containing string quotes
        source_name: string denoting source name
        source_url: string denoting source data url

    Returns:
        A string to be sent over Telegram or another messaging service.
    '''
    if len(quotes) < 1:
        print('Error! Expected more than 0 quotes.')
        return None

    processed_data = []
    processed_data.append(source_name)
    processed_data.append(source_url)
    for quote in quotes:
        processed_data.append(quote)

    formatted_message = format_message_helper(processed_data)
    return formatted_message

def format_message_helper(data):
    '''Formats data as message for sending.

    Args:
        data: an array of the format
                [author, source (link or book name), quotes...]

    Returns:
        A string to be sent over Telegram or another messaging service.
    '''
    if len(data) < 3:
        print('Error! Expected data format is ' + \
              '[author, source (link or book name), quotes...]')
        return None

    author = data[0]
    source = data[1]
    formatted = f'<b>{author}</b>\n'
    formatted += f'<i>{source}</i>\n'
    for quote_idx in range(2, len(data)):
        formatted += f'{quote_idx-1}: {data[quote_idx]}' + '\n'

    return formatted
