from models import RequestLog

class RequestLoggingMiddleware(object):
    
    def process_request(self, request):
        rlog = RequestLog(method=request.method, \
                   url=request.get_full_path(), \
                   remote_addr=request.META.get('remote_addr', ''))
        rlog.save()
