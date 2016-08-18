class rcdbase(object):
    record_id = ''

    def __init__(self):
        print 'rcdbase __init__ called.'

    def get_record_id(self):
        return self.record_id

class rcdheader(rcdbase):
    def __init__(self):
        print 'rcdheader called!'
        return super(rcdheader, self).__init__()

    create_date = ''
    create_time = '2015-8-6'
    software_name = 'imc'

header = rcdheader()
print header.record_id
print header.create_time
print header.software_name