class MiddleMetaIP:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = forwarded.split(',')[0] if forwarded else request.META.get('REMOTE_ADDR')
        request.ip = ip
        return self.get_response(request)
