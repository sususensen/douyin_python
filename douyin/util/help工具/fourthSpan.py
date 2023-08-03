class helpMe:
    @staticmethod
    def get_lowest_span(html_new, name):

        return html_new.find(class_=name).find_next("span").find_next("span").find_next("span").find_next('span')