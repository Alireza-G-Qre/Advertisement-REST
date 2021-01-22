from random import randint


class Packable:
    _total_Object = 0
    _dataBase = ''

    def __init__(self, address='default'):
        self._id = self.id_generator()
        self._dataBase = address

    @classmethod
    def id_generator(cls):
        cls._total_Object += 1
        return cls._total_Object

    def pack(self):
        pass

    def dpkg(self):
        pass

    def name_generator(self):
        return f'{self._id:03d}-{randint(1000, 10000)}'

    def get_id(self):
        return self._id


class BaseAdvertising(Packable):

    def __init__(self):
        super(BaseAdvertising, self).__init__('default')
        self._clicks = 0
        self._views = 0

    def increase_clicks(self):
        self._clicks += 1

    def increase_views(self):
        self._views += 1

    def get_clicks(self):
        return self._clicks

    def get_views(self):
        return self._views

    def reset_information(self):
        self._views = 0
        self._clicks = 0

    def describe_me(self):
        return f'method called in {self.__class__.__name__}'


class Advertiser(BaseAdvertising):

    _total_clicks = 0
    _total_views = 0

    @classmethod
    def get_total_clicks(cls):
        return cls._total_clicks

    @classmethod
    def get_total_views(cls):
        return cls._total_views

    @classmethod
    def increase_total_clicks(cls):
        cls._total_clicks += 1

    @classmethod
    def increase_total_views(cls):
        cls._total_views += 1

    def __init__(self, name):
        super(Advertiser, self).__init__()
        self._advertiser_name = name

    def increase_clicks(self):
        super(Advertiser, self).increase_clicks()
        self.increase_total_clicks()

    def increase_views(self):
        super(Advertiser, self).increase_views()
        self.increase_total_views()

    def get_name(self):
        return self._advertiser_name

    def set_name(self, new_name):
        self._advertiser_name = new_name

    @classmethod
    def help(cls):
        return 'Ok.'


class Ad(BaseAdvertising):

    def __init__(self, title, image_url, link, advertiser):
        super(Ad, self).__init__()
        self._title = title
        self._image_url = image_url
        self._advertiser = advertiser
        self._link = link

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_image_url(self):
        return self._image_url

    def set_image_url(self, url):
        self._image_url = url

    def get_link(self):
        return self._link

    def set_link(self, link):
        self._link = link

    def set_advertiser(self, advertiser):
        self._advertiser = advertiser

    def increase_clicks(self):
        super(Ad, self).increase_clicks()
        self._advertiser.increase_clicks()

    def increase_views(self):
        super(Ad, self).increase_views()
        self._advertiser.increase_views()
