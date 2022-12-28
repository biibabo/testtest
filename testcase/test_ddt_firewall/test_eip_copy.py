def test_02_susscec(self, data):
    print(data, '=======')
    default = {}
    v = data.get('Status', default)
    if v == default:
        return False
    if v == 1:
        return True
    return False