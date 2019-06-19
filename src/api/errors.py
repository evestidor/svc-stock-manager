

def _message(status, message):
    return {'status': status, 'message': message}


E001 = _message('E001', 'Stock already exists.')
E002 = _message('E002', 'Stock symbol is invalid.')
