import datetime


class Report(object):
    
    def __init__(self,request_duration=0,payload_size=0):
        self.request_duration = request_duration
        self.payload_size = payload_size
        self.sections = []
        
    @property
    def header(self):
        lines = [
                 'Metacontent file generated by OpenClimateGIS at {0} UTC.'.format(datetime.datetime.utcnow()),
                 '',
                 'Request Duration :: {0} seconds'.format(self.request_duration),
                 '    Payload Size :: {0} kilobytes'.format(self.payload_size),
                 ''
                 ]
        return(lines)
        
    def add_section(self,section):
        self.sections.append(section)

    def format(self):
        lines = self.header
        for section in self.sections:
            lines.extend(section.format())
            lines.append('')
        return(lines)