class helpMe:
    @staticmethod
    def get_lowest_span(html_new, name):

        return html_new.find(class_=name).find_next("span").find_next("span").find_next("span").find_next('span')

    @staticmethod
    def fill_https_head(url):
        if not url.startswith("https:"):
            url = "https:" + url
        return url